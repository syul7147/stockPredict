# 주식가격 시계열 예측 - 자기회귀 (AR).

# 필요한 라이브러리를 불러온다.    
import FinanceDataReader as fdr
import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from datetime import datetime, timedelta
# pip install scikit-learn
from sklearn.linear_model import LinearRegression              # 선형회귀 모형.
warnings.filterwarnings("ignore")                              # 성가신 warning을 꺼준다.
   
# 시장 데이터를 읽어오는 함수들을 정의한다.
def getData(code, datestart, dateend):
  df = fdr.DataReader(code, datestart, dateend ).drop(columns='Change')  
  return df

def getSymbols(market='KOSPI', sort='Marcap'):
  df = fdr.StockListing(market)
  ascending = False if sort == 'Marcap' else True
  df.sort_values(by=[sort], ascending = ascending, inplace=True)
  return df[['Code', 'Name', 'Market']]

# code에 해당하는 주식 데이터를 받아온다.
code = '005930'              # 삼성전자.
#code = '373220'             # LG 에너지솔루션.
date_start = (datetime.today()-timedelta(days=100)).date()          # 시분초 떼어내고 년월일 날짜만.
df = getData(code, date_start, datetime.today().date())     

# 캔들차트를 출력해 본다 (이동평균 없이).
chart_style = 'classic'   # 'default', 'binance', 'classic', 'yahoo', 등 중에서 선택.
marketcolors = mpf.make_marketcolors(up='red', down='blue')         # 양봉/음봉 선택.
mpf_style = mpf.make_mpf_style(base_mpf_style=chart_style, marketcolors=marketcolors)

fig, ax = mpf.plot(
    data=df,                            # 받아온 데이터.      
    volume=True,                       # True 또는 False.                   
    type='candle',                      # 캔들 차트.
    style=mpf_style,                    # 위에서 정의.
    figsize=(10,7),
    fontscale=1.1,
    returnfig=True                      # Figure 객체 반환.
)

# 여기에서 예측선을 추가한다. 
n = len(df)                 # 시계열의 길이.
pred_ndays = 10             # 미래 예측 기간.


print(df['Close'].reset_index(drop=True))
print(df['Close'].shape)
print('-----------')
print(df[['Close']].shape)
print('---------------')
df=df[["Close"]].reset_index(drop=True)
df['m1'] = df["Close"].shift(1) #t-1 값
df['m2'] = df["Close"].shift(2) #t-2 값
df['m3'] = df["Close"].shift(3) #t-3 값
df['m4'] = df["Close"].shift(4) #t-4 값
df['m5'] = df["Close"].shift(5) #t-5 값
print (df.head(10))

df = df.iloc[5:] # 결측치가 없는 부분부터 사용하기 위해 슬라이싱
print(df)

model = LinearRegression()
model.fit(df[['m1','m2','m3','m4','m5']],df['Close'])

# 선형회귀 기반 AR(5)모형 예측.
rdf =df['Close'][-5:]

for step in range(pred_ndays):                      # 미래 예측.
    past = pd.DataFrame(data={ f'm{i}': [rdf.iloc[-i]] for i in range(1,6)} ) 
    predicted = model.predict(past)[0]  
    print("----", pd.Series({n + step:predicted}))
    rdf = pd.concat( [rdf, pd.Series({n + step:predicted})])

print(rdf)

# ax에 추가하기
ax[0].plot(rdf, color='green',marker='o',linestyle='--',linewidth=1.5,label='AR(5)')
ax[0].legend(loc='best')

plt.show()


# df = df[['Close']].reset_index(drop=True)      

# 선형회귀 기반 AR(5)모형 학습.

# 선형회귀 기반 AR(5)모형 예측.


# plt.show()