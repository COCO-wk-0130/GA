class data_generator:
    def __init__(self):
        pass
    def data_generate(self):
        item_weight = [i//10+1 for i in range(100)]
        item_value = [i//10+6 for i in range(100)]
        return item_weight, item_value