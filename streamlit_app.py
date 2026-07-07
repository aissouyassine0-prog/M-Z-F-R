import streamlit as st
import pandas as pd

# ضع رابط جدولك هنا بين علامتي التنصيص
SHEET_URL = "ضع_رابط_جدول_بياناتك_هنا"

# تحويل الرابط لصيغة يفهمها النظام
csv_url = SHEET_URL.replace('/edit#gid=', '/export?format=csv&gid=')

def app():
    st.title("🏗️ نظام إدارة ورشة m z f r")
    
    try:
        # قراءة البيانات
        df = pd.read_csv(csv_url)
        st.subheader("📊 البيانات الحالية من الجدول")
        st.dataframe(df) # هذا يعرض الجدول في تطبيقك
    except:
        st.warning("يرجى التأكد من وضع رابط الجدول الصحيح في الكود.")

app()
