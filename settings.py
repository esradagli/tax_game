from os import environ

SESSION_CONFIGS = [
    dict(
        name='Groupthink_noinfo',
        display_name="Groupthink No Info",
        num_demo_participants=12,
        app_sequence=['entry_survey', 'group_decision_noinfo'],
     ),
    dict(
        name='Groupthink_info',
        display_name="Groupthink Info",
        num_demo_participants=12,
        app_sequence=['entry_survey', 'group_decision_info'],
     ),
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=100, participation_fee=1.50, doc="")

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'



# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '_*43f16+uc@9o_$&n3e=ithdb@j#h42pq)=t2@xd=6ad985+8@'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
