"""
Streamlit demo

    "matplotlib>=3.10.3",
    "pandas>=2.2.3",
    "plotly>=6.1.0",
    "pydeck>=0.9.1",
    "streamlit>=1.45.1",

uv add ... が必要

"""


import streamlit as st
st.title("My First Streamlit App")
st.write("Hello, Streamlit!")


## Magicコマンド"
import pandas as pd
df = pd.DataFrame({'col1':[1, 2], 'col2':[3, 4]})
df # st.write(df) と同様
  
  
# 4. 表示系ウィジェット: テキスト"
st.title("タイトル")
st.header("ヘッダー")
st.subheader("サブヘッダー")
st.write("通常のテキストや変数を表示")
st.markdown("Markdownも使えます: **太字**, *イタリック*")
st.caption("これはキャプション（注釈）です")
st.code("print('Hello, World!')", language='python')
st.latex(r''' e^{i\pi} + 1 = 0 ''')


# 表示系ウィジェット: データ
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(10, 5), columns=('col %d' % i for i in range(5)))
st.dataframe(df) # インタラクティブ
st.table(df.head()) # 静的

# JSON
st.json({'foo': 'bar', 'baz': 'qux'})

# Metric
st.metric(label="気温", value="25 °C", delta="1.5 °C")

# 表示系ウィジェット: メディア

#(ローカルファイル or URL)
try:
  st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit Logo", width=300)
except:
  st.warning("画像の読み込みに失敗しました。")

#音声 (ローカルファイル or URL)
st.audio("audio.mp3")

#動画 (ローカルファイル or URL)
st.video("video.mov")

# 5. 入力系ウィジェット: ボタン

# 通常ボタン
if st.button("クリックしてください"):
    st.write("ボタンがクリックされました！")

# ダウンロードボタン
data = "これはダウンロードされるテキストデータです。"
st.download_button(
    label="テキストファイルをダウンロード",
    data=data,
    file_name="sample.txt",
    mime="text/plain"
)

# リンクボタン
st.link_button("Streamlit公式サイトへ", "https://streamlit.io")


# 入力系ウィジェット: 選択 (単一)

# チェックボックス
agree = st.checkbox("利用規約に同意します")
if agree:
    st.write("同意ありがとうございます！")

# ラジオボタン
genre = st.radio(
    "好きな映画のジャンルは？",
    ('コメディ', 'ドラマ', 'ドキュメンタリー'),
    index=None # デフォルト未選択
)
if genre:
    st.write(f"{genre}を選びましたね。")


# 入力系ウィジェット: 選択 (複数)

# セレクトボックス (ドロップダウン)
option = st.selectbox(
    "連絡方法は？",
    ('メール', '電話', 'Slack'),
    placeholder="選択してください..."
)
st.write(f"選択: {option}")

# マルチセレクト
options = st.multiselect(
    "好きな色を教えてください",
    ['緑', '黄', '赤', '青'],
    ['黄', '赤'] # デフォルト選択
)
st.write("選択:", options)

## 入力系ウィジェット: テキスト入力

# 1行テキスト入力
name = st.text_input("名前を入力してください", placeholder="山田 太郎")
if name:
    st.write(f"こんにちは、{name}さん！")

# パスワード入力
password = st.text_input("パスワード", type="password")

# 複数行テキスト入力
feedback = st.text_area("フィードバックをお願いします", height=150)



## 入力系ウィジェット: 数値・日時入力


import datetime

# 数値入力
age = st.number_input("年齢を入力してください", min_value=0, max_value=120, value=25, step=1)
st.write(f"年齢: {age}歳")

# 日付入力
d = st.date_input("誕生日を選択してください", datetime.date(2000, 1, 1))
st.write('誕生日:', d)

# 時間入力
t = st.time_input('会議の時間を設定してください', datetime.time(9, 00))
st.write('会議時間:', t)


## 入力系ウィジェット: スライダー


# 数値スライダー
level = st.slider("レベルを選択", 0, 100, 50)
st.write(f"選択したレベル: {level}")

# 範囲スライダー
price_range = st.slider(
    "価格帯を選択",
    min_value=0, max_value=10000, value=(1000, 5000), step=100
)
st.write("選択した価格帯:", price_range)

# セレクトスライダー (離散値)
color = st.select_slider(
    '好きな色を選択',
    options=['赤', 'オレンジ', '黄', '緑', '青', '紫']
)
st.write('好きな色:', color)


## 入力系ウィジェット: その他


import pandas as pd

# カラーピッカー
color = st.color_picker('テーマカラーを選択', '#00f900')
st.write('選択した色:', color)

# ファイルアップローダー
uploaded_file = st.file_uploader("CSVファイルをアップロード", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("アップロードされたデータ:")
    st.dataframe(df.head())




## 6. レイアウト: サイドバー


# サイドバーに要素を追加
add_selectbox = st.sidebar.selectbox(
    "連絡方法は？",
    ("メール", "自宅電話", "携帯電話")
)

add_slider = st.sidebar.slider(
    "範囲を選択してください",
    0.0, 100.0, (25.0, 75.0)
)

st.write("メインコンテンツエリア")
st.write(f"サイドバーの選択: {add_selectbox}")
st.write(f"サイドバーのスライダー: {add_slider}")



## レイアウト: カラム (横並び)


import numpy as np

st.header("カラムレイアウト")

col1, col2, col3 = st.columns(3) # 3つの均等なカラム

with col1:
   st.write("ここは最初のカラムです。")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.write("ここは中央のカラムです。")
   st.line_chart(np.random.randn(10, 1))

with col3:
   st.write("ここは最後のカラムです。")
   st.button("カラム3のボタン")


## レイアウト: タブ


import numpy as np

st.header("タブレイアウト")

tab1, tab2, tab3 = st.tabs(["📈 チャート", "🗃 データ", "📝 説明"])

with tab1:
   st.header("チャートタブ")
   st.line_chart(np.random.randn(20, 3))

with tab2:
   st.header("データタブ")
   st.dataframe(np.random.randn(20, 3))

with tab3:
   st.header("説明タブ")
   st.write("これはタブ機能のデモンストレーションです。")
   st.image("https://static.streamlit.io/examples/owl.jpg")



## レイアウト: エキスパンダー (折りたたみ)


st.header("エキスパンダー")
st.bar_chart({"data":[1,5,2,6,2,1]})

with st.expander("詳細を見る"):
     st.write("""
         このチャートはランダムなデータを表示しています。
         エキスパンダーを使うことで、詳細情報を隠しておき、
         ユーザーが必要な時に展開できるようにします。
     """)
     st.image("https://static.streamlit.io/examples/dice.jpg")



## レイアウト: コンテナ


import time

st.header("コンテナ")


st.write("1行目")
st.write("")
container = st.container()
st.write("")
st.write("2行目")

time.sleep(5)

container.write("3行目")
container.write("4行目")

# レイアウト: 空の要素 (`st.empty`)


import time

st.header("st.empty: 動的更新")

placeholder = st.empty() # 空のプレースホルダーを作成

# プレースホルダーに要素を追加
placeholder.text("処理を開始します...")
time.sleep(2)

# プレースホルダーの内容を上書き
placeholder.text("処理中です... 50%")
time.sleep(2)

# さらに上書き
placeholder.success("処理が完了しました！")
st.button("完了ボタン") # emptyの後にも要素を追加できる

## 7. グラフ・チャート: 基本チャート


import pandas as pd
import numpy as np

st.header("Streamlit組み込みチャート")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

# ラインチャート
st.subheader("ラインチャート")
st.line_chart(chart_data)

# エリアチャート
st.subheader("エリアチャート")
st.area_chart(chart_data)

# バーチャート
st.subheader("バーチャート")
st.bar_chart(chart_data)

# グラフ・チャート: Matplotlib

import matplotlib.pyplot as plt
import numpy as np

st.header("Matplotlib")

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
ax.set_title("Matplotlib Histogram")

st.pyplot(fig)


## グラフ・チャート: Plotly

import plotly.express as px
import pandas as pd

st.header("Plotly")

df = px.data.iris() # Plotly組み込みデータセット
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Plotly Scatter Plot")

st.plotly_chart(fig, use_container_width=True)


## グラフ・チャート: Altair

import altair as alt
import pandas as pd
import numpy as np

st.header("Altair")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)



## グラフ・チャート: 地図 (Pydeck)


import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.header("地図 (Pydeck)")

# 東京駅周辺のランダムな点を生成
chart_data = pd.DataFrame(
   np.random.randn(100, 2) /[100,100] + [35.68, 139.76],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None, # or 'mapbox://styles/mapbox/light-v9' など
    initial_view_state=pdk.ViewState(
        latitude=35.68,
        longitude=139.76,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=100,
           elevation_scale=4,
           elevation_range=[1000],
           pickable=True,
           extruded=True,
        ),
    ],
))

### なぜSession Stateが必要か？ (復習)

# counter_bad.py
# st.title('カウンター (問題あり)')
# count = 0 # リランのたびに0に初期化される

# increment = st.button('増加')
# if increment:
#     count += 1

# st.write('カウント = ', count) # クリックしても常に1になる


### Session Stateの初期化


# # 'count' が session_state になければ 0 で初期化
# if 'count' not in st.session_state:
#     st.session_state['count'] = 0
#     # または st.session_state.count = 0

# st.write("初期化後のSession State:", st.session_state)


# ### Session Stateの値の読み書き

# if 'my_value' not in st.session_state:
#     st.session_state['my_value'] = "Initial Value"

# # 値の読み取り
# current_value = st.session_state['my_value']
# st.write(f"現在の値: {current_value}")

# # 値の書き込み (更新)
# if st.button("値を更新"):
#     st.session_state.my_value = "Updated Value!"
#     # または st.session_state['my_value'] = "Updated Value!"

### Session Stateを使ったカウンターアプリ (改善版)

# st.title('カウンター (Session State使用)')

# # 'count' が session_state になければ 0 で初期化
# if 'count' not in st.session_state:
#     st.session_state.count = 0 

# increment = st.button('増加')
# if increment:
#     st.session_state.count += 1 # Session Stateの値を更新

# st.write('カウント = ', st.session_state.count) # Session Stateの値を表示


### Session Stateとウィジェットの状態連携

# ウィジェットに `key` 引数を指定すると、そのウィジェットの状態が Session State に自動的に保存・同期される。

# st.title("ウィジェットとSession Stateの連携")

# # スライダーに key を設定
# temp_c = st.slider(
#     "温度 (°C)",
#     min_value=-50.0, max_value=50.0, value=25.0, step=0.1,
#     key="celsius" # このキーで Session State に保存される
# )

# # Session State を使ってスライダーの値を取得・表示
# st.write(f"Session Stateから取得した温度: {st.session_state.celsius} °C")

### Session Stateとウィジェット連携の注意点

# ウィジェットの状態は、Session State API を使って直接設定（書き込み）することはできない**。
# ウィジェットの状態を読み取ることは可能。

# これはエラーになる例
# if 'my_button_state' not in st.session_state:
#     st.session_state.my_button_state = True # ボタンの状態は設定できない

# st.button('エラーになるボタン', key='my_button_state') 
# # -> StreamlitAPIException

# # 読み取りは可能
# if st.button("クリックして状態確認", key="confirm_button"):
#     st.write(f"ボタンの状態 (押されたか): {st.session_state.confirm_button}")

### Session Stateの応用例: ユーザー入力の保持

# st.title("ユーザー入力の保持")

# # Session State の初期化
# if 'user_name' not in st.session_state:
#     st.session_state.user_name = "" 

# name = st.text_input("名前を入力してください", key="user_name_input")

# # Session State に入力値を保存 
# # この例では、次のリランで text_input が st.session_state.user_name を使う
# st.session_state.user_name = name

# if st.session_state.user_name:
#     st.write(f"こんにちは、{st.session_state.user_name} さん！")
# else:
#     st.write("まだ名前が入力されていません。")

### Session Stateの応用例: 簡易認証(1)

# # Session State の初期化
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False

# # Session State の初期化
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False

# def login():
#     # 実際の認証処理 (ここでは簡略化)
#     if st.session_state.username == "user" and st.session_state.password == "pass":
#         st.session_state.logged_in = True
#     else:
#         st.error("ユーザー名またはパスワードが違います")

# def logout():
#     st.session_state.logged_in = False
#     # 他のセッション情報もクリアすることが望ましい
#     # st.session_state.username = "" など

# if not st.session_state.logged_in:
#     st.text_input("ユーザー名", key="username")
#     st.text_input("パスワード", type="password", key="password")
#     st.button("ログイン", on_click=login)
# # --- ログイン後画面 ---
# else:
#     st.write(f"ようこそ、{st.session_state.username} さん！")
#     st.button("ログアウト", on_click=logout)

### Session State の中身を確認

# # Session State は辞書ライクなオブジェクトなので、そのまま表示できる。

# if 'counter' not in st.session_state:
#     st.session_state.counter = 0
# if 'text' not in st.session_state:
#     st.session_state.text = "Hello"

# st.session_state.counter += 1
# st.text_input("テキスト", key="text")

# st.write("現在のSession State:")
# st.write(st.session_state) # そのまま表示
# # またはマジックコマンドで:
# # st.session_state

### Session Stateのキーの削除

# Pythonの辞書と同様に `del` を使って削除できる。


# if 'temp_data' not in st.session_state:
#     st.session_state.temp_data = "一時的なデータ"

# st.write("削除前のSession State:", st.session_state)

# if st.button("一時データを削除"):
#     if 'temp_data' in st.session_state:
#         del st.session_state['temp_data']
#         st.success("一時データを削除しました。")
#     else:
#         st.warning("一時データは既に存在しません。")

# st.write("削除後のSession State:", st.session_state)

### コールバック関数とSession State (詳細)

# # コールバック関数: テキスト入力が変更されたら呼ばれる
# def update_text():
#     st.session_state.text_value = st.session_state.my_text_input.upper()
 
# if "text_value" not in st.session_state:
#     st.session_state.text_value = ""
    
# # テキスト入力ウィジェットに key と on_change を設定
# st.text_input(
#     "テキストを入力 (入力後にEnterかフォーカスを外すとコールバック実行):",
#     key="my_text_input", # Session Stateに値を保存するキー
#     on_change=update_text # 値が変更されたときに呼び出す関数
# )

# st.write(f"Session State に保存されたテキスト: {st.session_state.text_value}")

### コールバック引数 (`args`, `kwargs`)

#- コールバック関数に追加の引数を渡すことができる。

# if 'count' not in st.session_state:
#     st.session_state.count = 0

# def increment_counter(increment_value):
#     st.session_state.count += increment_value
#     st.info(f"{increment_value} だけ増加しました！")

# def set_value(key, value):
#     st.session_state[key] = value
#     st.info(f"キー '{key}' に値 '{value}' を設定しました。")

# # args を使用
# st.button("+1", on_click=increment_counter, args=(1,))
# st.button("+5", on_click=increment_counter, args=(5,))

# # kwargs を使用
# st.button("カウンターを0にリセット", on_click=set_value, 
#           kwargs={'key': 'count', 'value': 0})

# st.write(f"現在のカウント: {st.session_state.count}")

### `st.cache_data` : データ計算結果のキャッシュ(1)

# - **主な用途:** DataFrameの処理、Numpy配列の計算、APIからのデータ取得など、**シリアライズ可能（pickle化可能）なデータオブジェクト**を返す関数の結果をキャッシュする。
# - デコレータ `@st.cache_data` を関数に付与する。

# import time
# import pandas as pd
# import numpy as np
# @st.cache_data # データ処理関数にデコレータを付与
# def fetch_and_clean_data(url):
#     st.write(f"データを取得中: {url}") # このメッセージは初回のみ表示されるはず
#     time.sleep(3) # 時間のかかる処理をシミュレート
#     df = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
#     # (実際にはここで pd.read_csv(url) や前処理を行う)
#     return df

# st.title("st.cache_data のデモ")

# data_url_1 = "http://example.com/data1.csv"
# data_url_2 = "http://example.com/data2.csv"

# st.subheader("データセット1")
# if st.button("データ1をロード"):
#     df1 = fetch_and_clean_data(data_url_1) # 同じ引数ならキャッシュが返る
#     st.dataframe(df1)

# st.subheader("データセット2")
# if st.button("データ2をロード"):
#     df2 = fetch_and_clean_data(data_url_2) # 引数が違うので再計算される
#     st.dataframe(df2)

# st.subheader("再度データセット1")
# if st.button("データ1を再度ロード"):
#     df1_again = fetch_and_clean_data(data_url_1) # キャッシュが使われるはず
#     st.dataframe(df1_again)
#     st.success("キャッシュからロードされました！ (取得中のメッセージは表示されない)")


### `st.cache_resource` : リソースのキャッシュ

# - **主な用途:** 機械学習モデル、データベース接続、TensorFlowセッションなど、**シリアライズできない、またはグローバルに共有したいリソース**をキャッシュする。
# - デコレータ `@st.cache_resource` を関数に付与する。

# import time
# @st.cache_resource # リソース読み込み関数にデコレータを付与
# def load_heavy_model(model_path):
#     st.write(f"モデルをロード中: {model_path}") # このメッセージは初回のみ表示されるはず
#     time.sleep(5) # 重いモデルのロードをシミュレート
#     # model = load_model(model_path) # 実際のモデルロード処理
#     model = f"LOADED::{model_path}" # ダミーのモデルオブジェクト
#     return model

# st.title("st.cache_resource のデモ")

# model_path = "path/to/my/model.h5"

# st.subheader("機械学習モデル")
# if st.button("モデルをロード/使用"):
#     model = load_heavy_model(model_path) # 同じ引数ならキャッシュが返る
#     st.write(f"使用中のモデル: {model}")
#     # st.write(model.summary()) # 実際のモデル操作など

# st.subheader("再度モデルを使用")
# if st.button("モデルを再度ロード/使用"):
#     model_again = load_heavy_model(model_path) # キャッシュが使われるはず
#     st.write(f"再度取得したモデル: {model_again}")
#     st.success("キャッシュからロードされました！ (ロード中のメッセージは表示されない)")


### キャッシュのクリア
# import time
# @st.cache_data
# def get_current_time_cached():
#     st.write("関数実行: 現在時刻を取得中...")
#     time.sleep(1)
#     return time.time()

# st.title("キャッシュのクリア")

# st.write(f"キャッシュされた時刻: {time.ctime(get_current_time_cached())}")

# if st.button("キャッシュをクリア (st.cache_data)"):
#     st.cache_data.clear() # st.cache_data でキャッシュされた全関数をクリア
#     st.success("st.cache_data のキャッシュをクリアしました！")
#     st.rerun() # ページを再読み込みして効果を確認


### キャッシュのパラメータ(1)
# import time
# import random
# # TTL (Time To Live): 60秒間だけキャッシュを有効にする
# @st.cache_data(ttl=60)
# def get_data_with_ttl():
#     st.write("TTL付き関数実行中...")
#     time.sleep(1)
#     return random.randint(1, 1000)

# # max_entries: 最新5件の結果のみキャッシュ
# @st.cache_data(max_entries=5)
# def get_data_with_max_entries(param):
#     st.write(f"max_entries付き関数実行中 (param={param})...")
#     time.sleep(1)
#     return f"Data for {param} is {random.random()}"

# # show_spinner: キャッシュミス時に関数実行中にスピナーを表示
# @st.cache_data(show_spinner="重いデータを計算中...")
# def expensive_computation():
#     time.sleep(3)
#     return "計算結果"

# st.title("キャッシュパラメータ")

# st.subheader("TTL (Time To Live)")
# st.write(f"データ (60秒有効): {get_data_with_ttl()}")

# st.subheader("Max Entries")
# entry_param = st.number_input("パラメータ (1-10)", 1, 10, 1)
# st.write(f"データ (最新5件): {get_data_with_max_entries(entry_param)}")

# st.subheader("Show Spinner")
# if st.button("重い計算を実行"):
#     result = expensive_computation()
#     st.write(f"結果: {result}")


### フォームの基本的な使い方(1)

# 'my_form' というキーでフォームを作成
# with st.form(key='my_form'):
#     st.write("以下の項目を入力してください。")
#     name = st.text_input("名前")
#     age = st.number_input("年齢", min_value=0, max_value=120, step=1)
#     fav_color = st.selectbox("好きな色", ["赤", "青", "緑"])
#     feedback = st.text_area("ご意見・ご感想")

#     # フォーム専用の送信ボタン
#     submitted = st.form_submit_button("送信")
    
# if submitted:
#     st.success("フォームが送信されました！")
#     st.write("--- 入力内容 ---")
#     st.write(f"名前: {name}")
#     st.write(f"年齢: {age}")
#     st.write(f"好きな色: {fav_color}")
#     st.write(f"フィードバック: {feedback}")
#     # ここで入力データを使った処理（DB保存、メール送信など）を行う
# else:
#     st.info("フォームを入力して送信ボタンを押してください。")