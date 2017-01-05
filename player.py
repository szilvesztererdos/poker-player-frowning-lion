import json
import sys
import operator

class Player:
    VERSION = "0.3"

    def betRequest(self, game_state):

        current_buy_in = game_state["current_buy_in"]
        players = game_state["players"]
        in_action = int(game_state["in_action"])
        minimum_raise = game_state["minimum_raise"]
        small_blind = game_state["small_blind"]
        hole_cards = players[in_action]["hole_cards"]
        community_cards = game_state["community_cards"]
        #stack = game_state["stack"]

        figures_count = dict()
        colors_count = dict()

        for card in hole_cards:
            if card["rank"] in figures_count:
                figures_count[card["rank"]] += 1
            else:
                figures_count[card["rank"]] = 1
            
            if card["suit"] in colors_count:
                colors_count[card["suit"]] += 1
            else:
                colors_count[card["suit"]] = 1

        for card in community_cards:
            if card["rank"] in figures_count:
                figures_count[card["rank"]] += 1
            else:
                figures_count[card["rank"]] = 1
            
            if card["suit"] in colors_count:
                colors_count[card["suit"]] += 1
            else:
                colors_count[card["suit"]] = 1

        figures_count_sorted = sorted(figures_count.items(), key=operator.itemgetter(1), reverse=True)
        colors_count_sorted = sorted(colors_count.items(), key=operator.itemgetter(1), reverse=True)

        decision_value = max(figures_count_sorted[0][1], colors_count_sorted[0][1])

        if decision_value < 2:
            return 0
        elif decision_value < 3:
            return current_buy_in - players[in_action]["bet"] + minimum_raise
        elif decision_value < 4:
            return current_buy_in - players[in_action]["bet"] + small_blind * 4
        else:
            return 10000

    def showdown(self, game_state):
        pass
