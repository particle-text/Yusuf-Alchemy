# -*- coding: utf-8 -*-
# تطبيق ويب بسيط لعرض معلومات العناصر الكيميائية
# لتشغيله:
# 1) ثبّت فلاسـك: pip install flask
# 2) شغّل الملف: python app.py
# 3) افتح المتصفح: http://127.0.0.1:5000

from flask import Flask, render_template_string, request

app = Flask(__name__)

# قاعدة بيانات مبسطة للعناصر (يمكنك التوسعة لاحقاً)
elements = {
    "Hydrogen": {
        "symbol": "H",
        "atomic_number": 1,
        "mass_number": 1,
        "charge": "+1",
        "properties": "غاز عديم اللون، خفيف جداً، قابل للاشتعال.",
        "nature": "يوجد في الماء والنجوم."
    },
    "Oxygen": {
        "symbol": "O",
        "atomic_number": 8,
        "mass_number": 16,
        "charge": "-2",
        "properties": "غاز ضروري للتنفس ويدعم الاحتراق.",
        "nature": "يوجد في الهواء والماء."
    },
    "Carbon": {
        "symbol": "C",
        "atomic_number": 6,
        "mass_number": 12,
        "charge": "±4",
        "properties": "عنصر أساسي في المركبات العضوية.",
        "nature": "يوجد في الكائنات الحية والفحم."
    },
    "Sodium": {
        "symbol": "Na",
        "atomic_number": 11,
        "mass_number": 23,
        "charge": "+1",
        "properties": "فلز قلوي شديد التفاعل.",
        "nature": "يوجد في ملح الطعام."
    }
}

# صفحة HTML
page = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>البحث عن العناصر الكيميائية</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(135deg, #74ebd5, #ACB6E5);
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        .search-box {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 0 20px rgba(0,0,0,0.2);
            text-align: center;
            width: 400px;
        }

        input {
            width: 90%;
            padding: 12px;
            font-size: 18px;
            border-radius: 10px;
            border: 1px solid #ccc;
        }

        .result {
            margin-top: 20px;
            text-align: right;
        }

        .periodic-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            padding: 15px 20px;
            font-size: 16px;
            border: none;
            border-radius: 50px;
            background: #ff9800;
            color: white;
            cursor: pointer;
        }

        img {
            margin-top: 20px;
            max-width: 90%;
            display: none;
        }
    </style>
</head>
<body>

    <div class="search-box">
        <h2>ابحث عن عنصر كيميائي</h2>

        <form method="POST">
            <input type="text" name="element" placeholder="اكتب اسم العنصر بالإنجليزي" required>
        </form>

        {% if data %}
        <div class="result">
            <p><b>الرمز:</b> {{data.symbol}}</p>
            <p><b>العدد الذري:</b> {{data.atomic_number}}</p>
            <p><b>العدد الكتلي:</b> {{data.mass_number}}</p>
            <p><b>الشحنة:</b> {{data.charge}}</p>
            <p><b>الخصائص:</b> {{data.properties}}</p>
            <p><b>موقعه في الطبيعة:</b> {{data.nature}}</p>
        </div>
        {% elif searched %}
            <p>العنصر غير موجود في قاعدة البيانات</p>
        {% endif %}
    </div>

    <button class="periodic-btn" onclick="showTable()">عرض الجدول الدوري</button>

    <img id="ptable" src="https://upload.wikimedia.org/wikipedia/commons/0/01/Periodic_table_large.svg">

    <script>
        function showTable(){
            var img = document.getElementById('ptable');
            img.style.display = 'block';
        }
    </script>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    data = None
    searched = False

    if request.method == 'POST':
        element_name = request.form['element']
        searched = True
        data = elements.get(element_name)

    return render_template_string(page, data=data, searched=searched)


if __name__ == '__main__':
    app.run(debug=True)
