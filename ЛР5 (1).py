class technic:
    typ = "Для дома"
    age = 1
    model = "sony"
    product = "laptop"
    size = 15
    company = "dell"
    temp = 100
    def set(self, typ, age):
        self.typ = typ
        self.age = age
class TV(technic):
    price = 100000
    def technic_method(self, model, age):
        self.model = model
        self.age = age
class notebook(technic):
    processor = "intel core i7"
    def technic_note(self, product, age):
        self.product = product
        self.age = age
class monitor(technic):
    lightsync = "RGB"
    def technic_monitor(self, size, age):
        self.size = size
        self.age = age
class printer(technic):
    module = "bluetooth 5.0"
    def technic_printer(self, company, age):
        self.company = company
        self.age = age
class mikrovolnovka(technic):
    power = 700 # мощность микроволнвоки в Вт
    def technic_method(self, temp, age):
        self.temp = temp
        self.age = age

class employee:
    position = "employee"
    salary = 70000
    schedule = "free"
    def employee(self, position, salary, schedule):
        self.position = position
        self.salary = salary
        self.schedule = schedule 
class kassir(employee):
    position = "Кассир"
class manager(employee):
    position = "Мэнэджэр"
    
Manager = [
    {'name': 'Sergey', 'position': "assistant"},
    {'name': 'Artem', 'position': "manager"},
    {'name': 'Danil', 'position': "Head master"}
]
Customer = [
    {'name': 'Kolya'},
    {'name': 'Dima'},
    {'name': 'Nazar'}
]
Televisor = [
    {'model': 'dexp', 'price': 15000, 'quality': 8},
    {'model': 'sony', 'price': 35000, 'quality': 15},
    {'model': 'xiaomi', 'price': 36000, 'quality': 13},
]

items = list()  # global variable where we keep the data
people = list()  # global variable where we keep the data
customer = list()


# Добавить лист с телевизорами
def create_tele_list(app_items):
    global items
    items = app_items

# Создать новый лот
def create_item(model, price, quantity):
    global items
    items.append({'model': model, 'price': price, 'quality': quantity})


# Найти телевизор модели module
def read_item(model):
    global items
    myitems = list(filter(lambda x: x['model'] == model, items))
    if myitems:
        return myitems[0]
    else:
        print("oops!")


# Вывести список телевизоров
def read_items():
    global items
    return [item for item in items]

def read_names():
    global items
    return [item for item in items[0]]


# Добавим список менеджеров
def create_Manager_list(app_items):
    global people
    people = app_items

# Добавим список покупателей
def create_Customer_list(app_items):
    global customer
    customer = app_items


# Вывести список покупателей
def customer_list():
    global customer
    return [item for item in customer]


# Вывести список покупателей
def meneger_list():
    global people
    return [item for item in people]


# Функция, которая будет убирать телефизор, который купили
def buy_televisor(model):
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['model'] == model, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]

def choice_name(choice):
    new_model = input("Введите модель телевизора: ")
    Oleg.find(new_model)
    if read_item(new_model):
        ans = input("Хотите его преобрести? (Да/Нет): ")
        if ans == "Да":
            Oleg.buy("dexp")
            print("Поздравляю с покупкой! ")
# Класс покупателя, в котором будут инециализорованны функции
class cust_buy:

    def __init__(self, name):
        self.name = name

    # Найти необходимый телевизор
    def find(self, model):
        self.model = model
        if read_item(model):
            print("we have one!")
            return True
        else:
            print("take another choise")

    # купить телевизор
    def buy(self, model):
        self.model = model
        if read_item(model):
            buy_televisor(model)
            print("It's work!")
        else:
            print("Sorry! We don't have that's one(")



create_tele_list(Televisor)
create_Manager_list(Manager)
create_Customer_list(Customer)
# create_item("samsung", 15000, 15)
print(read_names())


name = input("Введте имя пользователя: ")
Oleg = cust_buy(name)
choice = int(input("Вы можете выбрать модель телевизора, "
               "который хотите купить, либо посмотреть список доступных телевизоров(1/2): "))
if choice == 1:
    choice_name(choice)
else:
    read_names()
choice = int(input("Вы можете выбрать модель телевизора, "
               "который хотите купить, либо посмотреть список доступных телевизоров(1/2): "))
if choice == 1:
    choice_name(choice)
else:
    read_names()



