import yaml
from cortex_core import data_loader
from cortex_core.execution_engine import ExecutionEngine
from cortex_core.risk_manager import RiskManager
from cortex_core.logger import log_trade
from strategies.sma_crossover import SMACrossover

if __name__ == "__main__":
    with open("configs/default_config.yaml") as file:
        config = yaml.safe_load(file)

    data = data_loader.load_data(config['ticker'], config['start_date'], config['end_date'])
    strategy = SMACrossover(config['short_window'], config['long_window'])
    signals = strategy.generate_signals(data)

    risk_manager = RiskManager()
    filtered_signals = risk_manager.filter_signals(signals)

    executor = ExecutionEngine()
    executor.execute(filtered_signals)

    for date, signal in filtered_signals.items():
        log_trade(date, signal)