# Decorator/alldecorators/CoffeeShop.py
# Coffee example using decorators
class PizzaComponent:

    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Packing(PizzaComponent):
    cost = 0.0


class Decorator(PizzaComponent):
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + '' + PizzaComponent.getDescription(self)


class Catupiry(Decorator):
    cost = 0.75

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Cheese(Decorator):
    cost = 0.0

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Chicken(Decorator):
    cost = 0.25

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Pepperoni(Decorator):
    cost = 0.25

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Portuguese(Decorator):
    cost = 0.25

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Chocolate(Decorator):
    cost = 0.25

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


pizza1 = Catupiry(Chicken(Packing()))
print(pizza1.getDescription() + ": $" + str(pizza1.getTotalCost()))

pizza2 = Catupiry(Pepperoni(Chocolate(Portuguese(Cheese(Packing())))))

print(pizza2.getDescription() + ": $" + str(pizza2.getTotalCost()))