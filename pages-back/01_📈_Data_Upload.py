import streamlit as st
import pandas as pd

st.set_page_config(page_title="データアップロード", page_icon="📈") # ページ固有設定

st.title("📈 データアップロード")
st.write("ここにCSVファイルをアップロードしてください。")

uploaded_file = st.file_uploader("CSVを選択", type="csv", key="uploader")

if uploaded_file is not None:
    # Session State を使ってDataFrameを他ページと共有
    try:
        df = pd.read_csv(uploaded_file)
        st.session_state['uploaded_df'] = df # Session Stateに保存
        st.success("ファイルがアップロードされ、データが保存されました！")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
        if 'uploaded_df' in st.session_state:
            del st.session_state['uploaded_df'] # エラー時は削除
else:
    if 'uploaded_df' in st.session_state:
        del st.session_state['uploaded_df'] # ファイルが選択されなくなったら削除