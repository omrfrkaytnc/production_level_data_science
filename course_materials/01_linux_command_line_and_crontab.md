## Ders1:Temel Komutlar

`mkdir prod_level` #mkdir dirname:klasör oluşturur

`cd prod_level` #klasör değiştirmek için kullanılır

`mkdir linux_basic`

```
mkdir notes
cd notes/
```

`pwd` #çalışılan klasörün yolunu yazdırır

`ls` #klasör içerisindeki dosyaları listeler

`cd~` #home dizine dönmeyi sağlar

`pwd`

`ls -l` #detaylı listeler (alfabetik)

`ls -lh` #detaylı ama daha okunaklı bir şekilde listeler

`ls -lr` #daha detaylı listeler (alfabenin tersine göre)

`ls -ltr` #detaylı listeler (tarihe göre sıralar)

`ls -lt` #detaylı listeler (tarihe göre sıralar)

`ls -la` #hidden file(gizli dosyalar) da gösterilir. Gizli dosyalar . ile başlar

`clear` # Syafayı temizler

`history` #kullanılan komutları listeler
`history 10` #Kullanılan son 10 komutu listeler
`history -c` #Kullanılan komut geçmişini siler

`cd prod_level/`

`cd linux_basic/notes/`

`cd ..` #önceki dizine dinmeyi sağlar

`alias` #uzun ve sık kullandığımız komutları kısaltmak için kullanılır

```
echo "merhaba linux"
alias ml="echo \ "merhaba linux \""
ml
```

## Ders2:Degiskenler

`env` #ortamdaki variable(değişkenler)'ları gösterir

`MY_NAME=Erkan` #değişken tanımlama

`echo $MY_NAME` #değişken yazdırma

`export MY_NAME` #env'a atmak için

`env | grep MY_NAME`#Değişkeni filtreleyip getirmek için

`unset MY_NAME` #değişken silmek için
`echo $MY_NAME`
`env | grep MY_NAME`

## Ders3:PATH Değişkeni ile Komutun Kaynağı: which ve types

`ls`

##### Komutların genel formatı :komut -options arguments

`ls -l /etc`

`cd ls`

`echo $path` #dizinleri gösterir.

`ls /usr/local/bin`

`pip -V` # pip versiyonu öğrenmek için

`/usr/local/bin/pip -V`

`nano simple_script.sh` # nano metin editörü olarak kullanılır

```
#!/bin/bash
echo "My name ise Murat"
```

`chmod +x simple_script.sh` #chmod, bir dosyanın erişim yetkilerini değiştirir

`./simple_script.sh`

`cd ..`

`simple_script.sh`

`cd notes/`

`pwd`

`/home/train/prod_level/linux_basic/notes/simple_script.sh`

`export PATH="/home/train/prod_level/linux_basic/notes:$PATH"`

`echo $PATH`

`simple_script.sh`

`cd ..`

`simple_script.sh`

`type ls` # type : hangi tipte komut (internal ya da external) olduğunu gösterir
`type cd`
`type nano`

`which nano` #which : komutun nereden (path olarak) çalıştırıldığını gösterir
`which echo`
`which cd`

## Ders4:Grep ile Düzenli İfadeler-1

##### global regular expression print, RegEx (düzenli ifadeler) kullanılarak filtrelemek için kullanılır. formatı : grep option  patern files

<https://github.com/erkansirin78/datasets>

`cd prod_level/linux_basic/notes/`

`wget https://github.com/erkansirin78/datasets/master/words.txt` # wget link : linkteki dosyayı indirir

`ls`

`grep ^Mur words.txt` #dosyada Mur ile başlayan ifadeleri arar

`grep ^mur words.txt`

`grep -i ^mur words.txt` #büyük/küçük harf duyarlılığını kaldırarak arama yapar

`grep -in ^mur words.txt` #ek olarak bulunan ifadenin hangi satırda olduğunu da gösterir.

`grep -in kuş$ words.txt` #dosyada kuş ile biten ifadeleri arar

`grep -in "k.ş" words.txt`

`grep -in "k.ş$" words.txt`

`grep bak words.txt` #dosyada bak içeren ifadeleri arar

`grep ' bak ' words.txt`

`grep '\ bak\ ' words.txt`

## Ders5:Grep ile Düzenli İfadeler-2

`grep M[au]k words.txt` #a ya da u içeren

`grep M[a-z]k words.txt` #a dan z’ye kadar harflerden herhangi birini içeren

`grep M[^ae]k words.txt` # [^ ] → köşeli parantez içerisindeki karakterler hariç tüm karakterleri içeren

`grep M[ae]k words.txt`

`grep M[ü]k words.txt`

`wget https://github.com/erkansirin78/datasets/master/sample_tc_kimlik_names_numbers.txt`

`grep [111] sample_tc_kimlik_names_numbers.txt`

`grep [0-4] sample_tc_kimlik_names_numbers.txt`

`grep [^0-9] sample_tc_kimlik_names_numbers.txt`

`grep "[0-9]\{11\}" sample_tc_kimlik_names_numbers.txt`

`grep "[A-Za-z]\{6\}" sample_tc_kimlik_names_numbers.txt`

`grep "[0-9]\{11\}" sample_tc_kimlik_names_numbers.txt`

`grep -v "[0-9]\{11\}" sample_tc_kimlik_names_numbers.txt`

`grep -v "^2" sample_tc_kimlik_names_numbers.txt`

`grep 'Ak\|ş$ sample_tc_kimlik_names_numbers.txt`

`grep -E 'Ak|ş$ sample_tc_kimlik_names_numbers.txt`

##### grep --help : grep komutunun optionları hakkında bilgi alabiliriz

`grep --help | grep '\-E'`

`grep -E 'Ak.ş$ sample_tc_kimlik_names_numbers.txt`

`grep -E 'Ak.n$ sample_tc_kimlik_names_numbers.txt`

`grep -E 'Ak.*n$ sample_tc_kimlik_names_numbers.txt`

`grep -E 'Ak.*ş$ sample_tc_kimlik_names_numbers.txt`

## Ders6:Klasör, Dosya Yaratma ve Silme: mkdir, touch, rm

`mkdir my_folder`

`ls`

`touch my_file` #dosya oluşturur

`ls`

`cd my_folder`

`pwd`

`rm my_file`

`rm my_folder`

`ls`

## Ders7:Dosya Kopyalama ve Taşıma: cp, mv

`touch my_file1`

`mkdir my_folder1`

`cp my_file1 my_folder1/` #dosya/klasör kopyalamak için kullanılır(cp filename hedefklasör)

`ls my_folder1`

`cat my_folder1/my_file1` #filename dosyası içerisindekileri yazdırır

`rm my_folder1/my_file1` #rm silmek için kullanılır

`ls my_folder1`

`mv my_file1 my_folder1/` #dosya/klasör taşımak için kullanılır(mv filename hedefklasör)

`mv my_folder1/my_file1 .`

`mv my_file1 my_file_renamed` #mv dosya veya klasör ismi değiştirmeye de yarar.

`cp my_file_renamed my_folder1/`

`mkdir second_folder`

`cp -r my_folder1/ second_folder/` #klasör dolu ise -r recursive kullanılır

`mv my_folder1/ my_folder_renam`

## Ders8:Sed Interaktif Editör

`touch output.txt`

`cat output.txt`

```
nano output.txt

line-1
line-2
line-3
line-4
line-5
```

`cat output.txt`

`sed '1d' output.txt` #ilk satırı geçici olarak siler

`sed -i '1d' output.txt` #ilk satırı kalıcı olarak siler

`cat output.txt`

##### sed 'aranan ifade yerine geçecek ifade' file

`sed 's+line+line_replaced+g' output.txt`

`sed -i 's+line+line_replaced+g' output.txt`

`sed '2,4s+line+line_replaced+g' output.txt`

## Ders9:Dosya İçeriği Okuma: cat, more, less, head ve tail

`less output.txt` # filename dosyası içerisindekileri yazdırır ve dosya içinde gezinmeyi sağlar.

`less ~/datasets/Advertising.csv`

`more ~/datasets/Advertising.csv` #filename dosyası içerisindekileri yazdırır ve dosya içinde gezinmeyi sağlar.
less'e göre biraz daha gelişmiş % olarak gösterir.

`head -n 5 ~/datasets/Advertising.csv` # İlk 5 satırı gösterir.(default=10)

`tail -n 15 ~/datasets/Advertising.csv` # son 15 satırı gösterir(default=10)

## Ders10:Standart Çıktıyı Standart Girdiye Aktarma: Pipe

`ls -l /etc`

`ls -l /etc | grep ssh`

`ls -l /etc | grep yum`

## Ders11:Standart Çıktı ve Hataları Yönlendirme: Direction

`cat output.txt`

`cat output.txt > output_directed` #> : Çıktıyı başka bir yere(dosya) yönlendirirken, olduğu gibi üzerine yazar

`cat output_directed`

`echo "This is new line" >> output_directed` #>> :  Çıktıyı başka bir yere(dosya) yönlendirir ve en alt satıra append eder

`cat output_directed`

`echo "This is another line" >> output_directed`

`cat output_directed`

`> output_directed`

`cat output_directed`

`> arrow_file`

`cat arrow_file`

`ls -l .`

`ls -l . > list_file`

`> list_file`

`&>`  #Hataları bir dosyalaya yönlendirmek için kullanılır.

`ls -l mahmut &> arrow_file`

`cat arrow_file`

`cat < output_directed` # Çıktı yönlendirme '>' ile benzer

`ls > output_directed`

`cat output_directed`

`cat < output_directed`

```
nano direction.sh

 #!/bin/bash
ls -l mahmut
ls -l
```

`chmod +> direction.sh`

`./direction.sh`

`./direction.sh > std_output`

`cat std_output`

`./direction.sh 2> std_error`

`cat std_error`

`./direction.sh &> std_err_out`

`cat std_err_out`

`./direction.sh > 2_and_1.txt 2>&1`

`cat 2_and_1.txt`

## Ders12: Kendi Çapında Bir SQL ORDER BY: sort

```
cat << EOF > sortfile.txt

ali,33
mahmut,25
cemal,41
gizem,27
burcu,33
zeynep,29
EOF
```

`cat sortfile.txt`

`sort sortfile.txt` #dosyayı alfabetik olarak sıralar

`sort -r sortfile.txt` #tam tersi şekilde sıralar

`sort -t, -k2 sortfile.txt`

`sort -t, -k2 -n sortfile.txt` #numerik olarak sıralar

## Ders13:Dosya Sıkıştırma

`for i in [1..50}; do echo "I am male"; done`

`cp ~/datasets/Advertising.csv`

`ls -l`

`ls -lh`

`gzip Advertising.csv` # Şıkıştırma işleminde kullanılır, dosyanın boyutu küçülür ve Advertising.csv.gz biçimine dönüşür

`ls -lh`

`gunzip Advertising.csv.gz` #bu dosyayı açmak için de gunzip komutu kullanılır

`gzip -c Advertising.csv > Advertising.csv.gz` #var olan Advertising.csv dosyasını bozmadan işlem yap

`ls -l`

`cp cp ~/datasets/retail_db/ .`

`ls -l retail_db/`

`gzip -r retail_db/` #Bir klasör içerisindeki tüm dosyaları sıkıştırır

`gunzip -r retail_db/`

`ls -l retail_db/`

## Ders14:Dosya Arsivleme

`ls retail_db/`

`tar -cf retail_db.tar retail_db` #dosyayı arşivlemek için kullanılır

`ls -lh`

`du -sh retail_db`

`ls -lh retail_db.tar`

`tar  -tvf retail_db.tar` #arşivin içerisindeki dosyaları listeler

`rm -r retail_db`

`tar xf retail_db.tar` #arşiv içerisindeki dosyayı çıkarır

`ls -lh`

`rm retail_db.tar`

`tar -czf retail_db.tar.gz retail_db` #arşivleyip zipler

`ls -lh`

`rm -r retail_db`

`tar xzf retail_db.tar.gz` #arşivlenniş ve ziplenmiş dosyayı çıkarır

`ls -lh`

`du -sh retail_db`

## Ders15:Dosya ve Dizin Arama

`sudo ls -l /var/lib/mlocate/`

`locate Advertising.csv`

`locate retail_db` #locate - veritabanında arama yapar

`find /home/train -name "Advertising*"` #bütün dosya sistemini dolaşır, bu yüzden bir path belirterek arama yaptırmak gerekir.

## Ders16:En Popüler İki Metin Editörü: vi ve nano

`vi list_file`
##### düzenlemek için i tusuna basabilirsiniz (kaydederek cikmak icin :wq, kaydetmeden cikmak icin :q!)

`cat list_file`

`vim list_file`

`nano list_file`

## Ders17:Dosya Sahipliği ve Erişim Yetkileri

`ls -l`

`- rw- rw- r--`

`chmod 755 2_and_1.txt`

`ls -l`

`chmod 000 simple_script.sh`

`chmod +x simple_script.sh`

`chown train:docker 2_and_1.txt`

`ls -l 2_and_1.txt`

## Ders17:Kullanıcı Oluşturma ve Silme

`sudo useradd user1`

`id user1`

`id user2`

`cat /etc/passwd | grep user1`

`sudo passwd`

`sudo usermod -aG docker user1`

`cat /etc/group | grep docker`

`sudo userdel -r user1`

## Ders18:Proses ve Servisler

`ps aux | wc -l`

`htop`

`sudo syttemctl status postresql-10`

`sudo syttemctl stop postresql-10`

`sudo syttemctl start postresql-10`

## Ders19:Bir Linux Paket Yöneticisi: yum

`sudo yum repolist`

`ls -l /etc/yum/.repos.d/`

`sudo yum install curl`

## Ders20: Crontab Giriş, Cron İfadesi ve Görev Listeleme

##### <https://crontab.guru/>

```
.---------------- dakika (0 - 59)
|  .------------- saat (0 - 23)
|  |  .---------- Ayın Günleri (1 - 31)
|  |  |  .------- Ay (1 - 12)
|  |  |  |  .---- Haftanın Günleri (0 - 6) (Pazar=0 ya da 7)
|  |  |  |  |
*  *  *  *  *  Çalıştırılacak komut
```

`crontab -l` #

`crontab -e` # Yorum satırı oluşturma

`crontab.guru/`

`* * * * * echo "hello crontab $(date)" >> /tmp/cronta.log`

`echo "hello $(date)"`

`crontab -l`

`touch /tmp/cronta.log`

`tail -f /tmp/cronta.log`

`crontab -e`

`mkdir crontab`

`cd crontab/`

`touch simple_python.py`

`vim simple_python.py`

`python simple_python.py`

`crontab -e`

```
* * * * * echo "hello crontab $(date)" >> /tmp/cronta.log
* * * * * python /home/train/crontab/simple_python.py >> /tmp/simple_python.log
```

`touch /tmp/simple_python.log`

`tail -f /tmp/simple_python.log`
