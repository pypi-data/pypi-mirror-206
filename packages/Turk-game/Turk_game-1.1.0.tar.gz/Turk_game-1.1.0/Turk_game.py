import pygame as pg
import threading as th
import keyboard as ky
import sys, os , time , random



pg.init()
pg.font.init()
#pygame baslatiliyor


class EKRAN(pg.Surface):#ekran sinifi pygame ekranı olarak kullanılacak sınıf ve bazi özellikleri turkce
    def __init__(self, boyut):
        super().__init__(boyut)
        self.boyut = boyut
        self.x,self.y = self.boyut[0] , self.boyut[1]
        self.doldur = self.fill
        self.yerlestir = self.blit
        self.cevir = self.convert
        self.kopyala = self.copy
        self.cevir_alpha = self.convert_alpha
        


class dikdortgen(pg.Rect):#dikdortgen sinifi pg.rect ozelliklerini alir ve bazi ozellikleri turkcedir
    def __init__(self,konum,boyut):
        super().__init__(konum,boyut)
        self.carpma_listesi = self.collidedict
        self.hareket = self.move
        self.carp = self.colliderect
        self.nokta_carpmasi = self.collidepoint



class Vektor2(pg.Vector2):
    def __init__(self,x,y):
        super().__init__(x,y)

    def dogrultu_al(self):
        return self.normalize()



class OYUN:#HER TURLU ISLEM BURADA YAPILIR
    def __init__(self):
        pass
    def ekran_olustur(self,x,y,baslik="Turk_game",ikon="",boyutlandirilabilir=False):
        self.boyutlandirilabilir = boyutlandirilabilir
        if self.boyutlandirilabilir:
            self.___ekran_altyapisi___ = pg.display.set_mode((x,y),pg.RESIZABLE)
        else:
            self.___ekran_altyapisi___ = pg.display.set_mode((x,y))
        if ikon != "":
            pg.display.set_icon(ikon)
        pg.display.set_caption(baslik)
        self.___ekran__ = EKRAN((x,y))
        self.update = pg.display.update
        self.flip = pg.display.flip
        self.ciz = pg.draw
        self.ciz.cizgi = self.ciz.line
        self.ciz.yay = self.ciz.arc
        self.ciz.daire = self.ciz.circle
        self.ciz.dikdortgen = self.ciz.rect
        self.font_size = 30
        self.yazi = pg.font.SysFont("calibri",self.font_size)  # 36 punto büyüklüğünde "calibri" fontu kullan
        self.resim = pg.image
        self.mask = pg.mask
        self.mask.yuzeyden = self.mask.from_surface
        self.all = pg
        self.events = {"MOUSE_BUTONU_İNDİ":self.all.MOUSEBUTTONDOWN,"MOUSE_BUTONU_KALKTI":self.all.MOUSEBUTTONUP}
        self.is_parcasi = th.Thread
        self.bekle = time.sleep
        self.dosya_yoneticisi = os
        self.rastgele = random
        self.rastgele.tamsayi = self.rastgele.randint
        self.rastgele.rasyonel_sayi = self.rastgele.uniform
        self.rastgele.secim = self.rastgele.choice
        return self.___ekran__
    
    def resim_yukle(self,yol):#pygame image ile resim yukler ve convert_alpha ise resmin bozulmasi ihtimalini azaltmak icindir
        return pg.image.load(yol).convert_alpha()
    
    def basildi(self,tus:str):#Bu fonksiyon keyboard modulunu kullanarak belirli bir tusun basilip basilmadigini kontrol eder
        return ky.is_pressed(tus)
    
    def dongu(self,normal_islem,event_islem,kapandi_islem,yenileme_cesidi):#Pygame icinde en cok satir yazdiran kisimdir.AMA BU FONKSİYON BUNUN ONUNE GECMEK ICINDIR
        while 1:
            self.___ekran_altyapisi___.blit(self.___ekran__,(0,0))
            normal_islem()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    kapandi_islem()
                    pg.quit()
                    sys.exit()
                if event.type == pg.VIDEORESIZE and self.boyutlandirilabilir:
                    x,y = event.w, event.h
                    self.___ekran__.__init__((x,y))
                event_islem(event)
            yenileme_cesidi()
                
#debug
def d():
    a.ciz.cizgi(ekran,(200,200,200),[0,0],ekran.boyut)
    ekran.yerlestir(a.yazi.render("ahhhhhh",True,(255,50,50)),[ekran.boyut[0]/2,ekran.boyut[1]/2])
def b():
    pass
def c(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        print("abuğğğğziiiiiddiiiiğn") 
a = OYUN()
ekran = a.ekran_olustur(200,200,"deneme","",True)
a.dongu(d,c,b,a.update)
