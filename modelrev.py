# MODEL REVENUE ACCURACY -----------------------------------------------------






import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from scipy.optimize import minimize
import numpy as np
import plotly.express as px
import streamlit as st

# STREAMLIT TITLE --------------------------------------------------------------------------------------------------
st.header('Tracker Penghasilan', divider='rainbow')

# Time of maximizng
with st.sidebar:
  jangka_revenue = st.selectbox(
      "Berikan jangka waktu analisa",
      ("1 Minggu", "1 Bulan", "1 Triwulan", "1 Tahun"))
  
jangka_revenue = 0

if jangka_revenue == "1 Minggu" :
  jangka_revenue = 8

if jangka_revenue == "1 Bulan" :
  jangka_revenue = 31

if jangka_revenue == "4 Bulan" :
  jangka_revenue = 91

if jangka_revenue == "1 Tahun" :
  jangka_revenue = 366

gsheetkey_rev = "1ToBs4foOAW6tuXFTgntxwisnCIfu48jalpQS0M-RWcI"
url_rev = f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey_rev}&output=csv'
df_rev = pd.read_csv(url_rev)
df_rev = df_rev.dropna()
df_rev = df_rev.tail(jangka_revenue)
#df_rev

st.write("Berikut adalah link untuk log dataset")
st.code("https://docs.google.com/spreadsheet/ccc?key=1ToBs4foOAW6tuXFTgntxwisnCIfu48jalpQS0M-RWcI")

# Regression value
gsheetkey_mkt = "1u-h4_J3VadEzbnfwbMLzTQ3QsJxEYGvsVPjKmY1GUjU"
url_mkt = f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey_mkt}&output=csv'
df_mkt = pd.read_csv(url_mkt)
df_mkt = df_mkt.dropna()
df_mkt = df_mkt.tail(jangka_revenue)
#df_mkt

x_mkt = df_mkt.drop(['Sales'], axis=1)
y_mkt = df_mkt['Sales']

xmkt_train, xmkt_test, ymkt_train, ymkt_test = train_test_split(x_mkt,y_mkt, test_size=0.2, random_state=2)

modelmkt = LinearRegression()
modelmkt.fit(xmkt_train, ymkt_train)

coefficients = modelmkt.coef_
intercept = modelmkt.intercept_

coef = pd.DataFrame(zip(x_mkt.columns,coefficients), columns = ['channel', 'coefficients'])

def objective(x):
    return - 1 * (coefficients[0] * x[0] + coefficients[1] * x[1] + coefficients[2] * x[2] + coefficients[3] * x[3] + coefficients[4] * x[4] + intercept)
def constraint(x):
    return 60000 - (coefficients[0] * x[0] + coefficients[1] * x[1] + coefficients[2] * x[2] + coefficients[3] * x[3] + coefficients[4] * x[4] + intercept)
x0 = np.array([1/5, 1/5, 1/5, 1/5, 1/5])

solution = minimize(objective, x0, constraints = {'type': 'eq', 'fun': constraint})

sales = -(solution.fun)
ayam = coefficients[0] * solution.x[0] / sales
daging = coefficients[1] * solution.x[1] / sales
cumi = coefficients[2] * solution.x[2]/ sales
telur = coefficients[3] * solution.x[3]/ sales
sosis = coefficients[4] * solution.x[4]/ sales

# STREAMLIT INPUT PRED --------------------------------------------------------------------------------------------------
st.write("Masukkan modal ayam")
number_1 = st.number_input("Masukkan budget")

st.write("Masukkan modal daging")
number_2 = st.number_input("Masukkan budget")

st.write("Masukkan modal cumi")
number_3 = st.number_input("Masukkan budget")

st.write("Masukkan modal telur")
number_4 = st.number_input("Masukkan budget")

st.write("Masukkan modal sosis")
number_5 = st.number_input("Masukkan budget")

if number != 0 :
  xmkt_predict = [[number_1, number_2, number_3, number_4, number_5]]
  ymkt_predict = modelmkt.predict(xmkt_predict)
  ymkt_predict

if number_1 != 0 and number_2 != 0 and number_3 != 0 and number_4 != 0 and number_5 != 0:
  st.subheader(f'Prediksi revenue adalah {ymkt_predict}', divider='rainbow')

df_sales = df_rev[["Sales"]]
df_sales = df_sales.tail(jangka_revenue)
#df_sales

url_rev = f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey_rev}&output=csv'
df_rev = pd.read_csv(url_rev)
df_rev = df_rev.dropna()
df_rev = df_rev.tail(jangka_revenue)
#df_rev

df_ayam = df_rev[["Ayam"]]
df_ayam = df_ayam.tail(jangka_revenue)
#df_ayam

df_daging = df_rev[["Daging"]]
df_daging = df_daging.tail(jangka_revenue)
#df_daging

df_cumi = df_rev[["Cumi"]]
df_cumi = df_cumi.tail(jangka_revenue)
#df_cumi

df_telur = df_rev[["Telur"]]
df_telur = df_telur.tail(jangka_revenue)
#df_telur

df_sosis = df_rev[["Sosis"]]
df_sosis = df_sosis.tail(jangka_revenue)
#df_sosis

hari = jangka_revenue - 1

fig_sales = px.line(df_sales, x=df_rev.index, y="Sales", title=f'Grafik penghasilan selama {hari} hari')
st.plotly_chart(fig_sales, theme="streamlit")

real_ayam = df_ayam.sum()
real_daging = df_daging.sum()
real_cumi = df_cumi.sum()
real_telur = df_telur.sum()
real_sosis = df_sosis.sum()

real_ayam = int(real_ayam)
real_daging = int(real_daging)
real_cumi = int(real_cumi)
real_telur = int(real_telur)
real_sosis = int(real_sosis)

st.subheader('Jumlah yang direkomendasikan', divider='rainbow')
st.write(f"Jumlah Ayam yang direkomendasikan adalah {real_ayam}")
st.write(f"Jumlah Daging yang direkomendasikan adalah {real_daging}")
st.write(f"Jumlah Cumi yang direkomendasikan adalah {real_cumi}")
st.write(f"Jumlah Telur yang direkomendasikan adalah {real_telur}")
st.write(f"Jumlah Sosis yang direkomendasikan adalah {real_sosis}")

xmkt_predict = [[real_ayam, real_daging, real_cumi, real_telur, real_sosis]]
ymkt_predict = modelmkt.predict(xmkt_predict)
ymkt_predict

st.subheader(f'Hasil prediksi adalah :blue[{ymkt_predict}]')

st.subheader(f'Hasil asli adalah :blue[{final_sales_value}]')

accuracy = ymkt_predict / final_sales_value * 100
st.subheader(f'Akurasi model adalah {accuracy}%')