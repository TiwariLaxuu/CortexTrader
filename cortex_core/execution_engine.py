class ExecutionEngine:
    def __init__(self):
        self.positions = []

    def execute(self, signals):
        for date, signal in signals.items():
            print(f"{date}: Executing {signal} trade")
            self.positions.append((date, signal))