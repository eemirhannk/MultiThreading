import csv
import string
import pandas
import codecs
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
nltk.download('punkt')

dataFrame = pandas.read_csv('rowsnew.csv',usecols=['Product','Issue','Company','State','Complaint ID','ZIP code'])

stop_words = set(stopwords.words('english'))

#print(dataFrame.head())

dataFrame['Product'] = dataFrame['Product'].str.replace(",","")
dataFrame['Product'] = dataFrame['Product'].str.replace(".","")
dataFrame['Product'] = dataFrame['Product'].str.replace("/","")
dataFrame['Issue'] = dataFrame['Issue'].str.replace(",","")
dataFrame['Issue'] = dataFrame['Issue'].str.replace(".","")
dataFrame['Issue'] = dataFrame['Issue'].str.replace("/","")
dataFrame['Company'] = dataFrame['Company'].str.replace(",","")
dataFrame['Company'] = dataFrame['Company'].str.replace(".","")
dataFrame['Company'] = dataFrame['Company'].str.replace("/","")

# Noktalama işareti olan 3 satırdaki noktalama işaretlerini boşluk karakteriyle replaceliyorum.

i=0
j=0
k=0

for sent in dataFrame['Issue']:
    # Issueları tokenize ettiğim kısım.
    tokenized_sent = nltk.word_tokenize(sent)

    # stopwordleri kaldırdığım kısım.
    tokenized_sent_no_stops = [
        tok for tok in tokenized_sent 
        if tok not in stop_words
    ]

    # Issueları untokenize ettiğim kısım. 
    dataFrame.at[i,'Issue']=TreebankWordDetokenizer().detokenize(tokenized_sent_no_stops)

    i=i+1

for sent in dataFrame['Product']:
    # Productları tokenize ettiğim kısım.
    tokenized_sent = nltk.word_tokenize(sent)

    # stopwordleri kaldırdığım kısım.
    tokenized_sent_no_stops = [
        tok for tok in tokenized_sent 
        if tok not in stop_words
    ]

    # Productları untokenize ettiğim kısım. 
    dataFrame.at[j,'Product']=TreebankWordDetokenizer().detokenize(tokenized_sent_no_stops)

    j=j+1

for sent in dataFrame['Company']:
    # Şirket isimlerini tokenize ettiğim kısım.
    sent = sent.lower()
    tokenized_sent = nltk.word_tokenize(sent)

    # stopwordleri kaldırdığım kısım.
    tokenized_sent_no_stops = [
        tok for tok in tokenized_sent 
        if tok not in stop_words
    ]

    # Şirket isimlerini untokenize ettiğim kısım. 
    company_upper = TreebankWordDetokenizer().detokenize(tokenized_sent_no_stops)
    # tokenize işleminden küçük harfle gelen şirket isimlerini tekrar büyük harfe çeviriyorum.
    dataFrame.at[k,'Company'] = company_upper.upper()

    k=k+1

dataFrame.to_csv('cleandata.csv')