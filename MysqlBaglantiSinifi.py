#------------------------------
#Emre c
#son class


import MySQLdb as mysql

class Baglanti():
    def __init__(self):
        self.ip="127.0.0.1"
        self.kullanici="root"
        self.sifre="123456"
        self.veritabani = "world"
        self.baglanti=mysql.connect(self.ip,self.kullanici,self.sifre,self.veritabani)
        self.islem=self.baglanti.cursor()
        #TABLE CREATE
        #DB CREATE ! EKLENCEK
        
    def tablo_olustur(self,sorgu):
        try:
            self.islem.execute(sorgu)
            print("basariyla olusturuldu!")
        except:
             print("hata")
        self.__out__()
        #CREATE - UPDATE - DELETE
        
    def veri_ekle(self,sorgu):
        try:
            self.islem.execute(sorgu)
            self.baglanti.commit()
            print("basariyla veri eklendi!")
        except:
             print("hata")
        self.__out__()
        
    def veri_guncelle(self,sorgu):
        try:
            self.islem.execute(sorgu)
            self.baglanti.commit()
            print("guncellendi")
        except:
             print("hata")
        self.__out__()

    def veri_sil(self,sorgu):
        try:
            self.islem.execute(sorgu)
            self.baglanti.commit()
            print("silindi")
        except:
             print("hata")
        self.__out__()

        #READ
    def veri_oku(self,sorgu):
        try:
            self.islem.execute(sorgu)
            sonuc=self.islem.fetchall()
            return sonuc
        except:
             print("hata")
        self.__out__()


    def __out__(self):
        self.baglanti.close()

    

sql=Baglanti()

#sql.tablo_olustur("""
#CREATE TABLE Ogretmenler(
#                        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#                        kull_adi varchar(20) NOT NULL,
#                        parola varchar(20) NOT NULL
#                        )
#""")

#ses = sql.veri_oku("SELECT * FROM ogretmenler")

#for x in ses:
#    print x
    
sql.veri_ekle("""
                insert into kullanicilar(kull_adi,parola)
                values ('root','1234')
              """)

#eklenecek veriler
