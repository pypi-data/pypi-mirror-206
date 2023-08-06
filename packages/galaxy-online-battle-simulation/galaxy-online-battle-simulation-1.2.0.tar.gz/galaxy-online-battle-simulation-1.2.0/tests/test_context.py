from battlesimulation import debug_print, Context

context = Context()
context.enable_debug_printing()

context.help()
print("\n\n")
context.help_game_parameters()
print("\n\n")

#context.add_javelin_to_fleet_1(10000)
#context.add_excalibur_to_fleet_2(1000)
#context.set_planet(5,2,60)
#context.set_rockets(((3,100),))
#context.simulate()

print("\n\n")

context = Context()

# base conditions
#context.add_excalibur_to_fleet_2(1000)
#context.add_javelin_to_fleet_3(10000)
# minimum
#context.add_raptor_to_fleet_1(5707)
#context.add_hornet_to_fleet_1(7320)
#context.add_javelin_to_fleet_1(15278)
#context.add_excalibur_to_fleet_1(3667)
#context.add_abaddon_to_fleet_1(2477)
# maximum
#context.add_raptor_to_fleet_1(18334)
#context.add_hornet_to_fleet_1(30556)
#context.add_javelin_to_fleet_1(50000)
#context.add_excalibur_to_fleet_1(10000)
#context.add_abaddon_to_fleet_1(7639)

#####

### With turrets and rockets
#context.set_planet(5,2,100)
#context.set_rockets(((3,100),(2,200)))
# minimum
#context.add_raptor_to_fleet_1(6441)
#context.add_hornet_to_fleet_1(8143)
#context.add_javelin_to_fleet_1(15278)
#context.add_excalibur_to_fleet_1(3744)
#context.add_abaddon_to_fleet_1(2663)
# maximum
#context.add_raptor_to_fleet_1(18334)
#context.add_hornet_to_fleet_1(30556)
#context.add_javelin_to_fleet_1(50000)
#context.add_excalibur_to_fleet_1(10000)
#context.add_abaddon_to_fleet_1(7639)

#####
#####
#####

#context.add_excalibur_to_fleet_2(10000)
#context.add_javelin_to_fleet_3(1000)
#context.set_planet(5,2,100)
#context.set_rockets(((3,100),(2,200)))
# minimum
#context.add_raptor_to_fleet_1(32332)
#context.add_hornet_to_fleet_1(37856)
#context.add_javelin_to_fleet_1(61877)
#context.add_excalibur_to_fleet_1(15463)
#context.add_abaddon_to_fleet_1(5196)
# maximum
#context.add_raptor_to_fleet_1(91834)
#context.add_hornet_to_fleet_1(153016)
#context.add_javelin_to_fleet_1(250545)
#context.add_excalibur_to_fleet_1(50136)
#context.add_abaddon_to_fleet_1(38334)

#####

### With turrets and rockets
#context.set_planet(5,2,100)
#context.set_rockets(((3,100),(2,200)))
# minimum
#context.add_raptor_to_fleet_1(33066)
#context.add_hornet_to_fleet_1(38679)
#context.add_javelin_to_fleet_1(62789)
#context.add_excalibur_to_fleet_1(15827)
#context.add_abaddon_to_fleet_1(5382)
# maximum
#context.add_raptor_to_fleet_1(92568)
#context.add_hornet_to_fleet_1(153839)
#context.add_javelin_to_fleet_1(251457)
#context.add_excalibur_to_fleet_1(50500)
#context.add_abaddon_to_fleet_1(38520)
#########
context.add_raptor_to_fleet_1(6441)
context.add_excalibur_to_fleet_2(1000)
#context.add_raptor_to_fleet_2(8000)
context.add_javelin_to_fleet_3(10000)
context.set_planet(5,2,100)
context.set_rockets(((3,100),(2,200)))
#context.set_fleet_1_acc_type("min")
#context.set_fleet_2_acc_type("max")
#context.set_fleet_3_acc_type("max")
context.set_fleet_1_acc_type("range_max")
context.set_fleet_2_acc_type("range_max")
context.set_fleet_3_acc_type("range_max")
context.set_add_energy_cost_to_depature(2)
context.set_energy_cost_coef(0.8)
context.set_build_time_coef(1.2)
context.set_length_of_top_sorted(3)
context.simulate()


#top_sorted = context._battle_simulation.select_top_results_to_beat_enemy(context._fleet_finder_raw_results_dict, context._fleet_finder_dict, \
#        2, 0.8, 1.2, 5)
#text = context.make_text_for_costs_and_build_times_for_top_sorted(top_sorted)
#print(text)
print("\n\n")
print("#######################################################################")
print("\n\n")
#print("\n")
context = Context()
context.add_raptor_to_fleet_1(6441)
context.add_abaddon_to_fleet_1(10000)
context.add_excalibur_to_fleet_2(1000)
context.add_raptor_to_fleet_2(3000)
context.add_javelin_to_fleet_3(10000)
context.set_fleet_1_acc_type("range_max")
context.set_fleet_2_acc_type("range_max")
context.set_fleet_3_acc_type("range_max")
context.simulate()


print("\n\n")
print("#######################################################################")
print("\n\n")
context = Context()
context.set_planet(1,1)
#context.set_buildings(((1,30),(9,30),(10,30)))
context.add_building(1,30)
context.add_building(9,30)
context.add_building(10,30)
#context.set_rockets(((4,100),))
context.add_rocket(4, 100)
print(context._planet.filtered_str_full)
context.reset_rockets_to_zero()
print(context._planet.filtered_str_full)
context.reset_all_buildings()
print(context._planet.filtered_str_full)
context.add_building(1,30)
context.add_building(10,30)
print(context._planet.filtered_str_full)
print(context._planet.buildings._array)
print("\n\n")
context.add_abaddon_to_fleet_1(1000)
print(context._fleet_1.filtered_str)
context.init_fleet_1([])
print(context._fleet_1.filtered_str)
context.set_fleet_1_module_by_id_and_level(3,100)
context.old_simulate_bombardment()
#result = context._battle_simulation.old_simulate_bombardment(context._fleet_1.modules, context._planet)
#print("\n\n")
#for key in result:
#    print(f"{key}:")
#    print(f"{result[key]}")
#    print("\n")
#print("\n\n")



#print("\n\n")
#print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#print("\n\n")
#
#fleet1_raw = ((5,10000),(9,4100),)
#fleet2_raw = ((6,1000),(9,5000))
#fleet1 = SpaceFleet()
#fleet2 = SpaceFleet()
#planet = Planet()
#fleet1.set_fleet(fleet1_raw)
#fleet2.set_fleet(fleet2_raw)
#fleet1.attacking = True
#fleet2.attacking = False
#fleet1.set_acc_type("max")
#fleet2.set_acc_type("max")
#planet.set_planet_type_and_size(5,2)
#planet.set_simple_turrets_lvl(100)
#planet.set_rockets(((2,200),(3,100)))
#battle_simulation = BattleSimulation()
#battle_simulation.simulate(fleet1, fleet2, planet)
#
#print("\n\n")
#print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#print("\n\n")
#
#fleet1_raw = ((5,10000),(9,4100),)
#fleet2_raw = ((6,1000),(9,5000))
#fleet1 = SpaceFleet()
#fleet2 = SpaceFleet()
#planet = Planet()
#fleet1.set_fleet(fleet1_raw)
#fleet2.set_fleet(fleet2_raw)
#fleet1.attacking = True
#fleet2.attacking = False
#fleet1.set_acc_type("min")
#fleet2.set_acc_type("min")
#planet.set_planet_type_and_size(5,2)
#planet.set_simple_turrets_lvl(100)
#planet.set_rockets(((2,200),(3,100)))
#battle_simulation = BattleSimulation()
#battle_simulation.simulate(fleet1, fleet2, planet)



# Target:
# Fleet 3 = [Javelin  10000]
# Fleet 2 = [Excalibur 1000]

# valid results:
# Raptor      5709
# Hornet      7323
# Javelins   15278
# Excalibur   3667
# Abaddon     2477
