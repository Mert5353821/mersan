import streamlit as st
import pandas as pd

# SAYFA AYARLARI
st.set_page_config(page_title="Mersan Gelişim Atölyesi", page_icon="🌿")

# GOOGLE TABLO BAĞLANTISI (Sadece ID'yi değiştirin)
SHEET_ID = "TABLO_ID_BURAYA" 
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

# TASARIM (CSS)
st.markdown("""
    <style>
    .report-card { background: white; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); margin-bottom: 10px; }
    .stButton>button { background-color: #2e7d32; color: white; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 Mersan Gelişim Atölyesi")
st.subheader("Veli Bilgi Sistemi")

# VELİ GİRİŞ EKRANI
veli_kodu = st.text_input("Size verilen veli kodunu giriniz:", type="password")

if veli_kodu:
    try:
        # Veriyi Google Tablodan Çek
        df = pd.read_csv(SHEET_URL)
        
        # Filtreleme
        filtre = df[df['veli_kodu'].astype(str) == veli_kodu]
        
        if not filtre.empty:
            ogrenci = filtre['ogrenci_adi'].iloc[0]
            st.success(f"Hoş geldiniz, {ogrenci} Velisi")
            
            for index, row in filtre[::-1].iterrows():
                st.markdown(f"""
                    <div class="report-card">
                        <small>{row['tarih']}</small>
                        <h4>Günlük Gelişim Raporu</h4>
                        <p>{row['rapor_notu']}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Hatalı kod! Lütfen kurumla iletişime geçin.")
    except Exception as e:
        st.error("Veri bağlantısında hata oluştu. Lütfen Tablo ID'sini kontrol edin.")

st.info("💡 Not: Raporları doğrudan Google E-Tablo üzerinden güncelleyebilirsiniz, siteye otomatik yansır.")

