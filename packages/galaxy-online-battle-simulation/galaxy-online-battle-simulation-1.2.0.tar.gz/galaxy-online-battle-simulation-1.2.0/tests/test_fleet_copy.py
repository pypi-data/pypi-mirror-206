import battlesimulation
from battlesimulation import debug_print, SpaceFleet

battlesimulation._debug_printing = True

fleet1_raw = ((5,1300),(3,800),(7,5000))
fleet2_raw = ((5,10000),(7,5000))
fleet1 = SpaceFleet()
fleet2 = SpaceFleet()
fleet1.set_fleet(fleet1_raw)
fleet2.set_fleet(fleet2_raw)
fleet1.attacking = True
fleet2.attacking = False
fleet1.set_acc_type("max")
fleet2.set_acc_type("random")
fleet1.set_module_params(1.3,0.0,1.15)
fleet2.set_module_params(0.0,1.25,0.0)
fleet1.set_module_attack_damage_mods([(1,1.6)])
fleet1.set_module_defense_damage_mods([(1,-6000)])

debug_print(f"Fleet 1: {fleet1}\n")
debug_print(f"Module: {fleet1.modules}\n")

fleet1_copy = fleet1.make_a_copy_of_self()
debug_print(f"Copy of Fleet1: {fleet1_copy}\n")
debug_print(f"Module: {fleet1_copy.modules}\n")

debug_print(f"Fleet 2: {fleet2}\n")
debug_print(f"Module: {fleet2.modules}\n")

fleet2_copy = fleet2.make_a_copy_of_self()
debug_print(f"Copy of Fleet2: {fleet2_copy}\n")
debug_print(f"Module: {fleet2_copy.modules}\n")