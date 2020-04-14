def fonk(hashtable_size,sayilar):
  hastable_liste = [None] * hashtable_size
  """
  Bellek yerine ornek olması acisindan liste kullandım.
  Olusturdugum listenin tum degerlerine None degerini atadim.
  Bu sayede cakisma durumu olup olmadigini daha rahat kontrol edeceğim
  """
  for i in range(len(sayilar)):
    #Girilen deger listesi kadar donecek bir dongu olusturdum
    ilk_fonksiyon_indisi = sayilar[i] % hashtable_size
    if hastable_liste[ilk_fonksiyon_indisi] is None:
      #Eger listemdeki indis degerim bos ise, sayiyi koy.
      hastable_liste[ilk_fonksiyon_indisi] = sayilar[i]
    else:
      
      ikinci_fonksiyon_indisi = ilk_fonksiyon_indisi
      #Yeni bir indis sayisi yarat
      while hastable_liste[ikinci_fonksiyon_indisi] is not None:
        #Eger listemdeki indis dolu ise bos bulana kadar bu islemi yap
        artan = (sayilar[i]//hashtable_size) 
        #İkinci matematik Fonksiyonum
        ikinci_fonksiyon_indisi = (ikinci_fonksiyon_indisi + artan) % hashtable_size
        #İndisi donguden cikana kadar arttır.
      hastable_liste[ikinci_fonksiyon_indisi] = sayilar[i]
      #İndis atamasi
      #end for
  for i in range(len(sayilar)):
    print("Kutu",i+1 ,":", hastable_liste[i])

values = [27, 18, 29, 28, 39, 13, 16] #Ornek deger

print(fonk(11,values)) #Uzunlugumu 11 olarak sectim (0-10)

