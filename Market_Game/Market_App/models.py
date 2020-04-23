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


doc = """
2 firms complete in a market by setting prices for homogenous goods.
See "Kruse, J. B., Rassenti, S., Reynolds, S. S., & Smith, V. L. (1994).
Bertrand-Edgeworth competition in experimental markets.
Econometrica: Journal of the Econometric Society, 343-371."
"""


class Constants(BaseConstants):
    players_per_group = 3
    name_in_url = 'market_game'
    num_rounds = 3


    # payoff if all play high""",
    player_high_hhh_payoff = c(800)

    # payoff if 2 players play high and the other low""",
    player_low_lhh_payoff = c(1440)
    player_high_lhh_payoff = c(0)


    # payoff if 2 players play low and the other high""",
    player_low_llh_payoff = c(720)

    # payoff if all play low""",
    player_low_lll_payoff = c(480)

class Subsession(BaseSubsession):
   #  def get_player_by_id(self):
    #    if self.round_number ==1:
    #        player1 = self.get_player_by_id_(1)
    #        player2 = self.get_player_by_id_(2)
    #        player3 = self.get_player_by_id_(3)
    #    else:
    #        self.group_like_round(1)
    pass

class Group(BaseGroup):

    def set_payoffs(self):
        player1 = self.get_player_by_id(1)
        player2 = self.get_player_by_id(2)
        player3 = self.get_player_by_id(3)

        if player1.decision == 100:
                if player2.decision == 60:
                    if player3.decision == 100:
                        player1.payoff = Constants.player_high_lhh_payoff
                        player2.payoff = Constants.player_low_lhh_payoff
                        player3.payoff = Constants.player_high_lhh_payoff
                    else:
                        player1.payoff = Constants.player_high_lhh_payoff
                        player2.payoff = Constants.player_low_llh_payoff
                        player3.payoff = Constants.player_low_llh_payoff
                else:
                    if player3.decision == 60:
                        player1.payoff = Constants.player_high_lhh_payoff
                        player2.payoff = Constants.player_high_lhh_payoff
                        player3.payoff = Constants.player_low_lhh_payoff
                    else:
                        player1.payoff = Constants.player_high_hhh_payoff
                        player2.payoff = Constants.player_high_hhh_payoff
                        player3.payoff = Constants.player_high_hhh_payoff
        else:
            if player2.decision == 60:
                if player3.decision == 100:
                    player1.payoff = Constants.player_low_llh_payoff
                    player2.payoff = Constants.player_low_llh_payoff
                    player3.payoff = Constants.player_high_lhh_payoff
                else:
                    player1.payoff = Constants.player_low_lll_payoff
                    player2.payoff = Constants.player_low_lll_payoff
                    player3.payoff = Constants.player_low_lll_payoff
            else:
                if player3.decision == 100:
                    player1.payoff = Constants.player_low_lhh_payoff
                    player2.payoff = Constants.player_high_lhh_payoff
                    player3.payoff = Constants.player_high_lhh_payoff
                else:
                    player1.payoff = Constants.player_low_llh_payoff
                    player2.payoff = Constants.player_high_lhh_payoff
                    player3.payoff = Constants.player_low_llh_payoff

class Player(BasePlayer):
    decision = models.IntegerField(
        choices=[60, 100],
        doc ="Zu welchem Preis möchten Sie ihr Gut anbieten",
        widget=widgets.RadioSelect,
    )

