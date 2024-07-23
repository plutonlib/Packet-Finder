import requests
import re
import logging
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import os

logging.basicConfig(level=logging.INFO)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Dosyadan URL adreslerini oku
def read_urls(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        logging.error(f"Dosya bulunamadı: {filename}")
        exit(1)

# URL'nin geçerli olup olmadığını kontrol et
def is_valid_url(url):
    parts = urllib.parse.urlparse(url)
    return parts.scheme in ['http', 'https', 'file'] and parts.netloc or parts.path

# URL veya dosyada ön uç paketleyici özelliği olup olmadığını kontrol et
def check_url(url):
    try:
        logging.info(f"URL kontrol ediliyor: {url}")
        parts = urllib.parse.urlparse(url)
        if parts.scheme in ['http', 'https']:
            response = requests.get(url, timeout=10, verify=False)
            logging.info(f"URL yanıt kodu: {response.status_code}")
            logging.info(f"Yanıt metni (ilk 500 karakter): {response.text[:500]}")

            if response.status_code == 200:
                return search_patterns(url, response.text, response.headers)
            else:
                logging.warning(f"URL {url} beklenmedik yanıt kodu aldı: {response.status_code}")
        elif parts.scheme == 'file':
            path = parts.path
            if os.path.exists(path):
                with open(path, 'r') as file:
                    content = file.read()
                    return search_patterns(url, content, {})
            else:
                logging.error(f"Dosya bulunamadı: {path}")
    except requests.exceptions.RequestException as e:
        logging.error(f"URL {url} erişimi başarısız: {e}")
    return None, None

# İçeriği kontrol edip desenleri arayan fonksiyon
def search_patterns(url, content, headers):
    found_patterns = []
    for pattern, pattern_type in patterns.items():
        if pattern_type == 'body':
            if re.search(pattern, content, re.IGNORECASE):
                logging.info(f"Özellik bulundu: {pattern}")
                found_patterns.append(pattern)
        elif pattern_type == 'header':
            for header, value in headers.items():
                if re.search(pattern, value, re.IGNORECASE):
                    logging.info(f"Özellik bulundu (header): {pattern}")
                    found_patterns.append(pattern)
    if found_patterns:
        return url, ', '.join(found_patterns)
    return None, None

if __name__ == '__main__':
    print("Scouter'a hoş geldiniz")
    print("Lütfen giriş türünü seçin:")
    print("1. Dosya")
    print("2. URL listesi")
    choice = input("Seçiminizi girin (sayı olarak):")
    if choice == "1":
        filename = input("Dosya adını girin:")
        urls = list(read_urls(filename))
        logging.info(f"Toplam {len(urls)} URL yüklendi.")
    elif choice == "2":
        urls = []
        while True:
            url = input("URL adresini girin (çıkmak için direkt Enter'a basın):")
            if not url:
                break
            if is_valid_url(url):
                urls.append(url)
            else:
                logging.warning(f"Geçersiz URL adresi: {url}")
        logging.info(f"Toplam {len(urls)} URL yüklendi.")
    else:
        logging.error("Geçersiz seçim")
        exit(1)

    patterns = {
        "webpack": "body", "vue": "body", "react": "body", "angular": "body",
        "parcel": "body", "gulp": "body", "grunt": "body", "rollup": "body",
        "babel": "body", "browserify": "body", "next.js": "body", "nuxt.js": "body",
        "svelte": "body", "jquery": "body", "ember.js": "body", "backbone.js": "body",
        "knockout.js": "body", "dojo": "body", "ext.js": "body", "meteor": "body",
        "aurelia": "body", "polymer": "body", "lit-element": "body", "stencil": "body",
        "mithril": "body", "marionette": "body", "riot.js": "body", "alpine.js": "body",
        "sproutcore": "body", "enyo": "body", "chaplin": "body", "famous": "body",
        "frzr": "body", "glimmer": "body", "rivets.js": "body", "derby": "body",
        "sammy.js": "body", "gwt": "body", "qooxdoo": "body", "zino-ui": "body",
        "wtk": "body", "zepto": "body", "highcharts": "body", "d3.js": "body",
        "chart.js": "body", "three.js": "body", "pixi.js": "body", "babylon.js": "body",
        "phaser": "body", "createjs": "body", "greensock": "body", "gsap": "body",
        "anime.js": "body", "p5.js": "body", "processing": "body", "paper.js": "body",
        "zdog": "body", "sprite.js": "body", "two.js": "body", "mo.js": "body",
        "kute.js": "body", "lottie": "body", "snap.svg": "body", "tailwind": "body",
        "bootstrap": "body", "foundation": "body", "bulma": "body", "materialize": "body",
        "uikit": "body", "semantic-ui": "body", "spectre.css": "body", "milligram": "body",
        "purecss": "body", "skeleton": "body", "xenforo": "body", "wordpress": "body",
        "drupal": "body", "joomla": "body", "magento": "body", "shopify": "body",
        "prestashop": "body", "ghost": "body", "jekyll": "body", "hugo": "body",
        "hexo": "body", "octopress": "body", "gatsby": "body", "eleventy": "body",
        "gridsome": "body", "nuxt": "body", "docusaurus": "body", "sapper": "body",
        "saber": "body", "nextra": "body", "middleman": "body", "brunch": "body",
        "assemble": "body", "roots": "body", "wintersmith": "body", "metalsmith": "body",
        "cloudflare": "header", "firebase": "header", "amazon cloudfront": "header",
        "akamai": "header", "incapsula": "header", "sucuri": "header"
    }

    hit_urls = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in urls}
        for future in tqdm(future_to_url):
            try:
                hit_url, hit_pattern = future.result()
                if hit_url is not None:
                    hit_urls.append(f"{hit_url} -> {hit_pattern}")
                    logging.info(f"URL {hit_url} ön uç paketleyici özelliği içeriyor: {hit_pattern}")
            except requests.exceptions.Timeout as e:
                logging.error(f"URL {future_to_url[future]} zaman aşımına uğradı, atlanıyor: {e}")
            except Exception as e:
                logging.error(f"URL {future_to_url[future]} işlenirken hata oluştu, atlanıyor: {e}")

    output_filename = input("Sonuçları kaydetmek için dosya adını girin:")
    with open(output_filename, "w") as f:
        for url in hit_urls:
            f.write(url + "\n")
    logging.info(f"URL adresleri dosyaya kaydedildi: {output_filename}")
