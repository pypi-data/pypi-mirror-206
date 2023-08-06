import battlesimulation
from battlesimulation import debug_print, Building, BuildingArray, Planet, Rocket

battlesimulation._debug_printing = True

test_building = Building(10, 30)
debug_print(f"test_building: {test_building}")
debug_print(f"test_building filtered_str: {test_building.filtered_str}")

test_array = BuildingArray()
debug_print(f"\nsetting whole array result: {test_array.set_whole_array([[1,3],[2,3],[2,3],[2,3],[3,3],[4,3],[5,3],[5,3],[5,3],[6,3],[6,3],[6,3],[6,3],[6,3],[7,3],[8,3],[9,3],[10,3]])}")
#length 18
debug_print(f"\ntest_array:\n{test_array}")
debug_print(f"test_array filtered_str:\n{test_array.filtered_str}")

debug_print(f"\nadd CC should be False: {test_array.set_item_of_array([1,3])}")
debug_print(f"add Cosmodrome: {test_array.set_item_of_array([5,3])}")
debug_print(f"add Cosmodrome: {test_array.set_item_of_array([5,3])}")
debug_print(f"add Cosmodrome: {test_array.set_item_of_array([5,3])}")
debug_print(f"add Cosmodrome: {test_array.set_item_of_array([5,3])}")
debug_print(f"add Cosmodrome: {test_array.set_item_of_array([5,3])}")
debug_print(f"add Cosmodrome: {test_array.set_item_of_array([5,3])}")
debug_print(f"total buildings: {len(test_array)}")
#length 24
debug_print(f"add Cosmodrome should be False: {test_array.set_item_of_array([5,3])}")
delete_keys = set()
total = 4
for key in test_array._array:
    if test_array._array[key].id == 5 and total > 0:
        delete_keys.add(key)
        total -= 1
for key in delete_keys:
    test_array._array.pop(key)
#length 20
debug_print(f"add Warehouse: {test_array.set_item_of_array([3,3])}")
debug_print(f"add Turret: {test_array.set_item_of_array([9,3])}")
debug_print(f"add Turret: {test_array.set_item_of_array([9,3])}")
debug_print(f"add Turret: {test_array.set_item_of_array([9,3])}")
debug_print(f"add Turret: {test_array.set_item_of_array([9,3])}")
#length 25
debug_print(f"add Warehouse should be False: {test_array.set_item_of_array([3,3])}")
debug_print(f"add Mine should be False: {test_array.set_item_of_array([3,3])}")
debug_print(f"add Mine should be False: {test_array.set_item_of_array([3,3])}")
#length 25
debug_print(f"\ntest_array filtered_str:\n{test_array.filtered_str}")
debug_print(f"\npretty:\n{test_array.filtered_pretty_str}")

debug_print("\n\nPlanet:\n")

test_planet = Planet()
test_planet.set_planet_type_and_size(7, 2)
test_planet.set_buildings([*test_array])
rocket_1 = Rocket(1, 100)
rocket_2 = Rocket(2, 150)
rocket_3 = Rocket(3, 200)
rocket_4 = Rocket(4, 300)
test_planet.set_rockets((rocket_1, rocket_2, rocket_3, rocket_4))
debug_print(f"\n{test_planet}")
debug_print(f"\n{test_planet.buildings.filtered_pretty_str}")
debug_print(f"\nTurrets level: {test_planet.turrets_lvl}")
debug_print("\n\n")
debug_print(f"\n{test_planet.filtered_str_full}")