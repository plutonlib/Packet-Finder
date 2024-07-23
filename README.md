
# Scouter

[English](#English) | [Türkçe](#Türkçe)

## English

Scouter is a Python program that detects frontend bundling technologies used in specified URLs. This program searches for predefined bundling features in the given URLs and saves the found URLs to a specified file.

### Features

- Checks URLs from a file or manually entered URL list.
- Verifies the validity of URLs.
- Utilizes multi-threading for fast URL checking.
- Detects various frontend bundling technologies and platforms:
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
  - jQuery
  - Ember.js
  - Backbone.js
  - Knockout.js
  - Dojo
  - Ext.js
  - Meteor
  - Aurelia
  - Polymer
  - Lit-element
  - Stencil
  - Mithril
  - Marionette
  - Riot.js
  - Alpine.js
  - SproutCore
  - Enyo
  - Chaplin
  - Famous
  - Frzr
  - Glimmer
  - Rivets.js
  - Derby
  - Sammy.js
  - GWT
  - Qooxdoo
  - Zino-UI
  - WTK
  - Zepto
  - Highcharts
  - D3.js
  - Chart.js
  - Three.js
  - Pixi.js
  - Babylon.js
  - Phaser
  - CreateJS
  - Greensock
  - GSAP
  - Anime.js
  - P5.js
  - Processing
  - Paper.js
  - Zdog
  - Sprite.js
  - Two.js
  - Mo.js
  - Kute.js
  - Lottie
  - Snap.svg
  - Tailwind
  - Bootstrap
  - Foundation
  - Bulma
  - Materialize
  - UIkit
  - Semantic-UI
  - Spectre.css
  - Milligram
  - PureCSS
  - Skeleton
  - Xenforo
  - WordPress
  - Drupal
  - Joomla
  - Magento
  - Shopify
  - PrestaShop
  - Ghost
  - Jekyll
  - Hugo
  - Hexo
  - Octopress
  - Gatsby
  - Eleventy
  - Gridsome
  - Nuxt
  - Docusaurus
  - Sapper
  - Saber
  - Nextra
  - Middleman
  - Brunch
  - Assemble
  - Roots
  - Wintersmith
  - Metalsmith
  - Cloudflare
  - Firebase
  - Amazon Cloudfront
  - Akamai
  - Incapsula
  - Sucuri

### Requirements

- Python 3.x
- The following Python libraries:
  - requests
  - re (standard library)
  - logging (standard library)
  - ssl (standard library)
  - urllib (standard library)
  - concurrent.futures (standard library)
  - tqdm

### Installation

1. Ensure that Python 3.x is installed on your system.
2. Install the required Python libraries:
   ```sh
   pip install requests tqdm
   ```

### Usage

#### 1. Checking URLs from a file

1. Create a file named `urls.txt` and write one URL per line.
2. Run the program and select the file option:
   ```sh
   python packer_finder.py
   ```
3. Enter the file name (e.g., `urls.txt`).
4. Enter the name of the file to save the results (e.g., `results.txt`).

#### 2. Manually entering URLs

1. Run the program and select the URL list option:
   ```sh
   python packer_finder.py
   ```
2. Enter the URLs one by one. Press Enter to finish.
3. Enter the name of the file to save the results (e.g., `results.txt`).

### Example Usage

#### Checking URLs from a file
```sh
python packer_finder.py
# Welcome message and selection screen
# Select 1 and enter the file name: urls.txt
# Enter the name of the file to save the results: results.txt
```

#### Manually entering URLs
```sh
python packer_finder.py
# Welcome message and selection screen
# Select 2 and enter the URLs one by one:
# http://example.com
# http://anotherexample.com
# (Press Enter to finish)
# Enter the name of the file to save the results: results.txt
```

### Code Explanation

- `read_urls(filename)`: Reads the specified file and returns the URLs.
- `is_valid_url(url)`: Checks if the URL is valid.
- `check_url(url)`: Sends a GET request to the given URL and searches for predefined bundling features.
- Main program:
  - Prompts the user to select the input type (file or manual URL).
  - Checks the URLs and saves the detected ones to a file.

### Logging and Error Handling

- The program logs errors and significant events.
- Invalid URLs and access errors are logged.

### License

This project is licensed under the MIT License. For more information, see the LICENSE file.

## Türkçe

Scouter, belirli URL'lerde kullanılan ön uç (frontend) paketleyici teknolojilerini tespit eden bir Python programıdır. Bu program, verilen URL'lerde önceden tanımlanmış paketleyici özelliklerini arar ve bulunan URL'leri belirtilen bir dosyaya kaydeder.

### Özellikler

- Dosyadan veya manuel olarak girilen URL listesinden URL'leri kontrol eder.
- URL'lerin geçerliliğini kontrol eder.
- Paralel işleme (multi-threading) kullanarak hızlı URL kontrolü sağlar.
- Çeşitli ön uç paketleyici teknolojilerini ve platformları tespit eder:
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
  - jQuery
  - Ember.js
  - Backbone.js
  - Knockout.js
  - Dojo
  - Ext.js
  - Meteor
  - Aurelia
  - Polymer
  - Lit-element
  - Stencil
  - Mithril
  - Marionette
  - Riot.js
  - Alpine.js
  - SproutCore
  - Enyo
  - Chaplin
  - Famous
  - Frzr
  - Glimmer
  - Rivets.js
  - Derby
  - Sammy.js
  - GWT
  - Qooxdoo
  - Zino-UI
  - WTK
  - Zepto
  - Highcharts
  - D3.js
  - Chart.js
  - Three.js
  - Pixi.js
  - Babylon.js
  - Phaser
  - CreateJS
  - Greensock
  - GSAP
  - Anime.js
  - P5.js
  - Processing
  - Paper.js
  - Zdog
  - Sprite.js
  - Two.js
  - Mo.js
  - Kute.js
  - Lottie
  - Snap.svg
  - Tailwind
  - Bootstrap
  - Foundation
  - Bulma
  - Materialize
  - UIkit
  - Semantic-UI
  - Spectre.css
  - Milligram
  - PureCSS
  - Skeleton
  - Xenforo
  - WordPress
  - Drupal
  - Joomla
  - Magento
  - Shopify
  - PrestaShop
  - Ghost
  - Jekyll
  - Hugo
  - Hexo
  - Octopress
  - Gatsby
  - Eleventy
  - Gridsome
  - Nuxt
  - Docusaurus
  - Sapper
  - Saber
  - Nextra
  - Middleman
  - Brunch
  - Assemble
  - Roots
  - Wintersmith
  - Metalsmith
  - Cloudflare
  - Firebase
  - Amazon Cloudfront
  - Akamai
  - Incapsula
  - Sucuri

### Gereksinimler

- Python 3.x
- Aşağıdaki Python kütüphaneleri:
  - requests
  - re (standart kütüphane)
  - logging (standart kütüphane)
  - ssl (standart kütüphane)
  - urllib (standart kütüphane)
  - concurrent.futures (standart kütüphane)
  - tqdm

### Kurulum

1. Python 3.x'in sisteminizde kurulu olduğundan emin olun.
2. Gerekli Python kütüphanelerini yükleyin:
   ```sh
   pip install requests tqdm
   ```

### Kullanım

#### 1. Dosyadan URL Okuma

1. `urls.txt` adında bir dosya oluşturun ve her satıra bir URL yazın.
2. Programı çalıştırın ve dosya seçeneğini seçin:
   ```sh
   python packer_finder.py
   ```
3. Dosya adını girin (örneğin: `urls.txt`).
4. Sonuçların kaydedileceği dosya adını girin (örneğin: `results.txt`).

#### 2. Manuel Olarak URL Girişi

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

### Kodun Açıklaması

- `read_urls(filename)`: Belirtilen dosyayı okuyarak URL'leri döner.
- `is_valid_url(url)`: URL'nin geçerli olup olmadığını kontrol eder.
- `check_url(url)`: Verilen URL'ye GET isteği yapar ve önceden tanımlanmış paketleyici özelliklerini arar.
- Ana program:
  - Kullanıcıdan giriş türünü (dosya veya manuel URL) seçmesini ister.
  - URL'leri kontrol eder ve tespit edilenleri bir dosyaya kaydeder.

### Loglama ve Hata Yönetimi

- Program, loglama ile hataları ve önemli olayları kaydeder.
- Geçersiz URL'ler ve erişim hataları loglanır.

### Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
