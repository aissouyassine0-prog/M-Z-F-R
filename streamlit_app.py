import streamlit as st

st.set_page_config(page_title="نظام لامار صوفا", layout="wide")
st.title("🏗️ نظام إدارة ورشة لامار صوفا")

menu = ["الرئيسية", "النجارة", "التنجيد والصباغة"]
choice = st.sidebar.selectbox("اختر القسم:", menu)

if choice == "الرئيسية":
    st.write("مرحباً بك في نظام الإدارة الخاص بورشة لامار صوفا.")
    st.success("تم تشغيل النظام بنجاح عبر السحابة!")
elif choice == "النجارة":
    st.header("🪚 ورشة النجارة")
    st.button("📦 مخزن الخشب")
    st.button("🪚 قسم التقطيع")
elif choice == "التنجيد والصباغة":
    st.header("🎨 ورشة التنجيد والصباغة")
    st.button("🧶 قسم التنجيد")
    st.button("🖌️ قسم الصباغة")
