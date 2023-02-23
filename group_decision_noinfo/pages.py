from ._builtin import Page, WaitPage
import time
import random


class GroupingWaitPage(WaitPage):
    title_text ="Please do not close the browser, we are searching for other participants. Also, we are tracking your waiting time. If you have waited for more than 5 mins, you are free to leave the experiment and you will receive 50 pence as a compensation. "
    group_by_arrival_time = True


class Decision(Page):
    form_model = 'player'
    form_fields = ['income_entered']

    def before_next_page(self):
        if self.player.id_in_group == 1:
            for p in self.group.get_players():
                if p.participant.vars['gender'] == 'Female':
                    self.group.females_in_group_counter += 1
            if self.group.females_in_group_counter == 1:
                self.subsession.group_counter_2m1f += 1
            elif self.group.females_in_group_counter == 2:
                self.subsession.group_counter_1m2f += 1
        if self.subsession.group_counter_2m1f >= 2.00:
            self.session.vars['enough 2m1f groups'] = 'yes'
            print(self.session.vars['enough 2m1f groups'])
        elif self.subsession.group_counter_1m2f >= 2.00:
            self.session.vars['enough 1m2f groups'] = 'yes'
            print(self.session.vars['enough 1m2f groups'])
        self.subsession.group_counter += 1
        if self.subsession.group_counter >= 4.00:
            self.session.vars['enough groups'] = 'yes'
            print(self.session.vars['enough groups'])




class AfterDecision(WaitPage):
    title_text = "Don't close the browser!! Payoffs are calculating."
    after_all_players_arrive = 'set_payoffs'


class Result(Page):
    pass


page_sequence = [GroupingWaitPage, Decision, AfterDecision, Result]
