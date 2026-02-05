# -*- coding: utf-8 -*-
# تطبيق Streamlit للبحث عن العناصر الكيميائية (نسخة معدلة)
# للتشغيل:
# pip install streamlit
# streamlit run app.py

import streamlit as st

# -----------------------------
# قاعدة بيانات العناصر (مع دعم العربية)
# -----------------------------

elements = {
    "hydrogen": {
        "names_ar": ["هيدروجين"],
        "symbol": "H",
        "atomic_number": 1,
        "mass_number": 1,
        "charge": "+1",
        "properties": "غاز عديم اللون، خفيف جداً، قابل للاشتعال.",
        "nature": "يوجد في الماء والنجوم."
    },
    "oxygen": {
        "names_ar": ["أكسجين", "اوكسجين"],
        "symbol": "O",
        "atomic_number": 8,
        "mass_number": 16,
        "charge": "-2",
        "properties": "غاز ضروري للتنفس ويدعم الاحتراق.",
        "nature": "يوجد في الهواء والماء."
    },
    "carbon": {
        "names_ar": ["كربون"],
        "symbol": "C",
        "atomic_number": 6,
        "mass_number": 12,
        "charge": "±4",
        "properties": "عنصر أساسي في المركبات العضوية.",
        "nature": "يوجد في الكائنات الحية والفحم."
    },
    "sodium": {
        "names_ar": ["صوديوم", "الصوديوم"],
        "symbol": "Na",
        "atomic_number": 11,
        "mass_number": 23,
        "charge": "+1",
        "properties": "فلز قلوي شديد التفاعل.",
        "nature": "يوجد في ملح الطعام."
    }
}

# -----------------------------
# دالة تنظيف النص (تشيل ال التعريف)
# -----------------------------

def normalize(text):
    text = text.strip().lower()
    if text.startswith("ال"):
        text = text[2:]
    return text

# -----------------------------
# إعداد الصفحة
# -----------------------------

st.set_page_config(
    page_title="العناصر الكيميائية",
    page_icon="🧪",
    layout="centered"
)

# -----------------------------
# تنسيق CSS
# -----------------------------

st.markdown(
    """
    <style>
    .center-box {
        text-align: center;
        margin-top: 120px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# واجهة البحث
# -----------------------------

st.markdown('<div class="center-box">', unsafe_allow_html=True)

st.title("🔬 البحث عن عنصر كيميائي")

query = st.text_input("اكتب اسم العنصر (عربي أو إنجليزي) ثم اضغط Enter")

# -----------------------------
# البحث
# -----------------------------

found = None

if query:
    q = normalize(query)

    # بحث إنجليزي
    if q in elements:
        found = elements[q]
    else:
        # بحث عربي
        for el in elements.values():
            ar_names = [normalize(n) for n in el.get("names_ar", [])]
            if q in ar_names:
                found = el
                break

# -----------------------------
# عرض النتائج
# -----------------------------

if query:
    if found:
        st.success("تم العثور على العنصر ✅")
        st.write(f"**الرمز:** {found['symbol']}")
        st.write(f"**العدد الذري:** {found['atomic_number']}")
        st.write(f"**العدد الكتلي:** {found['mass_number']}")
        st.write(f"**الشحنة:** {found['charge']}")
        st.write(f"**الخصائص:** {found['properties']}")
        st.write(f"**موقعه في الطبيعة:** {found['nature']}")
    else:
        st.error("العنصر غير موجود في قاعدة البيانات ❌")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# زر عرض الجدول الدوري (حل المشكلة)
# -----------------------------

st.markdown("---")

if st.button("📊 عرض الجدول الدوري"):
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Periodic_table_large.svg/1200px-Periodic_table_large.svg.png",
        caption="الجدول الدوري للعناصر",
        use_container_width=True
    )
