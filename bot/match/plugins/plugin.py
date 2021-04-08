class Plugin:
    def __init__(self, match):
        self.match = match

    def on_match_launching(self):
        pass

    def on_captain_selected(self):
        pass

    def on_teams_done(self):
        pass

    def on_faction_pick(self, team):
        pass

    def on_factions_picked(self):
        pass

    def on_base_selected(self, base):
        pass

    def on_team_ready(self, team):
        pass

    def on_match_starting(self):
        pass

    def on_round_over(self):
        pass

    def on_match_over(self):
        pass
