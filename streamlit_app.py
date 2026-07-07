import streamlit as st

st.set_page_config(page_title="نظام m z f r", layout="wide")

st.title("🏗️ نظام إدارة ورشة m z f r")

# هنا يمكنك إضافة أو حذف أي قسم بسهولة
menu = ["الرئيسية", "النجارة", "التنجيد والصباغة", "المخزن", "الحسابات"]
choice = st.sidebar.selectbox("📂 اختر القسم:", menu)

if choice == "الرئيسية":
    st.subheader("مرحباً بك في لوحة تحكم الورشة")
    st.write("نظام بسيط لإدارة سير العمل.")

else:
    st.header(f"قسم {choice}")
    # مساحة لكتابة ملاحظات يدوية (بدل الجداول المعقدة)
    st.text_area(f"سجل ملاحظات وأعمال {choice} هنا:", height=200)
    if st.button("حفظ الملاحظات"):
        st.success("تم حفظ الملاحظات بنجاح في النظام!")

st.sidebar.markdown("---")
st.sidebar.write("نظام الورشة - نسخة سهلة")
