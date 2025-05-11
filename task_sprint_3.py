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
    

    # Рассчет НДС 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])

        # Рассчитываем общую сумму НДС
        tax_total = sum(price * 0.2 for price in total)

        # Если количество товаров больше 10, применяем скидку на общую сумму НДС
        if len(self.__name_items) > 10:
            tax_total *= 0.9
        
        return tax_total
    

    # Расчет НДС для товаров 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])

        # Рассчитываем общую сумму НДС
        tax_total = sum(price * 0.1 for price in total)

        # Если количество товаров больше 10, применяем скидку на общую сумму НДС
        if len(self.__name_items) > 10:
            tax_total *= 0.9
        
        return tax_total
    

    # Расчет общей суммы налога
    def total_tax(self):
        total_twenty_percent_tax = self.twenty_percent_tax_calculation()
        total_ten_percent_tax = self.ten_percent_tax_calculation()
        
        return total_twenty_percent_tax + total_ten_percent_tax
    

    # Вовзрат телефона 
    @staticmethod
    def get_telephone_number(telephone_number):
        # Проверяем, является ли номер целым числом
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        
        # Преобразуем номер в строку для дальнейшей проверки длины
        telephone_str = str(telephone_number)

        # Проверяем длину номера
        if len(telephone_str) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        # Возвращаем полный номер телефона с кодом страны +7
        return f'+7{telephone_str}'
    
    telephone_number = 1234567890  # Пример корректного номера телефона
    full_number = OnlineSalesRegisterCollector.get_telephone_number(telephone_number)

# Выводим полный номер телефона
print(full_number)  # Ожидаемый вывод: +71234567890
    
