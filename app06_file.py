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

myFile = st.file_uploader("엑셀 파일을 선택하세요!!")
out = st.empty()
#openpyxl 설치
# pip install openpyxl



if myFile:
    out.write("xlse 파일 한개를 업로드 했습니다.")
    df = pd.read_excel(myFile, engine="openpyxl")
    st.write(df)

myFile2 = st.file_uploader("CSV 파일을 선택하세요")

out2 = st.empty()

if myFile2:
    out.write("CSV 파일 한개를 업로드 했습니다.")
    cdf = pd.read_csv(myFile2)
    st.write(cdf)

