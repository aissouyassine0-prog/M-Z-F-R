
import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="m z f r - نظام الإدارة", page_icon="🏗️", layout="wide")

# تنسيق العنوان باستخدام CSS مخصص
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #2E86C1;
        font-family: sans-serif;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🏗️ نظام إدارة ورشة m z f r</h1>", unsafe_allow_html=True)
st.divider()

# القائمة الجانبية
menu = ["الرئيسية", "النجارة", "التنجيد والصباغة"]
choice = st.sidebar.selectbox("📂 القائمة الرئيسية", menu)

# محتوى الأقسام
if choice == "الرئيسية":
    st.subheader("مرحباً بك في لوحة تحكم الورشة")
    st.write("هذا النظام مخصص لتنظيم ومتابعة سير العمل في ورشة **m z f r**.")
    st.info("💡 اختر قسماً من القائمة الجانبية للبدء.")
    
elif choice == "النجارة":
    st.header("🪚 قسم النجارة")
    col1, col2 = st.columns(2)
    with col1:
        st.button("📦 مخزن الخشب")
        st.button("📏 قسم التقطيع")
    with col2:
        st.button("📝 أوامر العمل الجديدة")
        st.button("📊 تقارير الإنتاج")

elif choice == "التنجيد والصباغة":
    st.header("🪑 قسم التنجيد والصباغة")
    col1, col2 = st.columns(2)
    with col1:
        st.button("🪡 قسم التنجيد")
        st.button("🎨 قسم الصباغة")
    with col2:
        st.button("📦 جرد المواد")
        st.button("✅ مراقبة الجودة")

# تذييل الصفحة
st.sidebar.markdown("---")
st.sidebar.success("✅ النظام يعمل بنجاح")
