from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass

class Introduction(Page):
    pass

class Control_questions(Page):
    pass

class Start(Page):
    pass

class Round(Page):
    pass

class Decision(Page):
    pass

class Period_Result(Page):
    pass

class Round_Result(Page):
    pass

class Question_Algo (Page):
    pass

class Demographics(Page):
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
