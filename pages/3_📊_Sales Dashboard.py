import streamlit as st
from PIL import Image
import subprocess
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Bruule.it",
    page_icon="🫶🏻", 
    layout="wide"                                                                      
)
st.sidebar.success("Made by kelompok . ")


# Menggunakan CSS lokal untuk gaya khusus
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#----memuat asset---
Image_contact_form = Image.open("images/1.png")
Image_lottie_animation = Image.open("images/2.png")
Image_3 = Image.open("images/3.png")
Image_4 = Image.open("images/4.png") 

#----manual selected----
if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
    manual_select = st.session_state['menu_option']
else:
    manual_select = None

selected4 = option_menu(None, ["Home", "Menu", "Kontak", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    orientation="horizontal", manual_select=manual_select, key='menu_4')
st.button(f"Next {st.session_state.get('menu_option', 1)}", key='switch_button')
# judul halaman 
with st.container():
    st.markdown("<h1 class='centered-header'>Review Product </h1>", unsafe_allow_html=True)
    st.header("Brulee.it - Cita Rasa Keju Autentik dalam Setiap Gigitan!")
st.write("""Selamat datang di Brulee.it! Di sini, kami menghadirkan hidangan lezat yang kaya
        akan keju dan rasa autentik Italia. Untuk kamu pecinta keju, Brulee.it adalah pilihan 
        yang sempurna!
""")
#---asset video---
with st.container():
    st.video('https://youtu.be/Imqlv3Tn9GY')

# Tambahkan judul
st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Testimoni")
st.header("Brulee.it - Cita Rasa Keju Autentik dalam Setiap Gigitan!")
st.write("""Brulee.it benar-benar memanjakan para pecinta makanan dengan hidangan 
        yang kaya akan keju dan rasa autentik ala Italia!
        Dari dimsum yang lembut dengan sentuhan saus keju yang lezat
        hingga spaghetti dan macaroni yang dimasak sempurna, setiap hidangan
        memberikan kenikmatan yang luar biasa. Pelanggan kami selalu memberi tanggapan 
        positif tentang rasa yang konsisten, porsi yang memuaskan, dan pelayanan yang ramah.
        Tak heran jika banyak yang kembali lagi dan menjadi pelanggan setia kami!
""")
# Siapkan daftar path atau URL gambar
gambar_list = [
    "path/1.jpg",
    "path/2.jpg",
    "path/3.jpg",
    "path/4.jpg",
    "path/5.jpg",
    "path/6.jpg"
]
# Menampilkan gambar dalam 3 baris dan 2 kolom
for i in range(0, len(gambar_list), 2):
    cols = st.columns(2)  # Buat dua kolom untuk setiap baris
    
    # Tampilkan gambar di kolom pertama dan kedua
    with cols[0]:
        st.image(gambar_list[i], use_column_width=True)
    with cols[1]:
        if i + 1 < len(gambar_list):  # Pastikan indeks tidak melebihi jumlah gambar
            st.image(gambar_list[i + 1], use_column_width=True)
