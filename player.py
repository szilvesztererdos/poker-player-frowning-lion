import json
import sys

class Player:
    VERSION = "0.2"

    def betRequest(self, game_state):

        current_buy_in = game_state["current_buy_in"]
        players = game_state["players"]
        in_action = int(game_state["in_action"])
        print(in_action)
        minimum_raise = game_state["minimum_raise"]
        
        return current_buy_in - players[in_action]["bet"] + minimum_raise

    def showdown(self, game_state):
        pass
