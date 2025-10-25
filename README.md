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

## セットアップ

```bash
# 依存関係のインストール
uv sync

# テストの実行
uv run pytest
```

## Docker

```bash
# イメージのビルド
docker-compose build

# コンテナの起動
docker-compose up
```
