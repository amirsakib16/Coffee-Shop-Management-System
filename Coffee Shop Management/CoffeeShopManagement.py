# task 5
class Menu:
    def __init__(self,name,menuName):
        self.menu = {
            "HOT COFFEE":["1. Americano","2. Cappuccino","3. Doppio","4. Espresso","5. Latte"],
            "COLD COFFEE":["1. Caramel_Mocha","2. Dark_Mocha","3. Freddo_Espresso","4. Freddo_Latte","5. Mocha"],
            "GRILLED SANDWICH":["1. BBQ_Chicken_Sandwich","2. Tandoori_Chicken_Sandwich","3. Tuna_Sandwich","4. Veggie_Sandwich"],
            "ICED":["1. Americano","2. Clod_Brew","3. Chai_Latte","4. Furyspresso"],
            "DESSERT":["1. Affogato","2. Brownie","3. NewYark_Cheesecake","4. RedVelvet_Cupcake"]
            }
        self.selected = []
        self.modified = []
        self.order = []
        self.customer_name = name
        self.menuName = menuName
        self.reply = None
        self.totalPrice = 0
        self.indPrice1 = []
        self.indPrice = []
        self.foodCode = []
        self.foodPrices = None
        self.quantity = []
    def add_food_items(self,args):
        x = args.split(" ")
        for j in self.menu[self.menuName]:
            n = j.split(". ")
            for k in x:
                if k == n[0]:
                    self.order.append(f"{n[0]}. {n[1]}")

    def remove_food_items(self,ans,food=None):
        modify = []
        new = []
        tempd = []
        dup = []
        l = []
        self.reply = ans
        if ans=="NO":
            for i in self.order:
                modify.append(i)
            print("************************ NO CHANGES!! *******************************")
            print("FOOD ITEM(S) IS/ARE")
            for i in modify:
                print(i)

        elif ans=="YES":
            for i in self.order:
                if i not in food:
                    modify.append(i)
            for i in food:
                for j in self.order:
                    if i==j:
                        tempd.append(j)
                new.append(tempd)
                tempd = []
            for i in food:
                for j in new:
                    if i in j:
                        j.pop()
            for i in new:
                if i not in l:
                    l.append(i)
            for i in l:
                for j in i:
                    modify.append(j)
            print(f"************************** {len(self.order)-len(modify)} ITEM(S) HAS BEEN REMOVED ************************")
            print("NEW FOOD ITEM(S) IS/ARE")
            modify.sort()
            for i in modify:
                print(i)
        for i in modify:
            n = i.split(". ")
            self.foodCode.append(int(n[0]))
        for i in modify:
            if i not in self.selected:
                self.selected.append(i)
        modify.sort()
        self.modified = modify

    def show_menu(self,p):
        self.foodPrices = p
        counter = 0
        print(f"Dear {self.customer_name.name},")
        print("The menu you have selected contains the following items:")
        for i in self.menu:
            if i == self.menuName:
                for j in self.menu[i]:
                    print(f"{j}  {self.foodPrices[i][counter]} BDT")
                    counter+=1
    def printDetails(self):
        print(f"Dear {self.customer_name.name}, The items you have selected is/are:")
        for i in self.order:
            print(i)

    def price(self):
        prices = {
            "HOT COFFEE":[290, 230, 320, 350, 200],
            "COLD COFFEE":[260, 210, 310, 360, 290],
            "GRILLED SANDWICH":[400, 430, 520, 480],
            "ICED":[190, 200, 280, 130],
            "DESSERT":[120, 170, 130, 150]
                    }
        return prices

    def calculation(self):
        for j in self.foodCode:
            self.totalPrice+=self.foodPrices[self.menuName][j-1]
            self.indPrice1.append(self.foodPrices[self.menuName][j-1])
        for i in self.indPrice1:
            if i not in self.indPrice:
                self.indPrice.append(i)

    def bill(self):
        x = []
        self.modified.sort()
        count = 0
        for i in self.menu[self.menuName]:
            for j in self.modified:
                if i==j:
                    count+=1
            x.append(count)
            count=0
        for i in x:
            if i!=0:
                self.quantity.append(i)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("********************************TOTAL BILL*****************************************************")
        print()
        print(f"Customer Name: {self.customer_name.name}")
        print("Food Items                           Price")
        pr = 0
        for i in self.selected:
            print(f"{i} (X{self.quantity[pr]})                  {(self.indPrice[pr])*(self.quantity[pr])} Taka")
            pr+=1
        print("___________________________________________________________________________")
        print(f"TOTAL:                               {self.totalPrice} Taka")
        print()
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


class Customer:
    def __init__(self,name):
        self.name = name



customer1 = Customer(input("Please enter your name here:   "))
print("ALL ITEMS")
items = ["HOT COFFEE","COLD COFFEE","GRILLED SANDWICH","ICED","DESSERT"]
for i in items:
    print(i)
m1 = Menu(customer1,input("Enter the menu you want to see:   ").upper())
m1.show_menu(m1.price())
print("Select the items that you wanna order by pressing the corresponding number")
print("Just type the serial number. For multiple items you can just type the serial numbers with space seperated")
m1.add_food_items(input())
m1.printDetails()
print()
ques1 = input("Do you want to remove any food items: yes/no  ").upper()

if ques1=="NO":
    m1.remove_food_items(ques1)
elif ques1=="YES":
    p1 = input("Items you want to remove: ")
    m1.remove_food_items(ques1,p1.split(", "))
m1.calculation()
m1.bill()
print("--------------------------------------------------------------------------------------------")
customer2 = Customer(input("Please enter your name here:   "))
m2 = Menu(customer2,input("Enter the menu you want to see:   ").upper())
m2.show_menu(m2.price())
print("Select the items that you wanna order by pressing the corresponding number")
m2.add_food_items(input())
m2.printDetails()
print()
ques2 = input("Do you want to remove any food items: ").upper()

if ques2=="NO":
    m2.remove_food_items(ques2)
elif ques2=="YES":
    p2 = input("Items you want to remove: ")
    m2.remove_food_items(ques2,p2.split(", "))
m2.calculation()
m2.bill()
print("--------------------------------------------------------------------------------------------")
customer3 = Customer(input("Please enter your name here:   "))
m3 = Menu(customer3,input("Enter the menu you want to see:   ").upper())
m3.show_menu(m3.price())
print()
print("Select the items that you wanna order by pressing the corresponding number")
m3.add_food_items(input())
m3.printDetails()
print()
ques3 = input("Do you want to remove any food items: ").upper()

if ques3=="NO":
    m3.remove_food_items(ques3)
elif ques3=="YES":
    p3 = input("Items you want to remove: ")
    m3.remove_food_items(ques3,p3.split(", "))
m3.calculation()
m3.bill()
print("--------------------------------------------------------------------------------------------")
customer4 = Customer(input("Please enter your name here:   "))
m4 = Menu(customer4,input("Enter the menu you want to see:   ").upper())
m4.show_menu(m4.price())
print()
print("Select the items that you wanna order by pressing the corresponding number")
m4.add_food_items(input())
m4.printDetails()
print()
ques4 = input("Do you want to remove any food items: ").upper()

if ques4=="NO":
    m4.remove_food_items(ques4)
elif ques4=="YES":
    p4 = input("Items you want to remove: ")
    m4.remove_food_items(ques4,p4.split(", "))
m4.calculation()
m4.bill()
print("--------------------------------------------------------------------------------------------")
customer5 = Customer(input("Please enter your name here:   "))
m5 = Menu(customer5,input("Enter the menu you want to see:   ").upper())
m5.show_menu(m5.price())
print("Select the items that you wanna order by pressing the corresponding number")
m5.add_food_items(input())
m5.printDetails()
print()
ques5 = input("Do you want to remove any food items: ").upper()

if ques5=="NO":
    m5.remove_food_items(ques5)
elif ques5=="YES":
    p5 = input("Items you want to remove: ")
    m5.remove_food_items(ques5,p5.split(", "))
m5.calculation()
m5.bill()
print("--------------------------------------------------------------------------------------------")