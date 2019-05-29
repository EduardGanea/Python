from search import *
from P1 import WaterJug
from P2 import *

def main():
    problema_WaterJug = WaterJug((0,0),(2,3))
    path1 = breadth_first_tree_search(problema_WaterJug).solution()
    print(path1, '\n')
    problem1 = fifteenpuzzleheur((1, 2, 6, 3, 4, 9, 5, 7, 8, 13, 11, 15, 12, 14, 0, 10),  (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ,15))
    problem2 = fifteenpuzzleheur2((1, 2, 6, 3, 4, 9, 5, 7, 8, 13, 11, 15, 12, 14, 0, 10),  (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    path = astar_search(problem1).solution()
    path2 = astar_search(problem2).solution()
    print(path, '\n')
    print(path2, '\n')


if __name__ == "__main__":
    main()
