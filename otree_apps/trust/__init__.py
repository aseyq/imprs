from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'trust'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    ENDOWMENT = cu(10)  ####
    MULTIPLIER = 3  ####

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    sent = models.CurrencyField(label="Please tell us the amount you'd like to send.",
                                min=0, max=C.ENDOWMENT)      ###
    returned = models.CurrencyField(label="Please tell us the amount you'd like to return",
                                    min=0)  ###
    
    budget_p2 = models.CurrencyField()

class Player(BasePlayer):
    pass

## Functions
def set_payoffs(group):

    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)

    p1.payoff = C.ENDOWMENT - group.sent + group.returned
    p2.payoff = group.sent * C.MULTIPLIER - group.returned



def set_payoffs2(group):

    players = group.get_players()

    for p in players:
        if p.id_in_group == 1: # trustor
            p.payoff = C.ENDOWMENT - group.sent + group.returned

        if p.id_in_group == 2: # trustee
            p.payoff = group.sent * C.MULTIPLIER - group.returned


# PAGES
class Send(Page):
    form_fields = ['sent']
    form_model = Group

    def is_displayed(player):
        return player.id_in_group == 1
    
    def before_next_page(player, timeout_happened):
        ### this runs only after the page is succesfully submitted
        player.group.budget_p2 = player.group.sent * C.MULTIPLIER

class WaitForP1(WaitPage):
    pass

class Returning(Page):
    form_fields = ['returned']
    form_model = Group

    def is_displayed(player):
        return player.id_in_group == 2

### form conditions
def returned_max(group):
    return group.budget_p2
###---------------

class WaitForP2(WaitPage):
    
    def after_all_players_arrive(group):
        set_payoffs(group)

class Results(Page):
    pass


page_sequence = [Send, WaitForP1, Returning, WaitForP2, Results]
