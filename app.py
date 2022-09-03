from crypt import methods
from datetime import datetime
from distutils.log import debug
from flask import Flask, request
import pytz, random

# Flaskのインスタンスをappという名前で作成
app = Flask(__name__)

# localhost:5000にアクセスした時の処理
@app.route('/')
def index():
    return 'Hello World'



# /timeへgetでアクセスしたら現在時刻を知らせる
@app.route('/time')
def current_time():
    dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
    date = dt_now.strftime('%Y年%m月%d日  %H時%M分%S秒')
    return f'現在時刻は{date}です'



# /dateにアクセスすると、入力メッセージが表示される
@app.route('/date', methods=['POST'])
def week_caluculation():
    """コマンド例: curl -X POST -d 'days=2022-10-03' http://localhost:5000/date"""
    
    w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    input_date = request.form.get('days')
    # 受け取った文字を日付に変換する
    date = datetime.strptime(input_date, '%Y-%m-%d')

    # 日付を曜日に変換する
    week = date.weekday()

    return f'{date}は{w_list[week]}です'



# /massageへアクセスすると、労いのメッセージが返ってくる。
@app.route('/message', methods=['POST'])
def gratitude_message():
    """コマンド例: curl -X POST -d 'name=kazu' http://localhost:5000/message"""
    username = request.form.get('name')
    return f'頑張りすぎるのも良くないぞ。{username}は既に頑張っている。ただ、情熱だけは忘れるな！！！'



# /aphorismへアクセルすると、名言をランダムに返す
@app.route('/aphorism')
def aphorism():
    aphorism_words = ['Done is better than perfect.', 'Stay hungry, stay foolish', 'We are What We Choose', 'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.']

    aphorism = random.choice(aphorism_words)
    
    return aphorism



@app.route('/fortune')
def random_fortune():
    fortunes = ['大吉', '中吉', '小吉', '吉']

    fortune = random.choice(fortunes)

    return f'今日の運勢は{fortune}です！頑張りましょう！'


@app.route('/calculation', methods=['POST'])
def json_calc():
    get_numbers = request.get_json(force=True)
    num1 = get_numbers.get('number1', None)
    num2 = get_numbers.get('number2', None)

    return num1 + num2

# python app.pyという名前で実行されたらサーバーが立ち上がる。
if __name__ == "main":
    app.run(debug=True)