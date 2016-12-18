import random
import math

RESOURCE_ORE = 3
RESOURCE_FOOD = 2
PERCENTAGE_ORE = 3
PERCENTAGE_FOOD = 3


class Map:
    terrain = [[]]

    def get_terrain(self):
        return self.terrain

    def __init__(self, height, width):
        self.w = width
        self.h = height
        self.num_cells_ore = math.floor(((self.h * self.w) / 100) * PERCENTAGE_ORE)
        self.num_cells_food = math.floor(((self.h * self.w) / 100) * PERCENTAGE_FOOD)
        self.terrain = [[0 for row in range(0, self.w)] for col in range(0, self.h)]
        self.spawn_random_terrain(RESOURCE_ORE)
        self.spawn_random_terrain(RESOURCE_FOOD)

    def get_terrain_unit(self, i, j):

        if self.index_is_valid(i, j):
            return self.terrain[i][j]

    def set_terrain_unit(self, i, j, resource):
        self.terrain[i][j] = resource

    def spawn_resource(self, resource, num_resource, i, j):
        if num_resource == 0:
            return 0

        if self.index_is_valid(i, j) and (self.terrain[i][j] == 0):
            self.terrain[i][j] = resource
            num_resource -= 1

        return num_resource

    def spawn_random_terrain(self, resource):
        num_resource = self.num_cells_ore if resource == RESOURCE_ORE else self.num_cells_food

        while num_resource > 0:
            # spawn some food
            i = random.randint(0, self.h - 1)
            j = random.randint(0, self.w - 1)

            print("[debug] random: " + i.__str__() + "," + j.__str__())

            for couples in get_close_indexes(i, j):
                num_resource = self.spawn_resource(resource, num_resource, couples[0], couples[1])

    def __str__(self):

        resp = ""
        for row in self.terrain:
            for val in row:
                resp += '{:4}'.format(val)
            resp += "\n"

        return resp

    def index_is_valid(self, i, j):
        return (j > 0) and (i > 0) and (i < self.h) and (j < self.w)


def get_close_indexes(i, j):
    return [(i, j), (i, j - 1), (i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1), (i + 1, j),
            (i + 1, j - 1)]
