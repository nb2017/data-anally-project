# data-anally-project
データ解析する為のコンテナを開発する目的のリポジトリ

# data_anally_container
## コンテナのインストール
下記コマンドを実行してdocker内にコンテナをインストールし、コンテナを起動する。
~~~
$ cd data_anally_container
$ docker compose up -d
~~~
下記コマンドを実行してdocker内にコンテナがインストールされたことを確認する。
~~~
$ docker ps
~~~
## パッケージのインストール
下記コマンドを実行してコンテナ内のターミナルに接続する。
~~~
$ docker compose exec data_anally_container bash
~~~
ターミナルに入ったら下記コマンドを実行してパッケージをインストールする。
~~~
$ cd dependencies
$ pip install -r requirements.txt
~~~
## スクリプトの起動
~~~
$ cd ../
$ python index.py [解析したい画像の相対パス]
~~~
