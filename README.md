# 概要
- postで受け取ったwavファイルを再生するサービス

# 起動方法
1. python3.11.4環境を構築する
2. このプロジェクトをcloneする
3. `pip install -r requirements.txt`
4. 必要に応じて`main.py`を書き換える
    1. `10 : config['CHUNK'] = 1024` wavから1回に読み込むチャンク数
    2. `11 : config['OUTPUT_DEVICE'] = NONE` 再生するデバイスの番号
    3. `38 : port=8889` サービスがリクエストを受けるポート番号
5. `python main.py`

# 送り方
- curlの場合 : `curl -X POST -F file=@Desktop/sample.wav http://localhost:8889/play`