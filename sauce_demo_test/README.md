## Pytest-Decarators


## ![image](https://github.com/mehtaptunc/Selenium-SauceDemo/assets/134071818/c00ad4d8-39e3-4356-b911-147eb45bf47b)


PyTest belgelerine göre, şu anda PyTest'te 100'den fazla decorator bulunmaktadır. Bu decoratorler, aşağıdaki kategorilere ayrılabilir:





1-Test çalıştırma davranışını kontrol eden decoratorler: Bu decoratorler, testlerin hangi durumlarda çalıştırılacağını ve nasıl çalıştırılacağını kontrol eder.

Örneğin, @pytest.mark.skip decoratoru, testi atlar, @pytest.mark.parametrize decoratoru, test fonksiyonunu farklı girdilerle çalıştırır ve @pytest.mark.xfail decoratoru, testin başarısız olmasını bekler.







2-Test sonuçlarını kontrol eden decoratorler: Bu decoratorler, testlerin başarısız olması için gereken koşulları kontrol eder. 

Örneğin, @pytest.mark.raises decoratoru, belirli bir hata türünün ortaya çıkmasını bekler.







3-Test verilerini kontrol eden decoratorler: Bu decoratorler, testlere sağlanan verileri kontrol eder.

Örneğin, @pytest.mark.config decoratoru, testlere sağlanan konfigürasyon verilerini kontrol eder.






4-Testleri raporlayan decoratorler: Bu decoratorler, testlerin sonuçlarını raporlar. 

Örneğin, @pytest.mark.describe decoratoru, testleri gruplar ve  @pytest.mark.tag decoratoru, testlere etiketler ekler.






Decoratorleri kullanmanın bazı örnekleri şunlardır:

## @pytest.mark.skip

![pytest_mark skip](https://github.com/mehtaptunc/Selenium-SauceDemo/assets/134071818/3cdef1d7-2e0b-48f9-bfd3-ecffd5000c09)


Bu decorator, testi atlar. Örneğin, aşağıdaki kod, yalnızca belirli bir ortamda çalışan bir testi atlar:


@pytest.mark.skipif(os.environ.get("ENV") != "prod", reason="Bu test yalnızca üretim ortamında çalışır")
def test_production(self):
   







## @pytest.mark.parametrize

Bu decorator, test fonksiyonunu farklı girdilerle çalıştırır. Örneğin, aşağıdaki kod, username ve password değişkenlerine farklı değerler atayarak test_login() testini çalıştırır:


@pytest.mark.parametrize("username, password", [("kullanıcıadı", "parola"), ("başka_kullanıcı", "başka_parola")])
def test_login(self, username, password):

 


![pytest_mark parametrize](https://github.com/mehtaptunc/Selenium-SauceDemo/assets/134071818/026d5b6d-077e-4459-a836-77c90b7edb3d)






## @pytest.mark.xfail

Bu decorator, testin başarısız olmasını bekler. Örneğin, aşağıdaki kod, henüz tamamlanmamış bir testi işaretler:

Python
@pytest.mark.xfail
def test_not_implemented(self):














## Decoratorleri kullanmanın bazı avantajları şunlardır:

-Testleri daha okunaklı ve yönetilebilir hale getirirler.

-Testleri tekrar kullanılabilir hale getirirler.

-Testlerin yürütülmesini daha esnek hale getirirler.

Decoratorleri kullanmanın diğer birçok yolu vardır. PyTest belgelerini daha fazla bilgi için inceleyebilirsiniz.




