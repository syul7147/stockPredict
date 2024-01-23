import streamlit as st
import time

# session_state : 딕셔너리

# session 초기화
if 'cnt' not in st.session_state:
    st.session_state['cnt']= 0


x = st.empty()

col1, col2, _ = st.columns([1,1,5])
# col1.button('+1')
if col1.button('+1'):
    st.session_state['cnt'] +=1
if col2.button('clear'):
    st.session_state['cnt']=0

x.write(f'Counter = {st.session_state["cnt"]}')

''
'---'
''
e = st.empty()

# if st.button('Show Form'):
    # with st.form(key='myForm',clear_on_submit=True):
    #     name = st.text_input('이름은 ?')
    #     age = st.slider('나이는 ?',1,100,20)
    #     gender = st.radio('성별은?',['남','여'])
    #     submitted = st.form_submit_button('확인')
    #     if submitted:
    #         e.write({'이름':name, '나이':age, '성별':gender})

#######################################
# session_state.keys() : 세션의 키값들
def hasClicked():
    if 'clicked' in st.session_state.keys():
        return True
    else:
        return False

if hasClicked:
    with st.form(key='myForm',clear_on_submit=True):
        name = st.text_input('이름은 ?')
        age = st.slider('나이는 ?',1,100,20)
        gender = st.radio('성별은?',['남','여'])
        submitted = st.form_submit_button('확인')
        if submitted:
            e.write({'이름':name, '나이':age, '성별':gender})
else:
    if st.button('Show Form'):
        st.session_state['clicked'] = True
        st.experimental_rerun()
