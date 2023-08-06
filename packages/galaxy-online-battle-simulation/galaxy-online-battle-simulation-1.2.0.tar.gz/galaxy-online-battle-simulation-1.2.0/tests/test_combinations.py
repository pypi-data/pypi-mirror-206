import battlesimulation
from battlesimulation import SpaceFleet, _GGP

#battlesimulation._debug_printing = True
bs = battlesimulation.BattleSimulation()

fleet1 = SpaceFleet()
fleet2 = SpaceFleet()

ss_ids_1 = [3,4,5,6,9]
ss_ids_2 = [3,4,5,6,9]
ss_id_1 = 5
ss_id_2 = 2

results_dict = {}

for ss_id_2 in ss_ids_2:
    for ss_id_1 in ss_ids_1:
        fleet2.set_fleet([(ss_id_2, 10000), ])
        final_results = bs._test_spaceship_double_combinations_to_beat_enemy_minimum(ss_id_1, 2, fleet1, fleet2)

        top_three = []

        for _ in range(1):
            index = 0
            minimum = final_results[0][2]
            for i, item in enumerate(final_results):
                if minimum > item[2]:
                    minimum = item[2]
                    index = i
            #top_three.append(final_results.pop(index))
            results_dict.update({(ss_id_2, ss_id_1): final_results.pop(index)})

        #for item in top_three:
        #    print(f"""{item[0]} of {_GGP.spaceships[ss_id_1]["name"]}, {item[1]} of {_GGP.spaceships[ss_id_2]["name"]}, antirating={int(item[2])}""")


for keys, item in results_dict.items():
    ss_id_2, ss_id_1 = keys
    print(f"""Target: 10000 of {_GGP.spaceships[ss_id_2]["name"]} vs {item[0]} of {_GGP.spaceships[ss_id_1]["name"]}, {item[1]} of {_GGP.spaceships[2]["name"]}, antirating={int(item[2])}""")