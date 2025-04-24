import pandas as pd
from strategies.sma_crossover import SMACrossover

def test_sma_strategy():
    df = pd.DataFrame({
        'Close': [1,2,3,4,5,6,7,8,9,10]*10  # 100 rows
    })
    strategy = SMACrossover(short_window=5, long_window=20)
    signals = strategy.generate_signals(df)
    assert isinstance(signals, dict)
    print("Test passed.")

if __name__ == '__main__':
    test_sma_strategy()
