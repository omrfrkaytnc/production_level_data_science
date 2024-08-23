# CEVAPLAR


- 1. linux_basic adında bir klasör oluşturup içine giriniz
```
[train@trainvm atscale5]$ mkdir linux_basic
[train@trainvm atscale5]$ cd linux_basic/
```

- 2. miuul_data isminde başka bir klasör oluşturunuz ve bu klasörün içine  Churn_Modelling.csv veri setini indiriniz.
```
mkdir miuul_data

wget -O miuul_data/Churn_modelling.csv https://raw.githubusercontent.com/erkansirin78/datasets/master/Churn_Modelling.csv

ls -l miuul_data/
```

- 3. /etc dizininde sadece .conf ile biten dosyaları listeleyiniz.
```
 ls -l /etc | grep .conf$
```

- 4. miuul.txt adında bir dosya oluşturunuz ve içine Merhaba! Miuul Data Engineer Path'e başladım. yazınız. miuul.txt dosya içeriğini okuyunuz.
```
vi ile dosya iç içine gir.
[train@trainvm linux_basic]$ vi miuul.txt

insert tuşu ile insert moduna geç

Cümleyi yaz 
Escape + : + wq + Enter  tuşlarına basarak kaydedip çık 

cat ile oku 
[train@trainvm linux_basic]$ cat miuul.txt
Merhaba! Miuul Data Engineer Path'e başladım
```


- 5. sarı adında bir klasör yaratınız.  
` [train@localhost atscale4]$ mkdir sarı `

- 6. sarı klasörün içine giriniz.  
` [train@localhost atscale4]$ cd sarı `  

- 7. sarı klasör içinde kırmızı ve mavi adında iki dosya yaratınız.  
` [train@localhost sarı]$ touch kırmızı mavi  `  

- 8. kırmızı  dosyanın içine `Benim Adım Kırmızı`, mavi dosyanın içine `Benim Adım Mavi` yazınız.
```
[train@localhost sarı]$ echo "Benim Adım Kırmızı" >> kırmızı
[train@localhost sarı]$ echo "Benim Adım Mavi" >> mavi
```

- 9. kırmızı dosyanın içeriğini yönlendirerek mavi dosyaya satır olarak ekleyiniz.  
` [train@localhost sarı]$ cat kırmızı >> mavi  `  

- 10. mavi dosyanın içeriğini yönlendirerek kırmızı dosyaya yeni satır olarak ekleyiniz.
` [train@localhost sarı]$ cat mavi >> kırmızı  ` 

- 11. kırmızı ve mavi dosyayı bir üst dizine isimlerini değiştirerek kopyalayınız.
```
[train@localhost sarı]$ cp kırmızı ../kırmızı_rn
[train@localhost sarı]$ cp mavi ../mavi_rn
```
- 12. tree uygulamasını kurunuz ve tree ile sarı klasörün ağaç yapısını inceleyiniz (tree sarı)
```
[train@localhost sarı]$ sudo yum -y install tree

[train@localhost sarı]$ cd ..
[train@localhost atscale4]$ tree sarı/
sar\304\261/
├── k\304\261rm\304\261z\304\261
└── mavi

0 directories, 2 files
```
- 13. https://github.com/erkansirin78/datasets reposunda bulunan `Wine.csv` dosyasını ~/datasets dizinine indiriniz.  
` wget -P ~/datasets/ https://raw.githubusercontent.com/erkansirin78/datasets/master/Wine.csv ` 

- 14. `Wine.csv` dosyasının ilk 15 satırını ekrana yazdırınız.
```
head -n 15 ~/datasets/Wine.csv
Alcohol,Malic_Acid,Ash,Ash_Alcanity,Magnesium,Total_Phenols,Flavanoids,Nonflavanoid_Phenols,Proanthocyanins,Color_Intensity,Hue,OD280,Proline,Customer_Segment
14.23,1.71,2.43,15.6,127,2.8,3.06,0.28,2.29,5.64,1.04,3.92,1065,1
13.2,1.78,2.14,11.2,100,2.65,2.76,0.26,1.28,4.38,1.05,3.4,1050,1
13.16,2.36,2.67,18.6,101,2.8,3.24,0.3,2.81,5.68,1.03,3.17,1185,1
14.37,1.95,2.5,16.8,113,3.85,3.49,0.24,2.18,7.8,0.86,3.45,1480,1
13.24,2.59,2.87,21,118,2.8,2.69,0.39,1.82,4.32,1.04,2.93,735,1
14.2,1.76,2.45,15.2,112,3.27,3.39,0.34,1.97,6.75,1.05,2.85,1450,1
14.39,1.87,2.45,14.6,96,2.5,2.52,0.3,1.98,5.25,1.02,3.58,1290,1
14.06,2.15,2.61,17.6,121,2.6,2.51,0.31,1.25,5.05,1.06,3.58,1295,1
14.83,1.64,2.17,14,97,2.8,2.98,0.29,1.98,5.2,1.08,2.85,1045,1
13.86,1.35,2.27,16,98,2.98,3.15,0.22,1.85,7.22,1.01,3.55,1045,1
14.1,2.16,2.3,18,105,2.95,3.32,0.22,2.38,5.75,1.25,3.17,1510,1
14.12,1.48,2.32,16.8,95,2.2,2.43,0.26,1.57,5,1.17,2.82,1280,1
13.75,1.73,2.41,16,89,2.6,2.76,0.29,1.81,5.6,1.15,2.9,1320,1
14.75,1.73,2.39,11.4,91,3.1,3.69,0.43,2.81,5.4,1.25,2.73,1150,1
```
- 15. `Wine.csv` dosyasında başlık satırı var mı? Sütunlar birbirinden hangi ayraç ile ayrılmıştır?  
Evet var. Virgülle ayrılmış.