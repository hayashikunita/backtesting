import pandas as pd

class Backtesterdata:
    @staticmethod
    def load_japan_stock_data(filepath):
        """
        日本株CSVデータを読み込む関数
        必要なカラム: DateTime, Open, High, Low, Close, Volume
        """
        df = pd.read_csv(filepath, parse_dates=['DateTime'])
        # 列名を統一（小文字化）
        df = df.rename(columns={
            'DateTime': 'date',
            'Open': 'open',
            'High': 'high',
            'Low': 'low',
            'Close': 'close',
            'Volume': 'volume'
        })
        return df