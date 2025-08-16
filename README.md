# 日本株バックテストプロジェクト

このプロジェクトは、日本株に特化したトレーディングストラテジーのバックテストを行うためのPythonアプリケーションです。  
東証形式のCSVデータを使い、シンプルな戦略の検証・パフォーマンス評価ができます。

## ディレクトリ構成

```
backtesting
├── src
│   ├── main.py          # アプリのエントリーポイント。バックテスト実行ロジック。
│   ├── strategies       # 売買戦略の定義。
│   │   └── __init__.py
│   ├── data             # 日本株データの読み込み・前処理。
│   │   └── __init__.py
│   ├── backtest         # バックテスト実行クラス。
│   │   └── __init__.py
│   └── utils            # パフォーマンス指標などのユーティリティ。
│       └── __init__.py
├── src/data/japan_stock.csv # サンプル日本株CSVデータ　（null）
├── pyproject.toml       # Pythonプロジェクト設定ファイル
├── README.md            # このドキュメント
```

## 必要なパッケージのインストール

```
uv init
```
（pyproject.toml利用の場合）

## 使い方

1. `src/data/japan_stock.csv` の様に日本株のCSVデータを配置してください。  
   - ヘッダー例: `DateTime,Open,High,Low,Close,Volume`
2. 以下のコマンドでバックテストを実行します。

```
uv run src/main.py
```

## 出力例

- 最終資金
- トレード履歴（買い・売り・利益）
- パフォーマンス指標（累積リターン、年率リターン、ボラティリティ、シャープレシオ）

## 貢献

バグ報告・機能追加のご提案はIssueまたはPull Requestでお願いします。

## ライセンス

MITライセンス
