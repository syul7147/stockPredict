import FinanceDataReader as fdr
import mplfinance as mpf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#Marcap(시가총액) 순으로 정렬
def getSymbols(market='KOSPI', sort='Marcap'):
    df = fdr.StockListing(market)
    ascending = False if sort == 'Marcap' else True # 내림차순
    df.sort_values(by=[sort], ascending = ascending, inplace=True)
    return df[ ['Code', 'Name', 'Market'] ]

code = '005930'              # 삼성전자.
df = fdr.DataReader(code, '2023-10-10')

# 시총 상위 10
print(getSymbols().head(10))

# 캔들차트를 출력해 본다.
chart_style = 'classic'           # 'default', 'binance', 'classic', 'yahoo', 등 중에서 선택.
marketcolors = mpf.make_marketcolors(up='red', down='blue')         # 양봉/음봉 선택.

# 차트 스타일
mpf_style = mpf.make_mpf_style(base_mpf_style=chart_style, marketcolors=marketcolors)

fig, ax = mpf.plot(
    data=df,                            # 받아온 데이터.      
    volume=True,                       # True 또는 False.                   
    type='candle',                      # 캔들 차트.
    style=mpf_style,                    # 위에서 정의.
    figsize=(10,7),
    fontscale=1.1,
    mav=(5,10,20),                      # 이동평균선 (mav) 3개.
    mavcolors=('red','green','blue'),   # 이동평균선 색상.
    returnfig=True                      # Figure 객체 반환.
)

plt.show()