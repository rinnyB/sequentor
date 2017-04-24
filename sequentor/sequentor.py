from Sequentor.func_list import func_list
class sequentor():
    def __init__(self, state):
        self.state = state
        self.actions = []

    def add_action(self,action):
        self.actions.append(action)
        return self

    def evaluate(self):
        for elem in self.actions:
            self.state = eval( str(self.state) + elem)
        if isinstance(self.state, list):
            return func_list(self.state)
        else:
            return self.state
            
    def show_graph(self):
        s = ""
        for i in range(len(self.actions)):
            if i == 0:
                s += str(self.state) +"\n{0}|\n{0}+---+>  ".format(i*4*" ")+ str(self.actions[i]) + "\n"
            else:
                s += "{0}|\n{0}+---+>  ".format(i*4*" ")+ str(self.actions[i]) + "\n"
        print(s)
