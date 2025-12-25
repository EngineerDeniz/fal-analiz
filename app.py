import streamlit as st
import time
import random
import plotly.graph_objects as go
import data  # data.py dosyasını kullanmaya devam ediyoruz

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="NEO-ANALİZ", page_icon="🧬", layout="centered")

# --- ÖZEL CSS (MATRIX TEMASI) ---
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(#111 1px, transparent 1px);
        background-size: 20px 20px;
    }
    /* Yazı Renkleri */
    h1, h2, h3 {
        color: #00FF41 !important;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px #00FF41;
    }
    .stMarkdown, p, li {
        color: #E0E0E0 !important;
        font-family: 'Consolas', monospace;
    }
    /* Buton Tasarımı */
    .stButton>button {
        color: #000000;
        background-color: #00FF41;
        border: 1px solid #00FF41;
        border-radius: 0px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #000000;
        color: #00FF41;
        box-shadow: 0 0 15px #00FF41;
    }
    /* Input Alanları */
    .stTextInput>div>div>input {
        background-color: #111;
        color: #00FF41;
        border: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)


# --- FONKSİYONLAR ---

def grafik_ciz(isim):
    """
    Kişinin ismine özel (ama rastgele görünen) tutarlı bir grafik çizer.
    seed(isim) sayesinde Ahmet hep aynı grafiği alır.
    """
    random.seed(isim)
    categories = ['Mantık', 'Duygu', 'Sezgi', 'Liderlik', 'Şans']

    # Değerleri 50-100 arasında üretelim ki kimse "kötü" hissetmesin
    values = [random.randint(60, 98) for _ in range(5)]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        line_color='#00FF41',
        fillcolor='rgba(0, 255, 65, 0.2)',
        name=isim
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], linecolor='#333', gridcolor='#333'),
            bgcolor='rgba(0,0,0,0)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E0E0E0', family="Courier New"),
        showlegend=False,
        margin=dict(l=40, r=40, t=20, b=20)
    )
    return fig


def isim_analizi_html(isim):
    isim = isim.upper().strip()
    html_kod = ""
    for harf in isim:
        if harf != " ":
            # Her harfe rastgele bir hex kodu atamış gibi gösterelim
            hex_val = f"0x{ord(harf)}"
            html_kod += f"""
            <div style='display:inline-block; margin:2px; text-align:center;'>
                <span style='border:1px solid #00FF41; padding:5px; color:#00FF41; font-weight:bold;'>{harf}</span>
                <br><span style='font-size:10px; color:#666;'>{hex_val}</span>
            </div>
            """
        else:
            html_kod += "<div style='display:inline-block; width:15px;'></div>"
    return html_kod


# --- ARAYÜZ AKIŞI ---

st.markdown("<h1 style='text-align: center;'>AI DATA ANALYZER <span style='font-size:15px'>v2.0</span></h1>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666 !important;'>Algorithm: Neural-Net / Source: Numerology DB</p>",
            unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    isim = st.text_input("Kişi Adı:", placeholder="Örn: AHMET YILMAZ")
with col2:
    dogum_yili = st.number_input("D. Yılı:", min_value=1950, max_value=2015, value=2001, label_visibility="visible")

if st.button(">> ANALİZİ BAŞLAT <<"):
    if not isim:
        st.error("ERR_NULL_INPUT: Lütfen bir isim girin.")
    else:
        # 1. TİYATRO: Yükleme Ekranı
        progress_text = st.empty()
        bar = st.progress(0)

        terminal_logs = [
            "Bağlantı kuruluyor... (IP: 192.168.1.X)",
            f"Hedef analiz ediliyor: {isim.upper()}",
            "Veri tabanından desenler çekiliyor...",
            "Duygusal zeka vektörleri hesaplanıyor...",
            "Barnum etkisi simüle ediliyor...",
            "Grafik motoru başlatılıyor..."
        ]

        for i in range(100):
            time.sleep(0.02)
            if i % 15 == 0:
                log = random.choice(terminal_logs)
                progress_text.code(f">_ {log}")
            bar.progress(i + 1)

        bar.empty()
        progress_text.empty()

        # 2. SONUÇ EKRANI
        st.success("✅ İŞLEM BAŞARILI. VERİLER GÖRÜNTÜLENİYOR.")

        # A. İsim Decoding
        st.markdown(isim_analizi_html(isim), unsafe_allow_html=True)
        st.write("---")

        # B. Radar Grafiği (En Havalı Kısım)
        st.markdown("### 📊 Kişilik Spektrumu")
        st.plotly_chart(grafik_ciz(isim), use_container_width=True, config={'displayModeBar': False})

        # C. Metin Analizi (Barnum)
        st.markdown("### 🧬 Yapay Zeka Tespiti")
        random.seed(isim)  # İsim değişmezse yorum da değişmesin (Tutarlılık)
        secilen_yorum = random.choice(data.genel_analizler)
        st.info(f"Tespit: {secilen_yorum}")

        # D. Çift İsim / Tek İsim Mantığı
        kelimeler = isim.split()
        if len(kelimeler) > 1:
            st.warning(f"⚠️ **Çatışma Algılandı:** {kelimeler[0]} (Mantık) vs {kelimeler[1]} (Duygu)")
            st.write("İki isminiz arasında enerji geçişleri var. Karar alırken zorlanmanızın sebebi bu.")
        else:
            st.success(f"🎯 **Tekil Odak:** {kelimeler[0]}")
            st.write("Enerjiniz tek bir noktada toplanmış. Net ve kararlı bir yapı.")

        # 3. UPSELL (KİLİTLİ ALAN)
        st.write("---")

        with st.container():
            st.markdown("""
            <div style="background-color: #111; padding: 20px; border: 1px solid #333; border-radius: 10px; text-align: center; opacity: 0.7;">
                <h3 style="color: red !important;">🔒 KİLİTLİ RAPORLAR</h3>
                <p>⚠️ Demo sürümdesiniz. Aşağıdaki veriler gizlenmiştir:</p>
                <ul style="text-align: left; list-style-type: none;">
                    <li>❌ Ruh Eşi Uyumu Skoru (??%)</li>
                    <li>❌ 2025 Kritik Tarihler Listesi</li>
                    <li>❌ Kariyer ve Para Haritası</li>
                </ul>
                <hr>
                <p style="color: #00FF41; font-weight: bold;">🔓 Tüm masanın detaylı PDF raporunu açmak için geliştiriciye danışın. (Öğrenci İndirimi Aktif)</p>
            </div>
            """, unsafe_allow_html=True)
