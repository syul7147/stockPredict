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
import pandas as pd

df = pd.DataFrame(data = {"col1":[100,200,300],
             "col2":['aa','bb','cc']})

st.write(df)
st.dataframe(df)
st.table(df)

# JSON데이터 출력
st.json({'name':'홍길동','age':22,'gender':'male'})

# Metric() 함수를 이용한 데이터 출력(변화가 있는 데이터)
st.metric(label='온도',value='13℃')
st.metric(label='카카오뱅크',value='55,000',delta='-1000')

# 이미지 데이터
st.image("ref.jpeg",width=100)