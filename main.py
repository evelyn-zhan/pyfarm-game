import os
import random

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

# === Start of UserStats Class ===
class UserStats:
    def __init__(self):
        self.day = 1
        self.financial = {
            1: {
                'Profit': 0,
                'Expense': 0
            }
        }
    
    def next_day(self):
        self.day += 1
        self.financial[self.day] = {
            'Profit': 0,
            'Expense': 0
        }
        market.sell.update_prices()
    
    def check_progress(self):
        if self.day == 4:
            seeds.list['Potato Seed']['unlocked'] = True
            inventory.list['Potato Seed']['quantity'] = 5
            market_items.list['Potato Seed']['unlocked'] = True
            market.sell.list['Potato']['unlocked'] = True

            print('> 🥳 Congratulations! You have reached Day 4.')
            print('> 🥔 Potato Seed is now unlocked. You received 5 potato seeds.')
            print('-' * 80)

            return
        
        if self.day == 5:
            market_items.list['Cow']['unlocked'] = True
            market_items.list['Cow Feed']['unlocked'] = True
            market.sell.list['Milk']['unlocked'] = True

            print('> 🥳 Congratulations! You have reached Day 5.')
            print('> 🐮 Cow is now unlocked. You can buy them at the market.')
            print('-' * 80)

            return
        
        if inventory.list['Coin']['quantity'] > 1100 and seeds.list['Tomato Seed']['unlocked'] is False:
            seeds.list['Tomato Seed']['unlocked'] = True
            inventory.list['Tomato Seed']['quantity'] = 5
            market_items.list['Tomato Seed']['unlocked'] = True
            market.sell.list['Tomato']['unlocked'] = True

            print('> 🥳 Congratulations! You have got more than 1100 🪙')
            print('> 😄 For this achievement, you will receive Tomato Seed!')
            print('> 🍅 Tomato Seed is now unlocked. You received 5 tomato seeds.')
            print('-' * 80)

            return
        
        if inventory.list['Coin']['quantity'] > 1500 and inventory.list['Corn']['quantity'] >= 15 and inventory.list['Potato']['quantity'] >= 10 and inventory.list['Tomato']['quantity'] >= 5 and seeds.list['Carrot Seed']['unlocked'] is False:
            seeds.list['Carrot Seed']['unlocked'] = True
            inventory.list['Carrot Seed']['quantity'] = 5
            market_items.list['Carrot Seed']['unlocked'] = True
            market.sell.list['Carrot']['unlocked'] = True

            print('> 🥳 Congratulations! You have reached the following conditions:')
            print('\t- You have more than 1500 🪙')
            print('\t- You have at least 15 corns in your inventory 🌽')
            print('\t- You have at least 10 potatoes in your inventory 🥔')
            print('\t- You have at least 5 tomatoes in your inventory 🍅')
            print('> 🥕 Carrot Seed is now unlocked. You received 5 carrot seeds.')
            print('-' * 80)

            return
# === End of UserStats Class ===

# === Start of Inventory Class ===
class Inventory:
    def __init__(self):
        
        self.list = {
            'Coin': {
                'quantity': 1000,
                'icon': '🪙',
                'type': 'currency'
            },
            'Corn Seed': {
                'quantity': 5,
                'icon': '🌽',
                'type': 'seed'
            },
            'Corn': {
                'quantity': 0,
                'icon': '🌽',
                'type': 'crop'
            },
            'Potato Seed': {
                'quantity': 0,
                'icon': '🥔',
                'type': 'seed'
            },
            'Potato': {
                'quantity': 0,
                'icon': '🥔',
                'type': 'crop'
            },
            'Tomato Seed': {
                'quantity': 0,
                'icon': '🍅',
                'type': 'seed'
            },
            'Tomato': {
                'quantity': 0,
                'icon': '🍅',
                'type': 'crop'
            },
            'Carrot Seed': {
                'quantity': 0,
                'icon': '🥕',
                'type': 'seed'
            },
            'Carrot': {
                'quantity': 0,
                'icon': '🥕',
                'type': 'crop'
            },
            'Egg': {
                'quantity': 0,
                'icon': '🥚',
                'type': 'product'
            },
            'Milk': {
                'quantity': 0,
                'icon': '🥛',
                'type': 'product'
            },
            'Chicken Feed': {
                'quantity': 0,
                'icon': '🫘',
                'type': 'product'
            },
            'Cow Feed': {
                'quantity': 0,
                'icon': '🌾',
                'type': 'product'
            }
        }

    def print_inventory(self):
        for item_name in self.list:
            item = self.list[item_name]
            if item['quantity'] > 0: print(f'> {item['icon']} {item_name}: {item['quantity']}')
# === End of Inventory Class ===

# === Start of Farm Class ===
class Farm:
    def __init__(self):
        self.size = 3
        self.field = [['No seed' for _ in range(self.size)] for _ in range(self.size)]
        self.field_detail = [['' for _ in range(self.size)] for _ in range(self.size)]
        self.field_day = [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def update_field(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.field_detail[row][col] == '': continue
                self.field_day[row][col] += 1
                if self.field_day[row][col] == seeds.list[self.field_detail[row][col]]['grow_time']:
                    self.field[row][col] = seeds.list[self.field_detail[row][col]]['icon']
    
    def print_field(self):
        print(f'> 🌽 Current field size: {self.size} x {self.size}\n')
        for row in self.field:
            count = 0
            for col in row:
                count += 1
                if col == 'No seed': print(f'{col:^9}', end='')
                else: print(f'{col:^8}', end='')
                if count < self.size: print('|', end='')
            print()
        print()
    
    def plant_seed(self, row, col, seed_name):
        if self.field_detail[row][col] == '':
            self.field_detail[row][col] = seed_name
            self.field[row][col] = '🌱'
            print(f'> 🌱 {seed_name} planted successfully!')
            return True
        
        print('> 🌱 There is already a seed in this field.')
        return False
    
    def harvest(self):
        crops = {
            'Corn': 0,
            'Potato': 0,
            'Tomato': 0,
            'Carrot': 0
        }

        for row in range(self.size):
            for col in range(self.size):
                seed_name = self.field_detail[row][col]
                if seed_name == '': continue
                seed = seeds.list[seed_name]
                if self.field_day[row][col] >= seed['grow_time']:
                    self.field[row][col] = 'No seed'
                    self.field_detail[row][col] = ''
                    self.field_day[row][col] = 0
                    crop_name = seed_name.replace(' Seed', '')
                    inventory.list[crop_name]['quantity'] += 1
                    crops[crop_name] += 1
        
        return crops
# === End of Farm Class ===

# === Start of Seeds Class ===
class Seeds:
    def __init__(self):
        self.list = {
            'Corn Seed': {
                'code': 1,
                'icon': '🌽',
                'grow_time': 3,
                'unlocked': True 
            },
            'Potato Seed': {
                'code': 2,
                'icon': '🥔',
                'grow_time': 4,
                'unlocked': False
            },
            'Tomato Seed': {
                'code': 3,
                'icon': '🍅',
                'grow_time': 4,
                'unlocked': False
            },
            'Carrot Seed': {
                'code': 4,
                'icon': '🥕',
                'grow_time': 3,
                'unlocked': False
            }
        }

    
    def count(self):
        count = 0
        for seed_name in self.list:
            seed = self.list[seed_name]
            if seed['unlocked'] == True: count += 1
        return count
    
    def print_seeds_list(self):
        print('> 🌱 List of unlocked seed(s):')
        print('-' * 80)

        count = 0
        for seed_name in self.list:
            seed = self.list[seed_name]
            if seed['unlocked'] == False: continue
            count += 1
            print(f'> {count}. {seed['icon']} {seed_name}: {inventory.list[seed_name]['quantity']} seed(s) left.')
        
        print()
# === End of Seeds Class ===

# === Start of Barn Class ===
class Barn:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def feed_animals(self):
        for animal in self.animals:
            if animal.feeded == True: continue
            animal.feeded = True
            animal.feeded_days += 1
            if animal.health + 10 <= 100: animal.health += 10
            else: animal.health = 100
            if animal.feeded_days >= 3: animal.collectable = True
    
    def feed_some(self, feed_list):
        for number in feed_list:
            number -= 1
            if self.animals[number].feeded == True: continue
            self.animals[number].feeded = True
            self.animals[number].feeded_days += 1
            if self.animals[number].health + 10 <= 100: self.animals[number].health += 10
            else: self.animals[number].health = 100
            if self.animals[number].feeded_days >= 3: self.animals[number].collectable = True
    
    def update_status(self):
        dead = 0
        for animal in self.animals:
            if animal.feeded == False:
                animal.feeded_days = 0
                if animal.health - 20 >= 0: animal.health -= 20
                else:
                    self.animals.remove(animal)
                    dead += 1
            else: animal.feeded = False
        return dead
# === End of Barn Class ===

# === Start of Template Pattern ===
class TemplatePattern:
    def startingText(self): pass
    def animalList(self): pass

    def show_animals(self):
        self.startingText()
        self.animalList()
# === End of Template Pattern ===

# === Start of Chicken Barn Class ===
class ChickenBarn(Barn, TemplatePattern):
    def __init__(self):
        super().__init__()
    
    def startingText(self):
        if len(self.animals) == 0:
            print('> 🐔 There are no chickens in the chicken barn...')
            print('-' * 80)
            return
        
        print('> 🐔 List of chickens in the chicken barn:')
        print('-' * 80)
        return
    
    def animalList(self):
        count = 0
        for animal in self.animals:
            count += 1
            print(f'Chicken {count}')
            print(f'> 🐔 Name: {animal.name}')
            print(f'> ⏳ Age: {animal.age}')
            print(f'> ❤️ Health: {animal.health}')
            print(f'> 🍚 Feeded Today: {'Yes' if animal.feeded == True else 'No'}')
            print(f'> 🍚 Feeded Streak: {animal.feeded_days} day(s)')
            print('-' * 80)
    
    def collect_egg(self):
        egg = 0
        for animal in self.animals:
            if animal.collectable == True:
                egg += 1
                animal.collectable = False
        inventory.list['Egg']['quantity'] += egg
        return egg
# === End of Chicken Barn Class ===

# === Start of Cow Barn Class ===
class CowBarn(Barn, TemplatePattern):
    def __init__(self):
        super().__init__()
    
    def startingText(self):
        if len(self.animals) == 0:
            print('> 🐄 There are no cows in the cow barn...')
            print('-' * 80)
            return
        
        print('> 🐄 List of cows in the cow barn:')
        print('-' * 80)
        return
    
    def animalList(self):
        count = 0
        for animal in self.animals:
            count += 1
            print(f'Cow {count}')
            print(f'> 🐮 Name: {animal.name}')
            print(f'> ⏳ Age: {animal.age}')
            print(f'> ❤️ Health: {animal.health}')
            print(f'> 🍚 Feeded Today: {'Yes' if animal.feeded == True else 'No'}')
            print(f'> 🍚 Feeded Streak: {animal.feeded_days} day(s)')
            print('-' * 80)
        
    def collect_milk(self):
        milk = 0
        for animal in self.animals:
            if animal.collectable == True:
                milk += 1
                animal.collectable = False
        inventory.list['Milk']['quantity'] += milk
        return milk
# === End of Cow Barn Class ===

# === Start of Chicken Class === 
class Chicken:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 100
        self.feeded = False
        self.feeded_days = 0
        self.collectable = False
# === End of Chicken Class ===

# === Start of Cow Class ===
class Cow:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 100
        self.feeded = False
        self.feeded_days = 0
        self.collectable = False
# === End of Cow Class ===

# === Start of Market Item Class ===
class MarketItems:
    def __init__(self):
        self.list = {
            'Corn Seed': {
                'icon': '🌽',
                'price': 25,
                'unlocked': True
            },
            'Potato Seed': {
                'icon': '🥔',
                'price': 45,
                'unlocked': False
            },
            'Tomato Seed': {
                'icon': '🍅',
                'price': 60,
                'unlocked': False
            },
            'Carrot Seed': {
                'icon': '🥕',
                'price': 45,
                'unlocked': False
            },
            'Chicken': {
                'icon': '🐔',
                'price': 120,
                'unlocked': True
            },
            'Cow': {
                'icon': '🐄',
                'price': 180,
                'unlocked': False
            },
            'Chicken Feed': {
                'icon': '🫘',
                'price': 15,
                'unlocked': True
            },
            'Cow Feed': {
                'icon': '🌾',
                'price': 20,
                'unlocked': False
            }
        }
# === End of Market Item Class ===

# === Start of Market Class ===
class Market:
    def __init__(self):
        self.buy = Buy()
        self.sell = Sell()
# === End of Market Class ===

# === Start of Buy (Market) CLass ===
class Buy:
    def __init__(self): pass
    
    def show_items(self):
        print('-' * 80)
        print(f'{'🏪 Buy Item 🏪':^80}')
        print('-' * 80)
        print(f'You currently have {inventory.list['Coin']['quantity']} {inventory.list['Coin']['icon']}')
        print('-' * 80)

        print('> 🌽 List of available item(s):')
        print('-' * 80)

        count = 0
        for item_name in market_items.list:
            item = market_items.list[item_name]
            if item['unlocked'] == False: continue
            count += 1
            print(f'> {count}. {item['icon']} {item_name}: {item['price']} 🪙')
        
        print(f'> {count + 1}. Back to Main Menu 👈')
        
        print('-' * 80)
        return count
    
    def get_item(self, index, quantity):
        count = 0
        for item_name in market_items.list:
            item = market_items.list[item_name]
            if item['unlocked'] == False: continue
            
            count += 1
            
            if count == index:
                if quantity * item['price'] > inventory.list['Coin']['quantity']:
                    print('> ❗ Not enough coins!\n')
                    return
                
                inventory.list['Coin']['quantity'] -= quantity * item['price']
                stats.financial[stats.day]['Expense'] += quantity * item['price']
                
                if item_name == 'Chicken' or item_name == 'Cow':
                    for i in range(quantity): buy_animal(item_name)
                else: inventory.list[item_name]['quantity'] += quantity

                print('-' * 80)
                print(f'> 🪙 You have bought {quantity} {item_name}!')
                print(f'> 🪙 You have {inventory.list['Coin']['quantity']} coins left.')
                print('-' * 80)

                return
        
        print('> ❗ Invalid option!\n')
        return
# === End of Buy (Market) Class ===

# === Start of Sell (Market) Class ===
class Sell:
    def __init__(self):
        self.list = {
            'Corn': {
                'icon': '🌽',
                'price': random.randint(15, 40),
                'unlocked': True
            },
            'Potato': {
                'icon': '🥔',
                'price': random.randint(25, 50),
                'unlocked': False
            },
            'Tomato': {
                'icon': '🍅',
                'price': random.randint(40, 80),
                'unlocked': False
            },
            'Carrot': {
                'icon': '🥕',
                'price': random.randint(25, 50),
                'unlocked': False
            },
            'Egg': {
                'icon': '🥚',
                'price': random.randint(15, 30),
                'unlocked': True
            },
            'Milk': {
                'icon': '🥛',
                'price': random.randint(25, 40),
                'unlocked': False
            }
        }
    
    def update_prices(self):
        self.list['Corn']['price'] = random.randint(15, 40)
        self.list['Potato']['price'] = random.randint(25, 50)
        self.list['Tomato']['price'] = random.randint(40, 80)
        self.list['Carrot']['price'] = random.randint(25, 50)
        self.list['Egg']['price'] = random.randint(15, 30)
        self.list['Milk']['price'] = random.randint(25, 40)

    def show_items(self):
        print('-' * 80)
        print(f'{'🏪 Sell Item 🏪':^80}')
        print('-' * 80)

        print("> 🌽 Today's pricelist:")
        print('-' * 80)

        count = 0
        for item_name in self.list:
            item = self.list[item_name]
            if item['unlocked'] == False: continue
            count += 1
            print(f'> {count}. {item['icon']} {item_name}: {item['price']} 🪙')
        
        print(f'> {count + 1}. Back to Main Menu 👈')
        
        print('-' * 80)
        return count
    
    def sell_item(self, index, quantity):
        count = 0
        for item_name in self.list:
            item = self.list[item_name]
            if item['unlocked'] == False: continue
            
            count += 1
            
            if count == index:
                if quantity > inventory.list[item_name]['quantity']:
                    print("> ❗ You don't have enough of this item! You can try to sell less.\n")
                    return
                
                inventory.list[item_name]['quantity'] -= quantity
                inventory.list['Coin']['quantity'] += quantity * item['price']
                stats.financial[stats.day]['Profit'] += quantity * item['price']

                print('-' * 80)
                print(f'> 🪙 You have sold {quantity} {item_name}!')
                print(f'> 🪙 You received {quantity * item['price']} coins.')
                print('-' * 80)

                return
        
        print('> ❗ Invalid option!\n')
        return
# === End of Sell (Market) Class ===

# User Instances
stats = UserStats()
inventory = Inventory()

# Farm Instances
farm = Farm()
seeds = Seeds()

# Barn Instances
chicken_barn = ChickenBarn()
cow_barn = CowBarn()

# Market Instances
market = Market()
market_items = MarketItems()

# === Start of Farm Menu ===
def farm_menu():
    print('-' * 80)
    print(f'{'🌽 Farm 🌽':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80)
    print('1. Plant Seed 🌱')
    print('2. Harvest 🌾')
    print('3. Back to Main Menu 👈')

    print('-' * 80)

    choice = input('> Enter menu number: ')

    if choice not in ['1', '2', '3']:
        print('> ❗ Invalid option!\n')
        return
    
    if choice in ['1', '2']: cls()
    
    if choice == '1': farm_plant_menu()
    elif choice == '2': farm_harvest_menu()
    else:
        print('-' * 80)
        return
# === End of Farm Menu ===

# Start of Farm Plant Menu
def farm_plant_menu():
    print('-' * 80)
    print(f'{'🌱 Plant Seed 🌱':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80 + '\n')

    seeds.print_seeds_list()

    seed_count = 0
    for seed_name in seeds.list:
        seed = seeds.list[seed_name]
        if seed['unlocked'] == True: seed_count += inventory.list[seed_name]['quantity']
    
    if seed_count == 0:
        print('> 🌱 There are no seeds left to be planted. You can buy them at the market.')
        print('-' * 80)
        return

    valid = False
    while valid is False:
        choice = input('> ❓ Do you want to plant any seed? (y/n): ').lower()
        try:
            if choice == '': raise ValueError('> ❗ Choice may not be empty!')
            if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!')
            valid = True
        except ValueError as e:
            print(str(e))
    
    print()

    if choice == 'n': return

    valid = False
    while valid is False:
        seed_code = input('> 🌱 Enter seed code number: ')
        try:
            if seed_code == '': raise ValueError('> ❗ Seed code may not be empty!')
            if not seed_code.isnumeric(): raise ValueError('> ❗ Seed code must be a number!')

            seed_code = int(seed_code)

            if seed_code < 1 or seed_code > seeds.count(): raise ValueError('> ❗ Invalid seed code!')

            if seed_code == 1: seed_name = 'Corn Seed'
            elif seed_code == 2: seed_name = 'Potato Seed'
            elif seed_code == 3: seed_name = 'Tomato Seed'
            elif seed_code == 4: seed_name = 'Carrot Seed'

            if inventory.list[seed_name]['quantity'] == 0: raise ValueError(f'> ❗ There are no {seed_name} left to be planted. You can buy them at the market.\n')
            # seed_code = seed_code
            valid = True

        except ValueError as e:
            print(str(e))
    
    print()

    valid = False
    while valid is False:
        row = input('> 🌱 Enter row number: ')
        try:
            if row == '': raise ValueError('> ❗ Row number may not be empty!')
            if not row.isnumeric(): raise ValueError('> ❗ Row number must be a number!')
            row = int(row)
            if row < 1 or row > farm.size: raise ValueError('> ❗ Invalid row number!')
            row -= 1
            valid = True
        except ValueError as e:
            print(str(e))
        
    print()

    valid = False
    while valid is False:
        col = input('> 🌱 Enter column number: ')
        try:
            if col == '': raise ValueError('> ❗ Column number may not be empty!')
            if not col.isnumeric(): raise ValueError('> ❗ Column number must be a number!')
            col = int(col)
            if col < 1 or col > farm.size: raise ValueError('> ❗ Invalid column number!')
            col -= 1
            valid = True
        except ValueError as e:
            print(str(e))
        
    print()

    valid = farm.plant_seed(row, col, seed_name)
    print('-' * 80)

    if valid:
        inventory.list[seed_name]['quantity'] -= 1
        print()
        farm.print_field()
        print('-' * 80)
# === End of Farm Plant Menu ===

# === Start of Farm Harvest Menu ===
def farm_harvest_menu():
    print('-' * 80)
    print(f'{'🌾 Harvest 🌾':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80)

    harvestable_count = 0

    for row in range(farm.size):
        for col in range(farm.size):
            if farm.field_detail[row][col] == '': continue
            if farm.field_day[row][col] >= seeds.list[farm.field_detail[row][col]]['grow_time']:
                harvestable_count += 1
    
    if harvestable_count == 0:
        print('> 🌾 There are no crops to be harvested')
        print('-' * 80)
        return
    
    print(f'> 🌾 There are {harvestable_count} crops to be harvested')
    input('> 🌽 Press any key to harvest all...')

    print('-' * 80)

    crop_quantity = farm.harvest()

    for crop_name in crop_quantity:
        seed_name = crop_name + ' Seed'
        if crop_quantity[crop_name] > 0: print(f'> {seeds.list[seed_name]['icon']} You harvested {crop_quantity[crop_name]} {crop_name}')
    
    print('-' * 80)
# === End of Farm Harvest Menu ===

# === Start of Barn Menu ===
def barn_menu():
    print('-' * 80)
    print(f'{'🐮🐔 Barn 🐔🐮':^80}')
    print('-' * 80)

    print('1. Chicken Barn 🐔')
    print('2. Cow Barn 🐮')
    print('3. Back to Main Menu 👈')

    print('-' * 80)

    choice = input('> Enter menu number: ')

    if choice not in ['1', '2', '3']:
        print('> ❗ Invalid option!\n')
        return
    
    if choice in ['1', '2']: cls()
    
    if choice == '1': chicken_barn_menu()
    elif choice == '2': cow_barn_menu()
    else:
        print('-' * 80)
        return
# === End of Barn Menu ===

# === Start of Chicken Barn Menu ===
def chicken_barn_menu():
    print('-' * 80)
    print(f'{'🐔 Chicken Barn 🐔':^80}')
    print('-' * 80)

    chicken_barn.show_animals()

    if len(chicken_barn.animals) == 0: return

    print('1. Feed Chicken 🍚')
    print('2. Collect Egg 🥚')
    print('3. Make Chicken Feed 🫘')
    print('4. Go back to Main Menu 👈')

    print('-' * 80)

    valid = False

    while valid is False:
        choice = input('> Enter menu number: ')
        try:
            if choice not in ['1', '2', '3', '4']:
                raise ValueError('> ❗ Invalid option!')
            valid = True
        except ValueError as e:
            print(str(e))
    
    if choice == '1':

        print('-' * 80)
        print(f'> 🫘 You have {inventory.list['Chicken Feed']['quantity']} Chicken Feed.')
        print('-' * 80)

        valid = False

        while valid == False:
            choice = input('> 🍚 Do you want to feed all the chicken(s)? (y/n): ').lower()
            try:
                if choice == '': raise ValueError('> ❗ Choice may not be empty!')
                if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!')
                valid = True
            except ValueError as e:
                print(str(e))
        
        if choice == 'y':

            if inventory.list['Chicken Feed']['quantity'] < len(chicken_barn.animals):
                print("> ❌ You don't have enough Chicken Feed to feed all the chicken(s)...")
                print('-' * 80)
                return
            
            chicken_barn.feed_animals()
            inventory.list['Chicken Feed']['quantity'] -= len(chicken_barn.animals)
            print('> 🍚 You fed all the chicken(s)!')
            print('-' * 80)
            return
        
        elif choice == 'n':

            valid = False

            while valid == False:
                numbers = list(map(str, input('> 🍚 Enter the number code of the chicken(s) that you want to feed (ex. 1 2 5): ').split()))
                try:
                    for number in numbers:
                        if not number.isnumeric(): raise ValueError('> ❗ Number code must be a number!')
                        number = int(number)
                        if number < 1 or number > len(chicken_barn.animals): raise ValueError('> ❗ There is invalid number code!')
                    valid = True
                except ValueError as e:
                    print(str(e))
            
            if inventory.list['Chicken Feed']['quantity'] < len(numbers):
                print("> ❌ You don't have enough Chicken Feed to feed all the chicken(s)...")
                print('-' * 80)
                return
            
            numbers = list(map(int, numbers))

            chicken_barn.feed_some(numbers)
            inventory.list['Chicken Feed']['quantity'] -= len(numbers)

            print('> 🍚 You fed the chicken(s)!')
            print('-' * 80)
            return

    elif choice == '2':

        egg = chicken_barn.collect_egg()
        print('-' * 80)
        if egg == 0: print('> 🥚 There are no eggs that are ready to be collected...')
        else: print(f'> 🥚 You collected {egg} Egg!')
        print('-' * 80)

    elif choice == '3':

        print('-' * 80)
        print('> 1 🌽 -> 3 🫘')
        
        if inventory.list['Corn']['quantity'] == 0:
            print("> ❌ You don't have enough Corn to make Chicken Feed...")
            print('-' * 80)
            return
        
        print(f'> 🌽 You have {inventory.list["Corn"]["quantity"]} Corn.\n')

        valid = False

        while valid == False:
            quantity = input('> 🌽 How many Corn do you want to use? ')
            try:
                if quantity == '': raise ValueError('> ❗ Quantity may not be empty!')
                if not quantity.isnumeric(): raise ValueError('> ❗ Quantity must be a number!')
                quantity = int(quantity)
                if quantity < 1: raise ValueError('> ❗ Quantity must be at least 1!')
                if quantity > inventory.list['Corn']['quantity']: raise ValueError("> ❗ You don't have enough Corn!")               
                valid = True           
            except ValueError as e:
                print(str(e))
        
        inventory.list['Corn']['quantity'] -= quantity
        inventory.list['Chicken Feed']['quantity'] += quantity * 3

        print('-' * 80)
        print(f'> 🫘 You made {quantity * 3} Chicken Feed!')
        print('-' * 80)

    else:
        print('-' * 80)
        return
# === End of Chicken Barn Menu ===

# === Start of Cow Barn Menu ===
def cow_barn_menu():
    print('-' * 80)
    print(f'{'🐮 Cow Barn 🐮':^80}')
    print('-' * 80)

    cow_barn.show_animals()

    if len(cow_barn.animals) == 0: return

    print('1. Feed Cow 🌾')
    print('2. Collect Milk 🥛')
    print('3. Go back to Main Menu 👈')

    print('-' * 80)

    valid = False

    while valid is False:
        choice = input('> Enter menu number: ')
        try:
            if choice not in ['1', '2', '3']:
                raise ValueError('> ❗ Invalid option!')
            valid = True
        except ValueError as e:
            print(str(e))
    
    if choice == '1':

        print('-' * 80)
        print(f'> 🌾 You have {inventory.list['Cow Feed']['quantity']} Cow Feed.')
        print('-' * 80)

        valid = False

        while valid == False:
            choice = input('> 🍚 Do you want to feed all the cows? (y/n): ').lower()
            try:
                if choice == '': raise ValueError('> ❗ Choice may not be empty!')
                if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!')
                valid = True
            except ValueError as e:
                print(str(e))
        
        if choice == 'y':

            if inventory.list['Cow Feed']['quantity'] < len(cow_barn.animals):
                print("> ❌ You don't have enough Cow Feed to feed all the cows...")
                print('-' * 80)
                return
            
            cow_barn.feed_animals()
            inventory.list['Cow Feed']['quantity'] -= len(cow_barn.animals)
            print('> 🍚 You fed all the cows!')
            print('-' * 80)
            return
        
        elif choice == 'n':

            valid = False

            while valid == False:
                numbers = list(map(str, input('> 🍚 Enter the number code of the cow(s) that you want to feed (ex. 1 2 5): ').split()))
                try:
                    for number in numbers:
                        if not number.isnumeric(): raise ValueError('> ❗ Number code must be a number!')
                        number = int(number)
                        if number < 1 or number > len(cow_barn.animals): raise ValueError('> ❗ There is invalid number code!')
                    valid = True
                except ValueError as e:
                    print(str(e))
            
            if inventory.list['Cow Feed']['quantity'] < len(numbers):
                print("> ❌ You don't have enough Cow Feed to feed all the cows...")
                print('-' * 80)
                return
            
            numbers = list(map(int, numbers))

            cow_barn.feed_some(numbers)
            inventory.list['Cow Feed']['quantity'] -= len(numbers)

            print('> 🍚 You fed the cows!')
            print('-' * 80)
            return

    elif choice == '2':

        milk = cow_barn.collect_milk()
        print('-' * 80)
        if milk == 0: print('> 🥛 There are no milk that are ready to be collected...')
        else: print(f'> 🥛 You collected {milk} milk!')
        print('-' * 80)

    else:
        print('-' * 80)
        return
# === End of Cow Barn Menu ===

# === Start of Buy Animal Menu ===
def buy_animal(animal):
    print('-' * 80)

    if animal == 'Chicken': icon = '🐔'
    elif animal == 'Cow': icon = '🐮'

    print(f'> {icon}')

    valid = False

    while valid == False:
        name = input(f'> Enter name for {animal}: ')

        try:
            if name == '': raise ValueError('> ❗ Name may not be empty!')

            space = 0
            
            for character in name:
                if character not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ': raise ValueError('> ❗ Invalid name!')
                if character == ' ': space += 1

            if space == len(name): raise ValueError('> ❗ Invalid name!')

            valid = True

        except ValueError as e:
            print(str(e))
    
    if animal == 'Chicken':
        chicken_barn.add_animal(Chicken(name))
    elif animal == 'Cow':
        cow_barn.add_animal(Cow(name))
# === End of Buy Animal Menu ===

# === Start of End Day Function ===
def end_day():
    print(f'\n> 🌙 End of Day {stats.day}')
    stats.next_day()
    print(f'> 🌞 Start of Day {stats.day}')
    print('-' * 80)

    farm.update_field()

    stats.check_progress()

    dead_chicken = chicken_barn.update_status()
    if dead_chicken > 0:
        print(f'> 🐔 Oh, no! {dead_chicken} chicken(s) died today. Remember to feed your animals!')
        print('-' * 80)
    
    dead_cow = cow_barn.update_status()
    if dead_cow > 0:
        print(f'> 🐄 Oh, no! {dead_cow} cow(s) died today. Remember to feed your animals!')
        print('-' * 80)
# === End of End Day Function ===

# === Start of Market Menu ===
def market_menu():
    print('-' * 80)
    print(f'{'🏪 Market 🏪':^80}')
    print('-' * 80)

    print('> 1. Buy 🌽')
    print('> 2. Sell 🪙')
    print('> 3. Back to Main Menu 👈')

    print('-' * 80)

    valid = False

    while valid is False:
        choice = input('> Enter menu number: ')
        try:
            if choice not in ['1', '2', '3']:
                raise ValueError('> ❗ Invalid option!')
            valid = True
        except ValueError as e:
            print(str(e))
        
    if choice in ['1', '2']: cls()
        
    if choice == '1': market_buy_menu()
    elif choice == '2': market_sell_menu()
    else:
        print('-' * 80)
        return
# === End of Market Menu ===

# === Start of Market Buy Menu ===
def market_buy_menu():
    itemCount = market.buy.show_items()

    valid = False

    while valid is False:
        choice = input('> Enter item code that you want to buy: ')

        try:
            if choice == '': raise ValueError('> ❗ Item code may not be empty!')
            if not choice.isnumeric(): raise ValueError('> ❗ Item code must be a number!')

            choice = int(choice)

            if choice < 1 or choice > itemCount + 1: raise ValueError('> ❗ Invalid item code!')

            valid = True

        except ValueError as e:
            print(str(e))
    
    if choice == itemCount + 1:
        print('-' * 80)
        return
    
    valid = False

    while valid is False:
        quantity = input('> Enter quantity: ')

        try:
            if quantity == '': raise ValueError('> ❗ Quantity may not be empty!')    
            if not quantity.isnumeric(): raise ValueError('> ❗ Quantity must be a number!')

            quantity = int(quantity)
            if quantity < 1: raise ValueError('> ❗ Quantity must be at least 1!')

            valid = True

        except ValueError as e:
            print(str(e))

    market.buy.get_item(choice, quantity)
# === End of Market Buy Menu ===

# === Start of Market Sell Menu ===
def market_sell_menu():
    itemCount = market.sell.show_items()

    valid = False

    while valid is False:
        choice = input('> Enter item code that you want to sell: ')

        try:
            if choice == '': raise ValueError('> ❗ Item code may not be empty!')
            if not choice.isnumeric(): raise ValueError('> ❗ Item code must be a number!')

            choice = int(choice)

            if choice < 1 or choice > itemCount + 1: raise ValueError('> ❗ Invalid item code!')

            valid = True

        except ValueError as e:
            print(str(e))
    
    if choice == itemCount + 1:
        print('-' * 80)
        return
    
    valid = False

    while valid is False:
        quantity = input('> Enter quantity: ')

        try:
            if quantity == '': raise ValueError('> ❗ Quantity may not be empty!')    
            if not quantity.isnumeric(): raise ValueError('> ❗ Quantity must be a number!')

            quantity = int(quantity)
            if quantity < 1: raise ValueError('> ❗ Quantity must be at least 1!')

            valid = True

        except ValueError as e:
            print(str(e))
    
    market.sell.sell_item(choice, quantity)
# === End of Market Sell Menu ===

# === Start of Show Inventory Function ===
def show_inventory():
    print('-' * 80)
    print(f'{'📦 Inventory 📦':^80}')
    print('-' * 80)
    inventory.print_inventory()
    print('-' * 80)
# === End of Show Inventory Function ===

# === Start of Statistics Menu ===
def statistics():
    print('-' * 80)
    print(f'{'📊 Statistics 📊':^80}')
    print('-' * 80)
    
    print(f'> 📅 Day: {stats.day}')
    print(f'> 🪙 Coins: {inventory.list['Coin']['quantity']}')
    print()

    print('> 💰 Financial State:')
    print('-' * 80)
    for day in stats.financial:
        data = stats.financial[day]
        print(f'🌞 Day {day}')
        print(f'🟩 Profit: {data['Profit']}')
        print(f'🟥 Expense: {data['Expense']}')
        print('-' * 80)
# === End of Statistics Menu ===

if __name__ == '__main__':
    while True:
        cls()

        print('-' * 80)
        print(f'{'🌽 Welcome to PyFarm 🌽':^80}')
        print('-' * 80)
        print(f'Coins: {inventory.list['Coin']['quantity']} {inventory.list['Coin']['icon']}')
        print(f'Day: {stats.day}')
        print('-' * 80)

        print('> 1. Farm 🌽')
        print('> 2. Barn 🐮')
        print('> 3. End the Day (Go to Next Day) 🌙')
        print('> 4. Market 🏪')
        print('> 5. Inventory 📦')
        print('> 6. Statistic 📊')
        print('> 7. Exit ⛔')

        print('-' * 80)

        choice = input('> Enter menu number: ')

        if choice in ['1', '2', '4', '5', '6']: cls()

        if choice == '1':
            farm_menu()
        elif choice == '2':
            barn_menu()
        elif choice == '3':
            end_day()
        elif choice == '4':
            market_menu()
        elif choice == '5':
            show_inventory()
        elif choice == '6':
            statistics()
        elif choice == '7':
            print('> Thank you for playing 🎉\n')
            break
        else:
            print('> ❗ Invalid option!')
        
        input('> Press any key to continue...')