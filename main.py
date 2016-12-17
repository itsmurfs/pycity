from terrain import Map

if __name__ == "__main__":
    # execute only if run as a script
    world = Map(25, 25)
    print("[bootstrap] world init OK")
    print("[bootstrap] spawning some FOOD")
    print("[bootstrap] printing map")
    #print(world.terrain)
    print(world)

