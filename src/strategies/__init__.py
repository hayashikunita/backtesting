import pandas as pd

class SimpleStrategy:
    def __init__(self, data, short_window=5, long_window=20):
        self.data = data
        self.short_window = short_window
        self.long_window = long_window
# # src/utils/__init__.py
# def calculate_performance(returns):
#     cumulative_return = (1 + returns).prod() - 1 # ここでエラー
#     # ...
# # src/utils/__init__.py
# def calculate_performance(returns):
#     cumulative_return = (1 + returns).prod() - 1 # ここでエラー
#     # ...
# # src/utils/__init__.py
# def calculate_performance(returns):
#     cumulative_return = (1 + returns).prod() - 1 # ここでエラー
#     # ...

    def execute(self):
        df = pd.DataFrame(self.data)
        df['short_sma'] = df['close'].rolling(window=self.short_window).mean()
        df['long_sma'] = df['close'].rolling(window=self.long_window).mean()
        df['signal'] = 0
        condition = df['short_sma'] > df['long_sma']
        df.loc[self.short_window:, 'signal'] = condition[self.short_window:].astype(int)

        df['position'] = df['signal'].diff()
        # position: 1=買いシグナル, -1=売りシグナル
        return df[['close', 'short_sma', 'long_sma', 'signal', 'position']]

__all__ = ['SimpleStrategy']