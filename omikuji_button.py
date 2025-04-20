from flask import Flask, render_template_string, redirect, url_for
import random

app = Flask(__name__)

results = [
    "🌟 大吉！最高の一日になるでしょう！",
    "😊 中吉！なかなかいい感じ！",
    "😌 小吉。穏やかに過ごせそう。",
    "😅 末吉。ちょっと注意して行動しよう！",
    "😐 凶…。でも前向きにいこう！",
    "🔥 大凶！？でも逆にレアかも！"
]

@app.route("/")
def index():
    return render_template_string("""
        <h1>🎱 おみくじ引いてみよう！</h1>
        <form action="/result">
            <button type="submit" style="font-size:20px">おみくじを引く</button>
        </form>
    """)

@app.route("/result")
def result():
    fortune = random.choice(results)
    return render_template_string(f"""
        <h1>🔮 結果発表！</h1>
        <p style='font-size:24px'>{fortune}</p>
        <a href="/" style="font-size:16px">もう一回引く</a>
    """)

if __name__ == "__main__":
    app.run(debug=True)
