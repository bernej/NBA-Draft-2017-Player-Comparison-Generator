from extensions import connect_to_database
from similarity import *
from misc import *

db = connect_to_database()

# NBA players in the database. Consists of every top 5 pick since the 1993 draft
# as well as every all star drafted since 1993. Additionally, contains more
# active players than retired, i.e. players who are 
players = {}        # NBA Players mapped to their NCAA seasonal per 40 minutes stats
adv_players = {}    # NBA Players mapped to their NCAA seasonal advanced stats

# Grab all the data from the tables in the database
prosp_szn_results, prosp_per40_results, prosp_adv_results, comps_per40_results, comps_adv_results = query_tables(db)

# For refreshing guards.txt, wings.txt, and bigs.txt
remove_output_files()

# Formatting strings
divider = "______________________________________________________________________________________________________________________________________\n"
half_divider = "\n___________________________________________________________________\n\n"

# Output file to write to. Either guards.txt, wings.txt, or bigs.txt
out_file = initialize_output_files(divider)

# Go through each prospect and compute their similarity to every NBA player in the database
for prospect in prosp_per40_results:

    # This variable will contain the prospect's advanced stats after the per40 similarity score is computed
    college_player = {}

    # Find the prospect's position and return that position-specific output file
    out_file = determine_output_file(prospect, prosp_szn_results)

    write_per40_stats(out_file, prospect) # Output this prospect's per 40 stats

    # Mapping of NBA players to their cosine similarity values pertaining to this particular prospect
    per40_comparables = {}  # Per 40 minutes similarity scores
    adv_comparables = {}    # Advanced stats similarity scores

    # Go through each NBA player and compute their per 40 min. cosine similarity score
    for nba_player in comps_per40_results:

        # NBA Player and their respective NCAA season
        comp_key = nba_player['Player'] + ", " + nba_player['Season'] + ", " + nba_player['School']

        # Map this NBA player to their NCAA season
        players[comp_key] = nba_player

        # Looks at FG%, 2P%, 3P%, and FT%
        per40_comparables[comp_key] = shot_percentage_similarity(prospect, nba_player)

        # Looks at PTS, AST, TRBs, STLs, and BLKs
        per40_comparables[comp_key] *= per_game_similarity(prospect, nba_player)

    # seasons that have complete advanced stats from sports-reference.com
    adv_seasons = ['11','12','13','14','15','16']

    # Go through each NBA player and compute their adv stats cosine similarity score
    for nba_player in comps_adv_results:

        # Need to get this prospect's advanced stats.
        college_player = get_advanced_stats(prospect, prosp_adv_results)

        # Seasons before 2010-11 do not have complete advanced stats. This check
        # makes sure that we are getting a player who's NCAA season came 2010-11 or later
        if any(season in nba_player['Season'] for season in adv_seasons):

            # NBA Player and their respective NCAA season
            comp_key = nba_player['Player'] + ", " + nba_player['Season'] + ", " + nba_player['School']

            # Map this NBA player to their NCAA season
            adv_players[comp_key] = nba_player

            # Looks at TS%, eFG%, FTr, and WS/40
            adv_comparables[comp_key] = adv_rate_similarity(college_player, nba_player)

            # Looks at ORB%, DRB%, AST%, STL%, BLK%, TOV%, and USG%
            adv_comparables[comp_key] *= adv_percent_similarity(college_player, nba_player)

            # Looks at PER, OBPM, and DBPM
            adv_comparables[comp_key] *= adv_misc_similarity(college_player, nba_player)

    # Sort the similarity scores into descending order
    per40_comparables = sorted(per40_comparables.items(), key=lambda x: x[1], reverse=True)
    adv_comparables = sorted(adv_comparables.items(), key=lambda x: x[1], reverse=True)

    # Dictionaries used for determing the intersection of per40 and adv scores
    per40_score = {}
    adv_score = {}

    # Output the Top 30 per 40 minute similarity scores for this prospect
    out_file.write("Per 40 minute comparisons:\n\n")
    vorp_comps = {}     # NBA Players mapped to their career Value Over Replacement Player value
    
    # Go through the Top 30 per 40 minute similarity scores
    idx = 0
    for comp in per40_comparables:
        # Map this score for possible future intersection calculation
        per40_score[comp[0]] = comp[1]
        # Map this NBA player's VORP
        vorp_comps[comp[0]] = players[comp[0]]['VORP']
        # Output this NBA player's per 40 minute stats for this NCAA season
        write_NBA_comp_per40(out_file, comp, players)
        # Check if the index has exceeded 30
        idx += 1
        if idx >= 30:
            break

    # Output the Top 30 per 40 minutes NBA comps in descending order based on their career VORPs
    out_file.write('\nThe Top 30 per 40 minute NBA comps sorted in descending order based on their career VORPs:\n\n')
    write_NBA_player_VORPs(out_file, vorp_comps)

    # Output the prospect's advanced stats
    write_adv_stats(out_file, college_player, half_divider)

    # Output the advanced stat similarity scores for the prospect that are 0.96 or above
    out_file.write("\nAdvanced stat comparisons:\n")
    vorp_comps = {}     # Reset the VORP mappings.

    # Go through the Top 30 advanced stats similarity scores
    idx = 0
    for comp in adv_comparables:
        # Map this score for possible future intersection calculation
        adv_score[comp[0]] = comp[1]
        # Map this NBA player's VORP
        vorp_comps[comp[0]] = players[comp[0]]['VORP']
        # Output this NBA player's advanced stats for this NCAA season
        write_NBA_comp_adv(out_file, comp, adv_players)
        # Check if the index has exceeded 30
        idx += 1
        if idx >= 30:
            break  

    # Output the Top 30 advanced stats NBA comps in descending order based on their career VORPs
    out_file.write('\nThe Top 30 advanced stats NBA comps sorted in descending order based on their career VORPs:\n\n')
    write_NBA_player_VORPs(out_file, vorp_comps)

    # Compute intersection similarities for players who appeared in both sets
    intersect_similarities(out_file, per40_score, adv_score, divider)
    # Close output file and move on to next prospect
    out_file.close()
