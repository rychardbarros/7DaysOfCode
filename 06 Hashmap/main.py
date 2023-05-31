class Game():
    def __init__(self):
        self.score = {}

    def add_player(self, user):
        self.score[user] = 0
    
    def update_score(self, user, score):
        if user in self.score:
            self.score[user] += score

