# pip install finance-datareader
# pip install bs4
# pip install plotly

import streamlit as st
import FinanceDataReader as fdr

df = fdr.StockListing('KOSPI')
# print(df.head())
print(df)
st.dataframe(df)

# 삼성전자
code = '005930'
code = '005380' # 현대차

# DataReader(코드번호, 시작날짜, 종료날짜)
# df = fdr.DataReader(code)
df = fdr.DataReader(code, "2024")
# print(df)
st.dataframe(df.sort_values(by=['Date'], ascending=False))
''
'---'
''
# 환율정보
df = fdr.DataReader("USD/KRW", "2024-01-01", "2024-01-18")
# df = fdr.DataReader("USD/JPY", "2024-01-01")
print(df)
st.dataframe(df)

import matplotlib.pyplot as plt
# df['Close'].plot()
# plt.show()

fig = plt.figure(figsize=(7, 5))
plt.plot(df.Close)
plt.xticks(rotation=90)
st.pyplot(fig)

print(df.index)

# Date, 인덱스
list_x = []
for idx in df.index:
    list_x.append(idx)

list_y = []
for Close in df.Close:
    list_y.append(Close) 

import seaborn as sns
fig2 = plt.figure(figsize=(11, 5))
sns.lineplot(x='Date', y='Close', marker='o', data=df, color='r')
plt.xticks(list_x, rotation=90)
st.pyplot(fig2)

fig3 = plt.figure(figsize=(11, 5))

########### lineplot에 모든 종가 출력하기
for i in range(len(list_x)):
    cValue = df.Close[i]    
    plt.text(df.index[i], cValue, '%.1f' %cValue, ha='center', va='bottom', size=12)

sns.lineplot(x='Date', y='Close', marker='o', data=df, color='r')
plt.xticks(list_x, rotation=90)
st.pyplot(fig3)
# plt.show()

########### lineplot에 최대값 출력하기
fig4 = plt.figure(figsize=(11, 5))

# {종가:날짜, 종가:날짜,.....}
dic = {y:x for x, y in zip(df.index, df.Close)}

print("키",max(dic)) # 종가 최대값
print("값",dic[max(dic)]) 

sns.lineplot(x='Date', y='Close', marker='o', data=df, color='r')
plt.text(dic[max(dic)], max(dic), '%.1f' %max(dic), ha='center', va='bottom', size=12)
plt.xticks(list_x, rotation=90)
st.pyplot(fig4)



















# 비트코인
df = fdr.DataReader("BTC/KRW", "2024")
st.dataframe(df.sort_values(by='Date', ascending=False))








