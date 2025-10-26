# Python の環境を構築するためのテンプレート

## 環境

- Python: 3.12
- パッケージマネージャー: uv

## 使用ライブラリ

- 必要に応じて変更する

### 開発ツール

- **ruff**: Linter & Formatter
- **lefthook**: Git hooks 管理
- **pytest**: テストフレームワーク

### データ処理・分析

- **pandas**: データ分析ライブラリ
- **pandera**: データバリデーション
- **matplotlib**: データ可視化

## Git

このプロジェクトでは、コード品質を保つために **lefthook** を使用して Git hooks を管理しています。

### Git hooks

`uv run lefthook install` を実行すると、以下の hooks が設定されます：

- **pre-commit**: コミット前に ruff によるリントとフォーマットチェックを実行
- **pre-push**: プッシュ前にテストを実行

### Docker イメージ内の Git

Docker イメージには以下のツールが含まれています：

- **git**: バージョン管理システム
- **openssh-client**: SSH 接続（プライベートリポジトリのクローン等に使用）

## Docker

```bash
# イメージのビルド
docker-compose build

# コンテナの起動
docker-compose up
```
