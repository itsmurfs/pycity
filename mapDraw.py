# from assets import map
#
import terrain
import config


def generateMap():

    world = terrain.Map(config.map_size_x, config.map_size_y)
    tiles = world.get_terrain()
    print(tiles)

    return world


def drawMap(xoffset, yoffset, tiles, display, world):
    currentRow = 0  # y
    currentTile = 0  # x
    for row in world:
        for tile in row:
            tileImage = tiles[world[currentRow][currentTile]]
            tileImage.set_colorkey((0, 0, 0))
            # TODO (@everyone) : let's try to understand that 64 value :S
            cartx = currentTile * 64
            carty = currentRow * 64

            x = xoffset + 0 + ((cartx - carty) / 2)
            y = yoffset + 0 + ((cartx + carty) / 4)

            currentTile += 1
            display.blit(tileImage, (x, y))

        currentTile = 0  # Reset for new row
        currentRow += 1
