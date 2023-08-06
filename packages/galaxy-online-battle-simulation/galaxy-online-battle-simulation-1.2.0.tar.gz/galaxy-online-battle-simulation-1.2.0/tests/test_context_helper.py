import battlesimulation
from battlesimulation import debug_print, Context, SpaceFleet, BattleSimulation, Planet, Rocket, RocketArray

battlesimulation._debug_printing = True

debug_print("\n\n")
debug_print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
debug_print("\n\n")

fleet1_raw = ((5,10000),(9,4100),)
fleet2_raw = ((6,1000),(9,5000))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
fleet1.set_fleet(fleet1_raw)
fleet2.set_fleet(fleet2_raw)
fleet1.attacking = True
fleet2.attacking = False
fleet1.set_acc_type("min")
fleet2.set_acc_type("min")
planet.set_planet_type_and_size(5,2)
planet.set_simple_turrets_lvl(100)
planet.set_rockets(((2,200),(3,100)))
battle_simulation = BattleSimulation()
battle_simulation.simulate(fleet1, fleet2, planet)

debug_print("\n\n")
debug_print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
debug_print("\n\n")

fleet1_raw = ((5,10000),(9,4100),)
fleet2_raw = ((6,1000),(9,5000))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
fleet1.set_fleet(fleet1_raw)
fleet2.set_fleet(fleet2_raw)
fleet1.attacking = True
fleet2.attacking = False
fleet1.set_acc_type("max")
fleet2.set_acc_type("max")
planet.set_planet_type_and_size(5,2)
planet.set_simple_turrets_lvl(100)
planet.set_rockets(((2,200),(3,100)))
battle_simulation = BattleSimulation()
battle_simulation.simulate(fleet1, fleet2, planet)

debug_print("\n\n")
debug_print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
debug_print("\n\n")

fleet1_raw = ((4,21604),)
fleet2_raw = ((4, 2000),(5, 7000),(9,5000))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
fleet1.set_fleet(fleet1_raw)
fleet2.set_fleet(fleet2_raw)
fleet1.attacking = True
fleet2.attacking = False
fleet1.set_acc_type("min")
fleet2.set_acc_type("max")
#planet.set_planet_type_and_size(5,2)
#planet.set_simple_turrets_lvl(100)
#planet.set_rockets(((2,200),(3,100)))
battle_simulation = BattleSimulation()
battle_simulation.simulate(fleet1, fleet2, planet)

debug_print("\n\n")
debug_print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
debug_print("\n\n")

fleet1_raw = ((1,6),)
fleet2_raw = ((4, 2000),(5, 7000),(9,5000))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
fleet1.set_fleet(fleet1_raw)
#fleet2.set_fleet(fleet2_raw)
fleet1.attacking = True
fleet2.attacking = False
fleet1.set_acc_type("min")
fleet2.set_acc_type("max")
#planet.set_planet_type_and_size(5,2)
#planet.set_simple_turrets_lvl(100)
planet.set_rockets(((2,10),))
battle_simulation = BattleSimulation()
battle_simulation.simulate(fleet1, fleet2, planet)

debug_print("\n\n")
debug_print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
debug_print("\n\n")

fleet1_raw = ((5,7020),)
#fleet2_raw = ((4, 2000),(5, 7000),(9,5000))
fleet2_raw = ((6, 1000),)
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
fleet1.set_fleet(fleet1_raw)
fleet2.set_fleet(fleet2_raw)
fleet1.attacking = True
fleet2.attacking = False
fleet1.set_acc_type("min")
fleet2.set_acc_type("max")
planet.set_planet_type_and_size(5,2)
planet.set_simple_turrets_lvl(100)
planet.set_rockets(((2,200),(3,100)))
battle_simulation = BattleSimulation()
battle_simulation.simulate(fleet1, fleet2, planet)

import sys
sys.exit(0)
debug_print("\n\n")
debug_print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
debug_print("\n\n")

fleet1_raw = ((5,48500),)
fleet2_raw = ((4, 2000),(5, 7000),(9,5000))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
planet = Planet()
fleet1.set_fleet(fleet1_raw)
#fleet2.set_fleet(fleet2_raw)
fleet1.attacking = True
fleet2.attacking = False
fleet1.set_acc_type("min")
fleet2.set_acc_type("max")
planet.set_planet_type_and_size(5,0)
#planet.set_simple_turrets_lvl(100)
planet.set_rockets(((2,200),(3,100)))
battle_simulation = BattleSimulation()
battle_simulation.simulate(fleet1, fleet2, planet, False)