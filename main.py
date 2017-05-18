from extensions import connect_to_database
from similarity import *

db = connect_to_database()

players = {}

# Gather the Top 10 prospects
cur = db.cursor()
cur.execute('SELECT * FROM prosp_per40')
prosp_per40_results = cur.fetchall()

# Gather all the NBA comps
cur = db.cursor()
cur.execute('SELECT * FROM comps_per40')
comps_per40_results = cur.fetchall()

# Compute similarity
for prospect in prosp_per40_results:
    
    print(prospect['Player'] + "\t " + str(prospect['FGP']) + " FG% / " + str(prospect['2PP']) + " 2P% / " + str(prospect['3PP']) + " 3P% /" + str(prospect['FTP']) + " FT% | \t" + \
          str(prospect['PTS']) + " PPG / " + str(prospect['AST']) + " AST / " + str(prospect['TRB']) + " TRB /" + str(prospect['STL']) + " STL /" + str(prospect['BLK']) + " BLK\n")

    comparables = {} # Cosine similarity values of prospect versus each NBA comp

    for nba_player in comps_per40_results:

        # NBA Player and their respective NCAA season
        comp_key = nba_player['Player'] + ", " + nba_player['Season'] + ", " + nba_player['School']

        players[comp_key] = nba_player

        # Look at FG%, 2P%, 3P%, and FT%
        shot_percentage_score = shot_percentage_similarity(prospect, nba_player)

        # Look at PTS, AST, TRBs, STLs, and BLKs
        per_game_score = per_game_similarity(prospect, nba_player)

        comparables[comp_key] = shot_percentage_score * per_game_score

    comparables = sorted(comparables.items(), key=lambda x: x[1], reverse=True)


    idx = 0
    for comp in comparables:
        # print(comp)
        print('\t' + comp[0] + "\t " + str(players[comp[0]]['FGP']) + " FG%/ " + str(players[comp[0]]['2PP']) + " 2P%/ " + str(players[comp[0]]['3PP']) + " 3P%/ " + str(players[comp[0]]['FTP']) + " FT% | \t" + \
              str(players[comp[0]]['PTS']) + " PPG / " + str(players[comp[0]]['AST']) + " AST / " + str(players[comp[0]]['TRB']) + " TRB /" + str(players[comp[0]]['STL']) + " STL /" + str(players[comp[0]]['BLK']) + " BLK\t" + \
              " similarity score:  " + str(comp[1]))
        idx += 1
        if idx == 5:
            break
    print('\n')
