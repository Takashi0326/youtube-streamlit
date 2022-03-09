import streamlit as st 
import numpy as np 
import pandas as pd 
from PIL import Image
import time

st.title('Streamlit 超入門')

#st.write('Interactive Widgets')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expandar1 = st.expander('問い合わせ')
expandar1.write('1の問い合わせを開く')

expandar2 = st.expander('問い合わせ')
expandar2.write('2の問い合わせを開く')


# text = st.text_input('あなたの趣味を教えて下さい。')
# condition = st.slider('あなたの調子は？', 0, 100, 50)

# 'あなたの趣味は：', text
# 'コンディション：', condition


# st.sidebar.write('Interactive Widgets')

# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# condition = st.sidebar.slider('あなたの調子は？', 0, 100, 50)


# condition = st.slider('あなたの今の調子は', 0, 100, 50)
# 'コンディション', condition

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は', text, 'です。'

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

# 'あなたの好きな数字は', option, 'です'


# if st.checkbox('Show Image'):
#     img = Image.open('cat.jpg')
#     st.image(img, caption='cat', use_column_width=True)