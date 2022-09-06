# Flask-API-Project

Python のフレームワークである Flask を利用した、API の Practice

## 使用言語とバージョン

![](https://img.shields.io/badge/python-v3.7.3-blue?style=plastic)
![](https://img.shields.io/badge/flask-v2.2.2-blue?style=plastic)

## API

| エンドポイント | method | コマンド例                                                                                 |
| -------------- | ------ | ------------------------------------------------------------------------------------------ |
| /              | GET    | `curl localhost:5000`                                                                      |
| /time          | GET    | `curl localhost:5000/time`                                                                 |
| /date          | GET    | `curl -X POST -d 'days=2022-10-03' http://localhost:5000/date`                             |
| aphorism       | GET    | `curl localhost:5000/aphorism`                                                             |
| /fortune       | GET    | `curl localhost:5000/fortune`                                                              |
| /message       | POST   | `curl -X POST -d 'name=kazu' http://localhost:5000/message`                                |
| /login         | POST   | `curl -X POST -d '{"username": "hoge", "password": "123456"}' http://localhost:5000/login` |

## サーバーの立ち上げ

`flask run` 　コマンドにてサーバー立ち上げ

`export FLASK_DEBUG=1` コマンドを立ち上げ前に行うことで、デバッグモードでサーバーを立ち上げることが可能。
