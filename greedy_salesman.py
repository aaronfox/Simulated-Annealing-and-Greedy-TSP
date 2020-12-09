import numpy as np
import math

""" Note: this code was only used as a test protype of the greedy algorith. The entire implementation can be found in salesman.py """
def greedy(cities, start_city):
    """ Implements greedy algorithm of TSP given a set of cities """

    final_order = []
    min_length = float('inf')

    for i in range(len(cities)):
        order = [start_city]
        length = 0

        next_city, distance = get_nearest_neighbor(cities, order, start_city)
        length = length + distance
        order.append(next_city)

        while len(order) < len(cities):
            next_city, distance = get_nearest_neighbor(cities, order, next_city)
            length = length + distance
            order.append(next_city)

        if length < min_length:
            min_length = length
            final_order = order
        
    return final_order, min_length


def get_distance_in_miles(city1, city2, cities):
    """Calculates distance between two latitude-longitude coordinates."""
    a = cities[city2]
    b = cities[city1]

    R = 3963  # radius of Earth (miles)
    lat1, lon1 = math.radians(a[0]), math.radians(a[1])
    lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)) * R

def get_nearest_neighbor(cities, visited, city):
    """ Gets nearest neighbor and returns the city name and the distance """
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
    """ Returns Euclidean distance between two cities """
    return math.sqrt((cities[city2][0] - cities[city1][0]) ** 2 + (cities[city2][1] - cities[city1][1]) ** 2)

if __name__ == '__main__':

    # latitude and longitude for the twenty largest U.S. cities
    cities = {
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

    print(greedy(cities, 'New York City'))
