# -*- coding: utf-8 -*-
# CREDIT TO: https://github.com/perrygeo/simanneal/tree/951e7d89a8b7f19aeb05b64e7cc8b844a734af89
from __future__ import print_function
import itertools
import math
import random
import matplotlib.pyplot as plt
from collections import defaultdict
from simanneal import Annealer
import threading
import queue
from collections import OrderedDict


def distance(a, b):
    """Calculates distance between two latitude-longitude coordinates."""
    R = 3963  # radius of Earth (miles)
    lat1, lon1 = math.radians(a[0]), math.radians(a[1])
    lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * R


class TravellingSalesmanProblem(Annealer):

    """Test annealer with a travelling salesman problem.
    """

    # pass extra data (the distance matrix) into the constructor
    def __init__(self, state, distance_matrix):
        self.distance_matrix = distance_matrix
        super(TravellingSalesmanProblem, self).__init__(state)  # important!

    def move(self):
        """Swaps two cities in the route."""
        # no efficiency gain, just proof of concept
        # demonstrates returning the delta energy (optional)
        initial_energy = self.energy()

        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

        return self.energy() - initial_energy

    def energy(self):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(self.state)):
            e += self.distance_matrix[self.state[i-1]][self.state[i]]
        return e


def print_route(route):
    for c in route:
        print(c)


def plot_route(route, cities, title):
    x1 = []
    y1 = []
    for k, (x, y) in cities.items():
        x1.append(x)
        y1.append(y)

    plt.scatter(x1, y1)
    plt.title(title)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    plt.draw()

    # Connect cities based on states

    x2 = []
    y2 = []
    for city in route:
        x2.append(cities[city][0])
        y2.append(cities[city][1])

    # Append route back to original
    x2.append(cities[route[0]][0])
    y2.append(cities[route[0]][1])

    plt.plot(x2, y2, '-o')

    plt.show()


#### BEGIN GREEDY ####


def greedy(cities, start_city):
    final_order = []
    min_length = float('inf')

    for city_name in cities.keys():
        order = [city_name]
        length = 0

        next_city, distance = get_nearest_neighbor(cities, order, city_name)
        length = length + distance
        order.append(next_city)

        while len(order) < len(cities):
            next_city, distance = get_nearest_neighbor(cities, order, next_city)
            length = length + distance

            order.append(next_city)
        # Append return length of route
        return_dist = get_distance_in_miles(order[0], order[len(order) - 1], cities)
        length = length + return_dist

        if length < min_length:
            min_length = length
            final_order = order

    return final_order, min_length


def get_distance_in_miles(city1, city2, cities):
    """Calculates distance between two latitude-longitude coordinates."""
    a = cities[city1]
    b = cities[city2]

    R = 3963  # radius of Earth (miles)
    lat1, lon1 = math.radians(a[0]), math.radians(a[1])
    lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * R


def get_nearest_neighbor(cities, visited, city):
    min_dist = float('inf')
    closest_city = None

    for c in cities:
        if c not in visited:
            dist = get_distance_in_miles(city, c, cities)

            if dist < min_dist:
                closest_city = c
                min_dist = dist

    return closest_city, min_dist


def get_distance(city1, city2, cities):
    return math.sqrt((cities[city2][0] - cities[city1][0]) ** 2 + (cities[city2][1] - cities[city1][1]) ** 2)

#### END GREEDY ####

def calc_distance_of_route(route, cities):
    length = 0
    for i in range(len(route) - 1):
        length = length + get_distance_in_miles(route[i], route[i+1], cities)

    # Add in return distance
    length = length + get_distance_in_miles(route[0], route[len(route) - 1], cities)


    
    return length


def run_sim_anneal(cities, result_queue):
      # initial state, a randomly-ordered itinerary
    init_state = list(cities)
    random.shuffle(init_state)

    # create a distance matrix
    distance_matrix = defaultdict(dict)
    for ka, va in cities.items():
        for kb, vb in cities.items():
            distance_matrix[ka][kb] = 0.0 if kb == ka else distance(va, vb)

    tsp = TravellingSalesmanProblem(init_state, distance_matrix)
    tsp.set_schedule(tsp.auto(minutes=0.2))
    # tsp.set_schedule(tsp.auto(minutes=0.001))

    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"
    state, e = tsp.anneal()

    while state[0] != 'New York City':
        state = state[1:] + state[:1]  # rotate NYC to start

    result_queue.put((state, e))


# def brute_force_tsp(cities):
#     print("Brute forcing TSP...")
#     ordered_dict = OrderedDict()
#     # Convert dict to orderedDict
#     cities
#     for key, val in cities.items():
#         citi

#     # generate all permutations of indices
#     indices = []
#     for i in range(len(cities)):
#         indices.append(i)

#     min_length = float('inf')
#     best_route = []
#     all_perms = itertools.permutations(indices)
#     print(all_perms)
#     for perm in all_perms:
#         if calc_distance_of_route
    
#     print(ordered_dict)


def test_algorithms(cities):
    num_threads = 1
    result_queue = queue.Queue()
    for i in range(num_threads):
        x = threading.Thread(target=run_sim_anneal,
                             args=(cities, result_queue,))
        x.start()
        x.join()
        # result_queue.get()


    # Print Threading results and get best distance
    best_distance = float('inf')
    best_route = []
    for i in range(num_threads):
        result_candidate = result_queue.get()
        if result_candidate[1] < best_distance:
            best_distance = result_candidate[1]
            best_route = result_candidate[0]

    print("Parallel Simulated Annealing Results: ")
    print('Best Route: ' + str(best_route))
    print('Distance of route: ' + str(best_distance))

    plot_route(best_route, cities, 'Simulated Annealing Route: ' +
               str(int(best_distance)) + ' Miles')

    greedy_route, min_dist = greedy(cities, 'New York City')
    plot_route(greedy_route, cities, 'Greedy Algorithm Route: ' +
               str(int(min_dist)) + ' Miles')

    print("Local Greedy Results: ")
    print('Best Route: ' + str(greedy_route))
    print('Distance of route: ' + str(min_dist))

if __name__ == '__main__':

    # latitude and longitude for the five largest U.S. cities
    cities5 = {
        'New York City': (40.72, 74.00),
        'Los Angeles': (34.05, 118.25),
        'Chicago': (41.88, 87.63),
        'Houston': (29.77, 95.38),
        'Phoenix': (33.45, 112.07),
    }

    # latitude and longitude for the ten largest U.S. cities
    cities10 = {
        'New York City': (40.72, 74.00),
        'Los Angeles': (34.05, 118.25),
        'Chicago': (41.88, 87.63),
        'Houston': (29.77, 95.38),
        'Phoenix': (33.45, 112.07),
        'Philadelphia': (39.95, 75.17),
        'San Antonio': (29.53, 98.47),
        'Dallas': (32.78, 96.80),
        'San Diego': (32.78, 117.15),
        'San Jose': (37.30, 121.87),
    }

    # latitude and longitude for the twenty largest U.S. cities
    cities20 = {
        'New York City': (40.72, 74.00),
        'Los Angeles': (34.05, 118.25),
        'Chicago': (41.88, 87.63),
        'Houston': (29.77, 95.38),
        'Phoenix': (33.45, 112.07),
        'Philadelphia': (39.95, 75.17),
        'San Antonio': (29.53, 98.47),
        'Dallas': (32.78, 96.80),
        'San Diego': (32.78, 117.15),
        'San Jose': (37.30, 121.87),
        'Detroit': (42.33, 83.05),
        'San Francisco': (37.78, 122.42),
        'Jacksonville': (30.32, 81.70),
        'Indianapolis': (39.78, 86.15),
        'Austin': (30.27, 97.77),
        'Columbus': (39.98, 82.98),
        'Fort Worth': (32.75, 97.33),
        'Charlotte': (35.23, 80.85),
        'Memphis': (35.12, 89.97),
        'Baltimore': (39.28, 76.62)
    }

    # latitude and longitude for the thirty largest U.S. cities
    cities30 = {
        'New York City': (40.72, 74.00),
        'Los Angeles': (34.05, 118.25),
        'Chicago': (41.88, 87.63),
        'Houston': (29.77, 95.38),
        'Phoenix': (33.45, 112.07),
        'Philadelphia': (39.95, 75.17),
        'San Antonio': (29.53, 98.47),
        'Dallas': (32.78, 96.80),
        'San Diego': (32.78, 117.15),
        'San Jose': (37.30, 121.87),
        'Detroit': (42.33, 83.05),
        'San Francisco': (37.78, 122.42),
        'Jacksonville': (30.32, 81.70),
        'Indianapolis': (39.78, 86.15),
        'Austin': (30.27, 97.77),
        'Columbus': (39.98, 82.98),
        'Fort Worth': (32.75, 97.33),
        'Charlotte': (35.23, 80.85),
        'Memphis': (35.12, 89.97),
        'Baltimore': (39.28, 76.62),
        'Boston': (42.71, 71.5),
        'El Paso': (31.46, 106.29),
        'Nashville': (36.10, 86.47),
        'Detroit': (42.20, 83.3),
        'Oklahoma City': (35.26, 97.28),
        'Portland': (45.31, 122.41),
        'Las Vegas': (36.10, 115.12),
        'Louisville': (38.15, 85.46),
        'MilWaukee': (43.2, 87.55),
        'Albuquerque': (35.05, 106.39)
    }

    test_algorithms(cities30)
    # brute_force_tsp(cities5)
   


