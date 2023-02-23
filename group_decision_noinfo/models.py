
from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random
import itertools
from numpy import median
author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'group_decision_noinfo'
    players_per_group = 3
    num_groups = 20
    num_rounds = 1
    company_income = c(800)
    tax_multiplier = 0.25
    payoff_multiplier = 0.20
    show_up_fee = c(1.5)
    divisor = 100


class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        print('in group_by_arrival_time_method')

        m_players = [p for p in waiting_players if p.participant.vars['gender'] == 'Male']
        f_players = [p for p in waiting_players if p.participant.vars['gender'] == 'Female']

        if len(m_players) >= 2 and len(f_players) >= 1:
            print('about to create a group')
            return [m_players[0], m_players[1], f_players[0]]
        elif len(f_players) >= 2 and len(m_players) >= 1:
            print('about to create a group')
            return [f_players[0], f_players[1], m_players[0]]
        print('not enough players yet to create a group')

    group_counter = models.IntegerField(initial=0)
    group_counter_1m2f = models.IntegerField(initial=0)
    group_counter_2m1f = models.IntegerField(initial=0)


class Group(BaseGroup):
    audited = models.BooleanField(initial=False)
    random_value = models.FloatField(initial=0)
    total_income_entered = models.IntegerField(initial=0)
    females_in_group_counter = models.IntegerField(initial=0)

    def set_payoffs(self):
        self.random_value = random.random()
        if self.random_value < 0.3:
            self.audited = True
        players = self.get_players()
        income_entered = [p.income_entered for p in players]
        self.total_income_entered = median(income_entered)
        tax_payment = Constants.tax_multiplier * self.total_income_entered
        unpaid_tax = Constants.tax_multiplier * (Constants.company_income - self.total_income_entered)
        for player in players:
            if self.audited:
                if Constants.company_income == self.total_income_entered:
                    player.payoff = (((Constants.payoff_multiplier * (Constants.company_income - tax_payment)) / Constants.divisor) + Constants.show_up_fee)
                else:
                    player.payoff = (((Constants.payoff_multiplier * (Constants.company_income - tax_payment - (2 * unpaid_tax))) / Constants.divisor) + Constants.show_up_fee)
            else:
                player.payoff = (((Constants.payoff_multiplier * (Constants.company_income - tax_payment)) / Constants.divisor) + Constants.show_up_fee)


class Player(BasePlayer):
    income_entered = models.IntegerField(label="Please declare the corporate income", min=0, max=800)








