import battlesimulation
from battlesimulation import debug_print

_data = {
    "Types": {
        "Damage": (1,2,3,4,5,6),                        # ids
        "Spaceship": (1,2,3,4,5,6,7,8,9),             # ids
        "Rocket": (1,2,3,4),                          # ids
        "Planet_type": (1,2,3,4,5,6,7,9,12,15),       # 1:7 - ordinary planets, 9,12,15(?) Space Stations [Resource, Production, Trade]
        "Planet_size": (0,1,2),                       # Mines: 0 -> 3 mines, 1 -> 4 mines, 2 -> 5 mines
        "Attack_type": (1,2,3),                       # for rockets: 1 - blockade, 2 - attack, 3 - both
        "Building": (1,2,3,4,5,6,7,8,9,10),           # ids
        "Module": (1,2,3,4,5,6,7,8,9,10),
        "Valid_targets" : (1,3,4,5,6,7,8,9)              # default valid targets for rockets, that have no valid targets specified
    },                                                  # Loki spaceships are not targeted by rockets at all
    "Spaceships": {
        1: {
            "id": 1,
            "name": "Геркулес",
            "name_en": "Hermes",
            "damage_type_id": 6,
            "attack": 250,
            "defense": 275,
            "defenses": { 1: 330, 2: 275, 3: 220, 4: 248, 5: 303, 6: 100 },
            "weight": 10,
            "attack_priority": 250,
            "defense_priority": 250,
            "speed": 5,
            "calc_speed": 2.56,
            "price": 500,
            "build_time": 300,
            "cargohold": 100,
            "radar": 0,
            "accuracy": 80
        },
        2: {
            "id": 2,
            "name": "Локи",
            "name_en": "Lokomotion",
            "damage_type_id": 3,
            "attack": 20,
            "defense": 20,
            "defenses": { 1: 22, 2: 24, 3: 20, 4: 16, 5: 18, 6: 100 },
            "weight": 1,
            "attack_priority": 250,
            "defense_priority": 100,
            "speed": 10,
            "calc_speed": 5.12,
            "price": 300,
            "build_time": 120,
            "cargohold": 0,
            "radar": 25,
            "accuracy": 80
        },
        3: {
            "id": 3,
            "name": "Раптор",
            "name_en": "Raptor",
            "damage_type_id": 3,
            "attack": 150,
            "defense": 150,
            "defenses": { 1: 180, 2: 210, 3: 150, 4: 90, 5: 120, 6: 100 },
            "weight": 6,
            "attack_priority": 1000,
            "defense_priority": 3000,
            "speed": 6,
            "calc_speed": 3.072,
            "price": 1500,
            "build_time": 720,
            "cargohold": 20,
            "radar": 0,
            "accuracy": 80
        },
        4: {
            "id": 4,
            "name": "Хорнет",
            "name_en": "Hornet",
            "damage_type_id": 2,
            "attack": 110,
            "defense": 90,
            "defenses": { 1: 126, 2: 90, 3: 54, 4: 72, 5: 108, 6: 100 },
            "weight": 4,
            "attack_priority": 1000,
            "defense_priority": 3000,
            "speed": 7,
            "calc_speed": 3.584,
            "price": 1000,
            "build_time": 528,
            "cargohold": 10,
            "radar": 0,
            "accuracy": 80
        },
        5: {
            "id": 5,
            "name": "Джавелин",
            "name_en": "Javelin",
            "damage_type_id": 1,
            "attack": 45,
            "defense": 55,
            "defenses": { 1: 55, 2: 33, 3: 44, 4: 66, 5: 77, 6: 100 },
            "weight": 2,
            "attack_priority": 1000,
            "defense_priority": 3000,
            "speed": 8,
            "calc_speed": 4.096,
            "price": 500,
            "build_time": 264,
            "cargohold": 20,
            "radar": 0,
            "accuracy": 80
        },
        6: {
            "id": 6,
            "name": "Экскалибр",
            "name_en": "Excalibur",
            "damage_type_id": 4,
            "attack": 225,
            "defense": 275,
            "defenses": { 1: 220, 2: 330, 3: 385, 4: 275, 5: 165, 6: 100 },
            "weight": 10,
            "attack_priority": 1000,
            "defense_priority": 3000,
            "speed": 5,
            "calc_speed": 2.56,
            "price": 2750,
            "build_time": 1200,
            "cargohold": 10,
            "radar": 0,
            "accuracy": 80
        },
        7: {
            "id": 7,
            "name": "Валькирия",
            "name_en": "Valkirie",
            "damage_type_id": 4,
            "attack": 50,
            "defense": 100,
            "defenses": { 1: 90, 2: 110, 3: 120, 4: 100, 5: 80, 6: 100 },
            "weight": 8,
            "attack_priority": 5000,
            "defense_priority": 250,
            "speed": 3,
            "calc_speed": 1.536,
            "price": 5000,
            "build_time": 2400,
            "cargohold": 10,
            "radar": 0,
            "accuracy": 80
        },
        8: {
            "id": 8,
            "name": "Титан",
            "name_en": "Titan",
            "damage_type_id": 5,
            "attack": 100,
            "defense": 900,
            "defenses": { 1: 720, 2: 810, 3: 990, 4: 1080, 5: 900, 6: 100 },
            "weight": 100,
            "attack_priority": 100,
            "defense_priority": 100,
            "speed": 3,
            "calc_speed": 1.536,
            "price": 32000,
            "build_time": 5400,
            "cargohold": 10,
            "radar": 0,
            "accuracy": 80
        },
        9: {
            "id": 9,
            "name": "Абаддон",
            "name_en": "Abaddon",
            "damage_type_id": 5,
            "attack": 440,
            "defense": 360,
            "defenses": { 1: 216, 2: 288, 3: 432, 4: 504, 5: 360, 6: 100 },
            "weight": 16,
            "attack_priority": 1000,
            "defense_priority": 3000,
            "speed": 4,
            "calc_speed": 2.048,
            "price": 4400,
            "build_time": 1800,
            "cargohold": 0,
            "radar": 0,
            "accuracy": 80
        }
    },
    "Damages": {
        1: { "id": 1, "name": "Плазма", "name_en": "Plasma" },
        2: { "id": 2, "name": "Лазер", "name_en": "Laser" },
        3: { "id": 3, "name": "Кинетика", "name_en": "Kinetic" },
        4: { "id": 4, "name": "Ракета", "name_en": "Rocket" },
        5: { "id": 5, "name": "Рельса", "name_en": "Rail" },
		6: { "id": 6, "name": "Аннигиляторная Пушка", "name_en": "Annihilator Cannon" }
    },
    "Planetary_coefs": {                                        # keys are "planet_id"+"planet_size"
        "10": 5.80, "11": 1.00, "12": 1.20,                     # Type 5 planet with 4 mines (planet_size=1)
        "20": 1.00, "21": 1.25, "22": 1.50,                     # key is "51" and value is 2.00
        "30": 1.20, "31": 1.50, "32": 1.80,
        "40": 1.40, "41": 1.75, "42": 2.10,
        "50": 1.60, "51": 2.00, "52": 2.40,
        "60": 2.00, "61": 2.50, "62": 3.00,
        "70": 2.40, "71": 3.00, "72": 3.60,
        "90": 3.00, "91": 3.00, "92": 3.00,
        "120": 3.00, "121": 3.00, "122": 3.00,
        "150": 3.00, "151": 3.00, "152": 3.00
    },
    "Rockets": {
        1: {"id":1,"name":"Sticks-XL","name_en":"Super InfraTimeSpaceContinuum","warheads":100,"damage":500,"price":100,"build_time":45,"damage_type_id":4,"attack_type":1},
        2: {"id":2,"name":"Кобра-М1","name_en":"Cobra-M1","warheads":1,"damage":150,"price":250,"build_time":90,"damage_type_id":4,"attack_type":2},
        3: {"id":3,"name":"Аврора","name_en":"Aurora","warheads":4,"damage":75,"price":600,"build_time":180,"damage_type_id":4,"attack_type":3},
        4: {"id":4,"name":"X-Ray","name_en":"X-Ray","warheads":1,"damage":100,"price":3000,"build_time":300,"damage_type_id":4,"attack_type":2,"valid_targets":(7,)}
    },
    "Buildings": {
        1: {"id":1,"name":"Командный центр","name_en":"Command Center","defense":700,"max_buildings":1},
        2: {"id":2,"name":"Шахта","name_en":"Mine","defense":500,"max_buildings":5},
        3: {"id":3,"name":"Склад","name_en":"Warehouse","defense":250,"max_buildings":21},
        4: {"id":4,"name":"Торговый центр","name_en":"Trade Office","defense":400,"max_buildings":1},
        5: {"id":5,"name":"Космопорт","name_en":"Сosmodrome","defense":450,"max_buildings":9},
        6: {"id":6,"name":"Завод космолётов","name_en":"Spacecraft Plant","defense":550,"max_buildings":5},
        7: {"id":7,"name":"Энергостанция","name_en":"Power Plant","defense":300,"max_buildings":1},
        8: {"id":8,"name":"Станция обнаружения","name_en":"Detection Station","defense":350,"max_buildings":1},
        9: {"id":9,"name":"Ракетная башня","name_en":"Missile Turret","defense":650,"max_buildings":20},
        10: {"id":10,"name":"Генератор щита","name_en":"Shield Generator Supreme","defense":75000,"max_buildings":1}
    },
    "Modules": {
        1: {"id":1,"name":"Дезинтегратор","name_en":"Disintegrator","attack":25,"defense":0,"speed":0,"price":10000,"solarium":1,"build_time":129},
        2: {"id":2,"name":"Форсажный Блок","name_en":"Afterburner Exhaust","attack":100,"defense":0,"speed":50,"price":7000,"solarium":1,"build_time":90},
        3: {"id":3,"name":"Усилитель Щита","name_en":"Shield Booster","attack":0,"defense":30,"speed":0,"price":13000,"solarium":1,"build_time":168},
        4: {"id":4,"name":"Комплекс Бастион","name_en":"Complex Bastion","attack":20,"defense":25,"speed":0,"price":23000,"solarium":1,"build_time":298},
        5: {"id":5,"name":"Комплекс Луч","name_en":"Complex Luch","attack":20,"defense":0,"speed":50,"price":17000,"solarium":1,"build_time":220},
        6: {"id":6,"name":"Комплекс Ореол","name_en":"Complex Halo","attack":0,"defense":25,"speed":50,"price":20000,"solarium":1,"build_time":259},
        7: {"id":7,"name":"Комплекс Страж","name_en":"Complex Guardian","attack":15,"defense":20,"speed":40,"price":30000,"solarium":1,"build_time":388},
        8: {"id":8,"name":"Спутник Соляриум","name_en":"Satellite Solarium","attack":0,"defense":0,"speed":0,"price":12000,"solarium":0,"build_time":155},
        9: {"id":9,"name":"Спутник Энергия","name_en":"Satellite Energy","attack":0,"defense":0,"speed":0,"price":10000,"solarium":0,"build_time":129},
        10: {"id":10,"name":"Комплекс Абордаж","name_en":"Complex Boarding","attack":0,"defense":0,"speed":0,"price":5000,"solarium":1,"build_time":64}
    },
    "Globals": {
        "turret_damage": 100,
        "turret_damage_type_id": 5,
        "shield_damage": 100,                                   #todo don't remember now
        "shield_damage_type_id": 2,
        "shield_max_coef": 0.5,
        "thold_per": 0.125,
        "thold_max": 1.5,
        "thold_max_bonus": 50,
        "threshold": 0.5,
        "accuracy": 80,
        "max_speed_bonus": 2.0,
        "max_building_level": 30
    }
}

battlesimulation._debug_printing = True

battlesimulation.load_global_game_parameters(_data)

debug_print(f"types_damage: {battlesimulation._GGP.types_damage}\n")
debug_print(f"types_spaceship: {battlesimulation._GGP.types_spaceship}\n")
debug_print(f"types_rocket: {battlesimulation._GGP.types_rocket}\n")
debug_print(f"types_planet_type: {battlesimulation._GGP.types_planet_type}\n")
debug_print(f"types_planet_size: {battlesimulation._GGP.types_planet_size}\n")
debug_print(f"types_attack: {battlesimulation._GGP.types_attack}\n")
debug_print(f"types_building: {battlesimulation._GGP.types_building}\n")
debug_print(f"spaceships: {battlesimulation._GGP.spaceships}\n")
debug_print(f"damages: {battlesimulation._GGP.damages}\n")
debug_print(f"planetary_coefs: {battlesimulation._GGP.planetary_coefs}\n")
debug_print(f"rockets: {battlesimulation._GGP.rockets}\n")
debug_print(f"buildings: {battlesimulation._GGP.buildings}\n")
debug_print(f"globals: {battlesimulation._GGP.globals}\n")
debug_print(f"thold_per: {battlesimulation._GGP.thold_per}\n")
debug_print(f"thold_max: {battlesimulation._GGP.thold_max}\n")
debug_print(f"thold_max_bonus: {battlesimulation._GGP.thold_max_bonus}\n")
debug_print(f"accuracy: {battlesimulation._GGP.accuracy}\n")
debug_print(f"threshhold: {battlesimulation._GGP.threshold}\n")

import json
#import ujson as json
#with open("/home/adminator/python/0_for_public/galaxy-online-battle-simulation/tests/data.json", "w", encoding="utf-8") as f:
#	json.dump(_data, f, indent=4)
with open("/home/adminator/python/0_for_public/galaxy-online-battle-simulation/tests/data.json", "r", encoding="utf-8") as f:
	loaded_data = json.load(f)
debug_print(f"New loaded from json:\n{loaded_data}")
battlesimulation.load_global_game_parameters(loaded_data)