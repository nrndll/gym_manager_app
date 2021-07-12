class Activity():
    def __init__(self, description, capacity, premium, date, time, id=None):
        self.description = description
        self.capacity = capacity
        self.premium = premium
        self.date = date
        self.time = time
        self.id = id