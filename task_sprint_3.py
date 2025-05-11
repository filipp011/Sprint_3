import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    
    # Добавляем Геттеры
    # геттер для __name_items
    @property
    def name_items(self):
        return self.__name_items
    
    # геттер для number_items
    @property
    def number_items(self):
        return self.__number_items

    
    # Добавляем товар в чек
    def add_item_to_cheque(self, name):
        # Проверяем длину названия товара
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        
        # Проверяем существует ли товар в списке цен
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')

        # Добавляем товар в чек
        self.__name_items.append(name)
        self.__number_items += 1

    
    # Удаляем товар из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        
        # Добавляем товар в чек
        self.__name_items.remove(name)
        self.__number_items -= 1

    
    # Считаем общую стоимость товара
    def check_amount(self):
        total = sum(self.__item_price[item] for item in self.__name_items)
        
        # Применяем скидку, если количество товаров больше 10
        if len(self.__name_items) > 10:
            total *= 0.9
        
        return total