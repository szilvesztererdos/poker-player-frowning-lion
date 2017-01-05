import json
import sys

class Player:
    VERSION = "0.2"

    def betRequest(self, game_state):

        current_buy_in = game_state["current_buy_in"]
        players = game_state["players"]
        in_action = int(game_state["in_action"])
        minimum_raise = game_state["minimum_raise"]
        small_blind = game_state["small_blind"]
        hole_cards = game_state["hole_cards"]
        community_cards = game_state["community_cards"]
        

        return current_buy_in - players[in_action]["bet"] + minimum_raise * 2

    def showdown(self, game_state):
        pass
