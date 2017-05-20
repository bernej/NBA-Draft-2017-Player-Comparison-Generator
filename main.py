from extensions import connect_to_database
from similarity import *
import os

db = connect_to_database()

# NBA players in the database. Consists of every top 5 pick since the 1993 draft
# as well as every all star drafted since 1993. Additionally, contains more
# active players than retired, i.e. players who are 
players = {}
adv_players = {}

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

# Gather their advanced stats
cur = db.cursor()
cur.execute('SELECT * FROM comps_adv')
comps_adv_results = cur.fetchall()

try:
    os.remove('analysis.txt')
except OSError:
    pass

out_file = open('analysis.txt', 'w')

# Compute similarity
for prospect in prosp_per40_results:
    college_player = {}    
    out_file.write(prospect['Player'] + "\t\t\t" + str(prospect['FGP']) + " FG% / " + str(prospect['2PP']) + " 2P% / " + str(prospect['3PP']) + " 3P% /" + str(prospect['FTP']) + " FT% | \t" + \
          str(prospect['PTS']) + " PPG / " + str(prospect['AST']) + " AST / " + str(prospect['TRB']) + " TRB /" + str(prospect['STL']) + " STL /" + str(prospect['BLK']) + " BLK\n")

    per40_comparables = {} # Cosine similarity values of prospect versus each NBA comp
    adv_comparables = {}

    score = 0.0 # Score of the current prospect versus the current NBA player

    # Traditional NBA comparisons
    for nba_player in comps_per40_results:

        # NBA Player and their respective NCAA season
        comp_key = nba_player['Player'] + ", " + nba_player['Season'] + ", " + nba_player['School']

        # todo: add more per40 prospect seasons
        # todo: figure out advanced stats calculation

        players[comp_key] = nba_player

        # Look at FG%, 2P%, 3P%, and FT%
        per40_comparables[comp_key] = shot_percentage_similarity(prospect, nba_player)

        # Look at PTS, AST, TRBs, STLs, and BLKs
        per40_comparables[comp_key] *= per_game_similarity(prospect, nba_player)

        # Look at FGA, 2PA, 3PA, and FTAs
        # shot_attempt_score = shot_attempt_similarity(prospect, nba_player)

        # per40_comparables[comp_key] = shot_percentage_score * per_game_score

    adv_seasons = ['11','12','13','14','15','16'] # seasons that have complete advanced stats

    # Modern NBA comparisons
    for nba_player in comps_adv_results:

        # Need to get this prospect's advanced stats.
        for nba_prospect in prosp_adv_results:
            key = nba_prospect['Player'] + ", " + nba_prospect['Season']
            desired_key = prospect['Player'] + ", " + prospect['Season']
            if key == desired_key:
                college_player = nba_prospect
                break

        # NBA Player and their respective NCAA season

        # Valid
        if any(season in nba_player['Season'] for season in adv_seasons):

            comp_key = nba_player['Player'] + ", " + nba_player['Season'] + ", " + nba_player['School']

            adv_players[comp_key] = nba_player

            adv_comparables[comp_key] = adv_rate_similarity(college_player, nba_player)

            adv_comparables[comp_key] *= adv_percent_similarity(college_player, nba_player)

            adv_comparables[comp_key] *= adv_misc_similarity(college_player, nba_player)

    per40_comparables = sorted(per40_comparables.items(), key=lambda x: x[1], reverse=True)
    adv_comparables = sorted(adv_comparables.items(), key=lambda x: x[1], reverse=True)

    per40_score = {}
    adv_score = {}

    out_file.write("Per 40 minute comparisons:\n")
    vorp_comps = {}
    idx = 0
    for comp in per40_comparables:
        # out_file.write(comp)
        per40_score[comp[0]] = comp[1]
        vorp_comps[comp[0]] = players[comp[0]]['VORP']
        out_file.write('\t' + comp[0] + '\t' + str(players[comp[0]]['FGP']) + " FG%/ " + str(players[comp[0]]['2PP']) + " 2P%/ " + str(players[comp[0]]['3PP']) + " 3P%/ " + str(players[comp[0]]['FTP']) + " FT% | " + \
              str(players[comp[0]]['PTS']) + " PPG / " + str(players[comp[0]]['AST']) + " AST / " + str(players[comp[0]]['TRB']) + " TRB /" + str(players[comp[0]]['STL']) + " STL /" + str(players[comp[0]]['BLK']) + " BLK\t" + \
              " similarity score: " + "{0:.4f}".format(comp[1]) + '\n')
        idx += 1
        if idx >= 30:
            break
    out_file.write('\n')

    vorp_comps = sorted(vorp_comps.items(), key=lambda x: x[1], reverse=True)
    for comp in vorp_comps:
        out_file.write('\t' + comp[0] + " with a career VORP of " + str(comp[1]) + '\n')
    out_file.write('\n')
    out_file.write("Advanced stat comparisons:\n")
    out_file.write(college_player['Player'] + '\t\t\t' + str(college_player['PER']) + " PER/" + str(college_player['TS']) + " TS/" + str(college_player['eFG']) + " eFG/" + \
       str(college_player['ORB']) + " ORB/" + str(college_player['DRB']) + " DRB/" + \
       str(college_player['AST']) + " AST/" + str(college_player['STL']) + " STL/" + str(college_player['BLK']) + " BLK/" + \
       str(college_player['TOV']) + " TOV/" + str(college_player['USG']) + " USG/" + str(college_player['WS40']) + " WS40/" + \
       str(college_player['OBPM']) + " OBPM/" + str(college_player['DBPM']) + " DBPM\n")
    vorp_comps = {}
    # idx = 0
    for comp in adv_comparables:
        if comp[1] < 0.96:
            break
        adv_score[comp[0]] = comp[1]
        vorp_comps[comp[0]] = players[comp[0]]['VORP']
        out_file.write(comp[0] + '  ' + str(adv_players[comp[0]]['PER']) + " PER/" + str(adv_players[comp[0]]['TS']) + " TS/" + str(adv_players[comp[0]]['eFG']) + " eFG/" + \
               str(adv_players[comp[0]]['ORB']) + " ORB/" + str(adv_players[comp[0]]['DRB']) + " DRB/" + \
               str(adv_players[comp[0]]['AST']) + " AST/" + str(adv_players[comp[0]]['STL']) + " STL/" + str(adv_players[comp[0]]['BLK']) + " BLK/" + \
               str(adv_players[comp[0]]['TOV']) + " TOV/" + str(adv_players[comp[0]]['USG']) + " USG/" + str(adv_players[comp[0]]['WS40']) + " WS40/" + \
               str(adv_players[comp[0]]['OBPM']) + " OBPM/" + str(adv_players[comp[0]]['DBPM']) + " DBPM\t" + " score: " + "{0:.4f}".format(comp[1]) + '\n')
        # idx += 1
    out_file.write('\n')

    vorp_comps = sorted(vorp_comps.items(), key=lambda x: x[1], reverse=True)
    for comp in vorp_comps:
        out_file.write('\t' + comp[0] + " with a career VORP of " + str(comp[1]) + '\n')

    out_file.write("INTERSECTION OF PER40 AND ADVANCED SIMILARITIES:\n")
    # Combine two scores
    combined_scores = {x:per40_score[x]*adv_score[x] for x in per40_score if x in adv_score}
    combined_scores = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
    for score in combined_scores:
        out_file.write('\t' + score[0] + " with a combined similarity score of: " + str(score[1]) + '\n')

    out_file.write('\n')

