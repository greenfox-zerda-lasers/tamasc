class Food():

    def __init__(self, type):
        self.type = type
        self.something = 15

    def eat(self):
        print('you ate the ' + self.type)


waffle = Food('waffle')


print(waffle.type)
print(waffle.something)

Food.type = 'asdasd'
Food.something = 'asdasd'
Food.x = 45

print(waffle.type)
print(waffle.something)
print(waffle.x)
