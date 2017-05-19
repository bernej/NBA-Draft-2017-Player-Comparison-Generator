from extensions import connect_to_database
from similarity import *

db = connect_to_database()

# NBA players in the database. Consists of every top 5 pick since the 1993 draft
# as well as every all star drafted since 1993. Additionally, contains more
# active players than retired, i.e. players who are 
players = {}

# Gather the Top 10 prospects
cur = db.cursor()
cur.execute('SELECT * FROM prosp_per40')
prosp_per40_results = cur.fetchall()

# Gather prospect advanced stats
cur = db.cursor()
cur.execute('SELECT * FROM prosp_adv')
prosp_adv_results = cur.fetchall()

# Gather all the NBA comps (per 40 minutes stats)
cur = db.cursor()
cur.execute('SELECT * FROM comps_per40')
comps_per40_results = cur.fetchall()

cur = db.cursor()
cur.execute('SELECT * FROM comps_adv')
comps_adv_results = cur.fetchall()

# Compute similarity
for prospect in prosp_per40_results:
    
    print(prospect['Player'] + "\t " + str(prospect['FGP']) + " FG% / " + str(prospect['2PP']) + " 2P% / " + str(prospect['3PP']) + " 3P% /" + str(prospect['FTP']) + " FT% | \t" + \
          str(prospect['PTS']) + " PPG / " + str(prospect['AST']) + " AST / " + str(prospect['TRB']) + " TRB /" + str(prospect['STL']) + " STL /" + str(prospect['BLK']) + " BLK\n")

    comparables = {} # Cosine similarity values of prospect versus each NBA comp
    score = 0.0 # Score of the current prospect versus the current NBA player

    for nba_player in comps_per40_results:

        # NBA Player and their respective NCAA season
        comp_key = nba_player['Player'] + ", " + nba_player['Season'] + ", " + nba_player['School']

        # todo: Add career VORP to comps_per40_results so results can be sorted in desscending order
        players[comp_key] = nba_player

        # Look at FG%, 2P%, 3P%, and FT%
        shot_percentage_score = shot_percentage_similarity(prospect, nba_player)

        # Look at PTS, AST, TRBs, STLs, and BLKs
        per_game_score = per_game_similarity(prospect, nba_player)

        # Look at FGA, 2PA, 3PA, and FTAs
        # shot_attempt_score = shot_attempt_similarity(prospect, nba_player)

        comparables[comp_key] = shot_percentage_score * per_game_score

    # for nba_player in comps_adv_results:

    #     # Need to get this prospect's advanced stats.
    #     college_player = {}
    #     for nba_prospect in prosp_adv_results:
    #         key = nba_prospect['Player'] + ", " + nba_prospect['Season']
    #         desired_key = prospect['Player'] + ", " + prospect['Season']
    #         if key == desired_key:
    #             college_player = nba_prospect
    #             break

    #     # NBA Player and their respective NCAA season
    #     comp_key = nba_player['Player'] + ", " + nba_player['Season'] + ", " + nba_player['School']

    #     adv_shooting_score = adv_shooting_similarity(college_player, nba_player)

    #     comparables[comp_key] *= adv_shooting_score




    # comparables[comp_key]

    comparables = sorted(comparables.items(), key=lambda x: x[1], reverse=True)

    vorp_comps = {}
    idx = 0
    for comp in comparables:
        # print(comp)
        vorp_comps[comp[0]] = players[comp[0]]['VORP']
        print('\t' + comp[0] + "\t " + str(players[comp[0]]['FGP']) + " FG%/ " + str(players[comp[0]]['2PP']) + " 2P%/ " + str(players[comp[0]]['3PP']) + " 3P%/ " + str(players[comp[0]]['FTP']) + " FT% | " + \
              str(players[comp[0]]['PTS']) + " PPG / " + str(players[comp[0]]['AST']) + " AST / " + str(players[comp[0]]['TRB']) + " TRB /" + str(players[comp[0]]['STL']) + " STL /" + str(players[comp[0]]['BLK']) + " BLK\t" + \
              " similarity score:  " + "{0:.4f}".format(comp[1]))
        idx += 1
        if idx >= 30:
            break
    print('\n')

    vorp_comps = sorted(vorp_comps.items(), key=lambda x: x[1], reverse=True)

    for comp in vorp_comps:
        print('\t' + comp[0] + " with a career VORP of " + str(comp[1]))
    print('\n')

