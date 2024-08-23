# CEVAPLAR

1. Aşağıdaki telefon numaralarını bir dosyaya kaydediniz. regex ile `(xxx) xxx xxxx` paternine sahip numaraları `gecerli-numaralar.txt` uymayanları da `gecersiz-numaralar.txt` dosyalarına yazdırınız.  

    ```
    (532) 432 5567
    (544) 213 8832
    (312) 244 4195
    0532 543456
    +90544 876 55 44
    (212) 220 2225
    0 (216) 395 9569
    ```

    Cevap-1:

    ```
    grep "^([0-9]\{3\}) [0-9]\{3\} [0-9]\{4\}$" numbers > gecerli-numaralar.txt
    grep -v "^([0-9]\{3\}) [0-9]\{3\} [0-9]\{4\}$" numbers > gecersiz-numaralar.txt

    [train@localhost linux]$ cat gecerli-numaralar.txt
    (532) 432 5567
    (544) 213 8832
    (312) 244 4195
    (212) 220 2225
    [train@localhost linux]$ cat gecersiz-numaralar.txt
    0532 543456
    +90544 876 55 44
    0 (216) 395 9569
    ```

2. Önemli bilgilerin bulunduğu bir dosya yaratın. Bu dosyayı sadece kullanıcı okuyabilsin.
    Cevap-2:

    ```
    [train@localhost linux]$ cat <<EOF > important_file
    > Ankara06
    > EOF
    [train@localhost linux]$ ll important_file
    -rw-rw-r--. 1 train train 9 Oct 17 22:29 important_file

    [train@localhost linux]$ chmod a=--- important_file

    [train@localhost linux]$ chmod u=r-- important_file

    [train@localhost linux]$ ll important_file
    -r--------. 1 train train 9 Oct 17 22:29 important_file

    [train@localhost linux]$ cat important_file
    Ankara06
    ```

3. 0 ile 7 arasındaki rakamların 2'lik sistemdeki ve okuma, yazma, çalıştırma modlarındaki karşılıklarını yazınız.
Örnek:

    ```
    0 -> 000 -> ---
    1 -> 001 -> --x
    2 -> 010 -> -w-
    3 -> 011 -> -wx 
    4 -> 100 -> r--
    5 -> 101 -> r-x
    6 -> 110 -> rw-
    7 -> 111 -> rwx 
    ```

4. Google'a 7 kez ping atınız ve sonuçları `google_ping_file` adında bir dosyaya yazınız.

    Cevap-4
    ```
    (venvspark) [train@localhost kurs]$ ping -c 7 google.com > google_ping_file 

    (venvspark) [train@localhost kurs]$ cat google_ping_file 
    PING google.com (172.217.169.110) 56(84) bytes of data.
    64 bytes from sof02s31-in-f14.1e100.net (172.217.169.110): icmp_seq=1 ttl=115 time=60.3 ms
    64 bytes from sof02s31-in-f14.1e100.net (172.217.169.110): icmp_seq=2 ttl=115 time=59.7 ms
    64 bytes from sof02s31-in-f14.1e100.net (172.217.169.110): icmp_seq=3 ttl=115 time=59.0 ms
    64 bytes from sof02s31-in-f14.1e100.net (172.217.169.110): icmp_seq=4 ttl=115 time=59.2 ms
    64 bytes from sof02s31-in-f14.1e100.net (172.217.169.110): icmp_seq=5 ttl=115 time=58.2 ms
    64 bytes from sof02s31-in-f14.1e100.net (172.217.169.110): icmp_seq=6 ttl=115 time=60.4 ms
    64 bytes from sof02s31-in-f14.1e100.net (172.217.169.110): icmp_seq=7 ttl=115 time=60.0 ms

    --- google.com ping statistics ---
    7 packets transmitted, 7 received, 0% packet loss, time 6036ms
    rtt min/avg/max/mdev = 58.242/59.590/60.438/0.744 ms
    ```

5. name, surname, ve age değişkenler tanımlayın. Bu değişkenleri echo ifadesi içinde aşağıdaki örnekteki sonucu verecek şekilde kullanın. 
`Hello, my name is Erkan Şirn and I am 33 years old.`
    Cevap-5
    ```
    [train@localhost kurs]$ name=Erkan
    [train@localhost kurs]$ surname=Şirin
    [train@localhost kurs]$ age=33

    [train@localhost kurs]$ echo  "Hello, my name is $name $surname and I am $age years old."
    Hello, my name is Erkan Şirin and I am 33 years old.
    ```

6. Herhangi bir metin editörü (vi, nano, gedit vb.) kullanmadan aşağıdaki yaml dosyası içinden CentOS ifadesi yerine Ubuntu yazınız. 
    ```
    cat install_httpd.yaml
    ---

    - hosts: all
    become: true
    tasks:

    - name: update yum repository
        dnf:
        update_cache: yes
        when: ansible_distribution == "CentOS"

    - name: install httpd and php package for CentOS
        dnf:
        name:
            - httpd
            - php
        state: latest
        when: ansible_distribution == "CentOS"
    ```
    Cevap-6

    ```
    sed -i 's+CentOS+Ubuntu+g' install_httpd.yaml


    cat install_httpd.yaml
    ---

    - hosts: all
    become: true
    tasks:

    - name: update yum repository
        dnf:
        update_cache: yes
        when: ansible_distribution == "Ubuntu"

    - name: install httpd and php package for Ubuntu
        dnf:
        name:
            - httpd
            - php
        state: latest
        when: ansible_distribution == "Ubuntu"
    ```

