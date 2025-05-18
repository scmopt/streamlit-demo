import streamlit as st

st.set_page_config(page_title="マルチページアプリ Demo", layout="wide")

st.title("ようこそ！")
st.sidebar.success("上のメニューからページを選択してください。")

st.markdown(
    """
    これはStreamlitのマルチページ機能のデモンストレーションです。
    サイドバーから他のページに移動できます。
    """
)