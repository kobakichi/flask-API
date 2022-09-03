# Flask を利用して API を作成する。

## 作成した機能

- アクセス毎に、偉人の名言が返ってくる /ahorism, method=GET 　コマンド例　 curl http://localhost:5000/aphorism
- 日付を送ると曜日が帰ってくる /date, method=POST コマンド例　 curl -X POST -d 'days=2022-10-03' http://localhost:5000/date
- アクセス毎に、今日の運勢が返ってくる。凶以下は無し。吉まで。ポジティブおみくじ /fortune, method=GET 　コマンド例　 curl http://localhost:5000/fortune
- 労いの言葉をかけてくれる /message, method=POST コマンド例　 curl -X POST -d 'name=kazu' http://localhost:5000/message
- アクセスすると、現在時刻を知らせてくれる /time, method=GET 　コマンド例　 curl http://localhost:5000/time
- ログイン機能のデモとしての API /login, method=POST 　コマンド例　 curl -X POST -d '{"username": "hoge", "password": "123456"}' http://localhost:5000/login

## サーバーの立ち上げ

flask run 　コマンドにてサーバー立ち上げ

export FLASK_DEBUG=1 コマンドを立ち上げ前に行うことで、デバッグモードでサーバーを立ち上げることが可能。
