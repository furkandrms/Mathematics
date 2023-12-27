import numpy as np 


class MetricSpace: 


    def __init__(self, n_points, dimension=2):

        self.points = np.random.rand(n_points, dimension)


    def euclidean_distance(self, point1, point2): 

        return np.sqrt(np.sum((point1 - point2) ** 2))
    
    def manhattan_distance(self, point1, point2): 

        return np.sum(np.abs(point1 - point2))
    
    def minkowski_distance(self, point1, point2, p=2): 

        return np.sum(np.abs(point1 - point2)**p) ** (1/p)
    
    def distance_matrix(self): 

        n = len(self.points)
        mat = np.zeros((n,n))
        for i in range(n): 
            for j in range(n): 
                mat[i, j] = self.euclidean_distance(self.points[i], self.points[j])
        return mat
    
    def d1(self, point1, point2): 
        return np.abs((point1 - point2)**2)
    
    def d2(self, point1, point2): 
        return 0 if point1 == point2 else (1 / (1 + min(point1, point2)))
    
    def d3(self, point1, point2): 
        return np.abs((point1**2) - (point2**2))
    
    def d4(self, point1, point2): 
        return np.log(1 + self.euclidean_distance(point1,point2))
    
    def d5(self, point1, point2):
        return min(1, self.euclidean_distance(point1, point2))

    



