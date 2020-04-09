#Yazan: Geomatik Mühendisi Tunahan Sarıgül
import time
import datetime
import requests
saat = int(input("Saat: "))
dakika = int(input("Dakika: "))
url="https://raw.githubusercontent.com/ozanerturk/covid19-turkey-api/master/dataset/timeline.json"
response=requests.get(url)
veri=response.json()

artis=datetime.timedelta(days=1)
bugün=datetime.datetime.now()

belirtilen_tarih=bugün-artis
tarih=belirtilen_tarih

olumSayisidun=veri[tarih.strftime("%d/%m/%Y")]["deaths"]
vakaSayisidun=veri[tarih.strftime("%d/%m/%Y")]["cases"]
iyilesenSayisidun=veri[tarih.strftime("%d/%m/%Y")]["recovered"]
testSayisidun=veri[tarih.strftime("%d/%m/%Y")]["tests"]

olumSayisibugün=veri[bugün.strftime("%d/%m/%Y")]["deaths"]
vakaSayisibugün=veri[bugün.strftime("%d/%m/%Y")]["cases"]
iyilesenSayisibugün=veri[bugün.strftime("%d/%m/%Y")]["recovered"]
testSayisibugün=veri[bugün.strftime("%d/%m/%Y")]["tests"]

mesaj= "Türkiye'de " +str(tarih.strftime("%d/%m/%Y"))+"'de Güncel Corona Virüs verileri"  + "ölüm sayısı:"+ str(olumSayisidun) +"vaka sayısı:" + str(vakaSayisidun)+"iyileşen hasta sayısı:" + str(iyilesenSayisidun)+"test sayısı:" + str(testSayisidun)
mesaj2="Türkiye'de " +str(bugün.strftime("%d/%m/%Y"))+"'de Güncel Corona Virüs verileri"  + "ölüm sayısı:"+ str(olumSayisibugün) +"vaka sayısı:" + str(vakaSayisibugün)+"iyileşen hasta sayısı:" + str(iyilesenSayisibugün)+"test sayısı:" + str(testSayisibugün)
mesaj3="Sağlıklı Günler"
while True:
  

    if (saat == datetime.datetime.now().hour and dakika == datetime.datetime.now().minute):
       requests.post(url='https://api.telegram.org/bot{telegram bot token'inizi buraya yazınız}/sendMessage', data={'chat_id': {chat ıd'nizi buraya yazınız}, 'text': mesaj}).json()
       
       requests.post(url='https://api.telegram.org/bot{telegram bot token'inizi buraya yazınız}/sendMessage', data={'chat_id':{chat ıd'nizi buraya yazınız}, 'text': mesaj2}).json()
       break
requests.post(url='https://api.telegram.org/bot{telegram bot token'inizi buraya yazınız}/sendMessage', data={'chat_id': {chat ıd'nizi buraya yazınız}, 'text': mesaj3}).json()
    
    
