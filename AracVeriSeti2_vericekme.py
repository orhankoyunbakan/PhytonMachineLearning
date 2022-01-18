
"""
"istanbul","ankara","izmir","bursa","adana","adıyaman","afyonkarahisar","ağrı"
belirtilen şehirlerde bulunan wolswagen marka aracları çekmektedir

"""
#kütüphanelerin import edildiği kısım
import requests
from bs4 import BeautifulSoup
import pandas as pd



AracListesi=list()
y=1
while y <11:#il 11 sayfadan veri çekiyotuz
    urlKategoriler="https://www.araba.com/otomobil/volkswagen?sayfa=10&siralama=fiyata-gore&yer%5B0%5D=adana&yer%5B1%5D=adiyaman&yer%5B2%5D=afyonkarahisar&yer%5B3%5D=agri&yer%5B4%5D=ankara&yer%5B5%5D=bursa&yer%5B6%5D=istanbul&yer%5B7%5D=izmir&viewType=katalog&sayfa="+str(y)
    response1 = requests.get(urlKategoriler)
    html_icerigi1 = response1.content
    soup1 = BeautifulSoup(html_icerigi1,"html.parser")
    liste=list()
    idler = soup1.find_all("p",{"class":"fr offer-no"})
    for id in idler:
        id=id.text.strip("#")
        print(id)
       
        url = "https://www.araba.com/ilan/"+str(id) #tek tek tüm ilanların idlerini alıp arac bilgilerini detay sayfalarından çekiyoruz
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi,"html.parser")
    
    
    
        #Fiyat verisimi Çeken Kısım
        fiyat = soup.find("span",{"class":"offer-price"})
        fiyat=fiyat.text.strip().strip(" TL")
    
        #sehir verisin Çeken Kısım
        sehir = soup.find("a",{"class":"offer-district-text"})
        yer=sehir.get("href")
        sehir=yer[30:]
    
        print("------------")
    
        #Containera tüm verileri aktarıyoruz
        container = soup.find("div",{"class":"offer-info-container"})
        x=0;
        for i in container:
            
            if x==3:
                #model  verisinin çekildiği kısım
                model=i.text.split(":")
                model=model[1]
                
            if x==5:
                #yıl  verisinin çekildiği kısım
                yil=i.text.split(":")
                yil=yil[1]
                
            elif x==6:
                #km verisinin çekildiği kısım
                km=i.text.split(":")
                km=km[1]
            elif x==7:
                #motor gücü  verisinin çekildiği kısım
                yakitTipi=i.text.split(":")
                yakitTipi=yakitTipi[1].split("/")
                yakitTipi=yakitTipi[0].strip()
            elif x==8:
                #vites tipi  verisinin çekildiği kısım
                vitesTipi=i.text.split(":")
                vitesTipi=vitesTipi[1]
                
            elif x==9:
                #motor hacmi  verisinin çekildiği kısım
                motorHacmi=i.text.split(":")
                motorHacmi=motorHacmi[1].split(" ")
                motorHacmi=motorHacmi[0].split("-")
                motorHacmi=motorHacmi[0]
            elif x==15:
                #motor gücü verisi
                motorGucu=i.text.split(":")
                motorGucu=motorGucu[1].split(" ")
                motorGucu=motorGucu[0].split("-")
                motorGucu=motorGucu[0]
            x=x+1
        
        #bilgilerin tek tek ekrana yazdırıması
        print("---------Bilgiler-------------"+str(id))
        print(fiyat)
        print(model)
        print(sehir)
        print(yil)
        print(km)
        print(yakitTipi.strip())
        print(vitesTipi)
        print(motorHacmi)
        print(motorGucu)
        #hersayfa ayrı ayrı listelere aktarılır
        liste.append([sehir,model,yakitTipi,vitesTipi,yil,km,motorHacmi,motorGucu,fiyat])
        #liste dataframe aktarılır
        df= pd.DataFrame(liste,columns = ['MODEL','SEHIR','YAKIT_TIPI','VITES_TIPI','YIL','KM','MOTOR_HACMI','MOTOR_GUCU','FIYAT'])
    
    print(df)
    AracListesi=AracListesi+liste #bakılan her sayfadaki veriler AracListesine eklenir
    y=y+1
    print("--------------------------------")

print("///son/////")#son olarak tüm listeler toplanıp csv formatına dönüştürülür.
AracListesidf=pd.DataFrame(AracListesi,columns = ['MODEL','SEHIR','YAKIT_TIPI','VITES_TIPI','YIL','KM','MOTOR_HACMI','MOTOR_GUCU','FIYAT'])
print(AracListesidf) 
AracListesidf.to_csv('C:/Users/orhan/Desktop/AracVeriSeti22.csv',sep=';',index=False, encoding = 'utf-8-sig')

  
        
        
        
        
        
    
    
    
