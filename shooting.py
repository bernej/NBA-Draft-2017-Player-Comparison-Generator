from extensions import connect_to_database
from misc import *


db = connect_to_database()

prosp_szn_results, prosp_per40_results, prosp_adv_results, comps_per40_results, comps_adv_results = query_tables(db)

for prospect in prosp_per40_results:

    print(prospect['Player'])

    print(prospect['3PP'])
    print(prospect['FTP'])

    sim_shooting_percentages = {}

    for nba_player in comps_per40_results:

        comp_key = nba_player['Player'] + ", " + nba_player['Season'] + ", " + nba_player['School']

        if nba_player['3PP'] is None or nba_player['3PA'] <= 1.0:
            nba_player['3PP'] = .000

        if prospect['3PP'] is None or prospect['3PA'] <= 1.0:
            prospect['3PP'] = .000

        three_diff = abs(float(nba_player['3PP']) - float(prospect['3PP']))
        FT_diff = abs(float(nba_player['FTP']) - float(prospect['FTP']))
        shot_diff = three_diff + FT_diff

        three_similar = three_diff <= .05
        FT_similar = FT_diff <= .05


        if  three_similar and FT_similar:

            sim_shooting_percentages[comp_key] = (float(nba_player['3PP']), float(nba_player['FTP']), float("{0:.5f}".format(shot_diff)))

    sim_shooting_percentages = sorted(sim_shooting_percentages.items(), key=lambda x: x[1][2], reverse=False)

    print(sim_shooting_percentages)