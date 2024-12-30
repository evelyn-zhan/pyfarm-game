# import pytest
from main import *

def test_harvest(): # Passed
    farm = Farm()
    harvested = farm.harvest()
    assert harvested == {
            'Corn': 0,
            'Potato': 0,
            'Tomato': 0,
            'Carrot': 0
        }
    
def test_plant_seed_1(): # Passed
    farm = Farm()
    possible_to_plant = farm.plant_seed(0, 0, 'Corn Seed')
    assert possible_to_plant == True
    
    possible_to_plant = farm.plant_seed(0, 0, 'Potato Seed')
    assert possible_to_plant == False

def test_plant_seed_2(): # Passed
    farm = Farm()
    possible_to_plant = farm.plant_seed(0, 0, 'Corn Seed')
    assert possible_to_plant == True
    
    possible_to_plant = farm.plant_seed(1, 1, 'Potato Seed')
    assert possible_to_plant == True

def test_plant_seed_3(): # Passed
    farm = Farm()
    farm.plant_seed(0, 0, 'Corn Seed')
    assert farm.field_detail[0][0] == 'Corn Seed'

def test_unlocked_seeds(): # Passed
    inventory = Inventory()
    user = UserStats()
    market_items = MarketItems()

    user.day = 4
    user.check_progress()

    assert seeds.list['Potato Seed']['unlocked'] == True
    # assert inventory.list['Potato Seed']['quantity'] == 5
    # assert market_items.list['Potato Seed']['unlocked'] == True