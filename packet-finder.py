import requests
import re
import logging
import ssl
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)

# Dosyadan URL adreslerini oku
def read_urls(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

# URL'nin geçerli olup olmadığını kontrol et
def is_valid_url(url):
    # URL'yi ayrıştır
    parts = urllib.parse.urlparse(url)
    # HTTP veya HTTPS protokolü olup olmadığını kontrol et
    return parts.scheme in ['http', 'https'] and parts.netloc

# URL'de ön uç paketleyici özelliği olup olmadığını kontrol et
def check_url(url):
    try:
        # GET isteği gönder ve yanıtı bekle
        response = requests.get(url, timeout=5, verify=False)
        # Tüm olası özellikleri kontrol et
        for pattern in patterns:
            if re.search(pattern, response.text, re.IGNORECASE):
                # Özellik bulundu, URL ve bulunan özellik ile geri dön
                logging.info(f"Bu URL'de ön uç paketleyici özelliği bulundu, URL: {url}, Özellik: {pattern}")
                return url, pattern
    except requests.exceptions.RequestException as e:
        # İstek sırasında hata oluştu, hata logunu kaydet ve None dön
        logging.error(f"URL {url} erişimi başarısız: {e}")
        return None, None

if __name__ == '__main__':
    print("Packer-Finder'a hoş geldiniz")
    print("Lütfen giriş türünü seçin:")
    print("1. Dosya")
    print("2. URL listesi")
    # Kullanıcının seçimini oku
    choice = input("Seçiminizi girin (sayı olarak):")
    # Kullanıcı dosya seçtiyse
    if choice == "1":
        filename = input("Dosya adını girin:")
        urls = read_urls(filename)
    # Kullanıcı URL listesi seçtiyse
    elif choice == "2":
        urls = []
        while True:
            url = input("URL adresini girin (çıkmak için direkt Enter'a basın):")
            if not url:
                break
            if is_valid_url(url):
                urls.append(url)
            else:
                # URL geçersizse, uyarı logunu kaydet
                logging.warning(f"Geçersiz URL adresi: {url}")
    else:
        # Geçersiz seçim yapıldıysa, hata logunu kaydet ve çık
        logging.error("Geçersiz seçim")
        exit(1)

    # Tüm olası ön uç paketleyici özellikleri
    patterns = ["webpack", "vue", "react", "angular", "parcel", "gulp", "grunt", "rollup", "babel", "browserify", "next.js", "nuxt.js", "svelte"]

    # Tüm URL'leri otomatik olarak kontrol et ve ön uç paketleyici özelliği içerip içermediğini kontrol et
    hit_urls = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in urls}
        # Tüm iş parçacıklarının sonuçlarını gez
        for future in tqdm(future_to_url):
            try:
                # İş parçacığının sonucunu al
                hit_url, hit_pattern = future.result()
                if hit_url is not None:
                    hit_urls.append(hit_url)
                    # Ön uç paketleyici özelliği bulunan URL ve özelliği kaydet
                    logging.info(f"URL {hit_url} ön uç paketleyici özelliği içeriyor: {hit_pattern}")
            except requests.exceptions.Timeout as e:
                # İstek zaman aşımına uğradıysa, hata logunu kaydet
                logging.error(f"URL {future_to_url[future]} zaman aşımına uğradı, atlanıyor: {e}")
            except Exception as e:
                # İş parçacığı sonucu işlenirken hata oluştuysa, hata logunu kaydet
                logging.error(f"URL {future_to_url[future]} işlenirken hata oluştu, atlanıyor: {e}")

    # Ön uç paketleyici özelliği içeren URL'leri dosyaya kaydet
    output_filename = input("Sonuçları kaydetmek için dosya adını girin:")
    with open(output_filename, "w") as f:
        for url in hit_urls:
            f.write(url + "\n")
    # Sonuç dosyasının yolunu göster
    logging.info(f"URL adresleri dosyaya kaydedildi: {output_filename}")