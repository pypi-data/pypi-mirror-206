import battlesimulation
from battlesimulation import Rocket, Planet, SpaceFleet, BattleSimulation

battlesimulation._debug_printing = True
bs = BattleSimulation()
fleet1_raw = ((1,350),(2,350),(3,100),(4,100),(5,100),(6,100),(7,5000),(8,1000),(9,100))
fleet2_raw = ((5,10000),(7,5000))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
rocket_1 = Rocket(1, 100)
rocket_2 = Rocket(2, 150)
rocket_3 = Rocket(3, 200)
rocket_4 = Rocket(4, 300)
planet.set_rockets((rocket_1, rocket_2, rocket_3, rocket_4))
print(planet.rockets.filtered_str)
print(planet.filtered_str_full)
fleet1.set_fleet(fleet1_raw)
fleet1.attacking = True
#fleet1.set_acc_type("max")
#fleet1.set_module_params(1.3,0.0,0.0)
#fleet1.set_module_attack_damage_mods([(1,1.6)])
#fleet1.set_module_defense_damage_mods([(1,-6000)])
print(fleet1.modules)
print(f"{fleet1.filtered_str}")
bs.simulate(fleet1, fleet2, planet)




fleet1_raw = ((1,350),(2,350),(3,100),(4,100),(5,100),(6,100),(7,5000),(9,100))
fleet2_raw = ((5,10000),(7,5000))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
rocket_1 = Rocket(1, 100)
rocket_2 = Rocket(2, 150)
rocket_3 = Rocket(3, 200)
rocket_4 = Rocket(4, 300)
planet.set_rockets((rocket_1, rocket_2, rocket_3, rocket_4))
print(planet.rockets.filtered_str)
print(planet.filtered_str_full)
fleet1.set_fleet(fleet1_raw)
fleet1.attacking = True
#fleet1.set_acc_type("max")
#fleet1.set_module_params(1.3,0.0,0.0)
#fleet1.set_module_attack_damage_mods([(1,1.6)])
#fleet1.set_module_defense_damage_mods([(1,-6000)])
print(fleet1.modules)
print(f"{fleet1.filtered_str}")
bs.simulate(fleet1, fleet2, planet)





fleet1_raw = ((1,35),(2,35),(5,750))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
#rocket_1 = Rocket(1, 100)
rocket_2 = Rocket(2, 50)
#rocket_3 = Rocket(3, 200)
#rocket_4 = Rocket(4, 300)
planet.set_rockets((rocket_2,))
planet.set_simple_turrets_lvl(1)
planet.set_planet_type_and_size(5,0)
print(planet.rockets.filtered_str)
print(planet.filtered_str_full)
fleet1.set_fleet(fleet1_raw)
fleet1.attacking = True
#fleet1.set_acc_type("max")
#fleet1.set_module_params(1.3,0.0,0.0)
#fleet1.set_module_attack_damage_mods([(1,1.6)])
#fleet1.set_module_defense_damage_mods([(1,-6000)])
print(fleet1.modules)
print(f"{fleet1.filtered_str}")
bs.simulate(fleet1, fleet2, planet)



fleet1_raw = ((1,100),(2,100),(5,750))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
#rocket_1 = Rocket(1, 100)
rocket_2 = Rocket(2, 50)
#rocket_3 = Rocket(3, 200)
#rocket_4 = Rocket(4, 300)
planet.set_rockets((rocket_2,))
planet.set_simple_turrets_lvl(1)
planet.set_planet_type_and_size(5,0)
print(planet.rockets.filtered_str)
print(planet.filtered_str_full)
fleet1.set_fleet(fleet1_raw)
fleet1.attacking = True
#fleet1.set_acc_type("max")
#fleet1.set_module_params(1.3,0.0,0.0)
#fleet1.set_module_attack_damage_mods([(1,1.6)])
#fleet1.set_module_defense_damage_mods([(1,-6000)])
print(fleet1.modules)
print(f"{fleet1.filtered_str}")
bs.simulate(fleet1, fleet2, planet)
