import self
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
    pass



class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Period_Result(Page):
    pass
#    def vars_for_template(self):
#      me = self.player
#      opponent_1 = me.other_player_1()
#      opponent_2 = me.other_player_2()
#       return dict(
#           my_decision=me.decision,
#           opponent_1_decision=opponent_1.decision,
#           opponent_2_decision=opponent_2.decision,)
#           #same_choice=me.decision == opponent_1.decision == opponent_2.decision,)


class Round_Result (Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        all_players = self.player.in_all_rounds()
        round_payoff = 0
        for player in all_players:
            round_payoff += player.payoff
        return {"round_payoff": round_payoff}


page_sequence = [Introduction,Start,Decision, ResultsWaitPage, Period_Result, Round_Result]
