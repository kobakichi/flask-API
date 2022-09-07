# Flask-API-Project

Python のフレームワークである Flask を利用した、API の Practice  
今回使用しているのは、Flask のみです。

## 使用言語とバージョン

![](https://img.shields.io/badge/python-v3.7.3-blue?style=plastic)
![](https://img.shields.io/badge/flask-v2.2.2-blue?style=plastic)

## API

| エンドポイント | method | コマンド例                                                                                 |                             |
| -------------- | ------ | ------------------------------------------------------------------------------------------ | --------------------------- |
| /              | GET    | `curl localhost:5000`                                                                      | RareTECH のメッセージを返す |
| /time          | GET    | `curl localhost:5000/time`                                                                 | 現在時刻を返す              |
| /date          | GET    | `curl -X POST -d 'days=2022-10-03' http://localhost:5000/date`                             | 入力した日付から曜日を算出  |
| /aphorism      | GET    | `curl localhost:5000/aphorism`                                                             | 偉人の名言を返す            |
| /fortune       | GET    | `curl localhost:5000/fortune`                                                              | ポジティブおみくじ          |
| /message       | POST   | `curl -X POST -d 'name=kazu' http://localhost:5000/message`                                | 労いの言葉を返す            |
| /login         | POST   | `curl -X POST -d '{"username": "hoge", "password": "123456"}' http://localhost:5000/login` | ログイン機能のサンプル      |

## 環境構築

### 1. virtualenv にて仮想環境構築(mac の場合)

Python での仮想環境を構築するため、virtualenv をインストール。

`pip3 install virtualenv`

もし  
`` Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/Library/Python/3.7'Consider using the `--user` option or check the permissions. ``  
というエラーが発生した場合、パーミッションがないと言われているので、`sudo`をつけて再度コマンドを実行する。

`sudo pip3 install virtualenv`

### 2. virtualenv 立ち上げ

プロジェクトを作成したいディレクトリへ移動して、下記コマンドを実行。  
`virtualenv env`  
これで、移動したディレクトリに virtualenv の設定ファイルが作成される。  
設定ファイルが作成されているのを確認したら、  
`source env/bin/activate`  
コマンドで virtualenv を有効化する。  
成功すると、  
`(env)user@hoge|ディレクトリ`  
と、プロンプトの前に()で`virtualenv`コマンドを実行した時の名前が表示される。

### 3. Flask のインストール

仮想環境が有効化されている状態で、  
`pip3 install flask`  
を実行すると、仮想環境内でだけ flask がインストールされる。

### 4. app.py の作成

flask をインストールした、現在のディレクトリにファイル`app.py`を作成する。  
`touch app.py`  
作成した`app.py`ファイルに以下の内容を記述する。

```python
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)
```

## サーバーの立ち上げ

`app.py`ファイルのあるディレクトリで  
`flask run`  
コマンドを実行することで、サーバーを立ち上げることができる。  
`localhost:5000`にブラウザでアクセスして、`Hello World`が表示されればサーバーの立ち上げに成功。

サーバーを立ち上げる前に、`export FLASK_DEBUG=1` コマンドを実行すると、デバッグモードでサーバーを立ち上げることが可能。
