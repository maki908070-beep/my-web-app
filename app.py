from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = request.form.get('user_name') if request.method == 'POST' else ""
    return f"""
    <html>
        <head>
            <style>
                @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
                .card {{ animation: fadeIn 1.5s ease-out; background: white; padding: 40px; border-radius: 25px; display: inline-block; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 500px; }}
            </style>
        </head>
        <body style="background: linear-gradient(135deg, #f5f7fa, #c3cfe2); font-family: 'Segoe UI', sans-serif; text-align: center; padding: 40px;">
            <div class="card">
                <h1 style="color: #2c3e50; font-size: 22px;">أهلاً بك {name if name else 'زائرنا الكريم'}</h1>
                <form method="POST" style="margin-bottom: 20px;">
                    <input type="text" name="user_name" placeholder="اكتب اسمك هنا..." style="padding: 10px; border-radius: 8px; border: 1px solid #ddd;">
                    <button type="submit" style="padding: 10px 20px; background: #5d6d7e; color: white; border: none; border-radius: 8px;">تحديث</button>
                </form>
                <div style="color: #444; line-height: 1.8;">
                    <h2 style="color: #d63384;">﴿يُحِبُّهُمْ وَيُحِبُّونَهُ﴾</h2>
                    <p>هي علاقة اصطفاء قبل أن تڪون اختيارًا، وقربٌ من الله يبدأ منه، ثم يعود إليه🤍🌸</p>
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

