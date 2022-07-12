class Node:
    def __init__(self, title, children = [], condition = lambda: True):
        self.children = children
        self.title = title
        self.condition = condition
    def get_next(self):
        for child in self.children:
            if child.condition():
                return child
    def print_path(self):
        print( " => " + self.title )
        if self.children:
            self.get_next().print_path()
    def print_tree(self, level = 1):
        print("=" * level + ">" + self.title)
        for child in self.children:
            child.print_tree(level + 1)


# starting variables
is_poisoned = True

ending_poisoned = Node("Hero is poisoned. Hero dies.")

poisoned = Node("Hero is poisoned", [ending_poisoned], lambda: is_poisoned )
not_poisoned = Node("Hero is not poisoned",[], lambda: not is_poisoned)

start = Node("Start of player", [poisoned, not_poisoned])


start.print_tree()
