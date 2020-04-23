import self
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Start(Page):
    def is_displayed(self):
        if self.round_number == 1 or self.round_number == 2 + Constants.extra_rounds_sg1 or self.round_number == 3 + Constants.extra_rounds_sg1 + Constants.extra_rounds_sg2:
            return True


class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
    pass


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Period_Result(Page):
    pass


class Round_Result(Page):
    def is_displayed(self):
        if self.round_number == 1 + Constants.extra_rounds_sg1 \
                or self.round_number == 2 + Constants.extra_rounds_sg1 + Constants.extra_rounds_sg2 \
                or self.round_number == 3 + Constants.extra_rounds_sg1 + Constants.extra_rounds_sg2 + Constants.extra_rounds_sg3:
            return True


class Final_Result(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        all_players = self.player.in_all_rounds()
        round_payoff = 0
        for player in all_players:
            round_payoff += player.payoff
        return {"round_payoff": round_payoff}


page_sequence = [Introduction, Start, Decision, ResultsWaitPage, Period_Result, Round_Result, Final_Result]
