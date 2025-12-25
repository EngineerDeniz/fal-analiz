import streamlit as st
import time
import random
import data  # data.py dosyasını çağırıyoruz

# --- AYARLAR ---
st.set_page_config(page_title="AI Karakter Analizi", page_icon="🧬", layout="centered")

# CSS: Matrix Havası (Siyah Arkaplan, Yeşil Yazılar)
st.markdown("""
<style>
    .stApp {background-color: #0E1117;}
    h1, h2, h3 {color: #00FF41 !important;}
    p {color: #E0E0E0;}
    .stButton>button {
        color: #0E1117;
        background-color: #00FF41;
        border-radius: 5px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# --- FONKSİYONLAR ---

def hayat_yolu_hesapla(dogum_yili):
    # Rakamları topla (Örn: 2002 -> 2+0+0+2 = 4)
    toplam = sum(int(hane) for hane in str(dogum_yili))
    # Eğer 9'dan büyükse tekrar topla (Örn: 1998 -> 27 -> 2+7=9)
    while toplam > 9:
        toplam = sum(int(hane) for hane in str(toplam))
    return toplam


def isim_analizi_yap(isim):
    isim = isim.strip().upper()
    kelimeler = isim.split()

    # Görsel "Decoding" Efekti
    st.markdown("### 🧬 Veri Çözümleniyor...")
    html_kod = "".join([
                           f"<span style='border:1px solid #00FF41; padding:3px; margin:1px; color:#00FF41; font-family:monospace'>{h}</span>"
                           for h in isim])
    st.markdown(f"<div style='text-align:center; font-size:20px; margin-bottom:20px'>{html_kod}</div>",
                unsafe_allow_html=True)

    if len(kelimeler) > 1:
        st.warning(f"⚠️ **Çift Çekirdek (Dual Core) Tespit Edildi:** {kelimeler[0]} vs {kelimeler[1]}")
        st.write(
            f"Algoritma, **{kelimeler[0]}** ismindeki mantık ile **{kelimeler[1]}** ismindeki duygu arasında bir çatışma yakaladı.")
    else:
        st.info(f"✅ **Tekil Odak (Single Core) Tespit Edildi:** {isim}")
        st.write(
            f"Enerjiniz bölünmemiş, **{isim[0]}** harfi ile güçlü bir başlangıç yapıp **{isim[-1]}** harfi ile işleri bitiriyorsunuz.")


# --- ARAYÜZ ---

st.title("VERİ TABANLI KARAKTER ANALİZİ v1.4")
st.caption("Not: Bu sistem fal değildir. İsim ve doğum tarihinin matematiksel izdüşümünü çıkarır.")

isim = st.text_input("İsim Soyisim Giriniz:")
dogum_yili = st.number_input("Doğum Yılı:", min_value=1950, max_value=2015, value=2000)

if st.button("ALGORİTMAYI ÇALIŞTIR"):
    if not isim:
        st.error("Lütfen bir veri girişi yapın.")
    else:
        # 1. TİYATRO KISMI (Loading Bar)
        bar = st.progress(0, text="Sunucuya bağlanılıyor...")
        for i in range(100):
            time.sleep(0.015)  # Bekleme süresi
            mesajlar = ["Veri setleri taranıyor...", "ASCII kodları çözülüyor...", "Kuantum eşleşme sağlanıyor...",
                        "Analiz tamamlanıyor..."]
            if i % 25 == 0:
                bar.progress(i + 1, text=random.choice(mesajlar))
            else:
                bar.progress(i + 1)
        time.sleep(0.5)
        bar.empty()

        # 2. SONUÇ EKRANI
        st.success("✅ ANALİZ BAŞARIYLA TAMAMLANDI")

        # Fonksiyonları Çağır
        isim_analizi_yap(isim)

        st.divider()

        # Numeroloji Sonucu
        sayi = hayat_yolu_hesapla(dogum_yili)
        st.subheader(f"🔢 Hayat Yolu Sayınız: {sayi}")
        st.write(data.numeroloji.get(sayi, "Özel bir enerji."))

        st.divider()

        # Barnum (Genel) Sonuç
        st.subheader("💡 Yapay Zeka Tespiti:")
        st.write(f"_{random.choice(data.genel_analizler)}_")

        # 3. UPSELL (SATIŞ) KISMI - PARA BURADA
        st.markdown("---")
        st.error("🔒 **KİLİTLİ ÖZELLİK: İLİŞKİ VE GELECEK RAPORU**")
        st.markdown("""
        Algoritma ayrıca şunları hesapladı ama **Demo Sürümde** gösterilmiyor:
        * ❤️ **Ruh Eşi Uyumu (Yüzdelik Skor)**
        * 📅 **2025 Kritik Tarihler Raporu**
        * ⚠️ **Gizli Tehlike Analizi**

        _Öğrenci işi bir kahve parasına (50₺) tüm detaylı PDF raporunu açtırabilirsiniz._
        """)