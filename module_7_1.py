class Product:  # зададим класс
    def __init__(self, name, weight, category):  # зададим атрибуты
        self.name = name     # название продукта
        self.weight = weight   # общий вес товара
        self.category = category # категория товара

    def __str__(self):  # вывод строки с инф-ей о товаре
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:  # зададим класс
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')  # откроем в режиме чтения
        products = file.read()  # чтение и сохр. данных в переменной
        file.close() # закрываем файл
        return products # возврат данных из переменной

    def add(self, *products):
        # возврат ин-фы из файла в виде строки, разделенной на строки
        existing_products = self.get_products().split('\n')
        # split(', ') - раздел. строк на запят. + пробел
        # [0] извлекает первый эл. разделенной строки - это назв. продукта
        # if product исключаем пустые строки
        existing_products = [product.split(', ')[0] for product in existing_products]

        file = open(self.__file_name, 'a') # откр. файл в режиме добавления
        for product in products:
            # переберем продукты чтобы узнать есть в списке существующих
            if product.name not in existing_products: # если нет, то даюавит в файл
                file.write(f"{product}\n")
            else: # иначе вывод строки
                print(f"Продукт {product.name} уже есть в магазине")
        file.close() # закр. файл

# Пример работы программы:

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')



print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())