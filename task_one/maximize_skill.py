class SkillMaximizer:
    def __init__(self, N, M, A, B):
        self.N = N
        self.M = M
        self.A = A
        self.B = B

    def solve(self):
        # The combination of each opponent's skill level and the skill boost obtained
        players = list(zip(self.A, self.B))
        
        # Sort players by skill level (Ai)
        players.sort(key=lambda x: x[0])
        
        current_skill = self.M
        
        for skill, boost in players:
            if current_skill >= skill:
                current_skill += boost
            else:
                break
        
        return current_skill