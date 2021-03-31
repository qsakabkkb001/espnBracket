import pickle
import math

class Team:
    def __init__(self, region, seed, name):
        assert region in ['West', 'East', 'South', 'Midwest']
        assert 0<seed<17
        self.region = region
        self.seed = seed
        self.name = name
    
    def __str__(self):
        return '('+self.name+', '+str(self.seed)+', '+self.region+')'

    def return_seed(self):
        return self.seed

    def return_region(self):
        return self.region

    def return_name(self):
        return self.name

class MatchUp:
    def __init__(self, team1=None, team2=None, roundNum=None):
        self.team1 = team1
        self.team2 = team2
        self.roundNum = roundNum
        self.winner = None
        self.pick = None
        self.score = 0

    def __str__(self):
        ret = ''
        if self.team1 is None:
            ret+= 'Team1 not set'
        else:
            ret+=self.team1.__str__()
        ret += ', '
        if self.team2 is None:
            ret+= 'Team2 not set'
        else:
            ret+=self.team2.__str__()
        ret+= ', '
        if self.roundNum is None:
            ret+= 'Round number is not set'
        else:
            ret+=str(self.roundNum)
        ret+= ', '
        if self.pick is None:
            ret+= 'Pick not set'
        else:
            ret+='Pick is: '
            ret+=self.pick.__str__()
        ret+= ', '
        if self.winner is None:
            ret+= 'Winner not set'
        else:
            ret+='Winner is: '
            ret+=self.winner.__str__()
        return ret

    def set_pick(self, pick):
        self.pick = pick
    
    def set_winner(self, t):
        self.winner = t
        if self.winner.return_name() == self.pick.return_name():
            self.score = (math.pow(2, self.roundNum-1))*10

    def return_score(self):
        return self.score

    def get_roundNum(self):
        return self.roundNum

    def get_pick(self):
        return self.pick

    def get_winner(self):
        return self.winner

class Bracket:
    def __init__(self, teams):
        self.teams = teams
        self.bracket = self.create_initial_bracket()
        self.winnerIndex = 0
                
    def __str__(self):
        ret = ''
        for m in self.bracket:
            ret+=m.__str__()
            ret+='\n'
        return ret

    def create_initial_bracket(self):
        iBracket = list()
        for i in range(0, len(self.teams), 2):
            m = MatchUp(self.teams[i], self.teams[i+1], roundNum=1)
            iBracket.append(m)
        return iBracket

    def set_picks(self, picks):
        for i in range(len(picks), 0, -1):
            self.bracket[-i].set_pick(picks[-i])
        try:
            self.update_bracket(picks)
        except:
            pass

    def set_winners(self, winners):
        for i in range(len(winners)):
            self.bracket[self.winnerIndex+i].set_winner(winners[i])
        self.winnerIndex+=len(winners)

    def update_bracket(self, picks):
        roundNum = self.bracket[-1].get_roundNum()+1
        for i in range(0, len(picks), 2):
            m = MatchUp(picks[i], picks[i+1], roundNum=roundNum)
            self.bracket.append(m)
    
    def get_score(self):
        score = 0
        for m in self.bracket:
            if m.get_winner() is not None:
                score += m.return_score()
        return score

    def seed_sort(self, region):
        return [team for team in sorted(region, key=lambda team: team.return_seed())] 
