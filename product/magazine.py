class Eliana:
    def __init__(self, имя, цена, размер, производство, год):
        self.имя = имя
        self.цена = цена
        self.размер = размер
        self.производство = производство
        self.год = год


    def get_data(self):
        return f'{self.имя} цена {self.цена} размеры {self.размер} производство от {self.производство} год создания {self.год}'

bluska =Eliana("блузка", 350, "34-44", "KG", 2023)
print(bluska.get_data())
