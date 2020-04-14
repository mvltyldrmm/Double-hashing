def fonk(hashtable_size,sayilar):
  hastable_liste = [None] * hashtable_size
  for i in range(len(sayilar)):
    ilk_fonksiyon_indisi = sayilar[i] % hashtable_size #islem 1 
    if hastable_liste[ilk_fonksiyon_indisi] is None:
      hastable_liste[ilk_fonksiyon_indisi] = sayilar[i]
    else:
      ikinci_fonksiyon_indisi = ilk_fonksiyon_indisi
      while hastable_liste[ikinci_fonksiyon_indisi] is not None:
        artan = (sayilar[i]//hashtable_size)  #islem2
        ikinci_fonksiyon_indisi = (ikinci_fonksiyon_indisi + artan) % hashtable_size
      hastable_liste[ikinci_fonksiyon_indisi] = sayilar[i]
  for i in range(len(sayilar)):
    print("Kutu",i+1 ,":", hastable_liste[i])

values = [27, 18, 29, 28, 39, 13, 16] #Ornek deger

print(fonk(11,values)) #Uzunlugumu 11 olarak sectim (0-10)

