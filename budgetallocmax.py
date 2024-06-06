import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from scipy.optimize import minimize
import numpy as np
import plotly.express as px
import streamlit as st

# STREAMLIT TITLE --------------------------------------------------------------------------------------------------

st.header('Prediksi hasil penjualan dari modal', divider='rainbow')

st.write("Halaman ini merupakan hasil prediksi dari modal yang dimasukkan oleh pengusaha. AI akan membuat constraint paling efektif untuk memaksimalkan penghasilan berdasarkan regresi matematis dan Machine Learning. Terdapat banyak periode yang dapat dipilih, untuk menguji efektivitas dari waktu ke waktu")
st.write("")
st.write("Database dapat diakses di :")
st.code("https://docs.google.com/spreadsheet/ccc?key=1u-h4_J3VadEzbnfwbMLzTQ3QsJxEYGvsVPjKmY1GUjU")

# Time of maximizng
with st.sidebar:
  st.subheader("Masukan jangka waktu", divider='rainbow')
  option_max = st.selectbox(
      "Berikan jangka waktu analisa",
      ("1 Minggu", "1 Bulan", "1 Triwulan", "1 Tahun"))
  st.write("Tolong masukkan terlebih dahulu agar dapat diproses")

period_max = 0

if option_max == "1 Minggu" :
  period_max = 8

if option_max == "1 Bulan" :
  period_max = 31

if option_max == "1 Triwulan" :
  period_max = 91

if option_max == "1 Tahun" :
  period_max = 366

if period_max != 0 :
  gsheetkey_mkt = "1u-h4_J3VadEzbnfwbMLzTQ3QsJxEYGvsVPjKmY1GUjU"
  url_mkt = f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey_mkt}&output=csv'
  df_mkt = pd.read_csv(url_mkt)
  df_mkt = df_mkt.dropna()
  df_mkt = df_mkt.tail(period_max)
  #df_mkt

# Dataset of everything besides sales
x_mkt = df_mkt.drop(['Sales'], axis=1)
y_mkt = df_mkt['Sales']

xmkt_train, xmkt_test, ymkt_train, ymkt_test = train_test_split(x_mkt,y_mkt, test_size=0.2, random_state=2)

modelmkt = LinearRegression()
modelmkt.fit(xmkt_train, ymkt_train)

coefficients = modelmkt.coef_
intercept = modelmkt.intercept_

coef = pd.DataFrame(zip(x_mkt.columns,coefficients), columns = ['channel', 'coefficients'])

# Plot effectivity of coefficient
st.subheader('Efektivitas Modal', divider='rainbow')

if period_max != 0 :
  fig_corr = px.histogram(coef, x="channel", y="coefficients")
  fig_corr.update_layout(bargap=0.2)
  st.plotly_chart(fig_corr, theme="streamlit")

ayamreq = coefficients[0]
dagingreq = coefficients[1]
cumireq = coefficients[2]
telurreq = coefficients[3]
sosisreq = coefficients[4]

ayamtext = f"Skala efektivitas dari Ayam adalah {coefficients[0]}"
dagingtext = f"Skala efektivitas dari Daging adalah {coefficients[1]}"
cumitext = f"Skala efektivitas dari Cumi adalah {coefficients[2]}"
telurtext = f"Skala efektivitas dari Telur adalah {coefficients[3]}"
sosistext = f"Skala efektivitas dari Sosis adalah {coefficients[4]}"

coeffinal = ayamtext + "\n" + "\n" + dagingtext + "\n" + "\n" + cumitext + "\n" + "\n" + telurtext + "\n" + "\n" + sosistext 

st.code(coeffinal)

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

# STREAMLIT Input the Budget -----------------------------------------------------------------------------------------------------------
with st.sidebar:
  st.subheader('Masukkan jumlah budget', divider='rainbow')
  budget = st.number_input("Input jumlah budget")
  budget = int(budget)
  st.write("Tolong masukkan terlebih dahulu agar dapat diproses")

# ----------------------------------------------------------------------------------------------------------------

item1 = "-"
item2 = "-"
item3 = "-"
item4 = "-"
item5 = "-"
item6 = "-"
item7 = "-"
item8 = "-"
item9 = "-"
item10 = "-"
item11 = "-"
item12 = "-"
item13 = "-"
item14 = "-"
item15 = "-"

price1 = 0
price2 = 0
price3 = 0
price4 = 0
price5 = 0
price6 = 0
price7 = 0
price8 = 0
price9 = 0
price10 = 0
price11 = 0
price12 = 0
price13 = 0
price14 = 0
price15 = 0

quantity1 = 0
quantity2 = 0
quantity3 = 0
quantity4 = 0
quantity5 = 0
quantity6 = 0
quantity7 = 0
quantity8 = 0
quantity9 = 0
quantity10 = 0
quantity11 = 0
quantity12 = 0
quantity13 = 0
quantity14 = 0
quantity15 = 0

total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3
total4 = price4 * quantity4
total5 = price5 * quantity5
total6 = price6 * quantity6
total7 = price7 * quantity7
total8 = price8 * quantity8
total9 = price9 * quantity9
total10 = price10 * quantity10
total11 = price11 * quantity11
total12 = price12 * quantity12
total13 = price13 * quantity13
total14 = price14 * quantity14
total15 = price15 * quantity15

if budget != 0:
  item1 = "Ayam"
  item2 = "Daging"
  item3 = "Cumi"
  item4 = "Telur"
  item5 = "Sosis"
  price1 = ayam * budget
  price2 = daging * budget
  price3 = cumi * budget
  price4 = telur * budget
  price5 = sosis * budget
  quantity1 = 1
  quantity2 = 1
  quantity3 = 1
  quantity4 = 1
  quantity5 = 1
  total1 = price1 * quantity1
  total2 = price2 * quantity2
  total3 = price3 * quantity3
  total4 = price4 * quantity1
  total5 = price5 * quantity1

# list of name, degree, score
itemname_sheet = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15]
price_sheet = [price1, price2, price3, price4, price5, price6, price7, price8, price9, price10, price11, price12, price13, price14, price15]
quantity_sheet = [quantity1, quantity2, quantity3, quantity4, quantity5, quantity6, quantity7, quantity8, quantity9, quantity10, quantity11, quantity12, quantity13, quantity14, quantity15]
total_sheet = [total1, total2, total3, total4, total5, total6, total7, total8, total9, total10, total11, total12, total13, total14, total15]

# dictionary of lists
budgetsheet = {'Item': itemname_sheet, 'Recommended Budget': price_sheet, 'Quantity' : quantity_sheet, 'Total Budget' : total_sheet}

st.header('Rekomendasi alokasi budget', divider='rainbow')

df = pd.DataFrame(budgetsheet)
filter = df['Item'].str.contains("-")
filtered_df = df[~filter]
filtered_df

maxayam = ayam * 100 
maxdaging = daging * 100
maxcumi = cumi * 100
maxtelur = telur * 100
maxsosis = sosis * 100

maxayamtext = f"Sebaiknya {maxayam}% dari dana dialokasikan untuk Ayam"
maxdagingtext = f"Sebaiknya {maxdaging}% dari dana dialokasikan untuk Daging"
maxcumitext = f"Sebaiknya {maxcumi}% dari dana dialokasikan untuk Cumi"
maxtelurtext = f"Sebaiknya {maxtelur}% dari dana dialokasikan untuk Telur"
maxsosistext = f"Sebaiknya {maxsosis}% dari dana dialokasikan untuk Sosis"

maxthingsfinal = maxayamtext + "\n" + "\n" + maxdagingtext + "\n" + "\n" + maxcumitext + "\n" + "\n" + maxtelurtext + "\n" + "\n" + maxsosistext
st.code(maxthingsfinal) 

if budget != 0:
  budget1 = filtered_df.iloc[0, 1]
  budget1 = int(budget1)
  budget2 = filtered_df.iloc[1, 1]
  budget2 = int(budget2)
  budget3 = filtered_df.iloc[2, 1]
  budget3 = int(budget3)
  budget4 = filtered_df.iloc[3, 1]
  budget4 = int(budget4)
  budget5 = filtered_df.iloc[4, 1]
  budget5 = int(budget5)

if budget != 0:
  xmkt_predict = [[budget1, budget2, budget3, budget4, budget5]]  # Social Media, Radio, TV
  ymkt_predict = modelmkt.predict(xmkt_predict)

if budget != 0:
  gross_revenue = ymkt_predict[0]
  cost = budget1 + budget2 + budget3 + budget4 + budget5
  profit = gross_revenue - cost

if budget != 0:
  st.subheader(f"Prediksi penghasilan kotor adalah :blue[{gross_revenue}]")
  st.subheader(f"Prediksi profit adalah :blue[{profit}]")