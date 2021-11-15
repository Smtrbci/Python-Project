# pip install speedtest-cli

import speedtest
speed = speedtest.Speedtest()

def Test():
    while True:
        print('\a')
        secim = int(input("""
        Internet baglantinizi kontrol ediniz...
        1) Indirme Hizi
        2) Yukleme Hizi
        3) Cikis
        Secim >>> """))
        
        print('\a')
        
        if secim == 1 :
            print('Test ediyor...')
            print(f"Indirme Hizi : {'{:.2f}'.format(speed.download()/1024/1024)} Mb/s")
            
        elif secim == 2 :
            print('Test ediyor...')
            print(f"Yukleme Hizi : {'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s")
        
        elif secim == 3 :
            print('Programdan cikis yapildi.')
            break
        
        else:
            print("Hatali secim lutfen tekrar deneyiniz.")

Test()
