# 正解データ取得用GUI

このプロジェクトは、画像に対してアノテーションを行い、正解データ（correct_position_data.csv）を取得するためのGUIツールです。

## 手順

1. 画像の配置
   - このプロジェクトのルートディレクトリ内にある "static/img/" フォルダに、アノテーション対象の画像フォルダを "(〇〇)_(番号).jpg" の形式で配置してください。

2. ツールの実行
   - コンソールで以下のコマンドを実行して、GUIツールを起動します。
     ```shell
     python main.py
     ```

3. ブラウザでアクセス
   - ブラウザを開き、`localhost:5000` にアクセスしてください。

4. アノテーションの実行
   - ブラウザ上で、以下の手順でアノテーションを行います。
     1. 1で配置した画像フォルダ名とアノテーションする部位名（例：NOSE）を入力します。
     2. 画像の特定の部位をクリックします。

5. 座標データ
   - 画像をクリックするたびに"static/data/correct_position_data.csv" ファイルに自動的に書き込まれます。

