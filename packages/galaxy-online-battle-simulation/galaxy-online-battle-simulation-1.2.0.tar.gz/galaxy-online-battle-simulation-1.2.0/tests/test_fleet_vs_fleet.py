import battlesimulation
from battlesimulation import Planet, SpaceFleet, BattleSimulation

battlesimulation._debug_printing = True
bs = BattleSimulation()

# first test empty SpaceFleets
fleet1_raw = ((5, 0), (3, 0), (7, 0))
fleet2_raw = ((5, 10000), (7, 5000))
# fleet2_raw = ((5,100),)
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
print(planet)
fleet1.set_fleet(fleet1_raw)
fleet2.set_fleet(fleet2_raw)
fleet1.attacking = True
fleet2.attacking = False
# fleet1.set_acc_type("max")
# fleet2.set_acc_type("max")
# fleet1.set_module_params(1.3,0.0,0.0)
# fleet2.set_module_params(0.0,1.25,0.0)
# fleet1.set_module_attack_damage_mods([(1,1.6)])
# fleet1.set_module_defense_damage_mods([(1,-6000)])
print(fleet1.modules)
print(f"{fleet1.filtered_str}")
print(f"{fleet2.filtered_str}")
bs.simulate(fleet1, fleet2, planet)

# first test empty SpaceFleets
print("\n\n")
fleet1_raw = ((5, 1300), (3, 800), (7, 5000))
fleet2_raw = ((5, 0), (7, 0))
# fleet2_raw = ((5,100),)
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
print(planet)
fleet1.set_fleet(fleet1_raw)
fleet2.set_fleet(fleet2_raw)
fleet1.attacking = True
fleet2.attacking = False
# fleet1.set_acc_type("max")
# fleet2.set_acc_type("max")
# fleet1.set_module_params(1.3,0.0,0.0)
# fleet2.set_module_params(0.0,1.25,0.0)
# fleet1.set_module_attack_damage_mods([(1,1.6)])
# fleet1.set_module_defense_damage_mods([(1,-6000)])
print(fleet1.modules)
print(f"{fleet1.filtered_str}")
print(f"{fleet2.filtered_str}")
bs.simulate(fleet1, fleet2, planet)

# and then two normal SpaceFleets
print("\n\n")
fleet1_raw = ((5, 1300), (3, 800), (7, 5000))
fleet2_raw = ((5, 10000), (7, 5000))
# fleet2_raw = ((5,100),)
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
planet.set_rockets(((2, 10), (3, 10)))
print(planet.filtered_str_full)
fleet1.set_fleet(fleet1_raw)
fleet2.set_fleet(fleet2_raw)
fleet1.attacking = True
fleet2.attacking = False
# fleet1.set_acc_type("max")
# fleet2.set_acc_type("max")
fleet1.set_acc_type("min")
fleet2.set_acc_type("min")
# fleet1.set_module_params(1.3,0.0,0.0)
# fleet2.set_module_params(0.0,1.25,0.0)
# fleet1.set_module_attack_damage_mods([(1,1.6)])
# fleet1.set_module_defense_damage_mods([(1,-6000)])
print(fleet1.modules)
print(f"{fleet1.filtered_str}")
print(f"{fleet2.filtered_str}")
bs.simulate(fleet1, fleet2, planet)  # , True)

# CBT Rift 2
print("\n\n")
fleet1_raw = ((3, 416666), (5, 1250000))
# fleet1_raw = ((3, 363980), (5, 1074490))
# fleet2_raw = ((6, 469), (9, 294))
# fleet2_raw = ((6, 858),)
# fleet2_raw = ((3, 778), (4, 1296),)
fleet2_raw = ((3, 0), (4, 2219), (5, 0))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
print(planet.filtered_str_full)
fleet1.set_fleet(fleet1_raw)
fleet2.set_fleet(fleet2_raw)
fleet1.attacking = False
fleet2.attacking = True
# fleet1.set_acc_type("max")
# fleet2.set_acc_type("max")
fleet1.set_acc_type("min")
fleet2.set_acc_type("min")
# for i in range(1, 6):
#    fleet1._array[3].defenses[i] = fleet1._array[3].defenses[i] * 0.5
#    fleet1._array[5].defenses[i] = fleet1._array[5].defenses[i] * 0.5
# print(fleet1._array[3].defenses)
# print(fleet1._array[5].defenses)
# input("test?")
#fleet1.set_module_params(1.0, 1.5, 0.0)
fleet1.modules.elder_buff_defense()
# fleet2.set_module_params(0.0,1.25,0.0)
# fleet1.set_module_attack_damage_mods([(1,1.6)])
fleet1.set_module_defense_damage_mods([(1, 4688), (3, 4814), (4, 2677)])
print(fleet1.modules)
print(f"{fleet1.filtered_str}")
print(f"{fleet2.filtered_str}")
bs.simulate(fleet1, fleet2, planet)
