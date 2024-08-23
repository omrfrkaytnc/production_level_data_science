
# CEVAPLAR
1. Bir dizini argüman olarak alan ve aşağıdakileri işleri yapan bir script yazınız.  
    - Bütün dosya ve klasörleri dolaşsın  
    - Klasör olanların disk kullanımlarını yazdırsın.

```
#!/bin/bash
# loops in arg1 and print folder sizes
for f in $1/*; do
   if [[ -d $f ]]; then
        sudo du -hs $f
   fi
done
```

- Run
```
[train@localhost linux_basic]$ ./bash_hw.sh ~/datasets
[sudo] password for train:
20M     /home/train/datasets/churn-telecom
229M    /home/train/datasets/market5mil_parquet
9.2M    /home/train/datasets/retail_db
```

2.  `xxxx-1, xxxx-2, ..... xxxx-n ` şeklinde isimlendirilmek üzere ardışık 
numaralarla klasör/dosya yaratan bir script yazınız.
- argüman 1: kaç tane klasör/dosya yaratılacak?
- argüman 2: Dosya mı klasör mü yaratılacak?
- argüman 3: Dosya/klasör sabit kısmında kullanılacak isim.

```
#!/bin/bash
# if $2 is folder it is folder else file
NUMBER=$1
FILE_OR_FOLDER=$2
CONSTANT_PART=$3

for (( i=1; i<=$NUMBER; i++ ))
  do
    if [ $FILE_OR_FOLDER = folder ]
      then
        mkdir ${CONSTANT_PART}-$i
      else
        touch ${CONSTANT_PART}-$i
    fi
  done
```

Test:
```
[train@localhost kurs]$ ./generate_filenames.sh 5 file myfile

[train@localhost kurs]$ ./generate_filenames.sh 5 folder myfolder

[train@localhost kurs]$ ll
total 4
-rwxr-xr-x. 1 train train 235 Oct 18 17:21 generate_filenames.sh
-rw-rw-r--. 1 train train   0 Oct 18 17:21 myfile-1
-rw-rw-r--. 1 train train   0 Oct 18 17:21 myfile-2
-rw-rw-r--. 1 train train   0 Oct 18 17:21 myfile-3
-rw-rw-r--. 1 train train   0 Oct 18 17:21 myfile-4
-rw-rw-r--. 1 train train   0 Oct 18 17:21 myfile-5
drwxrwxr-x. 2 train train   6 Oct 18 17:22 myfolder-1
drwxrwxr-x. 2 train train   6 Oct 18 17:22 myfolder-2
drwxrwxr-x. 2 train train   6 Oct 18 17:22 myfolder-3
drwxrwxr-x. 2 train train   6 Oct 18 17:22 myfolder-4
drwxrwxr-x. 2 train train   6 Oct 18 17:22 myfolder-5
```

4. Inline for loop döngüsü yazınız.
- Her döngüde 1 saniye uyusun
- 10 kez dönsün
- tek sayıları ekrana yazsın.

```
[train@localhost advanced_ds_bigdata]$ for i in {1..10}; do sleep 1; if [ $(($i%2)) = 1 ]; then echo $i; fi done
1
3
5
7
9
```

5. Paket yöneticisi ile `tree` paketini kurunuz. Eğitimi takip ettiğiniz dizini ağaç yapısında listeleyiniz.
tree paketinin kurulumu: `sudo yum -y install tree`

Örnek dizin ağaç yapısını görüntüleme:
```
(venvspark) [train@localhost play]$ tree nodejs-mongo-app/
nodejs-mongo-app/
├── app
│   ├── images
│   │   ├── docker-container-transparent.png
│   │   └── who_is_datascientist_960x640.jpg
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   └── server.js
├── docker-compose.yaml
├── Dockerfile
└── README.md

2 directories, 9 files
```