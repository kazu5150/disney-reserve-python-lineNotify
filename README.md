# Disney Hotel Availability Checker

このプロジェクトは東京ディズニーリゾートのホテル予約可能性をチェックし、空室がある場合にLINE通知を送信するPythonスクリプトです。

## 機能

- 指定された日付の東京ディズニーリゾートホテルの空室状況をチェック
- 空室がある場合、予約ページのURLを表示
- LINE Notifyを使用して、空室情報をLINEで通知

## 必要条件

- Python 3.6+
- pip

## インストール

1. リポジトリをクローンします：

```bash
git clone https://github.com/yourusername/disney-hotel-checker.git
cd disney-hotel-checker
```

2. 必要なパッケージをインストールします：

```bash
pip install requests python-dotenv
```

3. `.env`ファイルを作成し、LINE Notify トークンを設定します：

```
LINE_NOTIFY_TOKEN=your_line_notify_token_here
```

## 使用方法

1. スクリプト内の`research_month`変数を目的の日付に変更します（形式：YYYYMMDD）。

2. スクリプトを実行します：

```bash
python disney_hotel_checker.py
```

スクリプトは指定された日付のホテル空室状況をチェックし、空室がある場合はLINEに通知を送信します。

## カスタマイズ

- `payload`ディクショナリ内のパラメータを変更することで、大人数、子供の数、宿泊日数などを調整できます。
- `generate_room_url`関数を修正することで、異なるホテルや部屋タイプをチェックできます。

## 注意事項

- このスクリプトは東京ディズニーリゾートの公式APIを使用しています。過度な使用は避け、適切な間隔を空けて実行してください。
- LINE Notifyのトークンは秘密情報です。`.env`ファイルをGitにコミットしないよう注意してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 貢献

バグ報告や機能リクエストは、GitHubのIssueを通じて行ってください。プルリクエストも歓迎します。

## 免責事項

このスクリプトは個人的な使用を目的としています。東京ディズニーリゾートの利用規約に違反しないよう、適切に使用してください。