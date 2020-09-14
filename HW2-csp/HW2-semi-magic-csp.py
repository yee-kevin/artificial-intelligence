import pdb
from csp import *
from random import shuffle

def solve_semi_magic(algorithm=backtracking_search, **args):
    """ From CSP class in csp.py
        vars        A list of variables; each is atomic (e.g. int or string).
        domains     A dict of {var:[possible_value, ...]} entries.
        neighbors   A dict of {var:[var,...]} that for each variable lists
                    the other variables that participate in constraints.
        constraints A function f(A, a, B, b) that returns true if neighbors
                    A, B satisfy the constraint when they have values A=a, B=b
                    """
    # Use the variable names in the figure
    csp_vars = ['V%d'%d for d in range(1,10)]

    #########################################
    # Fill in these definitions

    csp_domains = {}
    csp_neighbors = {}

    for var_i, var in enumerate(csp_vars):
        csp_domains[var] = [1, 2, 3]
        row = (var_i // 3) + 1
        col = (var_i % 3) + 1
        
        row_values = [((row-1)*3) + i + 1 for i in range(3)]
        col_values = [(col-1) + 3*i + 1 for i in range(3)]
        diag_values = []
        
        if row == col:
            diag_values = [1, 5, 9]
        
        neighbors = row_values + col_values + diag_values
        neighbors[:] = sorted(value for value in neighbors if value != var_i+1)
        csp_neighbors["V" + str(var_i+1)] = ["V" + str(n) for n in neighbors]


    def csp_constraints(A, a, B, b):
        if a != b:
            return True
        else:
            return False
        pass

    #########################################
    
    # define the CSP instance
    csp = CSP(csp_vars, csp_domains, csp_neighbors,
              csp_constraints)

    # run the specified algorithm to get an answer (or None)
    ans = algorithm(csp, **args)
    
    print ('number of assignments', csp.nassigns)
    assign = csp.infer_assignment()
    if assign:
        for x in sorted(assign.items()):
            print (x)
    return csp


if __name__ == '__main__':
    # select_unassigned_variable
    variable_ordering = [first_unassigned_variable, mrv]

    # order_domain_values
    value_ordering = [unordered_domain_values, lcv]

    # inference
    inference = [no_inference, forward_checking, mac]

    for i in variable_ordering:
        for j in value_ordering:
            for k in inference:
                print('variable ordering:{}, value_ordering:{}, inference:{}'.format(i.__name__, j.__name__, k.__name__))
                solve_semi_magic(backtracking_search,
                                select_unassigned_variable = i,
                                order_domain_values = j,
                                inference=k)