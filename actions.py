import terrain

BUILDING_TYPE_HOUSE = 4
BUILDING_TYPE_STREET = 1
BUILDING_TYPE_FARM = 6
BUILDING_TYPE_FACTORY = 5


def build_street(world, i, j):
    if world.get_terrain_unit(i, j) == 0:
        world.set_terrain_unit(i, j, BUILDING_TYPE_STREET)
        return True

    return False


def build_house(world, i, j):
    if world.get_terrain_unit(i, j) == 0 and is_close_to(world, i, j, BUILDING_TYPE_STREET):
        world.set_terrain_unit(i, j, BUILDING_TYPE_HOUSE)
        return True

    return False


def build_factory(world, i, j):
    if world.get_terrain_unit(i, j) == 0 and is_close_to(world, i, j, terrain.RESOURCE_ORE) and is_close_to(world, i, j, BUILDING_TYPE_STREET):
        world.set_terrain_unit(i, j, BUILDING_TYPE_FACTORY)
        return True

    return False


def build_farm(world, i, j):
    if world.get_terrain_unit(i, j) == terrain.RESOURCE_FOOD and is_close_to(world, i, j, BUILDING_TYPE_STREET):
        world.set_terrain_unit(i, j, BUILDING_TYPE_FARM)
        return True

    return False


def is_close_to(world, i, j, element):
    for unit in terrain.get_close_indexes(i, j):
        if world.get_terrain_unit(unit[0], unit[1]) == element:
            return True

    return False
