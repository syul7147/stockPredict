import streamlit as st
import time

def getData(name,age,gender):
    data = {'이름':name, '나이':age, '성별':gender}
    time.sleep(3)
    return data

e = st.empty()

with st.form(key='myForm',clear_on_submit=True): #clear_on_submit=True 이면 submit후 form데이터 모두 삭제
    name = st.text_input('이름은 ?')
    age = st.slider('나이는 ?',1,100,20)
    gender = st.radio('성별은?',['남','여'])
    submitted = st.form_submit_button('확인')
    if submitted:
        e.write(getData(name,age,gender))

