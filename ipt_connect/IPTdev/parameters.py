# -*- coding: utf-8 -*-

from parameters_TTH2020 import *



NAME = {
    'short': 'ТТН 2020 Тест',
    'full': 'Турнир Трёх Наук 2020 - тестовый инстанс',
    # ... and the name used in tournament overview
    'front': 'Федерального Студенческого Турнира Трёх Наук',
}

# Tournaments to switch to by the menu
# Usually you should set it to None
# This is useful only for development and first stages of Three Science Tournament
sister_tournaments = (
	('Дальневосточный и Сибирский ФО','/TTH2020EAST/'),
	('Уральский ФО'                  ,'/TTH2020URAL/'),
	('Северо-Западный ФО'            ,'/TTH2020NW/'  ),
	('Центральный ФО'                ,'/TTH2020CFO/' ),
	('Приволжский ФО'                ,'/TTH2020POV/' ),
	('Северо-Кавказский ФО'          ,'/TTH2020SKFO/'),
	('Южный ФО'                      ,'/TTH2020YUG/' ),
	('Международный этап'            ,'/TTH2020INT/' ),
)

poster_url = ''

website_url = 'http://iturnir.ru'


# Tactical rejections
enable_tactical_rejections = True # False e.g. for IYPT
npfreject_max = 2       # Maximum number of free tactical rejections (per fight)
enable_eternal_rejections = True # False e.g. for IPT 2020
netreject_max = 2       # Maximum number of free eternal rejections
enable_apriori_rejections = False # False in most cases

# The precision of scores
# If 'None', no round up is made
# If an integer N, then the scores for each Round are rounded up to 10^(-N)
score_precision = 2 #TODO: use the same precision when displaying the results (as for now, it is always 2)


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

if instance_name == 'TTH2020EAST':
	NAME = {
		'short': 'ТТН 2020 ДФО и СФО',
		'full': 'Турнир Трёх Наук 2020 - Дальневосточный и Сибирский федеральные округа',
		# ... and the name used in tournament overview
		'front': 'отборочного этапа Федерального Студенческого Турнира Трёх Наук в Дальневосточном и Сибирском федеральных округах',
	}

	poster_url = ''

	website_url = 'http://iturnir.ru'


	npfreject_max = 2       # Maximum number of tactical rejection (per fight)
	netreject_max = 2       # Maximum number of eternal rejection


	# Is the fight status displayed?
	# Looks like there are some problems with it, so making it switchable
	display_pf_status = False


elif instance_name == 'TTH2020URAL':
	NAME = {
		'short': 'ТТН 2020 УФО',
		'full': 'Турнир Трёх Наук 2020 - Уральский федеральный округ',
		# ... and the name used in tournament overview
		'front': 'отборочного этапа Федерального Студенческого Турнира Трёх Наук в Уральском федеральном округе',
	}

	poster_url = ''

	website_url = 'http://iturnir.ru'


	npfreject_max = 2       # Maximum number of tactical rejection (per fight)
	netreject_max = 2       # Maximum number of eternal rejection


	# Is the fight status displayed?
	# Looks like there are some problems with it, so making it switchable
	display_pf_status = False


elif instance_name == 'TTH2020NW':
	NAME = {
		'short': 'ТТН 2020 СЗФО',
		'full': 'Турнир Трёх Наук 2020 - Северо-Западный федеральный округ',
		# ... and the name used in tournament overview
		'front': 'отборочного этапа Федерального Студенческого Турнира Трёх Наук в Северо-Западном федеральном округе',
	}

	poster_url = ''

	website_url = 'http://iturnir.ru'


	npfreject_max = 2       # Maximum number of tactical rejection (per fight)
	netreject_max = 2       # Maximum number of eternal rejection


	# Is the fight status displayed?
	# Looks like there are some problems with it, so making it switchable
	display_pf_status = False


elif instance_name == 'TTH2020INT':
	NAME = {
		'short': 'ТТН 2020 Международный',
		'full': 'Турнир Трёх Наук 2020 - Международный',
		# ... and the name used in tournament overview
		'front': 'Международного отборочного этапа Федерального Студенческого Турнира Трёх Наук',
	}

	poster_url = ''

	website_url = 'http://iturnir.ru'


	npfreject_max = 2       # Maximum number of tactical rejection (per fight)
	netreject_max = 2       # Maximum number of eternal rejection


	# Is the fight status displayed?
	# Looks like there are some problems with it, so making it switchable
	display_pf_status = False


elif instance_name == 'TTH2020CFO':
	NAME = {
		'short': 'ТТН 2020 ЦФО',
		'full': 'Турнир Трёх Наук 2020 - Центральный федеральный округ',
		# ... and the name used in tournament overview
		'front': 'отборочного этапа Федерального Студенческого Турнира Трёх Наук в Центральном федеральном округе',
	}

	poster_url = ''

	website_url = 'http://iturnir.ru'


	npfreject_max = 2       # Maximum number of tactical rejection (per fight)
	netreject_max = 2       # Maximum number of eternal rejection


	# Is the fight status displayed?
	# Looks like there are some problems with it, so making it switchable
	display_pf_status = False


elif instance_name == 'TTH2020POV':
	NAME = {
		'short': 'ТТН 2020 ПФО',
		'full': 'Турнир Трёх Наук 2020 - Приволжский федеральный округ',
		# ... and the name used in tournament overview
		'front': 'отборочного этапа Федерального Студенческого Турнира Трёх Наук в Приволжском федеральном округе',
	}

	poster_url = ''

	website_url = 'http://iturnir.ru'


	npfreject_max = 2       # Maximum number of tactical rejection (per fight)
	netreject_max = 2       # Maximum number of eternal rejection


	# Is the fight status displayed?
	# Looks like there are some problems with it, so making it switchable
	display_pf_status = False


elif instance_name == 'TTH2020SKFO':
	NAME = {
		'short': 'ТТН 2020 СКФО',
		'full': 'Турнир Трёх Наук 2020 - Северо-Кавказский федеральный округ',
		# ... and the name used in tournament overview
		'front': 'отборочного этапа Федерального Студенческого Турнира Трёх Наук в Северо-Кавказском федеральном округе',
	}

	poster_url = ''

	website_url = 'http://iturnir.ru'


	npfreject_max = 2       # Maximum number of tactical rejection (per fight)
	netreject_max = 2       # Maximum number of eternal rejection


	# Is the fight status displayed?
	# Looks like there are some problems with it, so making it switchable
	display_pf_status = False


elif instance_name == 'TTH2020YUG':
	NAME = {
		'short': 'ТТН 2020 ЮФО',
		'full': 'Турнир Трёх Наук 2020 - Южный федеральный округ',
		# ... and the name used in tournament overview
		'front': 'отборочного этапа Федерального Студенческого Турнира Трёх Наук в Южном федеральном округе',
	}

	poster_url = ''

	website_url = 'http://iturnir.ru'


	npfreject_max = 2       # Maximum number of tactical rejection (per fight)
	netreject_max = 2       # Maximum number of eternal rejection


	# Is the fight status displayed?
	# Looks like there are some problems with it, so making it switchable
	display_pf_status = False
