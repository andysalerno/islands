from __future__ import print_function
from random import randint
import sys


# return list of all immediate land neighbors of the land at (j, k)
def get_neighbors(j, k, island_map):
    neighbors_found = []
    if (j + 1, k) in island_map and island_map[(j + 1, k)] == 1:
        neighbors_found.append((j + 1, k))
    if (j - 1, k) in island_map and island_map[(j - 1, k)] == 1:
        neighbors_found.append((j - 1, k))
    if (j, k - 1) in island_map and island_map[(j, k - 1)] == 1:
        neighbors_found.append((j, k - 1))
    if (j, k + 1) in island_map and island_map[(j, k + 1)] == 1:
        neighbors_found.append((j, k + 1))
    return neighbors_found


# given a starting point, recursively check each neighboring island for more neighbors and return list of all coords
def recursive_search(j, k, map, all_neighbors=None):
    if all_neighbors is None:
        all_neighbors = []
    neighbors_found = get_neighbors(j, k, map)  # get list of all neighbors
    neighbors_found = [x for x in neighbors_found if x not in all_neighbors]  # remove neighbors we've seen before

    all_neighbors.extend(neighbors_found)
    for neighbor in neighbors_found:
        results = recursive_search(neighbor[0], neighbor[1], map, all_neighbors)
        all_neighbors.extend(results)
    return all_neighbors


def print_map(map, height, width):
    for j in range(height):
        for k in range(width):
            print(map[j, k], end='')
            if k == width - 1:
                print()


def populate_map(map, height, width):
    for j in range(height):
        for k in range(width):
            map[j, k] = randint(0, 1)
    print_map(map, height, width)
    return map


def main():
    island_count = 0
    map_height = 10
    map_width = 10
    island_map = {}  # matrix of coordinates with either 1 or 0. In this case, assume this matrix is populated.
    visited = []  # list of coordinates of islands.

    island_map = populate_map(island_map, map_height, map_width)

    for j in range(map_height):
        for k in range(map_width):
            if (j, k) not in visited and island_map[j, k] == 1:
                visited.extend(recursive_search(j, k, island_map))
                island_count += 1

    print("island count: " + str(island_count))


if __name__ == "__main__":
    main()

    # when we find a 'land', branch out as much as we can recursively and mark down those coordinates in our
    # islands_found list.
