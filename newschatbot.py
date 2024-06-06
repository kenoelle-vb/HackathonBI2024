# MODEL REVENUE ACCURACY --------------------------------------------------------








# IMPORT FOR NEWS SCRAPING
from bs4 import BeautifulSoup
#import streamlit as st
import requests
import tk as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import nltk
from langchain_groq import ChatGroq
import os
from groq import Groq
nltk.download('punkt')
#from google.colab import userdata

# IMPORT FOR CHATBOT
import langchain
from groq import Groq
from langchain_groq import ChatGroq
from langchain_community.chat_models import ChatOllama
import streamlit as st

category = "makro" #makro, regulator, nasional, rileks, informasi
regulator = "regulator"
nasional = "nasional"
rileks = "rileks"
informasi = "informasi"

# STREAMLIT INPUT NEWS TYPE ---------------------------------------------------------------------

progress_text = "Mohon ditunggu...."
progress_bar = st.progress(0, text=progress_text)

for percentage_complete in range(100):
    progress_bar.progress(percentage_complete + 1, text=progress_text)

with st.sidebar:
  newstype = st.selectbox(
      "Masukkan Tipe Berita : ",
      ("Keadaan Ekonomi", "Regulasi", "Indonesia", "Sosial", "General"), placeholder="Masukkan Tipe Berita......")

with st.sidebar:
  newstime = st.selectbox(
      "Masukkan waktu ",
      ("Minggu ini", "Bulan ini", "Tahun ini"), placeholder="Masukkan terkini...")

run = 0

time1 = 1
time2 = 2
time3 = 3
time4 = 4
time5 = 5

if newstime == "Minggu ini" :
  time1 = 1
  time2 = 2
  time3 = 3
  time4 = 4
  time5 = 5

if newstime == "Bulan ini" :
  time1 = 3
  time2 = 6
  time3 = 9
  time4 = 12
  time5 = 15

if newstime == "Tahun ini" :
  time1 = 20
  time2 = 40
  time3 = 60
  time4 = 80
  time5 = 100

category1 = time1
category2 = time2
category3 = time3
category4 = time4
category5 = time5

regulator1 = time1
regulator2 = time2
regulator3 = time3
regulator4 = time4
regulator5 = time5

nasional1 = time1
nasional2 = time2
nasional3 = time3
nasional4 = time4
nasional5 = time5

rileks1 = time1
rileks2 = time2
rileks3 = time3
rileks4 = time4
rileks5 = time5

informasi1 = time1
informasi2 = time2
informasi3 = time3
informasi4 = time4
informasi5 = time5

# MAKRO -------------------------------------------------------------------------------------------------

urlcategory = f"https://www.emitennews.com/category/{category}/{category1}"
webcontent = requests.get(urlcategory).text
soupcategory = BeautifulSoup(webcontent, "lxml")
linkcategory = soupcategory.find("a", class_ = 'news-card-2 search-result-item')
linkcategory = str(linkcategory)
substr1category = "href="
substr2category = '<div'
idxs1category = linkcategory.index(substr1category)
idxs2category = linkcategory.index(substr2category)
resxcategory = ""
for idxscategory in range(idxs1category + len(substr1category) + 1, idxs2category):
  resxcategory = resxcategory + linkcategory[idxscategory]
  resx1category = resxcategory[:-2]

urlcategory = f"https://www.emitennews.com/category/{category}/{category2}"
webcontent = requests.get(urlcategory).text
soupcategory = BeautifulSoup(webcontent, "lxml")
linkcategory = soupcategory.find("a", class_ = 'news-card-2 search-result-item')
linkcategory = str(linkcategory)
substr1category = "href="
substr2category = '<div'
idxs1category = linkcategory.index(substr1category)
idxs2category = linkcategory.index(substr2category)
resxcategory = ""
for idxscategory in range(idxs1category + len(substr1category) + 1, idxs2category):
  resxcategory = resxcategory + linkcategory[idxscategory]
  resx2category = resxcategory[:-2]

urlcategory = f"https://www.emitennews.com/category/{category}/{category3}"
webcontent = requests.get(urlcategory).text
soupcategory = BeautifulSoup(webcontent, "lxml")
linkcategory = soupcategory.find("a", class_ = 'news-card-2 search-result-item')
linkcategory = str(linkcategory)
substr1category = "href="
substr2category = '<div'
idxs1category = linkcategory.index(substr1category)
idxs2category = linkcategory.index(substr2category)
resxcategory = ""
for idxscategory in range(idxs1category + len(substr1category) + 1, idxs2category):
  resxcategory = resxcategory + linkcategory[idxscategory]
  resx3category = resxcategory[:-2]

urlcategory = f"https://www.emitennews.com/category/{category}/{category4}"
webcontent = requests.get(urlcategory).text
soupcategory = BeautifulSoup(webcontent, "lxml")
linkcategory = soupcategory.find("a", class_ = 'news-card-2 search-result-item')
linkcategory = str(linkcategory)
substr1category = "href="
substr2category = '<div'
idxs1category = linkcategory.index(substr1category)
idxs2category = linkcategory.index(substr2category)
resxcategory = ""
for idxscategory in range(idxs1category + len(substr1category) + 1, idxs2category):
  resxcategory = resxcategory + linkcategory[idxscategory]
  resx4category = resxcategory[:-2]

urlcategory = f"https://www.emitennews.com/category/{category}/{category5}"
webcontent = requests.get(urlcategory).text
soupcategory = BeautifulSoup(webcontent, "lxml")
linkcategory = soupcategory.find("a", class_ = 'news-card-2 search-result-item')
linkcategory = str(linkcategory)
substr1category = "href="
substr2category = '<div'
idxs1category = linkcategory.index(substr1category)
idxs2category = linkcategory.index(substr2category)
resxcategory = ""
for idxscategory in range(idxs1category + len(substr1category) + 1, idxs2category):
  resxcategory = resxcategory + linkcategory[idxscategory]
  resx5category = resxcategory[:-2]

# REGULATOR --------------------------------------------------------------------------------------------------------------------

urlregulator = f"https://www.emitennews.com/category/{regulator}/{regulator1}"
webcontent = requests.get(urlregulator).text
soupregulator = BeautifulSoup(webcontent, "lxml")
linkregulator = soupregulator.find("a", class_ = 'news-card-2 search-result-item')
linkregulator = str(linkregulator)
substr1regulator = "href="
substr2regulator = '<div'
idxs1regulator = linkregulator.index(substr1regulator)
idxs2regulator = linkregulator.index(substr2regulator)
resxregulator = ""
for idxsregulator in range(idxs1regulator + len(substr1regulator) + 1, idxs2regulator):
  resxregulator = resxregulator + linkregulator[idxsregulator]
  resx1regulator = resxregulator[:-2]

urlregulator = f"https://www.emitennews.com/category/{regulator}/{regulator2}"
webcontent = requests.get(urlregulator).text
soupregulator = BeautifulSoup(webcontent, "lxml")
linkregulator = soupregulator.find("a", class_ = 'news-card-2 search-result-item')
linkregulator = str(linkregulator)
substr1regulator = "href="
substr2regulator = '<div'
idxs1regulator = linkregulator.index(substr1regulator)
idxs2regulator = linkregulator.index(substr2regulator)
resxregulator = ""
for idxsregulator in range(idxs1regulator + len(substr1regulator) + 1, idxs2regulator):
  resxregulator = resxregulator + linkregulator[idxsregulator]
  resx2regulator = resxregulator[:-2]

urlregulator = f"https://www.emitennews.com/category/{regulator}/{regulator3}"
webcontent = requests.get(urlregulator).text
soupregulator = BeautifulSoup(webcontent, "lxml")
linkregulator = soupregulator.find("a", class_ = 'news-card-2 search-result-item')
linkregulator = str(linkregulator)
substr1regulator = "href="
substr2regulator = '<div'
idxs1regulator = linkregulator.index(substr1regulator)
idxs2regulator = linkregulator.index(substr2regulator)
resxregulator = ""
for idxsregulator in range(idxs1regulator + len(substr1regulator) + 1, idxs2regulator):
  resxregulator = resxregulator + linkregulator[idxsregulator]
  resx3regulator = resxregulator[:-2]

urlregulator = f"https://www.emitennews.com/category/{regulator}/{regulator4}"
webcontent = requests.get(urlregulator).text
soupregulator = BeautifulSoup(webcontent, "lxml")
linkregulator = soupregulator.find("a", class_ = 'news-card-2 search-result-item')
linkregulator = str(linkregulator)
substr1regulator = "href="
substr2regulator = '<div'
idxs1regulator = linkregulator.index(substr1regulator)
idxs2regulator = linkregulator.index(substr2regulator)
resxregulator = ""
for idxsregulator in range(idxs1regulator + len(substr1regulator) + 1, idxs2regulator):
  resxregulator = resxregulator + linkregulator[idxsregulator]
  resx4regulator = resxregulator[:-2]

urlregulator = f"https://www.emitennews.com/category/{regulator}/{regulator5}"
webcontent = requests.get(urlregulator).text
soupregulator = BeautifulSoup(webcontent, "lxml")
linkregulator = soupregulator.find("a", class_ = 'news-card-2 search-result-item')
linkregulator = str(linkregulator)
substr1regulator = "href="
substr2regulator = '<div'
idxs1regulator = linkregulator.index(substr1regulator)
idxs2regulator = linkregulator.index(substr2regulator)
resxregulator = ""
for idxsregulator in range(idxs1regulator + len(substr1regulator) + 1, idxs2regulator):
  resxregulator = resxregulator + linkregulator[idxsregulator]
  resx5regulator = resxregulator[:-2]

# NASIONAL --------------------------------------------------------------------------------------------------------------------

urlnasional = f"https://www.emitennews.com/category/{nasional}/{nasional1}"
webcontent = requests.get(urlnasional).text
soupnasional = BeautifulSoup(webcontent, "lxml")
linknasional = soupnasional.find("a", class_ = 'news-card-2 search-result-item')
linknasional = str(linknasional)
substr1nasional = "href="
substr2nasional = '<div'
idxs1nasional = linknasional.index(substr1nasional)
idxs2nasional = linknasional.index(substr2nasional)
resxnasional = ""
for idxsnasional in range(idxs1nasional + len(substr1nasional) + 1, idxs2nasional):
  resxnasional = resxnasional + linknasional[idxsnasional]
  resx1nasional = resxnasional[:-2]

urlnasional = f"https://www.emitennews.com/category/{nasional}/{nasional2}"
webcontent = requests.get(urlnasional).text
soupnasional = BeautifulSoup(webcontent, "lxml")
linknasional = soupnasional.find("a", class_ = 'news-card-2 search-result-item')
linknasional = str(linknasional)
substr1nasional = "href="
substr2nasional = '<div'
idxs1nasional = linknasional.index(substr1nasional)
idxs2nasional = linknasional.index(substr2nasional)
resxnasional = ""
for idxsnasional in range(idxs1nasional + len(substr1nasional) + 1, idxs2nasional):
  resxnasional = resxnasional + linknasional[idxsnasional]
  resx2nasional = resxnasional[:-2]

urlnasional = f"https://www.emitennews.com/category/{nasional}/{nasional3}"
webcontent = requests.get(urlnasional).text
soupnasional = BeautifulSoup(webcontent, "lxml")
linknasional = soupnasional.find("a", class_ = 'news-card-2 search-result-item')
linknasional = str(linknasional)
substr1nasional = "href="
substr2nasional = '<div'
idxs1nasional = linknasional.index(substr1nasional)
idxs2nasional = linknasional.index(substr2nasional)
resxnasional = ""
for idxsnasional in range(idxs1nasional + len(substr1nasional) + 1, idxs2nasional):
  resxnasional = resxnasional + linknasional[idxsnasional]
  resx3nasional = resxnasional[:-2]

urlnasional = f"https://www.emitennews.com/category/{nasional}/{nasional4}"
webcontent = requests.get(urlnasional).text
soupnasional = BeautifulSoup(webcontent, "lxml")
linknasional = soupnasional.find("a", class_ = 'news-card-2 search-result-item')
linknasional = str(linknasional)
substr1nasional = "href="
substr2nasional = '<div'
idxs1nasional = linknasional.index(substr1nasional)
idxs2nasional = linknasional.index(substr2nasional)
resxnasional = ""
for idxsnasional in range(idxs1nasional + len(substr1nasional) + 1, idxs2nasional):
  resxnasional = resxnasional + linknasional[idxsnasional]
  resx4nasional = resxnasional[:-2]

urlnasional = f"https://www.emitennews.com/category/{nasional}/{nasional5}"
webcontent = requests.get(urlnasional).text
soupnasional = BeautifulSoup(webcontent, "lxml")
linknasional = soupnasional.find("a", class_ = 'news-card-2 search-result-item')
linknasional = str(linknasional)
substr1nasional = "href="
substr2nasional = '<div'
idxs1nasional = linknasional.index(substr1nasional)
idxs2nasional = linknasional.index(substr2nasional)
resxnasional = ""
for idxsnasional in range(idxs1nasional + len(substr1nasional) + 1, idxs2nasional):
  resxnasional = resxnasional + linknasional[idxsnasional]
  resx5nasional = resxnasional[:-2]

# RILEKS -------------------------------------------------------------------------------------------------------------------

urlrileks = f"https://www.emitennews.com/category/{rileks}/{rileks1}"
webcontent = requests.get(urlrileks).text
souprileks = BeautifulSoup(webcontent, "lxml")
linkrileks = souprileks.find("a", class_ = 'news-card-2 search-result-item')
linkrileks = str(linkrileks)
substr1rileks = "href="
substr2rileks = '<div'
idxs1rileks = linkrileks.index(substr1rileks)
idxs2rileks = linkrileks.index(substr2rileks)
resxrileks = ""
for idxsrileks in range(idxs1rileks + len(substr1rileks) + 1, idxs2rileks):
  resxrileks = resxrileks + linkrileks[idxsrileks]
  resx1rileks = resxrileks[:-2]

urlrileks = f"https://www.emitennews.com/category/{rileks}/{rileks2}"
webcontent = requests.get(urlrileks).text
souprileks = BeautifulSoup(webcontent, "lxml")
linkrileks = souprileks.find("a", class_ = 'news-card-2 search-result-item')
linkrileks = str(linkrileks)
substr1rileks = "href="
substr2rileks = '<div'
idxs1rileks = linkrileks.index(substr1rileks)
idxs2rileks = linkrileks.index(substr2rileks)
resxrileks = ""
for idxsrileks in range(idxs1rileks + len(substr1rileks) + 1, idxs2rileks):
  resxrileks = resxrileks + linkrileks[idxsrileks]
  resx2rileks = resxrileks[:-2]

urlrileks = f"https://www.emitennews.com/category/{rileks}/{rileks3}"
webcontent = requests.get(urlrileks).text
souprileks = BeautifulSoup(webcontent, "lxml")
linkrileks = souprileks.find("a", class_ = 'news-card-2 search-result-item')
linkrileks = str(linkrileks)
substr1rileks = "href="
substr2rileks = '<div'
idxs1rileks = linkrileks.index(substr1rileks)
idxs2rileks = linkrileks.index(substr2rileks)
resxrileks = ""
for idxsrileks in range(idxs1rileks + len(substr1rileks) + 1, idxs2rileks):
  resxrileks = resxrileks + linkrileks[idxsrileks]
  resx3rileks = resxrileks[:-2]

urlrileks = f"https://www.emitennews.com/category/{rileks}/{rileks4}"
webcontent = requests.get(urlrileks).text
souprileks = BeautifulSoup(webcontent, "lxml")
linkrileks = souprileks.find("a", class_ = 'news-card-2 search-result-item')
linkrileks = str(linkrileks)
substr1rileks = "href="
substr2rileks = '<div'
idxs1rileks = linkrileks.index(substr1rileks)
idxs2rileks = linkrileks.index(substr2rileks)
resxrileks = ""
for idxsrileks in range(idxs1rileks + len(substr1rileks) + 1, idxs2rileks):
  resxrileks = resxrileks + linkrileks[idxsrileks]
  resx4rileks = resxrileks[:-2]

urlrileks = f"https://www.emitennews.com/category/{rileks}/{rileks5}"
webcontent = requests.get(urlrileks).text
souprileks = BeautifulSoup(webcontent, "lxml")
linkrileks = souprileks.find("a", class_ = 'news-card-2 search-result-item')
linkrileks = str(linkrileks)
substr1rileks = "href="
substr2rileks = '<div'
idxs1rileks = linkrileks.index(substr1rileks)
idxs2rileks = linkrileks.index(substr2rileks)
resxrileks = ""
for idxsrileks in range(idxs1rileks + len(substr1rileks) + 1, idxs2rileks):
  resxrileks = resxrileks + linkrileks[idxsrileks]
  resx5rileks = resxrileks[:-2]

# INFORMASI ---------------------------------------------------------------------------------------------------------------

urlinformasi = f"https://www.emitennews.com/category/{informasi}/{informasi1}"
webcontent = requests.get(urlinformasi).text
soupinformasi = BeautifulSoup(webcontent, "lxml")
linkinformasi = soupinformasi.find("a", class_ = 'news-card-2 search-result-item')
linkinformasi = str(linkinformasi)
substr1informasi = "href="
substr2informasi = '<div'
idxs1informasi = linkinformasi.index(substr1informasi)
idxs2informasi = linkinformasi.index(substr2informasi)
resxinformasi = ""
for idxsinformasi in range(idxs1informasi + len(substr1informasi) + 1, idxs2informasi):
  resxinformasi = resxinformasi + linkinformasi[idxsinformasi]
  resx1informasi = resxinformasi[:-2]

urlinformasi = f"https://www.emitennews.com/category/{informasi}/{informasi2}"
webcontent = requests.get(urlinformasi).text
soupinformasi = BeautifulSoup(webcontent, "lxml")
linkinformasi = soupinformasi.find("a", class_ = 'news-card-2 search-result-item')
linkinformasi = str(linkinformasi)
substr1informasi = "href="
substr2informasi = '<div'
idxs1informasi = linkinformasi.index(substr1informasi)
idxs2informasi = linkinformasi.index(substr2informasi)
resxinformasi = ""
for idxsinformasi in range(idxs1informasi + len(substr1informasi) + 1, idxs2informasi):
  resxinformasi = resxinformasi + linkinformasi[idxsinformasi]
  resx2informasi = resxinformasi[:-2]

urlinformasi = f"https://www.emitennews.com/category/{informasi}/{informasi3}"
webcontent = requests.get(urlinformasi).text
soupinformasi = BeautifulSoup(webcontent, "lxml")
linkinformasi = soupinformasi.find("a", class_ = 'news-card-2 search-result-item')
linkinformasi = str(linkinformasi)
substr1informasi = "href="
substr2informasi = '<div'
idxs1informasi = linkinformasi.index(substr1informasi)
idxs2informasi = linkinformasi.index(substr2informasi)
resxinformasi = ""
for idxsinformasi in range(idxs1informasi + len(substr1informasi) + 1, idxs2informasi):
  resxinformasi = resxinformasi + linkinformasi[idxsinformasi]
  resx3informasi = resxinformasi[:-2]

urlinformasi = f"https://www.emitennews.com/category/{informasi}/{informasi4}"
webcontent = requests.get(urlinformasi).text
soupinformasi = BeautifulSoup(webcontent, "lxml")
linkinformasi = soupinformasi.find("a", class_ = 'news-card-2 search-result-item')
linkinformasi = str(linkinformasi)
substr1informasi = "href="
substr2informasi = '<div'
idxs1informasi = linkinformasi.index(substr1informasi)
idxs2informasi = linkinformasi.index(substr2informasi)
resxinformasi = ""
for idxsinformasi in range(idxs1informasi + len(substr1informasi) + 1, idxs2informasi):
  resxinformasi = resxinformasi + linkinformasi[idxsinformasi]
  resx4informasi = resxinformasi[:-2]

urlinformasi = f"https://www.emitennews.com/category/{informasi}/{informasi5}"
webcontent = requests.get(urlinformasi).text
soupinformasi = BeautifulSoup(webcontent, "lxml")
linkinformasi = soupinformasi.find("a", class_ = 'news-card-2 search-result-item')
linkinformasi = str(linkinformasi)
substr1informasi = "href="
substr2informasi = '<div'
idxs1informasi = linkinformasi.index(substr1informasi)
idxs2informasi = linkinformasi.index(substr2informasi)
resxinformasi = ""
for idxsinformasi in range(idxs1informasi + len(substr1informasi) + 1, idxs2informasi):
  resxinformasi = resxinformasi + linkinformasi[idxsinformasi]
  resx5informasi = resxinformasi[:-2]

# URLs ----------------------------------------------------------------------------------------------------------------------

url1category = resx1category
url2category = resx2category
url3category = resx3category
url4category = resx4category
url5category = resx5category

url1regulator = resx1regulator
url2regulator = resx2regulator
url3regulator = resx3regulator
url4regulator = resx4regulator
url5regulator = resx5regulator

url1nasional = resx1nasional
url2nasional = resx2nasional
url3nasional = resx3nasional
url4nasional = resx4nasional
url5nasional = resx5nasional

url1rileks = resx1rileks
url2rileks = resx2rileks
url3rileks = resx3rileks
url4rileks = resx4rileks
url5rileks = resx5rileks

url1informasi = resx1informasi
url2informasi = resx2informasi
url3informasi = resx3informasi
url4informasi = resx4informasi
url5informasi = resx5informasi

# DOWNLOADING THE ARTICLE ------------------------------------------------------------------------------

if newstype == "Keadaan Ekonomi" and run == 0 :
  article1category = Article(url1category)
  article2category = Article(url2category)
  article3category = Article(url3category)
  article4category = Article(url4category)
  article5category = Article(url5category)

if newstype == "Regulasi" and run == 0 :
  article1regulator = Article(url1regulator)
  article2regulator = Article(url2regulator)
  article3regulator = Article(url3regulator)
  article4regulator = Article(url4regulator)
  article5regulator = Article(url5regulator)

if newstype == "Indonesia" and run == 0 :
  article1nasional = Article(url1nasional)
  article2nasional = Article(url2nasional)
  article3nasional = Article(url3nasional)
  article4nasional = Article(url4nasional)
  article5nasional = Article(url5nasional)

if newstype == "Sosial" and run == 0 :
  article1rileks = Article(url1rileks)
  article2rileks = Article(url2rileks)
  article3rileks = Article(url3rileks)
  article4rileks = Article(url4rileks)
  article5rileks = Article(url5rileks)

if newstype == "General" and run == 0 :
  article1informasi = Article(url1informasi)
  article2informasi = Article(url2informasi)
  article3informasi = Article(url3informasi)
  article4informasi = Article(url4informasi)
  article5informasi = Article(url5informasi)

# ARTICLE DOWNLOAD -------------------------------------------------------------------------------------

if newstype == "Keadaan Ekonomi" and run == 0 :
  article1category.download()
  article2category.download()
  article3category.download()
  article4category.download()
  article5category.download()

if newstype == "Regulasi" and run == 0 :
  article1regulator.download()
  article2regulator.download()
  article3regulator.download()
  article4regulator.download()
  article5regulator.download()

if newstype == "Indonesia" and run == 0 :
  article1nasional.download()
  article2nasional.download()
  article3nasional.download()
  article4nasional.download()
  article5nasional.download()

if newstype == "Sosial" and run == 0 :
  article1rileks.download()
  article2rileks.download()
  article3rileks.download()
  article4rileks.download()
  article5rileks.download()

if newstype == "General" and run == 0 :
  article1informasi.download()
  article2informasi.download()
  article3informasi.download()
  article4informasi.download()
  article5informasi.download()

# ARTICLE PARSE -------------------------------------------------------------------------------------

if newstype == "Keadaan Ekonomi" and run == 0 :
  article1category.parse()
  article2category.parse()
  article3category.parse()
  article4category.parse()
  article5category.parse()

if newstype == "Regulasi" and run == 0 :
  article1regulator.parse()
  article2regulator.parse()
  article3regulator.parse()
  article4regulator.parse()
  article5regulator.parse()

if newstype == "Indonesia" and run == 0 :
  article1nasional.parse()
  article2nasional.parse()
  article3nasional.parse()
  article4nasional.parse()
  article5nasional.parse()

if newstype == "Sosial" and run == 0 :
  article1rileks.parse()
  article2rileks.parse()
  article3rileks.parse()
  article4rileks.parse()
  article5rileks.parse()

if newstype == "General" and run == 0 :
  article1informasi.parse()
  article2informasi.parse()
  article3informasi.parse()
  article4informasi.parse()
  article5informasi.parse()

# ARTICLE NLP -------------------------------------------------------------------------------------------

if newstype == "Keadaan Ekonomi" and run == 0 :
  article1category.nlp()
  article2category.nlp()
  article3category.nlp()
  article4category.nlp()
  article5category.nlp()

if newstype == "Regulasi" and run == 0 :
  article1regulator.nlp()
  article2regulator.nlp()
  article3regulator.nlp()
  article4regulator.nlp()
  article5regulator.nlp()

if newstype == "Indonesia" and run == 0 :
  article1nasional.nlp()
  article2nasional.nlp()
  article3nasional.nlp()
  article4nasional.nlp()
  article5nasional.nlp()

if newstype == "Sosial" and run == 0 :
  article1rileks.nlp()
  article2rileks.nlp()
  article3rileks.nlp()
  article4rileks.nlp()
  article5rileks.nlp()

if newstype == "General" and run == 0 :
  article1informasi.nlp()
  article2informasi.nlp()
  article3informasi.nlp()
  article4informasi.nlp()
  article5informasi.nlp()

# EXTRACTING ARTICLE TEXT ---------------------------------------------------------------------------------

if newstype == "Keadaan Ekonomi" and run == 0 :
  article1category = article1category.text
  article2category = article2category.text
  article3category = article3category.text
  article4category = article4category.text
  article5category = article5category.text

if newstype == "Regulasi" and run == 0 :
  article1regulator = article1regulator.text
  article2regulator = article2regulator.text
  article3regulator = article3regulator.text
  article4regulator = article4regulator.text
  article5regulator = article5regulator.text

if newstype == "Indonesia" and run == 0 :
  article1nasional = article1nasional.text
  article2nasional = article2nasional.text
  article3nasional = article3nasional.text
  article4nasional = article4nasional.text
  article5nasional = article5nasional.text

if newstype == "Sosial" and run == 0 :
  article1rileks = article1rileks.text
  article2rileks = article2rileks.text
  article3rileks = article3rileks.text
  article4rileks = article4rileks.text
  article5rileks = article5rileks.text

if newstype == "General" and run == 0 :
  article1informasi = article1informasi.text
  article2informasi = article2informasi.text
  article3informasi = article3informasi.text
  article4informasi = article4informasi.text
  article5informasi = article5informasi.text

# SUMMARY VARIABLE ------------------------------------------------------------------------------------------------

if newstype == "Keadaan Ekonomi" and run == 0 :
  makro_summary = article1category + "\n" + "\n" + article2category + "\n" + "\n" + article3category + "\n" + "\n" + article4category + "\n" + "\n" + article5category

if newstype == "Regulasi" and run == 0 :
  regulator_summary = article1regulator + "\n" + "\n" + article2regulator + "\n" + "\n" + article3regulator + "\n" + "\n" + article4regulator + "\n" + "\n" + article5regulator

if newstype == "Indonesia" and run == 0 :
  nasional_summary = article1nasional + "\n" + "\n" + article2nasional + "\n" + "\n" + article3nasional + "\n" + "\n" + article4nasional + "\n" + "\n" + article5nasional

if newstype == "Sosial" and run == 0 :
  rileks_summary = article1rileks + "\n" + "\n" + article2rileks + "\n" + "\n" + article3rileks + "\n" + "\n" + article4rileks + "\n" + "\n" + article5rileks

if newstype == "General" and run == 0 :
  informasi_summary = article1informasi + "\n" + "\n" + article2informasi + "\n" + "\n" + article3informasi + "\n" + "\n" + article4informasi + "\n" + "\n" + article5informasi


# LLM Processing ----------------------------------------------------------------------------------------------------------------------------------------

clientsector = Groq(api_key="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")

#if newstype == "Keadaan Ekonomi" :
  #summary_bullet_pointmakro = f"Summarize {makro_summary} into 10 bullet points, and translate it into Indonesian, just print the bullet points, don't add anything else, not even an introduction:"
  #bulletpointsummarymakro = clientsector.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_pointmakro,}],model="llama3-8b-8192")

#if newstype == "Regulasi" :
  #summary_bullet_pointregulator = f"Summarize {regulator_summary} into 10 bullet points, and translate it into Indonesian, just print the bullet points, don't add anything else, not even an introduction:"
  #bulletpointsummaryregulator = clientsector.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_pointregulator,}],model="llama3-8b-8192")

#if newstype == "Indonesia" :
  #summary_bullet_pointnasional = f"Summarize {nasional_summary} into 10 bullet points, and translate it into Indonesian, just print the bullet points, don't add anything else, not even an introduction:"
  #bulletpointsummarynasional = clientsector.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_pointnasional,}],model="llama3-8b-8192")

#if newstype == "Sosial" :
  #summary_bullet_pointrileks = f"Summarize {rileks_summary} into 10 bullet points, and translate it into Indonesian, just print the bullet points, don't add anything else, not even an introduction:"
  #bulletpointsummaryrileks = clientsector.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_pointrileks,}],model="llama3-8b-8192")

#if newstype == "General" :
  #summary_bullet_pointinformasi = f"Summarize {informasi_summary} into 10 bullet points, and translate it into Indonesian, just print the bullet points, don't add anything else, not even an introduction:"
  #bulletpointsummaryinformasi = clientsector.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_pointinformasi,}],model="llama3-8b-8192")

# STORING IT INTO A VARIABLE -----------------------------------------------------------------------------------------------------------------------------

#if newstype == "Keadaan Ekonomi" :
  #bulletpointsummarymakro = bulletpointsummarymakro.choices[0].message.content

#if newstype == "Regulasi" :
  #bulletpointsummaryregulator = bulletpointsummaryregulator.choices[0].message.content

#if newstype == "Indonesia" :
  #bulletpointsummarynasional = bulletpointsummarynasional.choices[0].message.content

#if newstype == "Sosial" :
  #bulletpointsummaryrileks = bulletpointsummaryrileks.choices[0].message.content

#if newstype == "General" :
  #bulletpointsummaryinformasi = bulletpointsummaryinformasi.choices[0].message.content

# STREAMLIT CODE -------------------------------------------------------------------------------------

st.title("Chat Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if newsprompting := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(newsprompting)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": newsprompting})

# CHATBOT CODING --------------------------------------------------------------------------------------------------------------------------------------------

#st.title("Simple chat")

#newsprompting = st.chat_input("")

clientsector = Groq(api_key="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")

if newstype == "Keadaan Ekonomi" :
  summary_bullet_pointaggnews = f"Answer the question of {newsprompting}, only answer from {makro_summary} and translate it into Indonesian"
  bulletpointsummarymakro = clientsector.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_pointaggnews,}],model="llama3-8b-8192")
  answer_aggnews = bulletpointsummarymakro.choices[0].message.content

if newstype == "Regulasi" :
  summary_bullet_pointaggnews = f"Answer the question of {newsprompting}, only answer from {regulator_summary} and translate it into Indonesian"
  bulletpointsummaryregulasi = clientsector.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_pointaggnews,}],model="llama3-8b-8192")
  answer_aggnews = bulletpointsummaryregulasi.choices[0].message.content

if newstype == "Indonesia" :
  summary_bullet_pointaggnews = f"Answer the question of {newsprompting}, only answer from {nasional_summary} and translate it into Indonesian"
  bulletpointsummarynasional = clientsector.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_pointaggnews,}],model="llama3-8b-8192")
  answer_aggnews = bulletpointsummarynasional.choices[0].message.content

if newstype == "Sosial" :
  summary_bullet_pointaggnews = f"Answer the question of {newsprompting}, only answer from {rileks_summary} and translate it into Indonesian"
  bulletpointsummaryrileks = clientsector.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_pointaggnews,}],model="llama3-8b-8192")
  answer_aggnews = bulletpointsummaryrileks.choices[0].message.content

if newstype == "General" :
  summary_bullet_pointaggnews = f"Answer the question of {newsprompting}, only answer from {informasi_summary} and translate it into Indonesian"
  bulletpointsummaryinformasi = clientsector.chat.completions.create(messages=[{"role":"user", "content":summary_bullet_pointaggnews,}],model="llama3-8b-8192")
  answer_aggnews = bulletpointsummaryinformasi.choices[0].message.content

# DISPLAY ANSWER IN CHAT ------------------------------------------------------------------------------------------------------

# Display assistant response in chat message container
with st.chat_message("assistant"):
  st.markdown(answer_aggnews)
  # Add assistant response to chat history
  st.session_state.messages.append({"role": "assistant", "content": answer_aggnews})

# END CHAT BUTTON --------------------------------------------------------------------------------

with st.sidebar:
  if st.button("End Chat"):
      run == 1

with st.sidebar:
  st.subheader('Smart Summary', divider='rainbow')

if newstype == "Keadaan Ekonomi" :
  all_aggnews_summary = f"Summarize all of the key points of newws in {makro_summary} into 5 bullet points, and translate it into Indonesian, just print the bullet points, don't add anything else, not even an introduction"
  bulletpointsummaryallaggnews = clientsector.chat.completions.create(messages=[{"role":"user", "content":all_aggnews_summary,}],model="llama3-8b-8192")
  bullet_point_summary_aggnews = bulletpointsummaryallaggnews.choices[0].message.content
  with st.sidebar:
    st.code(bullet_point_summary_aggnews)

if newstype == "Regulasi" :
  all_aggnews_summary = f"Summarize all of the key points of newws in {regulator_summary} into 5 bullet points, and translate it into Indonesian, just print the bullet points, don't add anything else, not even an introduction"
  bulletpointsummaryallaggnews = clientsector.chat.completions.create(messages=[{"role":"user", "content":all_aggnews_summary,}],model="llama3-8b-8192")
  bullet_point_summary_aggnews = bulletpointsummaryallaggnews.choices[0].message.content
  with st.sidebar:
    st.code(bullet_point_summary_aggnews)

if newstype == "Indonesia" :
  all_aggnews_summary = f"Summarize all of the key points of newws in {nasional_summary} into 5 bullet points, and translate it into Indonesian, just print the bullet points, don't add anything else, not even an introduction"
  bulletpointsummaryallaggnews = clientsector.chat.completions.create(messages=[{"role":"user", "content":all_aggnews_summary,}],model="llama3-8b-8192")
  bullet_point_summary_aggnews = bulletpointsummaryallaggnews.choices[0].message.content
  with st.sidebar:
    st.code(bullet_point_summary_aggnews)

if newstype == "Sosial" :
  all_aggnews_summary = f"Summarize all of the key points of newws in {rileks_summary} into 5 bullet points, and translate it into Indonesian, just print the bullet points, don't add anything else, not even an introduction"
  bulletpointsummaryallaggnews = clientsector.chat.completions.create(messages=[{"role":"user", "content":all_aggnews_summary,}],model="llama3-8b-8192")
  bullet_point_summary_aggnews = bulletpointsummaryallaggnews.choices[0].message.content
  with st.sidebar:
    st.code(bullet_point_summary_aggnews)

if newstype == "General" :
  all_aggnews_summary = f"Summarize all of the key points of newws in {informasi_summary} into 5 bullet points, and translate it into Indonesian, just print the bullet points, don't add anything else, not even an introduction"
  bulletpointsummaryallaggnews = clientsector.chat.completions.create(messages=[{"role":"user", "content":all_aggnews_summary,}],model="llama3-8b-8192")
  bullet_point_summary_aggnews = bulletpointsummaryallaggnews.choices[0].message.content
  with st.sidebar:
    st.code(bullet_point_summary_aggnews)