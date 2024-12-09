import os
from field import Farm, Seeds
from inventory import Inventory

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

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

# User
stats = UserStats()
inventory = Inventory()

# Farm
farm = Farm()
seeds = Seeds()

def farm_menu():
    print('-' * 80)
    print(f'{'🌽 Farm 🌽':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80 + '\n')
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
        print()
        farm.print_field()
        print('-' * 80)

def farm_harvest_menu():
    print('-' * 80)
    print(f'{'🌾 Harvest 🌾':^80}')
    print('-' * 80 + '\n')

    farm.print_field()

    print('-' * 80 + '\n')

    harvestable_count = 0

    for row in range(farm.size):
        for col in range(farm.size):
            if farm.field_day[row][col] >= seeds.list[farm.field_detail[row][col] - 1]['grow_time']:
                harvestable_count += 1
    
    if harvestable_count == 0:
        print('> 🌾 There are no crops to be harvested\n')
        print('-' * 80)
        return
    
    print(f'> 🌾 There are {harvestable_count} crops to be harvested\n')
    input('> 🌽 Press any key to harvest all...')

    print('-' * 80)

    

def end_day():
    print(f'\n> 🌙 End of Day {stats.day}')
    stats.next_day()
    print(f'> 🌞 Start of Day {stats.day}')
    farm.update_field()
    stats.check_progress()
    print('-' * 80)

while True:
    cls()

    print('-' * 80)
    print(f'{'🌽 Welcome to PyFarm 🌽':^80}')
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
    elif choice == '7':
        print('> Thank you for playing 🎉\n')
        break
    else:
        print('Invalid option!')
    
    input('> Press any key to continue...')