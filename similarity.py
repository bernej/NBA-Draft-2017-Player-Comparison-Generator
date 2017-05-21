from math import sqrt

def shot_percentage_similarity(prospect, nba_player):

    numerator = float(prospect['FGP']) * float(nba_player['FGP'])
    numerator += ( float(prospect['2PP']) * float(nba_player['2PP']) )
    numerator += ( float(prospect['FTP']) * float(nba_player['FTP']) )

    prosp_denom = (float(prospect['FGP'])**2) + (float(prospect['2PP'])**2) + (float(prospect['FTP'])**2)
    comp_denom = (float(nba_player['FGP'])**2) + (float(nba_player['2PP'])**2) + (float(nba_player['FTP'])**2)

    # Ignore players who didn't take any 3s; similarity score was getting skewed
    if (str(nba_player['3PP']) == '0.000' or (nba_player['3PP'] is None)) and prospect['3PA'] <= 1.0:
        return numerator / (sqrt(prosp_denom) * sqrt(comp_denom))
    elif (str(nba_player['3PP']) == '0.000' or (nba_player['3PP'] is None)) or (nba_player['3PA'] < 1.0 and prospect['3PA'] > 1.0):
        return 0
    else:
        numerator += ( float(prospect['3PP']) * float(nba_player['3PP']) )
        comp_denom += (float(nba_player['3PP'])**2)
        prosp_denom += (float(prospect['3PP'])**2)

    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    score = numerator / denom

    return score

def per_game_similarity(prospect, nba_player):

    numerator = float(prospect['PTS']) * float(nba_player['PTS'])
    numerator += ( float(prospect['AST']) * float(nba_player['AST']) )
    numerator += ( float(prospect['TRB']) * float(nba_player['TRB']) )
    numerator += ( float(prospect['STL']) * float(nba_player['STL']) )
    numerator += ( float(prospect['BLK']) * float(nba_player['BLK']) )

    prosp_denom = (float(prospect['PTS'])**2) + (float(prospect['AST'])**2) + (float(prospect['TRB'])**2) + (float(prospect['STL'])**2) + (float(prospect['BLK'])**2)
    comp_denom = (float(nba_player['PTS'])**2) + (float(nba_player['AST'])**2) + (float(nba_player['TRB'])**2) + (float(nba_player['STL'])**2) + (float(nba_player['BLK'])**2)

    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    score = numerator / denom

    return score

def shot_attempt_similarity(prospect, nba_player):
    numerator = float(prospect['FGA']) * float(nba_player['FGA'])
    numerator += ( float(prospect['2PA']) * float(nba_player['2PA']) )
    numerator += ( float(prospect['FTA']) * float(nba_player['FTA']) )

    prosp_denom = (float(prospect['FGA'])**2) + (float(prospect['2PA'])**2) + (float(prospect['FTA'])**2)
    comp_denom = (float(nba_player['FGA'])**2) + (float(nba_player['2PA'])**2) + (float(nba_player['FTA'])**2)

    # Ignore players who didn't take any 3s; similarity score was getting skewed
    if str(nba_player['3PA']) == '0.0' or nba_player['3PA'] is None:
        return 0
    else:
        numerator += ( float(prospect['3PA']) * float(nba_player['3PA']) )
        comp_denom += (float(nba_player['3PA'])**2)
        prosp_denom += (float(prospect['3PA'])**2)

    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    score = numerator / denom

    return score

def adv_rate_similarity(prospect, nba_player):
    numerator = float(prospect['TS']) * float(nba_player['TS'])
    numerator += ( float(prospect['eFG']) * float(nba_player['eFG']) )    
    numerator += ( float(prospect['FTr']) * float(nba_player['FTr']) )
    numerator += ( float(prospect['WS40']) * float(nba_player['WS40']) )

    prosp_denom = (float(prospect['TS'])**2) + (float(prospect['eFG'])**2) + (float(prospect['FTr'])**2) + (float(prospect['WS40'])**2)
    comp_denom = (float(nba_player['TS'])**2) + (float(nba_player['eFG'])**2) + (float(nba_player['FTr'])**2) + (float(nba_player['WS40'])**2)
    
    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    score = numerator / denom

    return score

def adv_percent_similarity(prospect, nba_player):
    numerator = float(prospect['ORB']) * float(nba_player['ORB'])
    numerator += ( float(prospect['DRB']) * float(nba_player['DRB']) )
    numerator += ( float(prospect['AST']) * float(nba_player['AST']) )
    numerator += ( float(prospect['STL']) * float(nba_player['STL']) )
    numerator += ( float(prospect['BLK']) * float(nba_player['BLK']) )
    numerator += ( float(prospect['TOV']) * float(nba_player['TOV']) )
    numerator += ( float(prospect['USG']) * float(nba_player['USG']) )    

    prosp_denom = (float(prospect['ORB'])**2) + (float(prospect['DRB'])**2) + (float(prospect['AST'])**2) + (float(prospect['STL'])**2) + \
                  (float(prospect['BLK'])**2) + (float(prospect['TOV'])**2) + (float(prospect['USG'])**2)

    comp_denom = (float(nba_player['ORB'])**2) + (float(nba_player['DRB'])**2) + (float(nba_player['AST'])**2) + (float(nba_player['STL'])**2) + \
                  (float(nba_player['BLK'])**2) + (float(nba_player['TOV'])**2) + (float(nba_player['USG'])**2)

    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    score = numerator / denom

    return score

def adv_misc_similarity(prospect, nba_player):
    numerator = float(prospect['PER']) * float(nba_player['PER'])
    numerator += ( float(prospect['OBPM']) * float(nba_player['OBPM']) )
    numerator += ( float(prospect['DBPM']) * float(nba_player['DBPM']) )    

    prosp_denom = (float(prospect['PER'])**2) + (float(prospect['OBPM'])**2) + (float(prospect['DBPM'])**2)
    comp_denom = (float(nba_player['PER'])**2) + (float(nba_player['OBPM'])**2) + (float(nba_player['DBPM'])**2)

    denom = sqrt(prosp_denom) * sqrt(comp_denom)

    score = numerator / denom

    return score
