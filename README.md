# DonanımHabercisi
DonanımHabercisi, ayarladığınız altforumlarda yeni konu açıldığında Discord üzerinden yine sizin ayarladığınız kanallar üzerinden haber verir. Metin kanalına birden fazla altforum atayabilir, haber vermesini istemiyorsanız kanalınızı atılacaklar listesinden çıkarabilirsiniz.
## Kurulum
Bu botu çalıştırabilmek için Python 3.9 ve üst sürümleri ve birkaç paketin kurulu olması gerekir. Gereken paketleri kurmak için terminalinize aşağıdaki ifadeyi girin.
>```console
>pip install -r requirements.txt
Girdikten sonra .env dosyasında **BOT_TOKEN** ifadesine karşılık gelen kısma Discord botunuzun tokenini girin, daha sonrasında terminale aşağıdakileri girerek botu çalıştırın.
>```
>python main.py

## Komutlar

Botun varsayılan prefixi ?'dir, değiştirmek isterseniz main.py dosyasındaki **PREFIX** değişkeninin değerini istediğiniz bir değer yapabilirsiniz.

 ### ekle
 Komut şu şekilde çalışır
 >```
 >?ekle link
 ve link parametresini alır. Burada link kontrol edilmesini istediğiniz altforumun linkidir (Örnek: https://forum.donanimhaber.com/tyt-ayt-genel-sohbet--f2642)

### sitecikar

Komut şu şekilde çalıştırılır
>```
> ?sitecikar link
ve link parametresini alır. Burada link kontrol edilmesini istemediğiniz altforum linkidir. Verdiğiniz altforumda yeni bir konu açıldığında bu komutu çalıştırdığınız kanala haber verilmeyecektir.

### cikar
Komut şu şekilde çalıştırılır
>```
>?cikar

Bu komutu kullandığınız kanala hiçbir şekilde haber verilmeyecektir.

