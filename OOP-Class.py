class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    @classmethod
    def franchise(cls, name):
        return cls(name + ' Super Market')

    @staticmethod
    def store_details(store):
        return f"Store Title: {store.name}"

    # def store_details(self):
    #     return f"Store Title: {self.name}"


store = Store.franchise('Imtiaz DHA')
print(Store.store_details(store))
