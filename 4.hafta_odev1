# Başlangıç sözlüğü
ogrenciler = {
    "Ali": {"Matematik": 80, "Fizik": 75, "Kimya": 90},
    "Ayşe": {"Matematik": 90, "Fizik": 85, "Kimya": 88},
    "Mehmet": {"Matematik": 70, "Fizik": 60, "Kimya": 75}
}

print("Öğrenci Not Sistemi")

# Kullanıcıdan isim ve ders bilgisi alma
isim = input("Öğrenci adı: ")
ders = input("Ders adı (Matematik, Fizik, Kimya): ")

# Bilgi varsa gösterme
if isim in ogrenciler and ders in ogrenciler[isim]:
    print(f"{isim} adlı öğrencinin {ders} notu: {ogrenciler[isim][ders]}")
else:
    print("Böyle bir öğrenci veya ders bulunamadı.")

# --- Değer değiştirme ---
degistir = input("Bir not değiştirmek ister misiniz? (e/h): ")

if degistir == "e":
    isim2 = input("Notunu değiştirmek istediğiniz öğrenci: ")
    ders2 = input("Ders adı: ")
    yeni_not = int(input("Yeni not: "))
    
    if isim2 in ogrenciler and ders2 in ogrenciler[isim2]:
        ogrenciler[isim2][ders2] = yeni_not
        print("Not güncellendi!")
    else:
        print("Bilgi bulunamadı.")

# --- Yeni öğrenci ekleme ---
ekle = input("Yeni öğrenci eklemek ister misiniz? (e/h): ")

if ekle == "e":
    yeni_isim = input("Yeni öğrenci adı: ")
    mat = int(input("Matematik notu: "))
    fiz = int(input("Fizik notu: "))
    kim = int(input("Kimya notu: "))
    
    ogrenciler[yeni_isim] = {"Matematik": mat, "Fizik": fiz, "Kimya": kim}
    print("Öğrenci eklendi!")

# En son sözlüğü yazdırma
print("\nGüncel öğrenci listesi:")
print(ogrenciler)
