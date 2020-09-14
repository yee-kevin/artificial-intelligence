from search import *
import string

class Flight:
    def __init__(self, start_city, start_time, end_city, end_time):
        self.start_city = start_city
        self.start_time = start_time
        self.end_city = end_city
        self.end_time = end_time
        
    def matches(self, city_and_time):
        return (self.start_city == city_and_time[0]) and (self.start_time >= city_and_time[1])
        
    def __str__(self):
        return str((self.start_city, self.start_time))+' -> '
        + str((self.end_city, self.end_time))
    
    __repr__ = __str__

flightDB = [Flight('Rome', 1, 'Paris', 4),
            Flight('Rome', 3, 'Madrid', 5),
            Flight('Rome', 5, 'Istanbul', 10),
            Flight('Paris', 2, 'London', 4),
            Flight('Paris', 5, 'Oslo', 7),
            Flight('Paris', 5, 'Istanbul', 9),
            Flight('Madrid', 7, 'Rabat', 10),
            Flight('Madrid', 8, 'London', 10),
            Flight('Istanbul', 10, 'Constantinople', 10)]

class FlightItinerary(Problem):
    def actions(self, state):
        actions = []
        for f in range(len(flightDB)):
            if flightDB[f].matches(state):                
                actions.append((flightDB[f].end_city, flightDB[f].end_time))
        return actions

    def result(self, state, action):
        return action

    def value(self, state):
        pass
    
    def goal_test(self, state):
        return (state[1] <= self.goal[1]) and (state[0] == self.goal[0])
    
    def path_cost(self, c, state1, action, state2):
        return state2[1] - state1[1] + c

def find_itinerary(start_city, start_time, end_city, deadline):    
    flight_search = FlightItinerary((start_city, start_time), (end_city, deadline))
    try:
        plan = iterative_deepening_search(flight_search).solution()
        next_city, next_time = plan[0]
        for f in range(len(flightDB)):
            if flightDB[f].end_time == next_time and flightDB[f].end_city == next_city and flightDB[f].start_city == start_city and flightDB[f].start_time >= start_time:
                plan.insert(0, (flightDB[f].start_city, flightDB[f].start_time))
    except AttributeError:
        return 'Unable to find any possible plan.'    
    return plan

# Find the shortest itinerary by increasing the deadline one by one
def find_shortest_itinerary(start_city, end_city):
    deadline = 1
    while True:
        shortest_plan  = find_itinerary(start_city, 1, end_city, deadline)
        if type(shortest_plan) == list:
            return shortest_plan
        else:
            deadline += 1

# Find the shortest itinerary by minising the number of times the procedure calls find_itinerary
def find_shortest_itinerary_additional_challenge(start_city, end_city):
    for f in range(len(flightDB)):
        if flightDB[f].end_city == end_city:
            shortest_plan  = find_itinerary(start_city, 1, end_city, flightDB[f].end_time)
            if type(shortest_plan) == list:
                return shortest_plan
    return shortest_plan

if __name__ == '__main__':
	print("A possible plan: " + str(find_itinerary('Paris', 2, 'Constantinople', 15)) + '.')
	print("The shortest plan: " + str(find_shortest_itinerary('Rome', 'Constantinople')) + '.')
	print("The shortest plan (additional challenge): " + str(find_shortest_itinerary_additional_challenge('Rome', 'London')) + '.')