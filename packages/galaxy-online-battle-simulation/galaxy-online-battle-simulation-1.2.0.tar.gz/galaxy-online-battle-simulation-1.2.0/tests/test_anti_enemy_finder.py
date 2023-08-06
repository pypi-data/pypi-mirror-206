import battlesimulation
from battlesimulation import debug_print, Planet, SpaceFleet, BattleSimulation, Planet, Rocket, RocketArray, ModuleAndBonuses
from battlesimulation.components.utility import _my_round_up

battlesimulation._debug_printing = True
bs = BattleSimulation()

fleet_2_raw = ((4, 2000),(5, 7000),(9,5000))
fleet2 = SpaceFleet()
fleet2.set_fleet(fleet_2_raw)
fleet1_mod = ModuleAndBonuses()

debug_print(f"\nenemy is: {fleet2.filtered_str}")
debug_print(f"\nMinimal findings:\n")
debug_print(f"Herculeses needed:{bs._find_suitable_spaceship_to_beat_enemy_minimum(1, fleet1_mod, fleet2)}")
debug_print(f"Lokis needed:{bs._find_suitable_spaceship_to_beat_enemy_minimum(2, fleet1_mod, fleet2)}")
debug_print(f"Raptors needed:{bs._find_suitable_spaceship_to_beat_enemy_minimum(3, fleet1_mod, fleet2)}")
debug_print(f"Hornets needed:{bs._find_suitable_spaceship_to_beat_enemy_minimum(4, fleet1_mod, fleet2)}")
debug_print(f"Javelins needed:{bs._find_suitable_spaceship_to_beat_enemy_minimum(5, fleet1_mod, fleet2)}")
debug_print(f"Excaliburs needed:{bs._find_suitable_spaceship_to_beat_enemy_minimum(6, fleet1_mod, fleet2)}")
debug_print(f"Valkiries needed:{bs._find_suitable_spaceship_to_beat_enemy_minimum(7, fleet1_mod, fleet2)}")
debug_print(f"Titans needed:{bs._find_suitable_spaceship_to_beat_enemy_minimum(8, fleet1_mod, fleet2)}")
debug_print(f"Abaddons needed:{bs._find_suitable_spaceship_to_beat_enemy_minimum(9, fleet1_mod, fleet2)}")
debug_print(f"\nMaximum findings:\n")
debug_print(f"Herculeses needed:{bs._find_suitable_spaceship_to_beat_enemy_maximum(1, fleet1_mod, fleet2)}")
debug_print(f"Lokis needed:{bs._find_suitable_spaceship_to_beat_enemy_maximum(2, fleet1_mod, fleet2)}")
debug_print(f"Raptors needed:{bs._find_suitable_spaceship_to_beat_enemy_maximum(3, fleet1_mod, fleet2)}")
debug_print(f"Hornets needed:{bs._find_suitable_spaceship_to_beat_enemy_maximum(4, fleet1_mod, fleet2)}")
debug_print(f"Javelins needed:{bs._find_suitable_spaceship_to_beat_enemy_maximum(5, fleet1_mod, fleet2)}")
debug_print(f"Excaliburs needed:{bs._find_suitable_spaceship_to_beat_enemy_maximum(6, fleet1_mod, fleet2)}")
debug_print(f"Valkiries needed:{bs._find_suitable_spaceship_to_beat_enemy_maximum(7, fleet1_mod, fleet2)}")
debug_print(f"Titans needed:{bs._find_suitable_spaceship_to_beat_enemy_maximum(8, fleet1_mod, fleet2)}")
debug_print(f"Abaddons needed:{bs._find_suitable_spaceship_to_beat_enemy_maximum(9, fleet1_mod, fleet2)}")

# template
#rockets_array_raw = ((1,0),(2,0),(3,0),(4,0))
rockets_array_raw = ((1,0),(2,10),(3,0),(4,0))
rockets_array = RocketArray()
rockets_array.set_whole_array(rockets_array_raw)
fleet1_mod = ModuleAndBonuses()
blockade = False
debug_print(f"\n{rockets_array.filtered_str}")
# He-He, id 2 is Loki, and Loki are not targeted by rockets ;)
debug_print(f"Herculeses needed to neutralize rockets: {bs._find_number_of_spaceships_to_neutralize_rockets(1, fleet1_mod, rockets_array, blockade)}")
debug_print(f"Javelins needed to neutralize rockets: {bs._find_number_of_spaceships_to_neutralize_rockets(5, fleet1_mod, rockets_array, blockade)}")

rockets_array_raw = ((1,0),(2,0),(3,10),(4,0))
rockets_array.set_whole_array(rockets_array_raw)
fleet1_mod = ModuleAndBonuses()
blockade = False
debug_print(f"\n{rockets_array.filtered_str}")
debug_print(f"Herculeses needed to neutralize rockets: {bs._find_number_of_spaceships_to_neutralize_rockets(1, fleet1_mod, rockets_array, blockade)}")
debug_print(f"Javelins needed to neutralize rockets: {bs._find_number_of_spaceships_to_neutralize_rockets(5, fleet1_mod, rockets_array, blockade)}")


rockets_array_raw = ((1,0),(2,200),(3,100),(4,0))
rockets_array.set_whole_array(rockets_array_raw)
fleet1_mod = ModuleAndBonuses()
#fleet1_mod.set_module_by_id(3)
blockade = False
planet = Planet()
planet.set_planet_type_and_size(5,0)
planet.set_simple_turrets_lvl(100)
debug_print(f"\n{planet.filtered_str_full}")
herculeses = bs._find_number_of_spaceships_to_absord_turrets_damage(1, fleet1_mod, planet)
loki = bs._find_number_of_spaceships_to_absord_turrets_damage(2, fleet1_mod, planet)
raptor = bs._find_number_of_spaceships_to_absord_turrets_damage(3, fleet1_mod, planet)
hornet = bs._find_number_of_spaceships_to_absord_turrets_damage(4, fleet1_mod, planet)
javelins = bs._find_number_of_spaceships_to_absord_turrets_damage(5, fleet1_mod, planet)
excalibur = bs._find_number_of_spaceships_to_absord_turrets_damage(6, fleet1_mod, planet)
valkirie = bs._find_number_of_spaceships_to_absord_turrets_damage(7, fleet1_mod, planet)
titan = bs._find_number_of_spaceships_to_absord_turrets_damage(8, fleet1_mod, planet)
abaddon = bs._find_number_of_spaceships_to_absord_turrets_damage(9, fleet1_mod, planet)
#herculeses_mod = herculeses % int(herculeses) if herculeses > 1 else herculeses
#javelins_mod = javelins % int(javelins) if javelins > 1 else javelins
herculeses_r = bs._find_number_of_spaceships_to_neutralize_rockets(1, fleet1_mod, rockets_array, blockade, herculeses)
loki_r = bs._find_number_of_spaceships_to_neutralize_rockets(2, fleet1_mod, rockets_array, blockade, loki)
raptor_r = bs._find_number_of_spaceships_to_neutralize_rockets(3, fleet1_mod, rockets_array, blockade, raptor)
hornet_r = bs._find_number_of_spaceships_to_neutralize_rockets(4, fleet1_mod, rockets_array, blockade, hornet)
javelins_r = bs._find_number_of_spaceships_to_neutralize_rockets(5, fleet1_mod, rockets_array, blockade, javelins)
excalibur_r = bs._find_number_of_spaceships_to_neutralize_rockets(6, fleet1_mod, rockets_array, blockade, excalibur)
valkirie_r = bs._find_number_of_spaceships_to_neutralize_rockets(7, fleet1_mod, rockets_array, blockade, valkirie)
titan_r = bs._find_number_of_spaceships_to_neutralize_rockets(8, fleet1_mod, rockets_array, blockade, titan)
abaddon_r = bs._find_number_of_spaceships_to_neutralize_rockets(9, fleet1_mod, rockets_array, blockade, abaddon)
herculeses_tr=herculeses+herculeses_r
loki_tr=loki+loki_r
raptor_tr=raptor+raptor_r
hornet_tr=hornet+hornet_r
javelins_tr=javelins+javelins_r
excalibur_tr=excalibur+excalibur_r
valkirie_tr=valkirie+valkirie_r
titan_tr=titan+titan_r
abaddon_tr=abaddon+abaddon_r
herculeses = _my_round_up(herculeses)
loki = _my_round_up(loki)
raptor = _my_round_up(raptor)
hornet = _my_round_up(hornet)
javelins = _my_round_up(javelins)
excalibur = _my_round_up(excalibur)
valkirie = _my_round_up(valkirie)
titan = _my_round_up(titan)
abaddon = _my_round_up(abaddon)
herculeses_r = _my_round_up(herculeses_r)
loki_r = _my_round_up(loki_r)
raptor_r = _my_round_up(raptor_r)
hornet_r = _my_round_up(hornet_r)
javelins_r = _my_round_up(javelins_r)
excalibur_r = _my_round_up(excalibur_r)
valkirie_r = _my_round_up(valkirie_r)
titan_r = _my_round_up(titan_r)
abaddon_r = _my_round_up(abaddon_r)
debug_print(f"Herculeses agains turrets: {herculeses}")
debug_print(f"Loki agains turrets: {loki}")
debug_print(f"Raptor agains turrets: {raptor}")
debug_print(f"Hornet agains turrets: {hornet}")
debug_print(f"Javelins agains turrets: {javelins}")
debug_print(f"Excalibur agains turrets: {excalibur}")
debug_print(f"Valkirie agains turrets: {valkirie}")
debug_print(f"Titan agains turrets: {titan}")
debug_print(f"Abaddons agains turrets: {abaddon}")
debug_print(f"Herculeses against rockets: {herculeses_r}")
debug_print(f"Loki against rockets: {loki_r}")
debug_print(f"Raptor against rockets: {raptor_r}")
debug_print(f"Hornet against rockets: {herculeses_r}")
debug_print(f"Javelins against rockets: {javelins_r}")
debug_print(f"Excalibur against rockets: {herculeses_r}")
debug_print(f"Valkirie against rockets: {herculeses_r}")
debug_print(f"Titan against rockets: {herculeses_r}")
debug_print(f"Abaddons against rockets: {abaddon_r}")
debug_print(f"Herculeses needed to neutralize rockets including turrets: {herculeses_tr}, rounded={_my_round_up(herculeses_tr)}")
debug_print(f"Loki needed to neutralize rockets including turrets: {loki_tr}, rounded={_my_round_up(loki_tr)}")
debug_print(f"Raptor needed to neutralize rockets including turrets: {raptor_tr}, rounded={_my_round_up(raptor_tr)}")
debug_print(f"Hornet needed to neutralize rockets including turrets: {hornet_tr}, rounded={_my_round_up(hornet_tr)}")
debug_print(f"Javelins needed to neutralize rockets including turrets: {javelins_tr}, rounded={_my_round_up(javelins_tr)}")
debug_print(f"Excalibur needed to neutralize rockets including turrets: {excalibur_tr}, rounded={_my_round_up(excalibur_tr)}")
debug_print(f"Valkirie needed to neutralize rockets including turrets: {valkirie_tr}, rounded={_my_round_up(valkirie_tr)}")
debug_print(f"Titan needed to neutralize rockets including turrets: {titan_tr}, rounded={_my_round_up(titan_tr)}")
debug_print(f"Abaddons needed to neutralize rockets including turrets: {abaddon_tr}, rounded={_my_round_up(abaddon_tr)}")


rockets_array_raw = ((1,0),(2,200),(3,100),(4,0))
fleet1_mod = ModuleAndBonuses()
planet = Planet()
planet.set_planet_type_and_size(5,0)
planet.set_simple_turrets_lvl(100)
planet.set_rockets(rockets_array_raw)
debug_print(f"\n{planet.filtered_str_full}")
debug_print(f"Herculeses needed to neutralize Planet: {bs._find_number_of_spaceships_to_neutralize_planet_rockets_and_turrets_damage(1, fleet1_mod, planet,full_attack=True)}")
debug_print(f"Javelins needed to neutralize Planet: {bs._find_number_of_spaceships_to_neutralize_planet_rockets_and_turrets_damage(5, fleet1_mod, planet,full_attack=True)}")
debug_print(f"Abaddons needed to neutralize Planet: {bs._find_number_of_spaceships_to_neutralize_planet_rockets_and_turrets_damage(9, fleet1_mod, planet,full_attack=True)}")

fleet_2_raw = ((4, 2000),(5, 7000),(9,5000))
fleet2 = SpaceFleet()
fleet2.set_fleet(fleet_2_raw)
fleet2.set_acc_type("max")
rockets_array_raw = ((1,0),(2,200),(3,100),(4,0))
fleet1_mod = ModuleAndBonuses()
planet = Planet()
target_blockade = False
planet.set_planet_type_and_size(5,0)
planet.set_simple_turrets_lvl(100)
planet.set_rockets(rockets_array_raw)

debug_print(f"\nenemy is: {fleet2.filtered_str}")
debug_print(f"Planet is:\n{planet.filtered_str_full}")
debug_print(f"\nMinimal findings:\n")
result = bs.find_suitable_fleets_to_beat_enemy(fleet1_mod, fleet2, planet, target_blockade)
for ss_id in result:
    debug_print(f"{battlesimulation._GGP.spaceships[ss_id]['name_en']}: {result[ss_id][0]}")
debug_print(f"\nMaximum findings:\n")
for ss_id in result:
    debug_print(f"{battlesimulation._GGP.spaceships[ss_id]['name_en']}: {result[ss_id][1]}")

top_length = 5
top_results = bs.select_top_results_to_beat_enemy_simulate(result, fleet1_mod, fleet2, planet, target_blockade, 2, 0.8, 1.2, top_length)
debug_print(f"\n\nTop {top_length} results for minimum method:")
for ss_id in top_results["min"]:
    debug_print(f"{battlesimulation._GGP.spaceships[ss_id]['name_en']}: {result[ss_id][0]}")
debug_print(f"\n\nTop {top_length} results for maximum method:")
for ss_id in top_results["max"]:
    debug_print(f"{battlesimulation._GGP.spaceships[ss_id]['name_en']}: {result[ss_id][1]}")


import json
with open("/home/adminator/python/0_for_public/galaxy-online-battle-simulation/tests/data.json", "r", encoding="utf-8") as f:
	loaded_data = json.load(f)
battlesimulation.load_global_game_parameters(loaded_data)


fleet_2_raw = ((4, 2000),(5, 7000),(9,5000))
fleet2 = SpaceFleet()
fleet2.set_fleet(fleet_2_raw)
fleet2.set_acc_type("max")
rockets_array_raw = ((1,100),(2,200),(3,100),(4,0))
fleet1_mod = ModuleAndBonuses()
planet = Planet()
target_blockade = False
planet.set_planet_type_and_size(5,0)
planet.set_simple_turrets_lvl(100)
planet.set_rockets(rockets_array_raw)

debug_print(f"\nenemy is: {fleet2.filtered_str}")
debug_print(f"Planet is:\n{planet.filtered_str_full}")
debug_print(f"\nMinimal findings:\n")
result = bs.find_suitable_fleets_to_beat_enemy(fleet1_mod, fleet2, planet, target_blockade, list_of_spaceships_ids_to_use=(1,3,4,5,6,9))
for ss_id in result:
    debug_print(f"{battlesimulation._GGP.spaceships[ss_id]['name_en']}: {result[ss_id][0]}")
debug_print(f"\nMaximum findings:\n")
for ss_id in result:
    debug_print(f"{battlesimulation._GGP.spaceships[ss_id]['name_en']}: {result[ss_id][1]}")

top_length = 5
top_results = bs.select_top_results_to_beat_enemy_simulate(result, fleet1_mod, fleet2, planet, target_blockade, 2, 0.8, 1.2, top_length)
debug_print(f"\n\nTop {top_length} results for minimum method:")
for ss_id in top_results["min"]:
    debug_print(f"{battlesimulation._GGP.spaceships[ss_id]['name_en']}: {result[ss_id][0]}")
debug_print(f"\n\nTop {top_length} results for maximum method:")
for ss_id in top_results["max"]:
    debug_print(f"{battlesimulation._GGP.spaceships[ss_id]['name_en']}: {result[ss_id][1]}")
