import random

map_height = 200
map_width = 200


def find_neighbors(j, k, island_map):
    neighbors_found = []
    if j > 0 and island_map[(j - 1, k)] == 1:
        neighbors_found.append((j - 1, k))
    if j < map_height - 1 and island_map[(j + 1, k)] == 1:
        neighbors_found.append((j + 1, k))
    if k > 0 and island_map[(j, k - 1)] == 1:
        neighbors_found.append((j, k - 1))
    if k < map_width - 1 and island_map[(j, k + 1)] == 1:
        neighbors_found.append((j, k + 1))

    return neighbors_found


# given a j,k position, find the entire island landmass and return the list of coordinates
# that make up that landmass
def find_entire_island(j, k, island_map, island_coords=None):
    if island_coords is None:
        island_coords = set()
    cardinal_neighbors = find_neighbors(j, k, island_map)  # get all neighbors of this coord
    cardinal_neighbors = [x for x in cardinal_neighbors if
                          x not in island_coords]  # remove coords we've already checked
    island_coords.update(cardinal_neighbors)

    for neighbor in cardinal_neighbors:
        island_coords.update(find_entire_island(neighbor[0], neighbor[1], island_map, island_coords))

    return island_coords


def print_map(island_map):
    for j in range(map_height):
        for k in range(map_width):
            print(island_map[j, k], end='')
            if k == map_width - 1:
                print()


def populate_map(island_map):
    for j in range(map_height):
        for k in range(map_width):
            # island_map[j, k] = random.choice([1, 1, 1, 1, 1, 0])
            island_map[j, k] = random.randint(0, 1)
    print_map(island_map)


def main():
    island_count = 0
    island_map = {}  # matrix of coordinates with either 1 or 0
    visited = set()  # list of visited coordinates

    populate_map(island_map)

    for j in range(map_height):
        for k in range(map_width):
            if (j, k) not in visited and island_map[(j, k)] == 1:
                entire_island = find_entire_island(j, k, island_map)
                visited.update(entire_island)
                island_count += 1

    print("islands found: " + str(island_count))


if __name__ == "__main__":
    main()
