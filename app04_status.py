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
import time
st.progress(value=30)

# 눈송이 특수효과
# st.snow()
# st.balloons()
''
'---'
''
st.error('에러 메세지')
st.success('성공 메세지')
st.warning('경고 메세지')
st.info('공지 메세지')
''
'---'
''
# st.spinner(text='실행중 .....')
with st.spinner(text='실행중 .....'):
    time.sleep(3.0)
    st.success('실행완료!!')

