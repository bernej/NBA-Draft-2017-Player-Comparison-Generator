import os

def remove_output_files():
    try:
        os.remove('guards.txt')
    except OSError:
        pass
    try:
        os.remove('wings.txt')
    except OSError:
        pass
    try:
        os.remove('bigs.txt')
    except OSError:
        pass

def query_tables(db):
    # Gather prospect seasons
    cur = db.cursor()
    cur.execute('SELECT * FROM prosp_szns')
    prosp_szn_results = cur.fetchall()

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

    return prosp_szn_results, prosp_per40_results, prosp_adv_results, comps_per40_results, comps_adv_results

def initialize_output_files(divider):
    calculation_gist = "A cosine similarity is computed between each prospect and NBA player, using both their per 40 minutes and advanced statistics using their NCAA seasons (collected from sports-reference.com).\n\nThe NBA players collected are every top 5 pick since 1993 that played in the NCAA, every all-star or all-NBA drafted since 1993, as well as certain exceptions from recent drafts for proper \'modern NBA\' comparison who are currently contributing to an NBA team.\n"
    gist = calculation_gist + '\n' + divider + '\n'
    out_file = open('guards.txt', 'w')
    out_file.write("An analysis of the top Guards (1s & 2s) in the 2017 NBA Draft. " + gist)
    out_file = open('wings.txt', 'w')
    out_file.write("An analysis of the top Wings (3s & 4s) in the 2017 NBA Draft. " + gist)
    out_file = open('bigs.txt', 'w')
    out_file.write("An analysis of the top Bigs (4s & 5s) in the 2017 NBA Draft. " + gist)
    return out_file 

def determine_output_file(prospect, prosp_szn_results):
    position = ""
    for nba_prospect in prosp_szn_results:
        key = nba_prospect['Name'] + ", " + nba_prospect['Season']
        desired_key = prospect['Player'] + ", " + prospect['Season']
        if key == desired_key:
            position = nba_prospect['Position']
            break

    if position == 'Guard':
        out_file = open('guards.txt', 'a')
    elif position == 'Wing':
        out_file = open('wings.txt', 'a')
    else:
        out_file = open('bigs.txt', 'a')    

    return out_file

def write_per40_stats(out_file, prospect):
    out_file.write(prospect['Player'] + "\t\t\t" + str(prospect['FGP']) + " FG% / " + str(prospect['2PP']) + " 2P% / " + str(prospect['3PP']) + " 3P% /" + str(prospect['FTP']) + " FT% | \t" + \
                   str(prospect['PTS']) + " PPG / " + str(prospect['AST']) + " AST / " + str(prospect['TRB']) + " TRB /" + str(prospect['STL']) + " STL /" + str(prospect['BLK']) + " BLK\n\n")

def write_NBA_comp_per40(out_file, comp, players):
    out_file.write(comp[0] + '  ' + str(players[comp[0]]['FGP']) + " FG% " + str(players[comp[0]]['2PP']) + " 2P% " + str(players[comp[0]]['3PP']) + " 3P% " + str(players[comp[0]]['FTP']) + " FT% | " + \
                   str(players[comp[0]]['PTS']) + " PPG " + str(players[comp[0]]['AST']) + " AST " + str(players[comp[0]]['TRB']) + " TRB " + str(players[comp[0]]['STL']) + " STL " + str(players[comp[0]]['BLK']) + " BLK  " + \
                   "score: " + "{0:.4f}".format(comp[1]) + '\n')

def write_adv_stats(out_file, college_player, half_divider):
    out_file.write(half_divider + college_player['Player'] + '\t\t\t' + str(college_player['PER']) + " PER/" + str(college_player['TS']) + " TS/" + str(college_player['eFG']) + " eFG/" + \
       str(college_player['ORB']) + " ORB/" + str(college_player['DRB']) + " DRB/" + \
       str(college_player['AST']) + " AST/" + str(college_player['STL']) + " STL/" + str(college_player['BLK']) + " BLK/" + \
       str(college_player['TOV']) + " TOV/" + str(college_player['USG']) + " USG/" + str(college_player['WS40']) + " WS40/" + \
       str(college_player['OBPM']) + " OBPM/" + str(college_player['DBPM']) + " DBPM\n")

def write_NBA_comp_adv(out_file, comp, adv_players):
    player = comp[0].split(',')[0]
    out_file.write(player + '  ' + str(adv_players[comp[0]]['PER']) + " PER/" + str(adv_players[comp[0]]['TS']) + " TS/" + str(adv_players[comp[0]]['eFG']) + " eFG/" + \
           str(adv_players[comp[0]]['ORB']) + " ORB/" + str(adv_players[comp[0]]['DRB']) + " DRB/" + \
           str(adv_players[comp[0]]['AST']) + " AST/" + str(adv_players[comp[0]]['STL']) + " STL/" + str(adv_players[comp[0]]['BLK']) + " BLK/" + \
           str(adv_players[comp[0]]['TOV']) + " TOV/" + str(adv_players[comp[0]]['USG']) + " USG/" + str(adv_players[comp[0]]['WS40']) + " WS40/" + \
           str(adv_players[comp[0]]['OBPM']) + " OBPM/" + str(adv_players[comp[0]]['DBPM']) + " DBPM\t" + "| " + "{0:.4f}".format(comp[1]) + '\n')    

def get_advanced_stats(prospect, prosp_adv_results):
    for nba_prospect in prosp_adv_results:
        key = nba_prospect['Player'] + ", " + nba_prospect['Season']
        desired_key = prospect['Player'] + ", " + prospect['Season']
        if key == desired_key:
            college_player = nba_prospect
            break
    return college_player

def write_NBA_player_VORPs(out_file, vorp_comps):
    vorp_comps = sorted(vorp_comps.items(), key=lambda x: x[1], reverse=True)
    for comp in vorp_comps:
        out_file.write('\t' + comp[0] + " with a career VORP of " + str(comp[1]) + '\n')

def intersect_similarities(out_file, per40_score, adv_score, divider):
    out_file.write("\nINTERSECTION OF PER40 AND ADVANCED SIMILARITIES:\n\n")
    # Combine two scores
    combined_scores = {x:per40_score[x]*adv_score[x] for x in per40_score if x in adv_score}
    combined_scores = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
    for score in combined_scores:
        out_file.write('\t' + score[0] + " with a combined similarity score of: " + str(score[1]) + '\n')

    out_file.write('\n' + divider + '\n')



