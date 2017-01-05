import json

class Player:
    VERSION = "Default Python folding player+1"

    def betRequest(self, game_state):
        game_state_obj = json.loads(game_state)
        current_buy_in = game_state_obj["current_buy_in"]
        players = game_state_obj["players"]
        in_action = game_state_obj["in_action"]
        bet = game_state_obj["bet"]
        minimum_raise = game_state_obj["minimum_raise"]
        return current_buy_in - players[in_action][bet] + minimum_raise

    def showdown(self, game_state):
        pass

