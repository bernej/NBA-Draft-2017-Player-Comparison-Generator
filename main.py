from extensions import connect_to_database
from math import sqrt

db = connect_to_database()

# guards = {}
# wings = {}
# bigs = {}

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
    
    print(prospect['Player'] + " comparables are:")

    comparables = {} # Cosine similarity values of prospect and each NBA comp

    # Look at FG%, 2P%, 3P%, and FT%
    for nba_player in comps_per40_results:
        comp_key = nba_player['Player'] + ", " + nba_player['Season']
        numerator = float(prospect['PTS']) * float(nba_player['PTS'])
        numerator += ( float(prospect['AST']) * float(nba_player['AST']) )
        numerator += ( float(prospect['TRB']) * float(nba_player['TRB']) )
        numerator += ( float(prospect['STL']) * float(nba_player['STL']) )
        numerator += ( float(prospect['BLK']) * float(nba_player['BLK']) )

        prosp_denom = (float(prospect['PTS'])**2) + (float(prospect['AST'])**2) + (float(prospect['TRB'])**2) + (float(prospect['STL'])**2) + (float(prospect['BLK'])**2)
        comp_denom = (float(nba_player['PTS'])**2) + (float(nba_player['AST'])**2) + (float(nba_player['TRB'])**2) + (float(nba_player['STL'])**2) + (float(nba_player['BLK'])**2)
        # prosp_denom = float(prospect['PTS'])**2
        # comp_denom = float(nba_player['PTS'])**2
        # Look out for Players who didn't take any 3s
        # if str(nba_player['3PP']) == '0.000' or nba_player['3PP'] is None:
        #     continue
        # else:
        #     numerator += ( float(prospect['3PP']) * float(nba_player['3PP']) )
        #     comp_denom += (float(nba_player['3PP'])**2)
        #     prosp_denom += (float(prospect['3PP'])**2)

        denom = sqrt(prosp_denom) * sqrt(comp_denom)

        score = numerator / denom
        comparables[comp_key] = score

    comparables = sorted(comparables.items(), key=lambda x: x[1], reverse=True)

    idx = 0
    for comp in comparables:
        # print(comp)
        print('\t' + comp[0] + " with a similarity score of " + str(comp[1]))
        idx += 1
        if idx == 5:
            break

    # Look at FG attempts, 2-Point attempts, 3-Point attempts, FT attempts

    # Look at PTS, AST, and TRBs
    # Look at STLs and Blocks


# Query per game statistics
# cur = db.cursor()
# cur.execute('SELECT * FROM prosp_szns')
# pergame_results = cur.fetchall()

# Query per 100 possessions statistics
# cur = db.cursor()
# cur.execute('SELECT * FROM prosp_per100')
# per100_results = cur.fetchall()

# Query advanced statistics
# cur = db.cursor()
# cur.execute('SELECT * FROM prosp_adv')
# adv_results = cur.fetchall()

# for result in pergame_results:
#     # Unique key for each prospect season
#     key = result['Name'] + ", " + result['Season']
#     # Add player to the proper position group
#     if result['Position'] == 'Guard':
#         guards[key] = {}
#     elif result['Position'] == 'Wing':
#         wings[key] = {}
#     elif result['Position'] == 'Big':
#         bigs[key] = {}

# print(guards)
# print(wings)
# print(bigs)

# Compile offensive stats
# players = {}
# for result in adv_results:
#     key = result['Name'] + ", " + result['Season']
#     players[key] = []
#     players[key].append(float(result['TS']))
#     players[key].append(float(result['eFG']))
#     players[key].append(float(result['AST']))

# for result in per100_results:
#     key = result['Name'] + ", " + result['Season']
#     players[key].append(float(result['FTA']))
#     players[key].append(float(result['ORtg']))


# true_shooting = sorted(players.items(), key=lambda x: x[1][0], reverse=True)
# eff_fieldgoal = sorted(players.items(), key=lambda x: x[1][1], reverse=True)
# assist_rate = sorted(players.items(), key=lambda x: x[1][2], reverse=True)
# ft_per100 = sorted(players.items(), key=lambda x: x[1][3], reverse=True)
# ortg = sorted(players.items(), key=lambda x: x[1][4], reverse=True)

# rankings = {}
# idx = 1
# for key in true_shooting:
#     rankings[key[0]] = idx
#     idx += 1
# idx = 1
# for key in eff_fieldgoal:
#     rankings[key[0]] += idx
#     idx += 1

# idx = 1
# for key in assist_rate:
#     rankings[key[0]] += idx
#     idx += 1
# idx = 1
# for key in ft_per100:
#     rankings[key[0]] += idx
#     idx += 1
# idx = 1
# for key in ortg:
#     rankings[key[0]] += idx
#     idx += 1
# rankings = sorted(rankings.items(), key=lambda x: x[1], reverse=False)

# print("Measuring efficient shooting, assist rate, free throw rate, and offensive rating: ")
# idx = 1
# for player in rankings:
#     print("#" + str(idx) + ": " + player[0] + " with a True Shooting % of " + str(players[player[0]][0]) \
#           + " , an eFG% of " + str(players[player[0]][1]) + " , an assist rate per 100 possessions of " + \
#           str(players[player[0]][2]) + " , a FT rate per 100 possessions of " + str(players[player[0]][3]) + \
#           " , and an offensive rating of " + str(players[player[0]][4]))
# Split by positions. Shouldn't measure assist rate for big men.
# Come up with more position-specific rankings