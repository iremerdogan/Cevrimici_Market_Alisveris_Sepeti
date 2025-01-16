import os

class Market:
    def __init__(self, file_name="urunler.txt"):
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()

    def __del__(self):
        print("Market uygulaması sonlandırılıyor. Dosya kapatıldı.")

    def urunleri_listele(self):
        """Dosyadaki tüm ürünleri listele."""
        with open(self.file_name, "r") as file:
            lines = file.read().splitlines()

        if not lines:
            print("Ürün listesi boş.")
        else:
            print("Ürün Listesi:")
            for line in lines:
                urun_adi, kategori, fiyat, stok = line.split(",")
                print(f"Adı: {urun_adi}, Kategori: {kategori}, Fiyat: {fiyat} TL, Stok: {stok}")

    def urun_ekle(self):
        """Yeni bir ürün ekle."""
        urun_adi = input("Ürün adını girin: ")
        kategori = input("Kategori girin: ")
        fiyat = input("Fiyat girin: ")
        stok = input("Stok miktarını girin: ")

        with open(self.file_name, "a") as file:
            file.write(f"{urun_adi},{kategori},{fiyat},{stok}\n")

        print(f"{urun_adi} başarıyla eklendi.")

    def urun_sil(self):
        """Bir ürünü sil."""
        urun_adi = input("Silinecek ürünün adını girin: ")

        with open(self.file_name, "r") as file:
            lines = file.read().splitlines()

        updated_lines = [line for line in lines if not line.startswith(urun_adi + ",")]

        if len(lines) == len(updated_lines):
            print(f"{urun_adi} adında bir ürün bulunamadı.")
            return

        with open(self.file_name, "w") as file:
            for line in updated_lines:
                file.write(line + "\n")

        print(f"{urun_adi} başarıyla silindi.")

def menu():
    market = Market()

    while True:
        print("\n*** MENÜ ***")
        print("1) Ürünleri Listele")
        print("2) Ürün Ekle")
        print("3) Ürün Sil")
        print("4) Çıkış")

        secim = input("Seçiminizi yapın (1-4): ")

        if secim == "1":
            market.urunleri_listele()
        elif secim == "2":
            market.urun_ekle()
        elif secim == "3":
            market.urun_sil()
        elif secim == "4":
            print("Çıkış yapılıyor. Hoşça kalın!")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()
