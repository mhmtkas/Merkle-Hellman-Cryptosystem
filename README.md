# Merkle-Hellman-Cryptosystem
--Şifreleme

Mesajı şifrelemek için; A'nın kolay kırılamayan sırt çantasının altkümesinden seçilen anahtar uzunluğunda bit kümesi ile karşılastırılır. Açık anahtardaki her bir terim, düz metindeki bir elemanı A_m altkümesinin bir elemanını karşılar, düz metindeki 0 A_m kümesinin inşa edilmesini göz ardı eder.Bu altkümenin elemanları toplanmış ve toplamanın sonucu şifrelenmiş metindir.

--Deşifreleme

Deşifreleme mümkündür; çünkü çarpan ve modül kolayca çevrilebilir, süper artan sırt çantasındaki acık anahtar,böylece süper artan sırt çantasındaki elemanların karşılandığı toplamdaki şifreli metin sayı dönüştürme çevriminde kullanılabilir. Sonra; basit bir Greedy Algoritması kullanılarak, basit sırt çantası Büyük o gösterimindeki aritmetik operatörler kullanılarak çözülür. Böylece mesaj deşifrelenmiş olur.

# Matematiksel Metod #
--Anahtar üretimi

n bitten oluşan mesajı şifrelemek için süperartan bir dizi seçilir:
        w = (w1, w2, ..., wn)   n sıfırdan farklı doğal sayı. 
q gibi bir rastgele sayı seçilir:
        {\displaystyle q>\sum _{i=1}^{n}w_{i}} ve r gibi rastgele bir sayı seçilir:
        Ortak bölen(r,q) = 1 (r ve q  Aralarında asal)
q nun böyle seçilmesi şifrelenmiş metnin benzersiz olmasını sağlar. Eğer q düz metinden daha küçük seçilirse, aynı şifrelenmiş metinler elde edilebilir. r ile q aralarında asal olmalıdır yoksa mod q göre tersine çevrilemeyecektir. q nun tersinin olması gereklidir. Böylece deşifreleme yapılabilir.
Şimdi diziyi hesaplayalım:
β = (β1, β2, ..., βn)
βi = rwi mod q.
Açık Anahtar β ve Gizli Anahtarlar (w, q, r) dir.

--Şifreleme

n bit mesajı şifrelemek için

α = (α1, α2, ..., αn),
{\displaystyle \alpha _{i}}{\displaystyle \alpha _{i}} mesajın i. biti ve {\displaystyle \alpha _{i}{\boldsymbol {\in }}}{\displaystyle \alpha _{i}{\boldsymbol {\in }}}{0, 1}
{\displaystyle c=\sum _{i=1}^{n}\alpha _{i}\beta _{i}.}{\displaystyle c=\sum _{i=1}^{n}\alpha _{i}\beta _{i}.}
Şifrelenmiş metin c dir.
  


