from math import sqrt, floor

def tsp_approx(A: list, n):
    c = 0 # minimal cost TSP tour
    S = {x for x in range(1, n)} # vertices we haven't visited
    u = 0 # first node
    while S:
        nn = (float("inf"), None) # distance and index of nearest neighbour
        for v in range(n):
            if v in S:
                if nn[0] > A[u][v]:
                    nn = (A[u][v], v)
                elif nn[0] == A[u][v]:
                    if v < nn[1]:
                        nn = (A[u][v], v)
        c += nn[0]
        S.remove(nn[1])
        u = nn[1]
    return floor(c + A[nn[1]][0])


def compute_dist(coordinates, n):
    rows = [None for _ in range(n)]
    A = [rows[:] for _ in range(n)] # distances between each pair of points
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = float("inf")
                continue
            x, y = coordinates[i]
            z, w = coordinates[j]
            A[i][j] = sqrt(((x-z)**2)+((y-w)**2)) # Euclidean distance
    return A

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
    A = compute_dist(coordinates, n)
    return tsp_approx(A, n) 

if __name__ == "__main__":
    print(main())
    



    