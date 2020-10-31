# -*- coding: utf-8 -*-

from parameters_TTH2020 import *



NAME = {
    'short': 'ТТН 2019 Приволжье',
    'full': 'Турнир Трёх Наук 2019 - Приволжский этап',
    # ... and the name used in tournament overview
    'front': 'Приволжский этап Федерального Студенческого Турнира Трёх Наук',
}

# Tournaments to switch to by the menu
# Usually you should set it to None
# This is useful only for development and first stages of Three Science Tournament
sister_tournaments = (
	('IPT dev','/IPT'+'dev/'),
	('IPT dev (pf2)','/IPT'+'dev_pf2/'),
)

poster_url = ''

website_url = 'http://iturnir.ru'


# Tactical rejections
enable_tactical_rejections = True # False e.g. for IYPT - TODO
npfreject_max = 2       # Maximum number of free tactical rejections (per fight)
enable_eternal_rejections = True # False e.g. for IPT 2020 - TODO
netreject_max = 2       # Maximum number of free eternal rejections
enable_apriori_rejections = False # False in most cases - TODO

# The precision of scores
# If 'None', no round up is made
# If an integer N, then the scores for each Round are rounded up to 10^(-N)
score_precision = None #TODO: use the same precision when displaying the results (as for now, it is always 2)


# Is the fight status displayed?
# Looks like there are some problems with it, so making it switchable
display_pf_status = False

## Options for participants overview
display_participants_avg_grade_tot = True # Mean grade
display_participants_avg_grade_rep = True # Mean Rep. grade
display_participants_avg_grade_opp = True # Mean Opp. grade
display_participants_avg_grade_rev = True # Mean Rev. grade
display_participants_max_grade_tot = True # Best grade
display_participants_max_grade_rep = True # Best Rep. grade
display_participants_max_grade_opp = True # Best Opp. grade
display_participants_max_grade_rev = True # Best Rev. grade
display_participants_sum_grade_tot = True # Total points

