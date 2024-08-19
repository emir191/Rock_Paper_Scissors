   
import random as rand
restart="a"
oyuncupuanı=0
makinePuanı=0
tad=0

while (oyuncupuanı!=2 and makinePuanı!=2 or restart=="yes" ):
 
  seçenekler=("taş için t","kağıt için k","makas için m----------->>>>>>>>>>>>")
  tkm=("taş","kağıt","makas")
  if tad==0:
    
   print("Oyuna Hoşgeldin ")
   print("Taş-kâğıt-makas, genellikle iki oyuncuyla ve üç durumdan birinin seçilmesiyle oynanan bir el oyunudur. Taş makası, makas kağıdı, kâğıt da taşı yener. Eğer oyuncular aynı durumu seçerse oyun berabere biter.")
   print("iki turu kazanan oyunun galibi olur") 
  tad+=1
  a=input("terminale taş kağıt ya da makas şeklinde yazabilirsin").lower()
  #Machine=rand.randint(0,2)
  
  tur=True
  def tas_Kagit_Makas_Emir_Bahçacı(a):
      global oyuncupuanı
      global makinePuanı
      

       
       
  
    
      Machine=rand.randint(0,2)
      
        
      invalid=False
      while(oyuncupuanı!=2 and makinePuanı!=2 or restart=="yes"):

       if a=="taş" and Machine==0 or a=="kağıt" and Machine==1 or a=="makas" and Machine==2:
        print("BERABERE")
        print("makine değeri" , tkm[Machine])
        print("senin seçimin", a)
        print("oyuncu puanı",oyuncupuanı)
        print("makine puanı",makinePuanı)
        break
       
        
       elif a=="taş"and Machine==1 or a=="kağıt"and Machine==2 or a=="makas"and Machine==0:
        
       
        print("makine değeri" , tkm[Machine])
        print("senin seçimin", a)
        makinePuanı+=1
        print("oyuncu puanı",oyuncupuanı)
        print("makine puanı",makinePuanı)
        print("Makine kazandı")
        break
        
        
       elif a=="taş" and Machine==2 or a=="kağıt" and Machine==0 or a=="makas" and Machine==1:
        print("makine değeri" , tkm[Machine])
        print("senin seçimin", a)
        oyuncupuanı+=1
        print("oyuncu puanı",oyuncupuanı)
        print("makine puanı",makinePuanı)
        print("bu turu kazandın") 
        break
        
        

       else :
        print("Geçersiz seçim değeri")
        break
      if  oyuncupuanı==2:
       
       print("TEBRİKLER KAZANDINIZ") 
      if makinePuanı==2:

         print("Makine kazandı")
      if makinePuanı==2 or oyuncupuanı==2:

         print("devam edelim mi")
         restart=input("yes or no").lower()
         makineder=rand.randint(0,1)
         if restart=="yes" and makineder==1:
           oyuncupuanı=0
           makinePuanı=0
           print("TEKRARDAN BAŞLIYORUZ ")
         elif restart=="yes" and makineder==0:
           print("maalesef makine tekrar oynamak istemiyor") 
           print("Bir sonraki oyunda görüşmek üzere")
         elif restart!="yes" and restart!="no" :
           print("geçersiz bir değer girdiniz")
           print("Bir sonraki oyunda görüşmek üzere")    
         else:
           print("Bir sonraki oyunda görüşmek üzere")  
         
         

          
          
         
         
         
      
      
        
         

  
           
 
   
       
      
        
      
        
    
    
  
    
  def yeniBaştan():
   
    
         
    tas_Kagit_Makas_Emir_Bahçacı(a)
   
  
  yeniBaştan()
  #tas_Kagit_Makas_Emir_Bahçacı(a)  
     

  
  

       
      
          



