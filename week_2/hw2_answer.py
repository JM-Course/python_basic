class Calculator:
    def __init__(self):
        self.current_value = 0

    def add(self, value):
        self.current_value += value

    def sub(self, value):
        self.current_value -= value

    def mul(self, value):
        self.current_value *= value

    def get_value(self):
        return self.current_value

    def reset(self):
        self.current_value = 0


if __name__ == "__main__":
    cal = Calculator()
    cal.add(5)
    cal.sub(3)
    cal.mul(5)
    print(cal.get_value())
    cal.reset()
    print(cal.get_value())
