# -*- coding: utf-8 -*-
found = None


if query:
q = normalize(query)


for el in elements.values():
names = [
normalize(el["name_en"]),
normalize(el["name_ar"]),
normalize(el["symbol"])
]
if q in names:
found = el
break


# -------------------------
# عرض النتائج
# -------------------------


if query:
if found:
st.success("تم العثور على العنصر ✅")


st.write(f"**الاسم:** {found['name_ar']} / {found['name_en']}")
st.write(f"**الرمز:** {found['symbol']}")
st.write(f"**العدد الذري:** {found['atomic_number']}")
st.write(f"**العدد الكتلي:** {found['atomic_mass']}")
st.write(f"**الشحنة الشائعة:** {found['charge']}")
st.write(f"**التصنيف:** {found['category']}")
st.write(f"**المجموعة:** {found['group']}")
st.write(f"**الدورة:** {found['period']}")
st.write(f"**الخصائص:** {found['properties']}")
st.write(f"**موقعه في الطبيعة:** {found['nature']}")


else:
st.error("العنصر غير موجود ❌")


st.markdown('</div>', unsafe_allow_html=True)


# -------------------------
# زر الجدول الدوري
# -------------------------


st.markdown("---")


if st.button("📊 عرض الجدول الدوري التفاعلي"):
st.image(
"https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large.svg",
use_container_width=True
)
