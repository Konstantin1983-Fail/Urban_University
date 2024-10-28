class Car:
    def __init__(self, make, model):
        self.make = make  # атрибут
        self.model = model  # атрибут

    def start_engine(self):  # метод
        print(f"{self.make} {self.model} engine started")

    def stop_engine(self):  # метод
        print(f"{self.make} {self.model} engine stopped")
