from extensions import connect_to_database

db = connect_to_database()

guards = {}
wings = {}
bigs = {}

# Query per game statistics
cur = db.cursor()
cur.execute('SELECT * FROM prosp_szns')
pergame_results = cur.fetchall()

# Query per 100 possessions statistics
cur = db.cursor()
cur.execute('SELECT * FROM prosp_per100')
per100_results = cur.fetchall()

# Query advanced statistics
cur = db.cursor()
cur.execute('SELECT * FROM prosp_adv')
adv_results = cur.fetchall()

for result in pergame_results:
    # Unique key for each prospect season
    key = result['Name'] + ", " + result['Season']
    # Add player to the proper position group
    if result['Position'] == 'Guard':
        guards[key] = {}
    elif result['Position'] == 'Wing':
        wings[key] = {}
    elif result['Position'] == 'Big':
        bigs[key] = {}

print(guards)
print(wings)
print(bigs)

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