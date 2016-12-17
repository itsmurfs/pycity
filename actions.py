import terrain

BUILDING_TYPE_HOUSE = "HOUSE"
BUILDING_TYPE_STREET = "STREET"
BUILDING_TYPE_FARM = "FARM"
BUILDING_TYPE_FACTORY = "FACT"


def build_street(map, i, j):

    if map.get_terrain_unit(i, j) == 0:
        map.set_terrain_unit(i, j, BUILDING_TYPE_STREET)
        return True

    return False


def build_house(map, i, j):

    if map.get_terrain_unit(i, j) == 0 and is_close_to(map, i , j, BUILDING_TYPE_STREET):
        map.set_terrain_unit(i, j, BUILDING_TYPE_HOUSE)
        return True

    return False


def build_factory(map, i, j):

    if map.get_terrain_unit(i, j) == 0 and is_close_to(map, i, j, terrain.RESOURCE_ORE) and is_close_to(map, i, j, BUILDING_TYPE_STREET):
        map.set_terrain_unit(i, j, BUILDING_TYPE_FACTORY)
        return True

    return False

def build_farm(map, i, j):

    if map.get_terrain_unit(i, j) == terrain.PERCENTAGE_FOOD and is_close_to(map, i, j, BUILDING_TYPE_STREET):
        map.set_terrain_unit(i, j, BUILDING_TYPE_FARM)
        return True

    return False


def is_close_to(map, i, j, element):

    for unit in terrain.get_close_indexes(i, j):
        if map.get_terrain_unit(unit[0], unit[1]) == element:
            return True

    return False
