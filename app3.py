# ユーザーからExcelファイルをアップロードしてもらい，Excel内のすべてのsheetのデータを
# dataframeにopenpyxlで変換した後で
# ydata-profiling (旧名pandas-profiling) でEDA (Exploratory Data Analysis)
# 分析をした結果をユーザーに可視化するstreamlitのwebアプリを作ってください．
import streamlit as st
import pandas as pd
import openpyxl
from io import BytesIO
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# ページ設定
st.set_page_config(
    page_title="Excelデータ分析ツール",
    page_icon="📊",
    layout="wide"
)

# タイトル
st.title("📊 Excelデータ分析ツール")
st.markdown("""
**使い方:**
1. Excelファイルをアップロード
2. 分析したいシートを選択
3. 自動生成された分析レポートを確認
""")

# ファイルアップロード
uploaded_file = st.file_uploader(
    "Excelファイルをアップロードしてください",
    type=["xlsx", "xls"],
    accept_multiple_files=False
)

@st.cache_data
def load_excel_sheets(file_bytes):
    """Excelファイルから全シートを読み込んでデータフレームの辞書を返す"""
    workbook = openpyxl.load_workbook(filename=BytesIO(file_bytes), data_only=True)
    sheets_dict = {}
    for sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
        data = sheet.values
        cols = next(data)
        df = pd.DataFrame(data, columns=cols)
        sheets_dict[sheet_name] = df
    return sheets_dict

@st.cache_data(show_spinner="分析レポート生成中...")
def generate_profile_report(df, title):
    """データフレームからプロファイリングレポートを生成"""
    return ProfileReport(
        df,
        title=title,
        explorative=True,
        minimal=False,
        progress_bar=False
    )

if uploaded_file is not None:
    try:
        # ファイルをバイト列で読み込み
        file_bytes = uploaded_file.read()
        
        # 全シートを読み込み
        with st.spinner("Excelファイルを処理中..."):
            sheets_dict = load_excel_sheets(file_bytes)
        
        # シート選択UI
        sheet_names = list(sheets_dict.keys())
        # selected_sheet = st.selectbox(
        #     "分析するシートを選択:",
        #     options=sheet_names,
        #     index=0
        # )
        #st.write(sheet_names)
        tab_titles = [f"📄 {name}" for name in sheet_names] # 絵文字を追加して見やすく
        tabs = st.tabs(tab_titles)
        for i, selected_sheet in enumerate(sheet_names):
            df = sheets_dict[selected_sheet]
            with tabs[i]: 
                # 基本情報表示
                st.subheader(f"シート名: `{selected_sheet}`")
                st.info(f"行数: {df.shape[0]} | 列数: {df.shape[1]}")
                
                # データプレビュー
                with st.expander("データプレビュー", expanded=False):
                    st.dataframe(df.head())
                
                # 分析レポート生成
                st.divider()
                st.subheader("データ分析レポート")
                
                #if st.button("レポート生成開始", type="primary"):
                with st.spinner("詳細分析を実行中..."):
                    report = generate_profile_report(df, f"分析レポート: {selected_sheet}")
                
                # レポート表示
                st_profile_report(report)
    
    except Exception as e:
        st.error(f"エラーが発生しました: {str(e)}")
        st.error("サポートされている形式のExcelファイルをアップロードしてください")

else:
    st.info("👆 Excelファイルをアップロードしてください (.xlsx または .xls形式)")
    st.image("https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=600", 
             caption="データ分析イメージ", width=300)