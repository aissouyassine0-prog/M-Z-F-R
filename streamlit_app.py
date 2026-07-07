import streamlit as st

st.set_page_config(page_title="نظام m z f r", layout="wide")
st.title("🏗️ نظام إدارة ورشة m z f r المتكامل")

menu = ["الرئيسية", "العمال", "المنتجات", "المواد الأولية", "المخزن"]
choice = st.sidebar.selectbox("📂 القائمة الرئيسية", menu)

if choice == "الرئيسية":
    st.subheader("لوحة التحكم العامة")
    col1, col2, col3 = st.columns(3)
    col1.metric("عدد العمال", "12")
    col2.metric("المنتجات الجاهزة", "45")
    col3.metric("المواد بالمخزن", "80%")

elif choice == "المواد الأولية":
    st.header("🪵 تتبع المواد الأولية")
    material = st.text_input("اسم المادة", "خشب")
    qty = st.number_input("الكمية الحالية", min_value=0, value=15)
    
    if st.button("حفظ الكمية"):
        st.success(f"تم حفظ {material} بنجاح.")
        # هنا الذكاء: النظام يتحقق من الكمية بعد إدخالها
        if qty < 10:
            st.error(f"⚠️ تنبيه: كمية {material} منخفضة جداً! يجب طلب المزيد.")
        else:
            st.success(f"✅ كمية {material} كافية للعمل.")

elif choice == "العمال":
    st.header("👥 إدارة العمال")
    st.write("استخدم هذا القسم لتسجيل المهام.")
    
elif choice == "المنتجات":
    st.header("🪑 تتبع المنتجات")
    st.write("سجل حالة المنتجات هنا.")

elif choice == "المخزن":
    st.header("📦 إدارة المخزن")
    st.table({"المادة": ["خشب بلوط", "قماش تنجيد"], "الكمية": [50, 100]})
