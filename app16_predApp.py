#
# 주식가격 시계열 예측 앱.

# 필요한 라이브러리를 불러온다.
import streamlit as st
import FinanceDataReader as fdr
import mplfinance as mpf
import pandas as pd
import warnings
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression              # 선형회귀 모형.
warnings.filterwarnings("ignore")                              # 성가신 warning을 꺼준다.

# 자기회귀(AR) 예측을 추가해 주는 함수.
def addARPrediction(data, ax, pred_ndays):
    n = len(data)
# 그래프 출력에 유리한 형태로 데이터프레임 변환.
    df = data[ ['Close'] ].reset_index(drop=True)      # Pandas의 DataFrame 객체.     
    df['m1'] = df['Close'].shift(1)                    # t-1 값.
    df['m2'] = df['Close'].shift(2)                    # t-2 값.
    df['m3'] = df['Close'].shift(3)                    # t-3 값.
    df['m4'] = df['Close'].shift(4)                    # t-4 값.
    df['m5'] = df['Close'].shift(5)                    # t-5 값.     
    df = df.iloc[5:]

# 선형회귀 기반  AR(5)모형 학습.
    model = LinearRegression()
    model.fit(df[['m1','m2','m3','m4','m5']], df['Close'])
# 선형회귀 기반  AR(5)모형 예측.
    rdf = df['Close'][-5:]                             # 데이터 최신 5개 값.
    for step in range(pred_ndays):                     # 미래 예측.
        past = pd.DataFrame(data={ f'm{i}': [rdf.iloc[-i]] for i in range(1,6)} ) # 최신 5개값으로 데이터프레임을 만든다.
        predicted = model.predict(past)[0]                                        # 예측 결과는 원소가 1개인 데이터프레임.
        rdf = pd.concat( [rdf, pd.Series({n + step:predicted}) ])
    
    ax.plot(rdf, color = 'red', marker='o', linestyle ='--', linewidth=1.5, label = 'AR(5)')
    ax.legend(loc='best')    


st.title('주식 추세 예측')

# 시장 데이터를 읽어오는 함수들을 정의한다.
@st.cache_data
def getData(code, datestart, dateend):
    df = fdr.DataReader(code,datestart, dateend ).drop(columns='Change')  # 불필요한 'Change' 컬럼은 버린다.
    return df

@st.cache_data
def getSymbols(market='KOSPI', sort='Marcap'):
    df = fdr.StockListing(market)
    ascending = False if sort == 'Marcap' else True
    df.sort_values(by=[sort], ascending= ascending, inplace=True)
    return df[ ['Code', 'Name', 'Market'] ]

# 세션 상태를 초기화 한다.
if 'ndays' not in st.session_state:
    st.session_state['ndays'] = 30

if 'code_index' not in st.session_state:
    st.session_state['code_index'] = 0

if 'chart_style' not in st.session_state:
    st.session_state['chart_style'] = 'default'

if 'volume' not in st.session_state:
    st.session_state['volume'] = True

if 'pred_ndays' not in st.session_state:
    st.session_state['pred_ndays'] = 5

# 사이드바에서 폼을 통해서 차트 인자를 설정한다.
with st.sidebar.form(key="chartsetting", clear_on_submit=True):
    st.header('차트 설정')
    ''
    ''
    symbols = getSymbols()
    choices = zip( symbols.Code , symbols.Name , symbols.Market )
    choices = [ ' : '.join( x ) for x in choices ]  # Code, Name, Market을 한개의 문자열로.
    choice = st.selectbox( label='종목:', options = choices, index=st.session_state['code_index'] )
    code_index = choices.index(choice)
    code = choice.split()[0]                        # 실제 code 부분만 떼어 가져온다.
    ''
    ''
    ndays = st.slider(
        label='데이터 기간 (days):', 
        min_value= 20,
        max_value= 365, 
        value=st.session_state['ndays'],
        step = 1)
    ''
    ''
    chart_styles = ['default', 'binance', 'blueskies', 'brasil', 'charles', 'checkers', 'classic', 'yahoo','mike', 'nightclouds', 'sas', 'starsandstripes']
    chart_style = st.selectbox(label='차트 스타일:',options=chart_styles,index = chart_styles.index(st.session_state['chart_style']))
    ''
    ''
    volume = st.checkbox('거래량', value=st.session_state['volume'])

    '---'

    pred_ndays = st.slider(
        label='예측 기간 (days):', 
        min_value= 1,
        max_value= 10, 
        value=st.session_state['pred_ndays'],
        step = 1)
    
    '---'
    
    if st.form_submit_button(label="OK"):
        st.session_state['ndays'] = ndays
        st.session_state['code_index'] = code_index
        st.session_state['chart_style'] = chart_style
        st.session_state['volume'] = volume
        st.session_state['pred_ndays'] = pred_ndays
        st.experimental_rerun()
    

# 캔들 차트 위에 예측선 출력 
def plotChart(data, pred_ndays):
    chart_style = st.session_state['chart_style']
    marketcolors = mpf.make_marketcolors(up='red', down='blue')
    mpf_style = mpf.make_mpf_style(base_mpf_style= chart_style, marketcolors=marketcolors)

    fig, ax = mpf.plot(
        data,
        volume=st.session_state['volume'],
        type='candle',
        style=mpf_style,
        figsize=(10,7),
        fontscale=1.1,
        returnfig=True                  # Figure 객체 반환.
    )

    addARPrediction(data, ax[0], pred_ndays)        # AR 예측.
    st.pyplot(fig)


date_start = (datetime.today()-timedelta(days=st.session_state['ndays'])).date()
df = getData(code, date_start, datetime.today().date())     

chart_title = choices[st.session_state['code_index'] ]
st.markdown(f'<h3 style="text-align: center; color: red;">{chart_title}</h3>', unsafe_allow_html=True)

plotChart(df, st.session_state['pred_ndays'])