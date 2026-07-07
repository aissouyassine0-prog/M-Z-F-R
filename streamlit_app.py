import streamlit as st

st.set_page_config(page_title="نظام إدارة m z f r", layout="wide")

st.title("🏗️ نظام إدارة ورشة m z f r المتكامل")

# القائمة الجانبية
menu = ["الرئيسية", "العمال", "المنتجات", "المواد الأولية", "المخزن"]
choice = st.sidebar.selectbox("📂 القائمة الرئيسية", menu)

# قسم الرئيسية
if choice == "الرئيسية":
    st.subheader("لوحة التحكم العامة")
    col1, col2, col3 = st.columns(3)
    col1.metric("عدد العمال", "12")
    col2.metric("المنتجات الجاهزة", "45")
    col3.metric("المواد بالمخزن", "80%")

# قسم العمال
elif choice == "العمال":
    st.header("👥 إدارة العمال")
    name = st.text_input("اسم العامل")
    task = st.text_input("العمل الموكل إليه")
    if st.button("إضافة عامل"):
        st.success(f"تم تسجيل {name} للقيام بـ {task}")

# قسم المنتجات
elif choice == "المنتجات":
    st.header("🪑 تتبع المنتجات")
    product = st.text_input("اسم المنتج")
    status = st.selectbox("حالة الإنتاج", ["قيد التنفيذ", "جاهز", "تم التسليم"])
    if st.button("تحديث حالة المنتج"):
        st.info(f"تم تحديث {product} إلى حالة: {status}")

# قسم المواد الأولية
elif choice == "المواد الأولية":
    st.header("🪵 تتبع المواد الأولية")
    material = st.text_input("اسم المادة")
    qty = st.number_input("الكمية الحالية", min_value=0)
    if st.button("حفظ كمية المادة"):
        st.success(f"تم تحديث {material} لتصبح {qty}")

# قسم المخازن
elif choice == "المخزن":
    st.header("📦 إدارة المخزن")# كود الذكاء البسيط للمخزون
if qty < 10:
    st.error(f"⚠️ تنبيه: كمية {material} منخفضة جداً! يجب طلب المزيد.")
else:
    st.success(f"✅ كمية {material} كافية.")
    st.write("جدول جرد المخزن الحالي:")
    st.table({"المادة": ["خشب بلوط", "قماش تنجيد"], "الكمية": [50, 100]})
