from search import *
import string

# README: Select and set search methods ('breadth_first_tree_search'/'depth_first_tree_search'/'depth_first_graph_search'/'breadth_first_search'/'uniform_cost_search'/'depth_limited_search'/'iterative_deepening_search'/'astar_search')

def is_valid_word(word):
    return word in WORDS

WORDS = set(i.lower().strip() for i in open('words2.txt'))

class WordLadder(Problem):
    def actions(self, state):
        actions = []
        numberOfLetters = len(state)
        # for each letter in the state, replace each letter with a lowercase alphabet,
        # determine if possible action is a valid word and append to a list of possible actions
        for l in range(numberOfLetters):            
            for a in lowercase_alphabets: 
                if state[l] != a:
                    possible_action = state[:l] + a + state[l+1:]
                    if is_valid_word(possible_action):
                        actions.append(possible_action)
        return actions

    def result(self, state, action):
        return action

    def value(self, state):
        pass
    
    # Heuristics: Used for astar search to estimate distance from current state to goal state
    #             by checking the difference in the number of letters
    def h(self, n):
        heuristic = 0
        for l in range(len(n.state)):
            if self.goal_test(n.state) != True:
                heuristic += 1
        return heuristic

def get_solution(word_ladder, search_method):
    try:        
        actions = ""
        if search_method == 'breadth_first_tree_search':
            actions = breadth_first_tree_search(word_ladder).solution() 
        elif search_method == 'depth_first_tree_search':
            actions = depth_first_tree_search(word_ladder).solution()
        elif search_method == 'depth_first_graph_search':
            actions = depth_first_graph_search(word_ladder).solution()
        elif search_method == 'breadth_first_search':
            actions = breadth_first_search(word_ladder).solution()
        elif search_method == 'uniform_cost_search':
            actions = uniform_cost_search(word_ladder).solution()
        elif search_method == 'depth_limited_search':
            actions = depth_limited_search(word_ladder).solution()
        elif search_method == 'iterative_deepening_search':
            actions = iterative_deepening_search(word_ladder).solution()
        elif search_method == 'astar_search':
            actions = astar_search(word_ladder).solution()            
            
        if actions != "":
            print("initial state:'{}'".format(str(word_ladder.initial)) + " -> "
                      + "actions:{}".format(actions))
            
    except AttributeError:
        print("initial state:'{}'".format(str(word_ladder.initial)) + " -> unable to find any solution")


if __name__ == '__main__':
    WORDS = set(i.lower().strip() for i in open('words2.txt'))    
    def is_valid_word(word):
        return word in WORDS
    lowercase_alphabets = string.ascii_lowercase
    
    # README: Set search methods ('breadth_first_tree_search'/'depth_first_tree_search'/'depth_first_graph_search'/
    #   'breadth_first_search'/'uniform_cost_search'/'depth_limited_search'/'iterative_deepening_search'/'astar_search')
    search_method = 'breadth_first_tree_search'
    
    test_cases = [("cars", "cats"), ("cold", "warm"), ("best", "math")]
    print("search_method: " + str(search_method))
    for test_case in test_cases:        
        get_solution(WordLadder(test_case[0],test_case[1]), search_method)