# 가상환경 생성하기
# conda create -n st python=3.9.13

# 가상환경 삭제하기
# conda env remove -n st

# 가상환경 활성/비활성화
# conda activate st <-- 활성
# conda deactivate <-- 비활성

# streamlit 1.19버전 설치하기
# pip install streamlit==1.19.0

# ModuleNotFoundError: No module named 'altair.vegalite.v4'
# pip uninstall altair
# pip install altair==4.2.2

#실행하기 
# streamlit run 파일명(예>app01_text.py)

#실행중지 : ctrl + c 


import streamlit as st

#sidebar
# st.sidebar.title("스트림릿 연습")
# st.sidebar.header("스트림릿 연습")
# st.sidebar.subheader("스트림릿 연습")
# st.sidebar.write('''
# ---
# '''
# )
# z = st.sidebar.selectbox('선택하세요',["짜장면","짬뽕"])
# st.sidebar.write(f'선택메뉴 = {z}')
with st.sidebar:
    st.title("스트림릿 연습")
    st.header("스트림릿 연습")
    st.subheader("스트림릿 연습")
    st.write('''
---
    '''
    )
    z = st.selectbox('선택하세요',["짜장면","짬뽕"])
    st.write(f'선택메뉴 = {z}')

col1,col2,col3 = st.columns(3)
with col1:
    st.header(':blue[제목 1]')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with col2:
    st.header(':blue[제목 2]')
    st.image('https://static.streamlit.io/examples/dog.jpg')
with col3:
    st.header(':blue[제목 3]')
    st.image('https://static.streamlit.io/examples/owl.jpg')

''
'---'
''
tap1,tap2,tap3 = st.tabs(['cat','dog','owl'])

with tap1:
    st.header(':blue[야옹]')
    st.image('https://static.streamlit.io/examples/cat.jpg')
with tap2:
    st.header(':blue[멍멍]')
    st.image('https://static.streamlit.io/examples/dog.jpg')
with tap3:
    st.header(':blue[부엉]')
    st.image('https://static.streamlit.io/examples/owl.jpg')

''
'---'
''

#tap과 컬럼 혼용
tap1,tap2 = st.tabs(['왼쪽','오른쪽'])
with tap1:
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header(':blue[제목 1]')
        st.image('https://static.streamlit.io/examples/cat.jpg')
    with col2:
        st.header(':blue[제목 2]')
        st.image('https://static.streamlit.io/examples/dog.jpg')
    with col3:
        st.header(':blue[제목 3]')
        st.image('https://static.streamlit.io/examples/owl.jpg')
with tap2:
    col1,col2,col3 = st.columns([1,1,3])
    with col1:
        st.header(':blue[제목 1]')
        st.image('https://static.streamlit.io/examples/cat.jpg')
    with col2:
        st.header(':blue[제목 2]')
        st.image('https://static.streamlit.io/examples/dog.jpg')
    with col3:
        st.header(':blue[제목 3]')
        st.image('https://static.streamlit.io/examples/owl.jpg')

''
'---'
''

a = st.expander('Expander')
a.write('멍멍 사진')
a.image('https://static.streamlit.io/examples/dog.jpg')

''
'---'
''
# 특정 장소에 하나의 요소를 출력할 공간을 만들어 줌
b = st.empty()
b.write('**start** 버튼을 누르세요')

c1,c2,c3,x = st.columns([1,1,1,5])
start = c1.button('start',key=1)
clear = c2.button('clear',key=2)
reset = c3.button('reset',key=3)
import time
if start:
    with b:
        for i in range(6):
            t = 5-i
            st.write(f'카운트 다운 {t}초')
            time.sleep(1)

if clear:
    b.empty()

''
'---'
''

c = st.container()

c.write('**start** 버튼을 누르세요')

cc1,cc2,cc3,_ = st.columns([1,1,1,5])
start = cc1.button('start',key=4)
clear = cc2.button('clear',key=5)
reset = cc3.button('reset',key=6)
import time
if start:
    with c:
        for i in range(6):
            t = 5-i
            st.write(f'카운트 다운 {t}초')
            time.sleep(1)

if clear:
    c.empty()