from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import subprocess
from streamlit_option_menu import option_menu
from flask import Flask, render_template

#---- Set up page config ----
st.set_page_config(
    page_title="Bruule.it",
    page_icon="🫶🏻", 
    layout="wide"                                                                      
)
st.title("Menu")
st.sidebar.success("Made by kelompok . ")

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

result = subprocess.run(['node', 'path/indeks.js'], capture_output=True, text=True)
print(result.stdout) 


# Fungsi untuk memuat animasi Lottie dari URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Menggunakan CSS lokal untuk gaya khusus
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#---- Memuat aset ----
lottie_coding = load_lottieurl("https://lottie.host/355fa541-b609-43dc-ac4e-31fc080c2104/86nEFIiyws.json")
Image_contact_form = Image.open("images/1.png")
Image_lottie_animation = Image.open("images/2.png")
Image_3 = Image.open("images/3.png")
Image_4 = Image.open("images/4.png")
Image_5 = Image.open("images/5.png")
Image_6 = Image.open("images/6.png")
Image_7 = Image.open("images/7.png")
Image_8 = Image.open("images/8.png")
Image_9 = Image.open("images/9.png")
Image_10 = Image.open("images/10.png")

# CSS khusus untuk tombol dan animasi hover
st.markdown("""
    <style>
        .stButton button {
            background-color: #007bff;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 10px 20px;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: #0056b3;
            transform: scale(1.05);
        }
        .centered-header {
            font-size: 60px;
            text-align: center;
            font-weight: bold;
            color: #007bff;
            margin-top: 20px;
        }
        .product-card {
            border: 1px solid #e0e0e0;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }
        .product-card:hover {
            transform: translateY(-15px);
        }
        .product-header {
            font-size: 24px;
            font-weight: bold;
            color: #f5f5f5;
        }
        .product-description {
            color: white;  /* Mengubah warna font deskripsi produk menjadi putih */
        }
        body {
            background-color: #f5f5f5;
        }
    </style>
""", unsafe_allow_html=True)

#-----Bagian Prise list------
with st.container():
    st.write("------")
    st.header("Menu Brulee.it!")
    st.write("Kami hadir untuk memanjakan para pecinta makanan dengan cita rasa khas Italia yang kaya akan keju dan kelezatan.")
    st.write("Dengan bahan berkualitas dan resep yang dibuat khusus, setiap hidangan Brulee.it")
    st.write("""dirancang untuk memberikan pengalaman kuliner yang tak terlupakan. Dari dimsum hingga pasta,
            setiap gigitan menghadirkan kelezatan yang sempurna dan autentik.
            Yuk, jelajahi pilihan menu kami yang siap menggugah selera Anda!
""")
    st.header("Prise List Dimsum")
    st.write("Dimsum Brulee.it")
    image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(Image_8)
with text_column:
    st.markdown("""
            <div class="product-card">
                <h3 class="product-header">Prise list Dimsum</h3>
                <p class="product-description">Dimsum lembut yang meleleh di mulut dengan isian daging yang juicy,
                 dipadukan dengan saus keju yang creamy dan gurih. Setiap gigitan memberikan perpaduan rasa yang unik
                 antara kelembutan dimsum dan keju yang kaya, cocok untuk camilan atau hidangan pembuka.</p>
                <p class="product-description">Start from 15K </p>
                <a href="https://wa.link/rx574l" target="_blank"><button>DM untuk Pesanan 💌</button></a>
            </div>
        """, unsafe_allow_html=True)
    st.write("-----")

with st.container():
    st.header("Prise List Spaghetti")
    st.write("Spaghetti Brulee.it")
    image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(Image_6)
with text_column:
    st.markdown("""
            <div class="product-card">
                <h3 class="product-header">Prise list Spaghetti</h3>
                <p class="product-description">Spaghetti klasik ala Italia dengan saus brulee keju 
                spesial yang creamy dan penuh rasa. Tekstur spaghetti yang pas berpadu dengan keju yang melimpah,
                menciptakan sensasi yang lezat dan memuaskan. Cocok bagi pecinta pasta dan keju yang mencari 
                pengalaman rasa autentik.</p>
                <p class="product-description">Start from 15K </p>
                <a href="https://wa.link/rx574l" target="_blank"><button>DM untuk Pesanan 💌</button></a>
            </div>
        """, unsafe_allow_html=True)
    st.write("-----")

with st.container():
    st.header("Prise List Maccaroni")
    st.write("Maccaroni Brulee.it")
    image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(Image_7)
with text_column:
    st.markdown("""
            <div class="product-card">
                <h3 class="product-header">Prise list Maccaroni</h3>
                <p class="product-description">Macaroni yang dimasak sempurna,
                diselimuti saus keju kental yang creamy dan menggugah selera.
                Dengan taburan keju ekstra di atasnya, hidangan ini sempurna untuk disantap hangat.
                Setiap porsi macaroni ini membawa kenikmatan rasa Italia ke dalam setiap gigitan.</p>
                <p class="product-description">Start from 15K </p>
                <a href="https://wa.link/rx574l" target="_blank"><button>DM untuk Pesanan 💌</button></a>
            </div>
        """, unsafe_allow_html=True)
    st.write("-----")

#---- Bagian Produk dengan Kartu ----
with st.container():
    st.write("------")
    st.header("Menu Terlaris Kami! 🙋🏻‍♀️🫶🏻")
    
    # Kartu produk pertama
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Image_lottie_animation)
    with text_column:
        st.markdown("""
            <div class="product-card">
                <h3 class="product-header">Dimsum Brulee.it</h3>
                <p class="product-description">Cukup DM kami 🥢</p>
                <p class="product-description">Start from 15K </p>
                <a href="https://wa.link/rx574l" target="_blank"><button>DM untuk Pesanan 💌</button></a>
            </div>
        """, unsafe_allow_html=True)

    # Kartu produk kedua
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Image_contact_form)
    with text_column:
        st.markdown("""
            <div class="product-card">
                <h3 class="product-header">Dimsum Keluarga (16 pcs)</h3>
                <p class="product-description">Hanya 80k (Gratis 2 Minyak Cabai)</p>
                <a href="https://wa.link/rx574l" target="_blank"><button>DM untuk Pesanan 💌</button></a>
            </div>
        """, unsafe_allow_html=True)

    # Kartu produk ketiga
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Image_3)
    with text_column:
        st.markdown("""
            <div class="product-card">
                <h3 class="product-header">Pasta Kecil dan Dimsum Kecil 🥢</h3>
                <p class="product-description">Pesan sekarang dari Brulee.it</p>
                <a href="https://wa.link/rx574l" target="_blank"><button>DM untuk Pesanan 💌</button></a>
            </div>
        """, unsafe_allow_html=True)

    # Kartu produk keempat
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Image_4)
    with text_column:
        st.markdown("""
            <div class="product-card">
                <h3 class="product-header">Dimsum Kecil (3 pcs)</h3>
                <p class="product-description">Hanya 15k (+2k untuk Cabai)</p>
                <p>Sempurna dengan kopi Anda ☕</p>
                <a href="https://wa.link/rx574l" target="_blank"><button>DM untuk Pesanan 💌</button></a>
            </div>
        """, unsafe_allow_html=True)

    #Kartu product kelima
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Image_5)
    with text_column:
        st.markdown("""
            <div class="product-card">
                <h3 class="product-header">Spaghetti Bruule.it</h3>
                <p class="product-description">Cukup DM kami 🥢</p>
                <p class="product-description">Start from 15K </p>
                <a href="https://wa.link/rx574l" target="_blank"><button>DM untuk Pesanan 💌</button></a>
            </div>
        """, unsafe_allow_html=True)
        st.write("----")
        st.write("##")
        