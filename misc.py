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


