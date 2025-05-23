import pandas as pd
import sys
import os

# Add project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

# This test checks if the SMACrossover strategy generates signals correctly.
# It creates a DataFrame with dummy data and verifies that the output is a dictionary.
# The test can be run by executing this script directly.
# The test can be expanded to include more specific checks, such as verifying the contents of the signals.

