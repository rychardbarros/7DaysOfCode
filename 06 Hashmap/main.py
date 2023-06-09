class Game():
    def __init__(self):
        self.score = {}

    def add_player(self, user):
        self.score[user] = 0
    
    def update_score(self, user, score):
        if user in self.score:
            self.score[user] += float(score)

    def remove_user(self, user):
        del self.score[user]

    def list_score(self):
        if len(self.score) == 0:
            print('Não há jogadores no momento!!!')
            return
        ranking = sorted(self.score.items(), key=lambda x: x[1], reverse=True)
        for user, score in ranking:
            print(f'{user}, pontos: {score}')

    def get_winner(self):
        max_score = max(self.score.values())
        for user, score in self.score.items():
            if score == max_score:
                print(f'O vencedor foi {user} com {score} pontos')
        return user

game = Game()

game.add_player('MrRychk')
game.add_player('italoMtitus')
game.add_player('r3nanp')

game.update_score('MrRychk', '80')
game.update_score('italoMtitus', '60')
game.update_score('r3nanp', '40')

game.list_score()

game.remove_user('r3nanp')

game.list_score()

game.get_winner()

