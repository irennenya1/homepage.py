import streamlit as st 
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import subprocess
from streamlit_option_menu import option_menu
from flask import Flask, render_template

#---bagian title---
st.set_page_config(
    page_title="Bruule.it",
    page_icon="🫶🏻", 
    layout="wide"                                                                      
)
st.title("kontak")
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

#---import style.css---

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

#---- Bagian Kontak ----
with st.container():
    st.write("------")
    st.header("Formulir Umpan Balik Pelanggan")
    st.write("##")

    # Formulir kontak untuk umpan balik pelanggan
    contact_form = """
    <form action="https://formsubmit.co/ryandika.official@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nama Anda" required>
        <input type="email" name="email" placeholder="Email Anda" required>
        <textarea name="message" placeholder="Pesan Anda di sini" required></textarea>
        <button type="submit">Kirim</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

with st.container():
    st.write("----")
    st.subheader("Kami siap melayani pesanan Anda!")
    st.write("WhatsApp, Grabfood, ShopeeFood👇")
    st.write("Link WhatsApp")
    st.write("[Link WhatsApp untuk Pesan 👈](https://wa.link/rx574l)")
    st.write("Link GrabFood")
    st.write("[Link GrabFood untuk presan 🛵](https://food.grab.com/id/id/restaurant/brulee-it-adiarsa-timur-delivery/6-C6TBRUJAUA6YNX?sourceID=20240808_233808_4a3bec2307dce745_MEXMPS)")
    st.write("Link ShopeeFood")
    st.write("[Link ShopeeFood untuk pesan 📳](https://shopee.co.id/universal-link/now-food/shop/21742059?deep_and_deferred=1&shareChannel=copy_link)")
    st.write("Link Instagram")
    st.write("[Kunjungi Instagram Kami 👇](https://www.instagram.com/brulee.it?igsh=MW1iano3Nm9qcWEzZw==)")