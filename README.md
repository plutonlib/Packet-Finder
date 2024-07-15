
# Packer-Finder

Packer-Finder, belirli URL'lerde kullanılan ön uç (frontend) paketleyici teknolojilerini tespit eden bir Python programıdır. Bu program, verilen URL'lerde önceden tanımlanmış paketleyici özelliklerini arar ve bulunan URL'leri belirtilen bir dosyaya kaydeder.

## Özellikler

- Dosyadan veya manuel olarak girilen URL listesinden URL'leri kontrol eder.
- URL'lerin geçerliliğini kontrol eder.
- Paralel işleme (multi-threading) kullanarak hızlı URL kontrolü sağlar.
- Belirli ön uç paketleyici teknolojilerini tespit eder:
  - Webpack
  - Vue.js
  - React
  - Angular
  - Parcel
  - Gulp
  - Grunt
  - Rollup
  - Babel
  - Browserify
  - Next.js
  - Nuxt.js
  - Svelte
- Bulunan URL'leri belirtilen bir dosyaya kaydeder.

## Gereksinimler

- Python 3.x
- Aşağıdaki Python kütüphaneleri:
  - requests
  - re (standard library)
  - logging (standard library)
  - ssl (standard library)
  - urllib (standard library)
  - concurrent.futures (standard library)
  - tqdm

## Kurulum

1. Python 3.x'in sisteminizde kurulu olduğundan emin olun.
2. Gerekli Python kütüphanelerini yükleyin:
   ```sh
   pip install requests tqdm
   ```

## Kullanım

### 1. Dosyadan URL Okuma

1. `urls.txt` adında bir dosya oluşturun ve her satıra bir URL yazın.
2. Programı çalıştırın ve dosya seçeneğini seçin:
   ```sh
   python packer_finder.py
   ```
3. Dosya adını girin (örneğin: `urls.txt`).
4. Sonuçların kaydedileceği dosya adını girin (örneğin: `results.txt`).

### 2. Manuel Olarak URL Girişi

1. Programı çalıştırın ve URL listesi seçeneğini seçin:
   ```sh
   python packer_finder.py
   ```
2. URL'leri teker teker girin. Girişi bitirmek için sadece Enter tuşuna basın.
3. Sonuçların kaydedileceği dosya adını girin (örneğin: `results.txt`).

### Örnek Kullanım

#### Dosyadan URL Okuma
```sh
python packer_finder.py
# Hoş geldiniz mesajı ve seçim ekranı
# 1'i seçin ve dosya adını girin: urls.txt
# Sonuçların kaydedileceği dosya adını girin: results.txt
```

#### Manuel URL Girişi
```sh
python packer_finder.py
# Hoş geldiniz mesajı ve seçim ekranı
# 2'yi seçin ve URL'leri tek tek girin:
# http://example.com
# http://anotherexample.com
# (Enter tuşuna basarak bitirin)
# Sonuçların kaydedileceği dosya adını girin: results.txt
```

## Kodun Açıklaması

- `read_urls(filename)`: Belirtilen dosyayı okuyarak URL'leri döner.
- `is_valid_url(url)`: URL'nin geçerli olup olmadığını kontrol eder.
- `check_url(url)`: Verilen URL'ye GET isteği yapar ve önceden tanımlanmış paketleyici özelliklerini arar.
- Ana program:
  - Kullanıcıdan giriş türünü (dosya veya manuel URL) seçmesini ister.
  - URL'leri kontrol eder ve tespit edilenleri bir dosyaya kaydeder.

## Loglama ve Hata Yönetimi

- Program, loglama ile hataları ve önemli olayları kaydeder.
- Geçersiz URL'ler ve erişim hataları loglanır.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
