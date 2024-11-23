import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import subprocess
from streamlit_option_menu import option_menu
from flask import Flask, render_template 

st.set_page_config(
    page_title="Bruule.it",
    page_icon="🫶🏻", 
    layout="wide"                                                                      
)

st.title("Standart Operational Prosedur")
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


st.sidebar.success("dapatkkan lebih banyak informasi. ")

#---- Memuat aset ----
Image_contact_form = Image.open("image/1.png")
Image_lottie_animation = Image.open("image/2.png")
Image_3 = Image.open("image/3.png")
Image_4 = Image.open("image/4.png")
Image_5 = Image.open("image/5.png")
Image_6 = Image.open("image/6.png")
Image_7 = Image.open("image/7.png")
Image_8 = Image.open("image/8.png")
Image_9 = Image.open("image/9.png")
Image_10 = Image.open("image/10.png")

with st.container():
    st.write("----")
    st.header("Keselamatan dan Kesehatan Kerja")
    st.write("K3")
    image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(Image_9)
    st.write("1. Keselamatan Tempat Kerja")
    st.write("Menjaga tempat kerja yang aman dan bebas dari potensi bahaya.")
    st.write("2. Pelatihan K3")
    st.write("Memberikan pelatihan dasar kepada karyawan tentang prosedur keselamatan kerja,")
    st.write(" misalnya bagaimana menangani situasi darurat atau menggunakan alat pemadam kebakaran.")
    st.write("3. Alat Pelindung Diri (APD)")
    st.write("Menyediakan dan mewajibkan penggunaan APD yang sesuai, seperti sarung tangan & masker.")
    st.write("4. Managemen Limbah")
    st.write("UMKM bergerak di bidang produksi atau makanan, manajemen limbah yang baik akan sangat penting")
    st.write("untuk mencegah polusi dan menjaga kebersihan lingkungan kerja.")
    st.write("5. Perencanaan Darurat")
    st.write("Mempersiapkan prosedur evakuasi dan tindakan darurat untuk menghadapi kebakaran atau bencana alam lainnya.")
    st.write("6. Kebersihan Dan Kesehatan kerja")
    st.write("Menjaga kebersihan tempat kerja, memastikan ventilasi dan penerangan yang baik,")
    st.write("serta menyediakan fasilitas kebersihan seperti wastafel, sabun, dan sanitizer.")
    st.write("7. Pencegahan Kecelakaan Kerja")
    st.write("Memastikan penggunaan mesin atau alat sesuai prosedur, serta")
    st.write(" mengecek alat-alat secara rutin agar terhindar dari risiko kecelakaan.")

#----Bagian Sop----
with st.container():
    st.markdown("<h1 class='centered-header'>Standard Operasional Prosedur</h1>", unsafe_allow_html=True)
    st.write("SOP")
    image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(Image_10)
    st.write("1. Cuci tangan dengan sabun dan air mengalir setidaknya selama 20 detik sebelum menangani makanan")
    st.write("2. Lakukan pembersihan menyeluruh pada dapur dan peralatan setelah tutup operasional,")
    st.write("3. termasuk membersihkan kompor, oven, dan alat masak lainnya.")
