from app import mainmenu, gameloop
import terrain
import threading
import time

if __name__ == "__main__":

    #mainmenu(gameloop)
    w = terrain.Map(10, 10)
    matrix = w.get_terrain()

    def worker(*args):
        """thread worker function"""
        time.sleep(args[0])
        'Worker'
        return


    threads = []

    for row in matrix:
        for item in row:
            t = threading.Thread(target=worker, args=[item, ])
            threads.append(t)
            t.start()
            # time.sleep(item)

