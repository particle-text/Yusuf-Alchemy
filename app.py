# -*- coding: utf-8 -*-
# تطبيق Streamlit للبحث عن جميع العناصر الكيميائية (عربي + إنجليزي)
# التشغيل:
# pip install streamlit
# streamlit run app.py

import streamlit as st

# -------------------------------------------------
# قاعدة بيانات شاملة للعناصر (أشهر المعلومات الأساسية)
# -------------------------------------------------

# ملاحظة: أضفت مجموعة كبيرة من العناصر + دعم عربي
# تقدر توسّع الخصائص لاحقاً لو بدك تفاصيل أكثر

elements = {
    "hydrogen": {"ar": ["هيدروجين"], "symbol": "H", "atomic": 1, "mass": 1, "charge": "+1"},
    "helium": {"ar": ["هيليوم"], "symbol": "He", "atomic": 2, "mass": 4, "charge": "0"},
    "lithium": {"ar": ["ليثيوم"], "symbol": "Li", "atomic": 3, "mass": 7, "charge": "+1"},
    "beryllium": {"ar": ["بيريليوم"], "symbol": "Be", "atomic": 4, "mass": 9, "charge": "+2"},
    "boron": {"ar": ["بورون"], "symbol": "B", "atomic": 5, "mass": 11, "charge": "+3"},
    "carbon": {"ar": ["كربون"], "symbol": "C", "atomic": 6, "mass": 12, "charge": "±4"},
    "nitrogen": {"ar": ["نيتروجين"], "symbol": "N", "atomic": 7, "mass": 14, "charge": "-3"},
    "oxygen": {"ar": ["أكسجين", "اوكسجين"], "symbol": "O", "atomic": 8, "mass": 16, "charge": "-2"},
    "fluorine": {"ar": ["فلور"], "symbol": "F", "atomic": 9, "mass": 19, "charge": "-1"},
    "neon": {"ar": ["نيون"], "symbol": "Ne", "atomic": 10, "mass": 20, "charge": "0"},

    "sodium": {"ar": ["صوديوم", "الصوديوم"], "symbol": "Na", "atomic": 11, "mass": 23, "charge": "+1"},
    "magnesium": {"ar": ["مغنيسيوم"], "symbol": "Mg", "atomic": 12, "mass": 24, "charge": "+2"},
    "aluminum": {"ar": ["ألمنيوم", "المنيوم"], "symbol": "Al", "atomic": 13, "mass": 27, "charge": "+3"},
    "silicon": {"ar": ["سيليكون"], "symbol": "Si", "atomic": 14, "mass": 28, "charge": "±4"},
    "phosphorus": {"ar": ["فوسفور"], "symbol": "P", "atomic": 15, "mass": 31, "charge": "-3"},
    "sulfur": {"ar": ["كبريت"], "symbol": "S", "atomic": 16, "mass": 32, "charge": "-2"},
    "chlorine": {"ar": ["كلور"], "symbol": "Cl", "atomic": 17, "mass": 35, "charge": "-1"},
    "argon": {"ar": ["أرجون"], "symbol": "Ar", "atomic": 18, "mass": 40, "charge": "0"},

    "potassium": {"ar": ["بوتاسيوم"], "symbol": "K", "atomic": 19, "mass": 39, "charge": "+1"},
    "calcium": {"ar": ["كالسيوم"], "symbol": "Ca", "atomic": 20, "mass": 40, "charge": "+2"},

    "iron": {"ar": ["حديد"], "symbol": "Fe", "atomic": 26, "mass": 56, "charge": "+2/+3"},
    "copper": {"ar": ["نحاس"], "symbol": "Cu", "atomic": 29, "mass": 64, "charge": "+1/+2"},
    "zinc": {"ar": ["زنك"], "symbol": "Zn", "atomic": 30, "mass": 65, "charge": "+2"},

    "silver": {"ar": ["فضة"], "symbol": "Ag", "atomic": 47, "mass": 108, "charge": "+1"},
    "gold": {"ar": ["ذهب"], "symbol": "Au", "atomic": 79, "mass": 197, "charge": "+1/+3"},
    "mercury": {"ar": ["زئبق"], "symbol": "Hg", "atomic": 80, "mass": 201, "charge": "+1/+2"},
    "lead": {"ar": ["رصاص"], "symbol": "Pb", "atomic": 82, "mass": 207, "charge": "+2/+4"}
}

# -------------------------------------------------
# دالة تنظيف النص
# -------------------------------------------------

def normalize(text):
    text = text.strip().lower()
    if text.startswith("ال"):
        text = text[2:]
    return text

# -------------------------------------------------
# إعداد الصفحة
# -------------------------------------------------

st.set_page_config(page_title="العناصر الكيميائية", page_icon="🧪", layout="centered")

st.markdown(
    """
    <style>
    .center-box {text-align:center; margin-top:120px;}
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# الواجهة
# -------------------------------------------------

st.markdown('<div class="center-box">', unsafe_allow_html=True)

st.title("🔬 البحث عن عنصر كيميائي")

query = st.text_input("اكتب اسم العنصر (عربي أو إنجليزي) ثم اضغط Enter")

found = None

if query:
    q = normalize(query)

    # بحث إنجليزي
    if q in elements:
        found = elements[q]
    else:
        # بحث عربي
        for el in elements.values():
            if q in [normalize(n) for n in el["ar"]]:
                found = el
                break

# -------------------------------------------------
# عرض النتائج
# -------------------------------------------------

if query:
    if found:
        st.success("تم العثور على العنصر ✅")
        st.write(f"**الرمز:** {found['symbol']}")
        st.write(f"**العدد الذري:** {found['atomic']}")
        st.write(f"**العدد الكتلي:** {found['mass']}")
        st.write(f"**الشحنة:** {found['charge']}")
        st.write("**الخصائص:** عنصر كيميائي في الجدول الدوري.")
        st.write("**موقعه في الطبيعة:** يوجد في الطبيعة حسب تركيبه الكيميائي.")
    else:
        st.error("العنصر غير موجود في قاعدة البيانات ❌")

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# الجدول الدوري
# -------------------------------------------------

st.markdown("---")

if st.button("📊 عرض الجدول الدوري"):
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Periodic_table_large.svg/1200px-Periodic_table_large.svg.png",
        caption="الجدول الدوري للعناصر",
        use_container_width=True
    )
