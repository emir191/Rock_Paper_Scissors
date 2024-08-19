"""
ar="elma"=="elma"
print (5>3 and print("sa"))
    
x=0
fibonacci=0
if x in range(0,5):
    fibonacci=float(fibonacci*x)
    x=x+1
    print(fibonacci) 
            

message="sett emessage"
s=set(message)
print(s)
# SADECE FARKLI ÖĞELERİ SET EDER.
print(message.split())
a="----".join(message)
print(a)

matrix=[[j for j in range(3)] for _ in range(3)]
print(matrix)
x,y,*z=(2,2,6,9,8)
print(z)
adlar=['tyler','jonson','kvara']
for i,e in enumerate(adlar):
    print(i,"indexindeki eleman:",e)
       
satis=[3500,7630,7521]
maliyet=[4551,2222,1023]
for s,c in zip(satis,maliyet):
  kar=float(s-c)
  print(f'yapılan kar:{kar}')
def weird(a):
   return 5+a
   print("selam")


print(weird(8))
def hello(end,start="hello"):
   print(start + " " + end)
print(hello("dddd"))
l=[1,2,3,4]
def apply(l,f):
   n=len(l)
   for i in range(n):
      l[i]=f(l[i])
def kare(x):
   return x**2
apply(l,kare)
print(l)  
"""


"""
seçenekler=("taş için 0","kağıt için 1","makas için 2----------->>>>>>>>>>>>")
tkm=("taş","kağıt","makas")
a=int(input(seçenekler))
Machine=rand.randint(0,2)
   #Machine=rand.randint(1,3)
if a==0 and Machine==0 or a==1 and Machine==1 or a==2 and Machine==2:
        print("BERABERE")
        print("makine değeri" , tkm[Machine])
        print("senin seçimin", tkm[a])
        print("oyuncu puanı",oyuncupuanı)
        print("makine puanı",makinePuanı)
        
elif a==0 and Machine==1 or a==1 and Machine==2 or a==2 and Machine==0:
        print("Makine kazandı")
        print("makine değeri" , tkm[Machine])
        print("senin seçimin", tkm[a])
        makinePuanı+=1
        print("oyuncu puanı",oyuncupuanı)
        print("makine puanı",makinePuanı)
elif a==0 and Machine==2 or a==1 and Machine==0 or a==2 and Machine==1:
        print("makine değeri" , tkm[Machine])
        print("senin seçimin", tkm[a])
        print("bu turu kazandın") 
        oyuncupuanı+=1
        print("oyuncu puanı",oyuncupuanı)
        print("makine puanı",makinePuanı)

else :
        print("Geçersiz seçim değeri")
      """   
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
     

  
  

       
      
          



