from search import Problem


class WaterJug(Problem):
    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def value(self, state):
        pass

    def __init__(self, initial, goal):
        self.goal = goal
        self.initial = initial
        self.visited_states = []
        Problem.__init__(self, self.initial, self.goal)
        

    def __repr__(self):
        return "< State (%s, %s) >" % (self.initial, self.goal)

    def goal_test(self, state):
        return state == self.goal

    def actions(self, cur_state):
        actions = []
        self.visited_states.append(cur_state)
        # umplem ulciorul de 4 litri
        if(cur_state[0] == 0):
            new_state= (4,cur_state[1])
            actions.append(new_state)
        #umplem ulciorul de 3 litri
        if(cur_state[1] == 0):
            new_state= (cur_state[0],3)
            actions.append(new_state)
        #golim ulciorul de 4 litri
        if(cur_state[0]==4):
            new_state= (0,cur_state[1])
            actions.append(new_state)
        #golim ulciorul de 3 litri
        if(cur_state[1]==3):
            new_state= (cur_state[0],0)
            actions.append(new_state)
        #turnam din ulciorul de 3 litri in cel de 4 litri o cantitate astfel incat ulciorul de 4 litri este plin
        if(cur_state[0]+cur_state[1] >= 4 and cur_state[1] > 0):
          new_state= (4, cur_state[1] - (4-cur_state[0]))
          actions.append(new_state)
        #turnam din ulciorul de 4 litri in cel de 3 litri o cantitate astfel incat ulciorul de 3 litri este plin
        if(cur_state[0]+cur_state[1] >= 3 and cur_state[0] > 0):
          new_state= (cur_state[0] - (3-cur_state[1]), 3)
          actions.append(new_state)
        #turnam din ulciorul de 3 litri in cel de 4 litri astfel incat primul ulcior sa aiba cantitatea de apa din cele doua, iar al doilea sa fie gol
        if(cur_state[0]+cur_state[1] <= 4 and cur_state[1] > 0):
          new_state= (cur_state[0]+cur_state[1], 0)
          actions.append(new_state)
        #turnam din ulciorul de 4 litri in cel de 3 litri astfel incat al doilea ulcior sa aiba cantitatea de apa din cele doua ,iar primul sa fie gol
        if(cur_state[0]+cur_state[1] <= 3 and cur_state[0] > 0):
          new_state= (0,cur_state[0]+cur_state[1])
          actions.append(new_state)


        return actions
