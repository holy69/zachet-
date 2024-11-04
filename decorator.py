# Задача:
# Создадим класс Coffee, представляющий кофе, и декораторы MilkDecorator и SugarDecorator, которые добавляют к кофе молоко и сахар.
# Автор: Соколов Е.А. 43ИС-21


class Coffee:
    def cost(self):
        return 5  #стоимость кофе

    def description(self):
        return "Простой кофе"

# декоратор для молока
class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ", Молоко"

# декоратор для сахара
class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1  #стоимость сахара

    def description(self):
        return self._coffee.description() + ", Сахар"

# паттерн Декоратор
simple_coffee = Coffee()
print(simple_coffee.description(), "- $", simple_coffee.cost())

milk_coffee = MilkDecorator(simple_coffee)
print(milk_coffee.description(), "- $", milk_coffee.cost())

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(sugar_milk_coffee.description(), "- $", sugar_milk_coffee.cost())
