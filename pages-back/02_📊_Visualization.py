import streamlit as st
import pandas as pd

st.set_page_config(page_title="データ可視化", page_icon="📊")

st.title("📊 データ可視化")

# Session State からデータを取得
if 'uploaded_df' in st.session_state and isinstance(st.session_state['uploaded_df'], pd.DataFrame):
    df = st.session_state['uploaded_df']
    st.write("アップロードされたデータの可視化:")

    cols = df.columns.tolist()
    if len(cols) >= 2:
        x_axis = st.selectbox("X軸を選択", cols, index=0)
        y_axis = st.selectbox("Y軸を選択", cols, index=1 if len(cols)>1 else 0)

        if x_axis and y_axis:
            try:
                st.scatter_chart(df, x=x_axis, y=y_axis)
                st.line_chart(df, x=x_axis, y=y_axis)
            except Exception as e:
                st.error(f"チャート描画エラー: {e}")
        else:
            st.warning("X軸とY軸を選択してください。")
    else:
        st.warning("可視化には少なくとも2つの列が必要です。")
else:
    st.warning("まず「データアップロード」ページでデータをアップロードしてください。")
    st.page_link("pages/01_📈_Data_Upload.py", label="データアップロードページへ", icon="📈")