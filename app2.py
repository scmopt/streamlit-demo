import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import io # uploaded_file を BytesIO に変換するために必要
import re # シート名をキーとして安全に使用するため

# Streamlitアプリのタイトルを設定
st.set_page_config(page_title="Excel EDA アプリ", layout="wide")
st.title("📊 Excelファイル EDA (探索的データ分析) アプリ")
st.markdown("""
Excelファイルをアップロードすると、ファイル内の各シートのデータに対して
[ydata-profiling](https://github.com/ydataai/ydata-profiling) (旧 pandas-profiling)
を用いた探索的データ分析レポートをタブ形式で表示します。
""")

# --- キャッシュ用関数 ---
@st.cache_data
def load_excel_data(_uploaded_file_bytes):
    """
    アップロードされたExcelファイル（バイト列）から全シートのデータを読み込み、
    シート名をキー、DataFrameを値とする辞書を返す。
    _uploaded_file_bytes: アップロードされたファイルの内容 (bytes)
    """
    dataframes = {}
    try:
        excel_file = pd.ExcelFile(io.BytesIO(_uploaded_file_bytes), engine='openpyxl')
        sheet_names = excel_file.sheet_names
        for sheet_name in sheet_names:
            df = pd.read_excel(excel_file, sheet_name=sheet_name)
            dataframes[sheet_name] = df
        return dataframes, None
    except Exception as e:
        return None, f"Excelファイルの読み込み中にエラーが発生しました: {e}"

@st.cache_data()
def generate_profile_report(_df, _sheet_name_for_title):
    """
    DataFrameからydata-profilingレポートを生成する。
    _df: 分析対象のDataFrame
    _sheet_name_for_title: シート名 (レポートタイトル用)
    """
    if _df.empty:
        return None
    try:
        profile = ProfileReport(_df, title=f"Profiling Report for sheet: '{_sheet_name_for_title}'", explorative=True)
        return profile
    except Exception as e:
        # エラーは呼び出し元で処理するため、ここではNoneを返し、エラーメッセージをログに出力するか、
        # 例外を再スローする（今回は呼び出し元でst.errorを表示）
        print(f"Error generating report for sheet '{_sheet_name_for_title}': {e}")
        raise # エラーを呼び出し元に伝播させる
        # return None # またはNoneを返して呼び出し元でエラーを検知

def sanitize_string_for_key(s):
    """Streamlitのキーとして安全な文字列に変換する"""
    return re.sub(r'\W+', '_', s) # 非英数字をアンダースコアに置換

# --- ファイルアップローダー ---
uploaded_file = st.file_uploader("Excelファイルを選択してください (.xlsx, .xls)", type=["xlsx", "xls"])

if uploaded_file is not None:
    st.info(f"ファイル名: `{uploaded_file.name}` がアップロードされました。処理を開始します...")

    uploaded_file_bytes = uploaded_file.getvalue()

    with st.spinner("Excelファイルを読み込んでいます..."):
        dataframes_dict, error_message = load_excel_data(uploaded_file_bytes)

    if error_message:
        st.error(error_message)
    elif dataframes_dict:
        if not dataframes_dict:
            st.warning("Excelファイルにシートが見つかりませんでした。")
        else:
            st.success(f"{len(dataframes_dict)}個のシートが読み込まれました: {', '.join(dataframes_dict.keys())}")

            sheet_names_list = list(dataframes_dict.keys())

            if sheet_names_list:
                # st.tabs() に渡すタブのタイトルリスト
                tab_titles = [f"📄 {name}" for name in sheet_names_list] # 絵文字を追加して見やすく
                tabs = st.tabs(tab_titles)

                # 各タブにレポートを表示
                st.write(sheet_names_list)
                for i, sheet_name in enumerate(sheet_names_list):
                    with tabs[i]: # i番目のタブのコンテキスト
                        df = dataframes_dict[sheet_name]
                        # st.subheader(f"分析結果: シート '{sheet_name}'") # タブ名でわかるので、必須ではない

                        if df.empty:
                            st.warning(f"シート '{sheet_name}' は空です。分析をスキップします。")
                            continue

                        # レポート生成（キャッシュ利用）
                        # スピナーはタブごとに表示する
                        with st.spinner(f"シート '{sheet_name}' のEDAレポートを生成中... これには数分かかることがあります。"):
                            try:
                                # df.copy() を渡して、元のDataFrameが変更されないようにする
                                profile = generate_profile_report(df.copy(), sheet_name)
                                if profile:
                                    # キーは各タブ内で重複しなければ良いが、念のため全体でユニークにする
                                    # シート名に特殊文字が含まれる可能性を考慮してサニタイズ
                                    report_key = f"profile_{sanitize_string_for_key(sheet_name)}"
                                    st_profile_report(profile, key=report_key)
                                else:
                                    # generate_profile_reportがNoneを返した場合（現在は空のDFの場合のみ）
                                    st.warning(f"シート '{sheet_name}' のレポートは生成されませんでした（空のデータ）。")
                            except Exception as e:
                                st.error(f"シート '{sheet_name}' のレポート生成または表示中にエラーが発生しました: {e}")
                #st.balloons()
            else:
                # このケースは dataframes_dict が空でない限りは通常発生しない
                st.info("読み込まれたシートがありません。")
    else:
        st.error("Excelデータの読み込みに失敗しました。")

else:
    st.info("分析を開始するには、Excelファイルをアップロードしてください。")

st.markdown("---")
st.markdown("Created with ❤️ by Streamlit, Pandas, Openpyxl, and YData-Profiling.")