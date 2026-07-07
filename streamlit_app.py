import streamlit as st
import pandas as pd

# سنقوم هنا بقراءة بيانات الجدول مباشرة
# ملاحظة: يجب أن يكون رابط الجدول "عاماً" (Public) ليتمكن التطبيق من قراءته
sheet_url = "ضع_رابط_جدول_البيانات_هنا" 
csv_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

elif choice == "المواد الأولية":
    st.header("🪵 جرد المواد الأولية من الجدول")
    try:
        # تحميل البيانات من الجدول وعرضها
        df = pd.read_csv(csv_url)
        st.table(df)
        
        st.write("---")
        st.info("💡 ملاحظة: قم بتحديث الجدول وسيقوم النظام بتحديث البيانات فوراً.")
    except:
        st.error("خطأ: تأكد أن رابط الجدول متاح للعامة (Public)."
