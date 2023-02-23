from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'entry_survey'
    players_per_group = None
    num_rounds = 1
    correct_q1 = 1
    correct_q2 = 2
    correct_q3 = 3
    correct_q4 = 3
    show_up_fee = c(1.5)

# num_attention_check_tries = 2
# num_rounds = num_game_rounds + num_attention_check_tries - 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolific_id = models.StringField()
    age = models.IntegerField(label="", min=18, max=99)
    gender = models.StringField(
        choices=["Male", "Female"],
        label="",
    )
    consent = models.BooleanField(
        label="Please give your consent to this study",
        choices=[[True, "I consent"], [False, "I do not consent"]],
    )

    def consent_error_message(self, value):
        if value != True:
            return "You have to consent to this study in order to take part. If you do not, you can simply close this browser window."

    risk = models.IntegerField(
        label='''
            Please tell me, in general, how willing or unwilling you are to take risks. 
            Please use a scale from 0 to 10, where 0 means you are ”completely unwilling to take risks” 
            and a 10 means you are ”very willing to take risks”. 
            You may also use any numbers between 0 and 10 to indicate where you fall on the scale, 
            like 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            ''',
        choices=[[0, '0 '], [1, '1 '], [2, '2 '], [3, '3 '], [4, '4 '], [5, '5 '], [6, '6 '], [7, '7 '], [8, '8 '], [9, '9 '], [10, '10 ']],
    )

    major = models.IntegerField(
        label="",
        choices=[
            [1, 'Arts (e.g Visual Arts, Performing Arts'],
            [2, 'Humanities (e.g. History, Language, Literature, Philosophy'],
            [3, 'Social Sciences ( e.g. Economics, Law, Psychology)'],
            [4, 'Natural Sciences (e.g. Biology, Mathematics)'],
            [5, 'Applied Sciences (e.g. Engineering, Computer Science, Medicine and Health'],
            ],
    )
    education = models.IntegerField(
        label="",
        choices=[
            [1, 'No formal qualification'],
            [2, 'Secondary Education (e.g. GED/GCSE)'],
            [3, 'High school diploma / A Levels'],
            [4, 'Technical / Community College'],
            [5, 'Undergraduate degree (e.g. BA, BSc, other)'],
            [6, 'Graduate degree (e.g. MA, MSc, MPhil, other)'],
            [7, 'Doctorate degree (e.g. PhD, other)']
        ],
    )

    q1 = models.IntegerField(
        label="Tax payment is ..... percent of the declared income.",
        choices=[[1, "30"],
                 [2, "25"],
                 [3, "50"],
                 ],

    )

    q2 = models.IntegerField(
        label="Personal payoff depends on ......",
        choices=[
            [1, "median income"],
            [2, "after-tax profit"],
            [3, "average income"],
        ],

    )

    q3 = models.IntegerField(
        label="With a probability of ....., the provided information on the corporate income is audited.",
        choices=[[1, "15"],
                 [2, "20"],
                 [3, "30"],
                 ],
    )

    q4 = models.IntegerField(
        label="The declared corporate income can not be  ..... than the actual corporate income.",
        choices=[
            [1, "less"],
            [2, "same"],
            [3, "more"],
        ],
    )

