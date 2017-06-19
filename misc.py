# Helper Module with miscellaneous functionality to make main.py more readable

import os

# Removes output files if they existed.
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


# Gathers all the season stat lines and returns them in dictionaries
def query_tables(db):

    # Gather prospect seasons
    cur = db.cursor()
    cur.execute('SELECT * FROM prosp_szns')
    prosp_szn_results = cur.fetchall()

    # Gather the Top prospects
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

    # Return the dictionaries with all the season stat lines
    return prosp_szn_results, prosp_per40_results, prosp_adv_results, comps_per40_results, comps_adv_results


# Writes a header message on the top of the output files
def initialize_output_files(divider):

    # Message to be printed at the top of each output file
    header = "A cosine similarity is computed between each prospect and NBA player, using both their per 40 minutes and advanced statistics from their NCAA seasons (collected from sports-reference.com).\n\nThe NBA players collected are every top 5 pick since 1993 that played in the NCAA, every all-star or all-NBA drafted since 1993, as well as certain exceptions from recent drafts for proper \'modern NBA\' comparisons of players who are currently contributing to an NBA team.\n"
    gist = header + '\n' + divider + '\n'

    # Write header to each output file
    out_file = open('guards.txt', 'w')
    out_file.write("An analysis of the top Guards (1s & 2s) in the 2017 NBA Draft.\n\n" + gist)
    out_file = open('wings.txt', 'w')
    out_file.write("An analysis of the top Wings (2s, 3s & small-ball 4s) in the 2017 NBA Draft.\n\n" + gist)
    out_file = open('bigs.txt', 'w')
    out_file.write("An analysis of the top Bigs (4s & 5s) in the 2017 NBA Draft.\n\n" + gist)

    # Close the output file and return it for future use
    out_file.close()
    return out_file 


# Determines the position of the prospect and opens the output file associated with that position.
def determine_output_file(prospect, prosp_szn_results):

    # Find the position of the prospect
    position = ""
    for nba_prospect in prosp_szn_results:
        key = nba_prospect['Name'] + ", " + nba_prospect['Season']
        desired_key = prospect['Player'] + ", " + prospect['Season']
        if key == desired_key:
            position = nba_prospect['Position']
            break

    # Open the file associated with the prospect's position
    if position == 'Guard':
        out_file = open('guards.txt', 'a')
    elif position == 'Wing':
        out_file = open('wings.txt', 'a')
    else:
        out_file = open('bigs.txt', 'a')    

    # Return the output file so it can be written to
    return out_file


# Writes the per 40 minute stat line that the prospect produced
def write_per40_stats(out_file, prospect):

    # Write prospect's specified college season to output file    
    out_file.write(prospect['Player'] + "\t\t\t" + str(prospect['FGP']) + " FG% / " + str(prospect['2PP']) + " 2P% / " + str(prospect['3PP']) + " 3P% /" + str(prospect['FTP']) + " FT% | \t" + \
                   str(prospect['PTS']) + " PPG / " + str(prospect['AST']) + " AST / " + str(prospect['TRB']) + " TRB /" + str(prospect['STL']) + " STL /" + str(prospect['BLK']) + " BLK /" + \
                   str(prospect['3PA']) + " 3PA /" + str(prospect['FTA']) +  " FTA\n\n")


# Writes the per 40 minute stat line that the NBA player produced during a specified NCAA season
def write_NBA_comp_per40(out_file, comp, players):

    # Write NBA player's specified college season to output file    
    out_file.write(comp[0] + '  ' + str(players[comp[0]]['FGP']) + " / " + str(players[comp[0]]['2PP']) + " / " + str(players[comp[0]]['3PP']) + " / " + str(players[comp[0]]['FTP']) + " | " + \
                   str(players[comp[0]]['PTS']) + " PPG " + str(players[comp[0]]['AST']) + " AST " + str(players[comp[0]]['TRB']) + " TRB " + str(players[comp[0]]['STL']) + " STL " + str(players[comp[0]]['BLK']) + " BLK | " + \
                   str(players[comp[0]]['3PA']) + " 3PA " + str(players[comp[0]]['FTA']) + " FTA |" + "\t{0:.4f}".format(comp[1]) + '\n')


# Writes the advanced stat line that the prospect produced
def write_adv_stats(out_file, prospect, half_divider):

    # Write prospect's specified college season to output file
    out_file.write(half_divider + prospect['Player'] + '\t\t\t' + str(prospect['PER']) + " PER/" + str(prospect['TS']) + " TS/" + \
                   str(prospect['eFG']) + " eFG/" + str(prospect['ORB']) + " ORB/" + str(prospect['DRB']) + " DRB/" + \
                   str(prospect['AST']) + " AST/" + str(prospect['STL']) + " STL/" + str(prospect['BLK']) + " BLK/" + \
                   str(prospect['TOV']) + " TOV/" + str(prospect['USG']) + " USG/" + str(prospect['WS40']) + " WS40/" + \
                   str(prospect['OBPM']) + " OBPM/" + str(prospect['DBPM']) + " DBPM\n")


# Writes the advanced stat line that the NBA player produced during a specified NCAA season
def write_NBA_comp_adv(out_file, comp, adv_players):

    # Get the NBA player's name and ignore the College and season.
    player = comp[0].split(',')[0]

    # Write NBA player's specified college season to output file
    out_file.write(player + '  ' + str(adv_players[comp[0]]['PER']) + " PER/" + str(adv_players[comp[0]]['TS']) + " TS/" + \
                   str(adv_players[comp[0]]['eFG']) + " eFG/" + str(adv_players[comp[0]]['ORB']) + " ORB/" + str(adv_players[comp[0]]['DRB']) + " DRB/" + \
                   str(adv_players[comp[0]]['AST']) + " AST/" + str(adv_players[comp[0]]['STL']) + " STL/" + str(adv_players[comp[0]]['BLK']) + " BLK/" + \
                   str(adv_players[comp[0]]['TOV']) + " TOV/" + str(adv_players[comp[0]]['USG']) + " USG/" + str(adv_players[comp[0]]['WS40']) + " WS40/" + \
                   str(adv_players[comp[0]]['OBPM']) + " OBPM/" + str(adv_players[comp[0]]['DBPM']) + " DBPM\t" + "| " + "{0:.4f}".format(comp[1]) + '\n')    


# Return the advanced stats for this particular prospect
def get_advanced_stats(prospect, prosp_adv_results):

    # Find the prospect in the advanced stats results and return his advanced stats
    for nba_prospect in prosp_adv_results:
        key = nba_prospect['Player'] + ", " + nba_prospect['Season']
        desired_key = prospect['Player'] + ", " + prospect['Season']
        if key == desired_key:
            prospect = nba_prospect
            break
    return prospect


# Writes the career VORPs (Value Over Replacement Player) of the similar NBA players to the output file
def write_NBA_player_VORPs(out_file, vorp_comps):

    # Sort the NBA players in descending order based on their career VORP 
    vorp_comps = sorted(vorp_comps.items(), key=lambda x: x[1], reverse=True)

    # Go through all the similar players and output their VORPs
    for comp in vorp_comps:
        out_file.write('\t' + comp[0] + " with a career VORP of " + str(comp[1]) + '\n')


# Finds the most similar players by taking the intersection of the per 40 minute set and advanced stat set.
# After finding the intersection, it then outputs the players in that set in descending order of the product
# of their per 40 and advanced stat similarity scores.
def intersect_similarities(out_file, per40_score, adv_score, divider):

    # Find the players who were in both sets and put the product of their similarity scores into another set
    combined_scores = {x:per40_score[x]*adv_score[x] for x in per40_score if x in adv_score}

    # Sort the combined scores into descending order of their combine similarity score
    intersection_set = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)

    # If the intersection set was empty
    if not intersection_set:
        out_file.write("\nThere are no NBA Player NCAA seasons in the intersection of the per40 and advanced similarity score sets.\n\n")
    # Otherwise, output the intersection set
    else:
        out_file.write("\nINTERSECTION OF PER40 AND ADVANCED SIMILARITIES:\n\n")
        for score in intersection_set:
            out_file.write('\t' + score[0] + " with a combined similarity score of: " + str(score[1]) + '\n')

    # Output the divider for formatting purposes
    out_file.write('\n' + divider + '\n')
