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
        pass

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