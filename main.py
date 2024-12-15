import os

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

# === Start of UserStats Class ===
class UserStats:
    def __init__(self):
        self.day = 1
    
    def next_day(self):
        self.day += 1
    
    def check_progress(self):
        if self.day == 4:
            for seed in seeds.list:
                if seed['name'] == 'Potato':
                    seed['unlocked'] = True
                    seed['quantity'] = 5
            
            inventory.list['potato_seed']['quantity'] = 5

            print('> 🥳 Congratulations! You have reached Day 4.')
            print('> 🌱 Potato Seed is now unlocked. You received 5 potato seeds.')
            return
# === End of UserStats Class ===

# === Start of Inventory Class ===
class Inventory:
    def __init__(self):
        self.list = {
            'coin': {
                'quantity': 1000,
                'icon': '🪙',
                'name': 'Coin',
                'type': 'currency'
            },
            'corn_seed': {
                'quantity': 5,
                'icon': '🌽',
                'name': 'Corn Seed',
                'type': 'seed'
            },
            'corn': {
                'quantity': 0,
                'icon': '🌽',
                'name': 'Corn',
                'type': 'crop'
            },
            'potato_seed': {
                'quantity': 0,
                'icon': '🥔',
                'name': 'Potato Seed',
                'type': 'seed'
            },
            'potato': {
                'quantity': 0,
                'icon': '🥔',
                'name': 'Potato',
                'type': 'crop'
            },
            'tomato_seed': {
                'quantity': 0,
                'icon': '🍅',
                'name': 'Tomato Seed',
                'type': 'seed'
            },
            'tomato': {
                'quantity': 0,
                'icon': '🍅',
                'name': 'Tomato',
                'type': 'crop'
            },
            'carrot_seed': {
                'quantity': 0,
                'icon': '🥕',
                'name': 'Carrot Seed',
                'type': 'seed'
            },
            'carrot': {
                'quantity': 0,
                'icon': '🥕',
                'name': 'Carrot',
                'type': 'crop'
            },
            'egg': {
                'quantity': 0,
                'icon': '🥚',
                'name': 'Egg',
                'type': 'product'
            }
        }

    def print_inventory(self):
        for key in self.list:
            item = self.list[key]
            if item['quantity'] > 0: print(f'> {item['icon']} {item['name']}: {item['quantity']}')
# === End of Inventory Class ===

# === Start of Farm Class ===
class Farm:
    def __init__(self):
        self.size = 3
        self.field = [['No seed' for _ in range(self.size)] for _ in range(self.size)]
        self.field_detail = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.field_day = [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def update_field(self):
        seeds = Seeds()
        for row in range(self.size):
            for col in range(self.size):
                if self.field_detail[row][col] != 0:
                    self.field_day[row][col] += 1
                if self.field_day[row][col] == seeds.list[self.field_detail[row][col] - 1]['grow_time']:
                    self.field[row][col] = seeds.list[self.field_detail[row][col] - 1]['icon']
    
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
    
    def plant_seed(self, row, col, seed_code, seed_name):
        if self.field_detail[row][col] == 0:
            self.field_detail[row][col] = seed_code
            self.field[row][col] = '🌱'
            print(f'> 🌱 {seed_name} seed planted successfully!')
            return True
        
        print('> 🌱 There is already a seed in this field.')
        return False
    
    def harvest(self):
        crops = {
            'corn': 0,
            'potato': 0,
            'tomato': 0,
            'carrot': 0
        }

        for seed in seeds.list:
            for row in range(self.size):
                for col in range(self.size):
                    if self.field_detail[row][col] == seed['code'] and self.field_day[row][col] == seed['grow_time']:
                        self.field[row][col] = 'No seed'
                        self.field_detail[row][col] = 0
                        self.field_day[row][col] = 0
                        crops[seed['name'].lower()] += 1
                        inventory.list[seed['name'].lower()]['quantity'] += 1
        
        return crops
# === End of Farm Class ===

# === Start of Seeds Class ===
class Seeds:
    def __init__(self):
        self.list = [
            {
                'code': 1,
                'name': 'Corn',
                'icon': '🌽',
                'grow_time': 3,
                'quantity': 5,
                'unlocked': True 
            },
            {
                'code': 2,
                'name': 'Potato',
                'icon': '🥔',
                'grow_time': 4,
                'quantity': 0,
                'unlocked': False
            },
            {
                'code': 3,
                'name': 'Tomato',
                'icon': '🍅',
                'grow_time': 4,
                'quantity': 0,
                'unlocked': False
            },
            {
                'code': 4,
                'name': 'Carrot',
                'icon': '🥕',
                'grow_time': 3,
                'quantity': 0,
                'unlocked': False
            }
        ]

    
    def count(self):
        count = 0
        for seed in self.list:
            if seed['unlocked'] == True: count += 1
        return count
    
    def print_seeds_list(self):
        print('> 🌱 List of unlocked seed(s):')
        print('-' * 80)

        count = 0
        for seed in self.list:
            if seed['unlocked'] == False: continue
            count += 1
            print(f'> {count}. {seed['icon']} {seed['name']}: {seed['quantity']} seed(s) left.')
        
        print()
# === End of Seeds Class ===

# User Instances
stats = UserStats()
inventory = Inventory()

# Farm Instances
farm = Farm()
seeds = Seeds()

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
    for seed in seeds.list:
        if seed['unlocked'] == True: seed_count += seed['quantity']
    
    if seed_count == 0:
        print('> 🌱 There are no seeds left to be planted. You can buy them at the market.')
        print('-' * 80)
        return

    valid = False
    while valid is False:
        choice = input('> ❓ Do you want to plant any seed? (y/n): ').lower()
        try:
            if choice == '': raise ValueError('> ❗ Choice may not be empty!\n')
            if choice not in ['y', 'n']: raise ValueError('> ❗ Invalid option!\n')
            valid = True
        except ValueError as e:
            print(str(e))
    
    print()

    if choice == 'n': return

    valid = False
    while valid is False:
        seed_code = input('> 🌱 Enter seed code number: ')
        try:
            if seed_code == '': raise ValueError('> ❗ Seed code may not be empty!\n')
            if not seed_code.isnumeric(): raise ValueError('> ❗ Seed code must be a number!\n')
            if int(seed_code) < 1 or int(seed_code) > seeds.count(): raise ValueError('> ❗ Invalid seed code!\n')
            if seeds.list[int(seed_code) - 1]['quantity'] == 0: raise ValueError(f'> ❗ There are no {seeds.list[int(seed_code) - 1]['name']} seeds left to be planted. You can buy them at the market.\n')
            seed_code = int(seed_code)
            valid = True
        except ValueError as e:
            print(str(e))
    
    print()

    valid = False
    while valid is False:
        row = input('> 🌱 Enter row number: ')
        try:
            if row == '': raise ValueError('> ❗ Row number may not be empty!\n')
            if not row.isnumeric(): raise ValueError('> ❗ Row number must be a number!\n')
            if int(row) < 1 or int(row) > farm.size: raise ValueError('> ❗ Invalid row number!\n')
            row = int(row) - 1
            valid = True
        except ValueError as e:
            print(str(e))
        
    print()

    valid = False
    while valid is False:
        col = input('> 🌱 Enter column number: ')
        try:
            if col == '': raise ValueError('> ❗ Column number may not be empty!\n')
            if not col.isnumeric(): raise ValueError('> ❗ Column number must be a number!\n')
            if int(col) < 1 or int(col) > farm.size: raise ValueError('> ❗ Invalid column number!\n')
            col = int(col) - 1
            valid = True
        except ValueError as e:
            print(str(e))
        
    print()

    valid = farm.plant_seed(row, col, seed_code, seeds.list[seed_code - 1]['name'])
    print('-' * 80)

    if valid:
        seeds.list[seed_code - 1]['quantity'] -= 1
        inventory.list[seeds.list[seed_code - 1]['name'].lower() + '_seed']['quantity'] -= 1
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
            if farm.field_day[row][col] >= seeds.list[farm.field_detail[row][col] - 1]['grow_time']:
                harvestable_count += 1
    
    if harvestable_count == 0:
        print('> 🌾 There are no crops to be harvested\n')
        print('-' * 80)
        return
    
    print(f'> 🌾 There are {harvestable_count} crops to be harvested')
    input('> 🌽 Press any key to harvest all...')

    print('-' * 80)

    crop_quantity = farm.harvest()
    index = 0

    for crop_name in crop_quantity:
        if crop_quantity[crop_name] > 0:
            print(f'> {seeds.list[index]['icon']} You harvested {crop_quantity[crop_name]} {crop_name}')
        index += 1
    
    print('-' * 80)
# === End of Farm Harvest Menu ===

# === Start of End Day Function ===
def end_day():
    print(f'\n> 🌙 End of Day {stats.day}')
    stats.next_day()
    print(f'> 🌞 Start of Day {stats.day}')
    farm.update_field()
    stats.check_progress()
    print('-' * 80)
# === End of End Day Function ===

# === Start of Show Inventory Function ===
def show_inventory():
    print('-' * 80)
    print(f'{'📦 Inventory 📦':^80}')
    print('-' * 80)
    inventory.print_inventory()
    print('-' * 80)
# === End of Show Inventory Function ===

while True:
    cls()

    print('-' * 80)
    print(f'{'🌽 Welcome to PyFarm 🌽':^80}')
    print('-' * 80)

    print(f'Coins: {inventory.list['coin']['quantity']} {inventory.list['coin']['icon']}')
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
    elif choice == '3':
        end_day()
    elif choice == '5':
        show_inventory()
    elif choice == '7':
        print('> Thank you for playing 🎉\n')
        break
    else:
        print('Invalid option!')
    
    input('> Press any key to continue...')