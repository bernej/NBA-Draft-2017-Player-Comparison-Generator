from math import sqrt

def shot_percentage_similarity(prospect, nba_player):

    numerator = float(prospect['FGP']) * float(nba_player['FGP'])
    numerator += ( float(prospect['2PP']) * float(nba_player['2PP']) )
    numerator += ( float(prospect['FTP']) * float(nba_player['FTP']) )

    prosp_denom = (float(prospect['FGP'])**2) + (float(prospect['2PP'])**2) + (float(prospect['FTP'])**2)
    comp_denom = (float(nba_player['FGP'])**2) + (float(nba_player['2PP'])**2) + (float(nba_player['FTP'])**2)

    # Ignore players who didn't take any 3s; similarity score was getting skewed
    if str(nba_player['3PP']) == '0.000' or nba_player['3PP'] is None:
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