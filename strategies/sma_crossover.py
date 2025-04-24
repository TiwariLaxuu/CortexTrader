class SMACrossover(Strategy):
    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame):
        signals = {}
        data['short_ma'] = data['Close'].rolling(self.short_window).mean()
        data['long_ma'] = data['Close'].rolling(self.long_window).mean()
        for date, row in data.iterrows():
            if row['short_ma'] > row['long_ma']:
                signals[date] = 'BUY'
            elif row['short_ma'] < row['long_ma']:
                signals[date] = 'SELL'
        return signals