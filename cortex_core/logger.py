from loguru import logger
logger.add("logs/trading.log", rotation="500 KB")

def log_trade(date, signal):
    logger.info(f"Trade on {date}: {signal}")