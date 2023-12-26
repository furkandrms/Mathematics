from MetricSpaces import MetricSpace
import visualization

def main(): 
    n_points = int(input("Enter the number of points in the metric space: "))
    dimension = int(input("Enter the size of the points (e.g. 2D for 2): "))
    metric_space = MetricSpace(n_points, dimension)

    options = {
        1: MetricSpace.euclidean_distance,
        2: MetricSpace.manhattan_distance,
        3: MetricSpace.minkowski_distance,
        4: MetricSpace.distance_matrix,
        5: MetricSpace.distance_matrix
    }

    choice = int(input("Seçiminiz (1-5): "))

    action = options.get(choice)

    if action: 
        action(metric_space)
    else: 
        return f"Error"
    

if __name__ == "__main__":
    main()
