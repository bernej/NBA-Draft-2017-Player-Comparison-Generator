# Computation Module with cosine similarity calculations

from math import sqrt


# Computes the cosine similarity value for a specified prospect and an NBA player's NCAA shooting percentages
def shot_percentage_similarity(prospect, nba_player):

    # Dot product
    numerator = float(prospect['FGP']) * float(nba_player['FGP'])
    numerator += ( float(prospect['2PP']) * float(nba_player['2PP']) )
    numerator += ( float(prospect['FTP']) * float(nba_player['FTP']) )

    # Sum of squares
    prosp_denom = (float(prospect['FGP'])**2) + (float(prospect['2PP'])**2) + (float(prospect['FTP'])**2)
    comp_denom = (float(nba_player['FGP'])**2) + (float(nba_player['2PP'])**2) + (float(nba_player['FTP'])**2)

    # If NBA player didn't take 3s and the prospect didn't take more than one 3 per game, ignore 3-point percentage and return the score as is
    if (str(nba_player['3PP']) == '0.000' or (nba_player['3PP'] is None)) and prospect['3PA'] <= 1.0:
        return numerator / (sqrt(prosp_denom) * sqrt(comp_denom))
    # If the NBA player wasn't a 3-point shooter, but the prospect is, ignore this NBA player as a comp.
    elif (str(nba_player['3PP']) == '0.000' or (nba_player['3PP'] is None)) or (nba_player['3PA'] < 1.0 and prospect['3PA'] > 1.0):
        return 0
    # Otherwise, factor in 3-point percentage
    else:
        numerator += ( float(prospect['3PP']) * float(nba_player['3PP']) )
        comp_denom += (float(nba_player['3PP'])**2)
        prosp_denom += (float(prospect['3PP'])**2)

    # Multiply the norm of the two vectors
    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    # Compute the score and return it
    score = numerator / denom
    return score


# Computes the cosine similarity value for a specified prospect and an NBA player's NCAA counting stats per 40 minutes
def per_game_similarity(prospect, nba_player):

    # Dot product
    numerator = float(prospect['PTS']) * float(nba_player['PTS'])
    numerator += ( float(prospect['AST']) * float(nba_player['AST']) )
    numerator += ( float(prospect['TRB']) * float(nba_player['TRB']) )
    numerator += ( float(prospect['STL']) * float(nba_player['STL']) )
    numerator += ( float(prospect['BLK']) * float(nba_player['BLK']) )

    # Sum of squares
    prosp_denom = (float(prospect['PTS'])**2) + (float(prospect['AST'])**2) + (float(prospect['TRB'])**2) + (float(prospect['STL'])**2) + (float(prospect['BLK'])**2)
    comp_denom = (float(nba_player['PTS'])**2) + (float(nba_player['AST'])**2) + (float(nba_player['TRB'])**2) + (float(nba_player['STL'])**2) + (float(nba_player['BLK'])**2)

    # Multiply the norm of the two vectors
    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    # Compute the score and return it
    score = numerator / denom
    return score


# Computes the cosine similarity value for a specified prospect and an NBA player's NCAA advanced stats that are between 0 and 1
def adv_rate_similarity(prospect, nba_player):

    # Dot product
    numerator = float(prospect['TS']) * float(nba_player['TS'])
    numerator += ( float(prospect['eFG']) * float(nba_player['eFG']) )    
    numerator += ( float(prospect['FTr']) * float(nba_player['FTr']) )
    numerator += ( float(prospect['WS40']) * float(nba_player['WS40']) )

    # Sum of squares
    prosp_denom = (float(prospect['TS'])**2) + (float(prospect['eFG'])**2) + (float(prospect['FTr'])**2) + (float(prospect['WS40'])**2)
    comp_denom = (float(nba_player['TS'])**2) + (float(nba_player['eFG'])**2) + (float(nba_player['FTr'])**2) + (float(nba_player['WS40'])**2)
    
    # Multiply the norm of the two vectors
    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    # Compute the score and return it
    score = numerator / denom
    return score


# Computes the cosine similarity value for a specified prospect and an NBA player's NCAA advanced stats that are between 0 and 100
def adv_percent_similarity(prospect, nba_player):

    # Dot product
    numerator = float(prospect['ORB']) * float(nba_player['ORB'])
    numerator += ( float(prospect['DRB']) * float(nba_player['DRB']) )
    numerator += ( float(prospect['AST']) * float(nba_player['AST']) )
    numerator += ( float(prospect['STL']) * float(nba_player['STL']) )
    numerator += ( float(prospect['BLK']) * float(nba_player['BLK']) )
    numerator += ( float(prospect['TOV']) * float(nba_player['TOV']) )
    numerator += ( float(prospect['USG']) * float(nba_player['USG']) )    

    # Sum of squares
    prosp_denom = (float(prospect['ORB'])**2) + (float(prospect['DRB'])**2) + (float(prospect['AST'])**2) + (float(prospect['STL'])**2) + \
                  (float(prospect['BLK'])**2) + (float(prospect['TOV'])**2) + (float(prospect['USG'])**2)

    comp_denom = (float(nba_player['ORB'])**2) + (float(nba_player['DRB'])**2) + (float(nba_player['AST'])**2) + (float(nba_player['STL'])**2) + \
                  (float(nba_player['BLK'])**2) + (float(nba_player['TOV'])**2) + (float(nba_player['USG'])**2)

    # Multiply the norm of the two vectors
    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    # Compute the score and return it
    score = numerator / denom
    return score


# Computes the cosine similarity value for a specified prospect and an NBA player's NCAA Player Efficiency Rating and Offensive & Defensive Box Plus Minus values
def adv_misc_similarity(prospect, nba_player):

    # Dot product
    numerator = float(prospect['PER']) * float(nba_player['PER'])
    numerator += ( float(prospect['OBPM']) * float(nba_player['OBPM']) )
    numerator += ( float(prospect['DBPM']) * float(nba_player['DBPM']) )    

    # Sum of squares
    prosp_denom = (float(prospect['PER'])**2) + (float(prospect['OBPM'])**2) + (float(prospect['DBPM'])**2)
    comp_denom = (float(nba_player['PER'])**2) + (float(nba_player['OBPM'])**2) + (float(nba_player['DBPM'])**2)

    # Multiply the norm of the two vectors
    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    # Compute the score and return it
    score = numerator / denom
    return score
