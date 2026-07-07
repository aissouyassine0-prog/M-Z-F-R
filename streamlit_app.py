import streamlit as st
import pandas as pd

st.set_page_config(page_title="نظام m z f r", layout="wide")
st.title("🏗️ نظام إدارة ورشة m z f r")

# جدول بيانات تجريبي مدمج داخل الكود لضمان عمل النظام فوراً
data = {
    "القسم": ["النجارة", "التنجيد", "الصباغة"],
    "العمال_الموجودون": [5, 3, 2],
    "حالة_العمل": ["مكتمل", "قيد التنفيذ", "متوقف"]
}
df = pd.DataFrame(data)

menu = ["الرئيسية", "عرض البيانات"]
choice = st.sidebar.selectbox("📂 اختر القسم:", menu)

if choice == "الرئيسية":
    st.subheader("مرحباً بك في لوحة تحكم الورشة")
    st.write("النظام يعمل الآن بنجاح! يمكنك التنقل بين الأقسام من القائمة الجانبية.")
else:
    st.header("📊 عرض البيانات الحالية")
    st.dataframe(df, use_container_width=True)
    st.success("هذه البيانات قادمة من النظام مباشرة.")
