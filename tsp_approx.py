from math import sqrt, floor

def tsp_approx(coordinates: list, n: int):
    c = 0 # minimal cost TSP tour
    S = {x for x in range(1, n)} # vertices we haven't visited
    u = 0 # first node
    while S:
        nn = (float("inf"), None) # distance and index of nearest neighbour
        for v in range(n):
            if v in S:
                d = compute_dist(u, v, coordinates)
                if nn[0] > d:
                    nn = (d, v)
                elif nn[0] == d:
                    if v < nn[1]:
                        nn = (d, v)
        c += nn[0]
        S.remove(nn[1])
        u = nn[1]
    return floor(c + compute_dist(u, 0, coordinates))


def compute_dist(u, v, coordinates):
    x, y = coordinates[u]
    z, w = coordinates[v]
    return sqrt(((x-z)**2)+((y-w)**2)) # Euclidean distance

def get_coordinates(file_name: str = "nn.txt"):
    coordinates = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        n = int(lines[0])
        for line in lines[1:]:
            _, x, y = [float(a) for a in line.strip().split()]
            coordinates.append((x, y))
    return coordinates, n

def main():
    coordinates, n = get_coordinates("nn_small.txt")
    return tsp_approx(coordinates, n) 

if __name__ == "__main__":
    print(main())
    



    