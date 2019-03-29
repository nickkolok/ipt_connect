# -*- coding: utf-8 -*-

# Views parameters
app_version = "repnoe7"     # keyword for url parsing
NAME = {
    'short': 'Золотое сечение',
    'full': 'Турнир "Золотое сечение" в Репном'
}

# Models parameters
npf = 4                 # Number of Physics fights
with_final_pf = False    # Is there a Final Fight ?
reject_malus = 0.2      # Malus for too many rejections
npfreject_max = 3       # Maximum number of tactical rejection (per fight)
netreject_max = 1       # Maximum number of eternal rejection

# Personal ranking
personal_ranking = {
    'active': True,
    'rep_threshold': 5,
    'opp_threshold': 5,
    'rev_threshold': 5,
    'rep_coeff': 3,
    'opp_coeff': 2,
    'rev_coeff': 1
}

# Calculating the mean
mean = 'ipt_mean'  # String with name of function for calculating mean (ipt_mean or iypt_mean)
