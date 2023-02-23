from ._builtin import Page
from .models import Constants


class GeneralInformation(Page):
    form_model = "player"
    form_fields = ['consent']

    def is_displayed(self):
        return self.round_number == 1


class Survey(Page):
    form_model = "player"
    form_fields = ["prolific_id", "risk", "age", "gender", "major", "education"]

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.participant.vars['gender'] = self.player.gender


# def error_message(self, values):
#    if len(values['prolific_id']) != 24:
#        return 'Please, enter a valid Prolific ID'

class GameInfo1(Page):
    form_model = "player"
    form_fields = ["q1", "q2"]

    def q1_error_message(self, value):
        if value != 2:
            return 'Wrong answer, please answer again'

    def q2_error_message(self, value):
        if value != 2:
            return 'Wrong answer, please answer again'


class GameInfo2(Page):
    form_model = "player"
    form_fields = ["q3", "q4"]

    def q3_error_message(self, value):
        if value != 3:
            return 'Wrong answer, please answer again'

    def q4_error_message(self, value):
        if value != 3:
            return 'Wrong answer, please answer again'


class GameInfo3(Page):
    pass


page_sequence = [GeneralInformation, Survey, GameInfo1, GameInfo2, GameInfo3]

