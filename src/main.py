from strategies import SimpleStrategy
from data import Backtesterdata
from backtest import Backtester
from utils import calculate_performance

def main():
    # 日本株データの読み込み（例: 東証のCSV形式、日付・終値・始値・高値・安値・出来高など）
    # data = Backtesterdata.load_japan_stock_data('src/data/japan_stock.csv')
    # data = Backtesterdata.load_japan_stock_data('src\data\japan_stock.csv')
    data = Backtesterdata.load_japan_stock_data('src/data/japan_stock.csv')

    # 戦略の初期化（日本株は取引時間や祝日などに注意）
    strategy = SimpleStrategy(data, short_window=5, long_window=25)

    # バックテストの実行
    backtester = Backtester(strategy, data)
    results = backtester.run(initial_cash=1000000)  # 初期資金100万円

    # パフォーマンスの計算（日本株向け指標例: 年率リターン、最大ドローダウン、勝率など）
    performance = calculate_performance(results['returns'])
    
    # 結果の表示
    # print("日本株バックテスト結果:", results)
# ...existing code...
    print("トレード履歴:")
    for trade in results['trade_log']:
        if trade['type'] == 'buy':
            print(f"  買い: 価格={float(trade['price'])} 日付/インデックス={trade['index']}")
        elif trade['type'] == 'sell':
            print(f"  売り: 価格={float(trade['price'])} 日付/インデックス={trade['index']} 利益={float(trade['profit'])}")
# ...existing code...

    # print("パフォーマンス指標:", performance)

# ...existing code...
    # 結果の表示
    print("日本株バックテスト結果（最終資金）:", float(results['final_cash']))
    # print("トレード履歴:", results['trade_log'])
    print("パフォーマンス指標:")
    for k, v in performance.items():
        print(f"  {k}: {float(v):.4%}" if 'return' in k or 'volatility' in k else f"  {k}: {float(v):.4f}")
# ...existing code...

if __name__ == "__main__":
    main()