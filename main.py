from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

# Distance callback
class CreateDistanceCallback(object):
  """Create callback to calculate distances between points."""
  def __init__(self):
    """Array of distances between points."""

    self.matrix = [
    [0, 55, 82, 12, 25, 77, 18, 24, 71, 65, 43, 82, 10, 48, 50, 68, 58, 30, 54, 10, 70, 37, 17, 39, 30, 75, 75, 18, 58, 53, 10, 30, 81, 14, 32, 26, 49, 37, 77, 30, 34, 34, 82, 41, 50, 22, 39, 26, 53, 14],
    [110, 0, 27, 122, 60, 22, 128, 62, 16, 10, 24, 27, 114, 14, 10, 13, 10, 140, 10, 108, 15, 36, 76, 32, 140, 20, 20, 74, 10, 10, 96, 140, 26, 82, 142, 58, 12, 36, 22, 140, 144, 144, 27, 28, 10, 132, 32, 136, 10, 124],
    [164, 54, 0, 176, 114, 10, 182, 116, 22, 34, 78, 0, 168, 68, 64, 28, 48, 194, 56, 162, 24, 90, 130, 86, 194, 14, 14, 128, 48, 58, 150, 194, 10, 136, 196, 112, 66, 90, 10, 194, 198, 198, 0, 82, 64, 186, 86, 190, 58, 178],
    [10, 61, 88, 0, 31, 83, 10, 30, 77, 71, 49, 88, 10, 54, 56, 74, 64, 18, 60, 10, 76, 43, 23, 45, 18, 81, 81, 24, 64, 59, 13, 18, 87, 20, 20, 32, 55, 43, 83, 18, 22, 22, 88, 47, 56, 10, 45, 14, 59, 10],
    [50, 30, 57, 62, 0, 52, 68, 10, 46, 40, 18, 57, 54, 23, 25, 43, 33, 80, 29, 48, 45, 12, 16, 14, 80, 50, 50, 14, 33, 28, 36, 80, 56, 22, 82, 10, 24, 12, 52, 80, 84, 84, 57, 16, 25, 72, 14, 76, 28, 64],
    [154, 44, 10, 166, 104, 0, 172, 106, 12, 24, 68, 10, 158, 58, 54, 18, 38, 184, 46, 152, 14, 80, 120, 76, 184, 10, 10, 118, 38, 48, 140, 184, 10, 126, 186, 102, 56, 80, 0, 184, 188, 188, 10, 72, 54, 176, 76, 180, 48, 168],
    [10, 64, 91, 10, 34, 86, 0, 33, 80, 74, 52, 91, 10, 57, 59, 77, 67, 12, 63, 10, 79, 46, 26, 48, 12, 84, 84, 27, 67, 62, 16, 12, 90, 23, 14, 35, 58, 46, 86, 12, 16, 16, 91, 50, 59, 10, 48, 10, 62, 10],
    [48, 31, 58, 60, 10, 53, 66, 0, 47, 41, 19, 58, 52, 24, 26, 44, 34, 78, 30, 46, 46, 13, 14, 15, 78, 51, 51, 12, 34, 29, 34, 78, 57, 20, 80, 10, 25, 13, 53, 78, 82, 82, 58, 17, 26, 70, 15, 74, 29, 62],
    [142, 32, 11, 154, 92, 10, 160, 94, 0, 12, 56, 11, 146, 46, 42, 10, 26, 172, 34, 140, 10, 68, 108, 64, 172, 10, 10, 106, 26, 36, 128, 172, 10, 114, 174, 90, 44, 68, 10, 172, 176, 176, 11, 60, 42, 164, 64, 168, 36, 156],
    [130, 20, 17, 142, 80, 12, 148, 82, 10, 0, 44, 17, 134, 34, 30, 10, 14, 160, 22, 128, 10, 56, 96, 52, 160, 10, 10, 94, 14, 24, 116, 160, 16, 102, 162, 78, 32, 56, 12, 160, 164, 164, 17, 48, 30, 152, 52, 156, 24, 144],
    [86, 12, 39, 98, 36, 34, 104, 38, 28, 22, 0, 39, 90, 10, 10, 25, 15, 116, 11, 84, 27, 12, 52, 10, 116, 32, 32, 50, 15, 10, 72, 116, 38, 58, 118, 34, 10, 12, 34, 116, 120, 120, 39, 10, 10, 108, 10, 112, 10, 100],
    [164, 54, 0, 176, 114, 10, 182, 116, 22, 34, 78, 0, 168, 68, 64, 28, 48, 194, 56, 162, 24, 90, 130, 86, 194, 14, 14, 128, 48, 58, 150, 194, 10, 136, 196, 112, 66, 90, 10, 194, 198, 198, 0, 82, 64, 186, 86, 190, 58, 178],
    [10, 57, 84, 10, 27, 79, 14, 26, 73, 67, 45, 84, 0, 50, 52, 70, 60, 26, 56, 10, 72, 39, 19, 41, 26, 77, 77, 20, 60, 55, 10, 26, 83, 16, 28, 28, 51, 39, 79, 26, 30, 30, 84, 43, 52, 18, 41, 22, 55, 10],
    [96, 10, 34, 108, 46, 29, 114, 48, 23, 17, 10, 34, 100, 0, 10, 20, 10, 126, 10, 94, 22, 22, 62, 18, 126, 27, 27, 60, 10, 10, 82, 126, 33, 68, 128, 44, 10, 22, 29, 126, 130, 130, 34, 14, 10, 118, 18, 122, 10, 110],
    [100, 10, 32, 112, 50, 27, 118, 52, 21, 15, 14, 32, 104, 10, 0, 18, 10, 130, 10, 98, 20, 26, 66, 22, 130, 25, 25, 64, 10, 10, 86, 130, 31, 72, 132, 48, 10, 26, 27, 130, 134, 134, 32, 18, 0, 122, 22, 126, 10, 114],
    [136, 26, 14, 148, 86, 10, 154, 88, 10, 10, 50, 14, 140, 40, 36, 0, 20, 166, 28, 134, 10, 62, 102, 58, 166, 10, 10, 100, 20, 30, 122, 166, 13, 108, 168, 84, 38, 62, 10, 166, 170, 170, 14, 54, 36, 158, 58, 162, 30, 150],
    [116, 10, 24, 128, 66, 19, 134, 68, 13, 10, 30, 24, 120, 20, 16, 10, 0, 146, 10, 114, 12, 42, 82, 38, 146, 17, 17, 80, 0, 10, 102, 146, 23, 88, 148, 64, 18, 42, 19, 146, 150, 150, 24, 34, 16, 138, 38, 142, 10, 130],
    [15, 70, 97, 10, 40, 92, 10, 39, 86, 80, 58, 97, 13, 63, 65, 83, 73, 0, 69, 16, 85, 52, 32, 54, 0, 90, 90, 33, 73, 68, 22, 0, 96, 29, 10, 41, 64, 52, 92, 0, 10, 10, 97, 56, 65, 10, 54, 10, 68, 10],
    [108, 10, 28, 120, 58, 23, 126, 60, 17, 11, 22, 28, 112, 12, 10, 14, 10, 138, 0, 106, 16, 34, 74, 30, 138, 21, 21, 72, 10, 10, 94, 138, 27, 80, 140, 56, 10, 34, 23, 138, 142, 142, 28, 26, 10, 130, 30, 134, 10, 122],
    [10, 54, 81, 14, 24, 76, 20, 23, 70, 64, 42, 81, 10, 47, 49, 67, 57, 32, 53, 0, 69, 36, 16, 38, 32, 74, 74, 17, 57, 52, 10, 32, 80, 13, 34, 25, 48, 36, 76, 32, 36, 36, 81, 40, 49, 24, 38, 28, 52, 16],
    [140, 30, 12, 152, 90, 10, 158, 92, 10, 10, 54, 12, 144, 44, 40, 10, 24, 170, 32, 138, 0, 66, 106, 62, 170, 10, 10, 104, 24, 34, 126, 170, 11, 112, 172, 88, 42, 66, 10, 170, 174, 174, 12, 58, 40, 162, 62, 166, 34, 154],
    [74, 18, 45, 86, 24, 40, 92, 26, 34, 28, 10, 45, 78, 11, 13, 31, 21, 104, 17, 72, 33, 0, 40, 10, 104, 38, 38, 38, 21, 16, 60, 104, 44, 46, 106, 22, 12, 0, 40, 104, 108, 108, 45, 10, 13, 96, 10, 100, 16, 88],
    [34, 38, 65, 46, 10, 60, 52, 10, 54, 48, 26, 65, 38, 31, 33, 51, 41, 64, 37, 32, 53, 20, 0, 22, 64, 58, 58, 10, 41, 36, 20, 64, 64, 10, 66, 10, 32, 20, 60, 64, 68, 68, 65, 24, 33, 56, 22, 60, 36, 48],
    [78, 16, 43, 90, 28, 38, 96, 30, 32, 26, 10, 43, 82, 10, 11, 29, 19, 108, 15, 76, 31, 10, 44, 0, 108, 36, 36, 42, 19, 14, 64, 108, 42, 50, 110, 26, 10, 10, 38, 108, 112, 112, 43, 10, 11, 100, 0, 104, 14, 92],
    [15, 70, 97, 10, 40, 92, 10, 39, 86, 80, 58, 97, 13, 63, 65, 83, 73, 0, 69, 16, 85, 52, 32, 54, 0, 90, 90, 33, 73, 68, 22, 0, 96, 29, 10, 41, 64, 52, 92, 0, 10, 10, 97, 56, 65, 10, 54, 10, 68, 10],
    [150, 40, 10, 162, 100, 10, 168, 102, 10, 20, 64, 10, 154, 54, 50, 14, 34, 180, 42, 148, 10, 76, 116, 72, 180, 0, 0, 114, 34, 44, 136, 180, 10, 122, 182, 98, 52, 76, 10, 180, 184, 184, 10, 68, 50, 172, 72, 176, 44, 164],
    [150, 40, 10, 162, 100, 10, 168, 102, 10, 20, 64, 10, 154, 54, 50, 14, 34, 180, 42, 148, 10, 76, 116, 72, 180, 0, 0, 114, 34, 44, 136, 180, 10, 122, 182, 98, 52, 76, 10, 180, 184, 184, 10, 68, 50, 172, 72, 176, 44, 164],
    [36, 37, 64, 48, 10, 59, 54, 10, 53, 47, 25, 64, 40, 30, 32, 50, 40, 66, 36, 34, 52, 19, 10, 21, 66, 57, 57, 0, 40, 35, 22, 66, 63, 10, 68, 10, 31, 19, 59, 66, 70, 70, 64, 23, 32, 58, 21, 62, 35, 50],
    [116, 10, 24, 128, 66, 19, 134, 68, 13, 10, 30, 24, 120, 20, 16, 10, 0, 146, 10, 114, 12, 42, 82, 38, 146, 17, 17, 80, 0, 10, 102, 146, 23, 88, 148, 64, 18, 42, 19, 146, 150, 150, 24, 34, 16, 138, 38, 142, 10, 130],
    [106, 10, 29, 118, 56, 24, 124, 58, 18, 12, 20, 29, 110, 10, 10, 15, 10, 136, 10, 104, 17, 32, 72, 28, 136, 22, 22, 70, 10, 0, 92, 136, 28, 78, 138, 54, 10, 32, 24, 136, 140, 140, 29, 24, 10, 128, 28, 132, 0, 120],
    [14, 48, 75, 26, 18, 70, 32, 17, 64, 58, 36, 75, 18, 41, 43, 61, 51, 44, 47, 12, 63, 30, 10, 32, 44, 68, 68, 11, 51, 46, 0, 44, 74, 10, 46, 19, 42, 30, 70, 44, 48, 48, 75, 34, 43, 36, 32, 40, 46, 28],
    [15, 70, 97, 10, 40, 92, 10, 39, 86, 80, 58, 97, 13, 63, 65, 83, 73, 0, 69, 16, 85, 52, 32, 54, 0, 90, 90, 33, 73, 68, 22, 0, 96, 29, 10, 41, 64, 52, 92, 0, 10, 10, 97, 56, 65, 10, 54, 10, 68, 10],
    [162, 52, 10, 174, 112, 10, 180, 114, 20, 32, 76, 10, 166, 66, 62, 26, 46, 192, 54, 160, 22, 88, 128, 84, 192, 12, 12, 126, 46, 56, 148, 192, 0, 134, 194, 110, 64, 88, 10, 192, 196, 196, 10, 80, 62, 184, 84, 188, 56, 176],
    [28, 41, 68, 40, 11, 63, 46, 10, 57, 51, 29, 68, 32, 34, 36, 54, 44, 58, 40, 26, 56, 23, 10, 25, 58, 61, 61, 10, 44, 39, 14, 58, 67, 0, 60, 12, 35, 23, 63, 58, 62, 62, 68, 27, 36, 50, 25, 54, 39, 42],
    [16, 71, 98, 10, 41, 93, 10, 40, 87, 81, 59, 98, 14, 64, 66, 84, 74, 10, 70, 17, 86, 53, 33, 55, 10, 91, 91, 34, 74, 69, 23, 10, 97, 30, 0, 42, 65, 53, 93, 10, 10, 10, 98, 57, 66, 10, 55, 10, 69, 10],
    [52, 29, 56, 64, 10, 51, 70, 10, 45, 39, 17, 56, 56, 22, 24, 42, 32, 82, 28, 50, 44, 11, 18, 13, 82, 49, 49, 16, 32, 27, 38, 82, 55, 24, 84, 0, 23, 11, 51, 82, 86, 86, 56, 15, 24, 74, 13, 78, 27, 66],
    [98, 10, 33, 110, 48, 28, 116, 50, 22, 16, 12, 33, 102, 10, 10, 19, 10, 128, 10, 96, 21, 24, 64, 20, 128, 26, 26, 62, 10, 10, 84, 128, 32, 70, 130, 46, 0, 24, 28, 128, 132, 132, 33, 16, 10, 120, 20, 124, 10, 112],
    [74, 18, 45, 86, 24, 40, 92, 26, 34, 28, 10, 45, 78, 11, 13, 31, 21, 104, 17, 72, 33, 0, 40, 10, 104, 38, 38, 38, 21, 16, 60, 104, 44, 46, 106, 22, 12, 0, 40, 104, 108, 108, 45, 10, 13, 96, 10, 100, 16, 88],
    [154, 44, 10, 166, 104, 0, 172, 106, 12, 24, 68, 10, 158, 58, 54, 18, 38, 184, 46, 152, 14, 80, 120, 76, 184, 10, 10, 118, 38, 48, 140, 184, 10, 126, 186, 102, 56, 80, 0, 184, 188, 188, 10, 72, 54, 176, 76, 180, 48, 168],
    [15, 70, 97, 10, 40, 92, 10, 39, 86, 80, 58, 97, 13, 63, 65, 83, 73, 0, 69, 16, 85, 52, 32, 54, 0, 90, 90, 33, 73, 68, 22, 0, 96, 29, 10, 41, 64, 52, 92, 0, 10, 10, 97, 56, 65, 10, 54, 10, 68, 10],
    [17, 72, 99, 11, 42, 94, 10, 41, 88, 82, 60, 99, 15, 65, 67, 85, 75, 10, 71, 18, 87, 54, 34, 56, 10, 92, 92, 35, 75, 70, 24, 10, 98, 31, 10, 43, 66, 54, 94, 10, 0, 0, 99, 58, 67, 10, 56, 10, 70, 10],
    [17, 72, 99, 11, 42, 94, 10, 41, 88, 82, 60, 99, 15, 65, 67, 85, 75, 10, 71, 18, 87, 54, 34, 56, 10, 92, 92, 35, 75, 70, 24, 10, 98, 31, 10, 43, 66, 54, 94, 10, 0, 0, 99, 58, 67, 10, 56, 10, 70, 10],
    [164, 54, 0, 176, 114, 10, 182, 116, 22, 34, 78, 0, 168, 68, 64, 28, 48, 194, 56, 162, 24, 90, 130, 86, 194, 14, 14, 128, 48, 58, 150, 194, 10, 136, 196, 112, 66, 90, 10, 194, 198, 198, 0, 82, 64, 186, 86, 190, 58, 178],
    [82, 14, 41, 94, 32, 36, 100, 34, 30, 24, 10, 41, 86, 10, 10, 27, 17, 112, 13, 80, 29, 10, 48, 10, 112, 34, 34, 46, 17, 12, 68, 112, 40, 54, 114, 30, 10, 10, 36, 112, 116, 116, 41, 0, 10, 104, 10, 108, 12, 96],
    [100, 10, 32, 112, 50, 27, 118, 52, 21, 15, 14, 32, 104, 10, 0, 18, 10, 130, 10, 98, 20, 26, 66, 22, 130, 25, 25, 64, 10, 10, 86, 130, 31, 72, 132, 48, 10, 26, 27, 130, 134, 134, 32, 18, 0, 122, 22, 126, 10, 114],
    [11, 66, 93, 10, 36, 88, 10, 35, 82, 76, 54, 93, 10, 59, 61, 79, 69, 10, 65, 12, 81, 48, 28, 50, 10, 86, 86, 29, 69, 64, 18, 10, 92, 25, 10, 37, 60, 48, 88, 10, 12, 12, 93, 52, 61, 0, 50, 10, 64, 10],
    [78, 16, 43, 90, 28, 38, 96, 30, 32, 26, 10, 43, 82, 10, 11, 29, 19, 108, 15, 76, 31, 10, 44, 0, 108, 36, 36, 42, 19, 14, 64, 108, 42, 50, 110, 26, 10, 10, 38, 108, 112, 112, 43, 10, 11, 100, 0, 104, 14, 92],
    [13, 68, 95, 10, 38, 90, 10, 37, 84, 78, 56, 95, 11, 61, 63, 81, 71, 10, 67, 14, 83, 50, 30, 52, 10, 88, 88, 31, 71, 66, 20, 10, 94, 27, 10, 39, 62, 50, 90, 10, 10, 10, 95, 54, 63, 10, 52, 0, 66, 10],
    [106, 10, 29, 118, 56, 24, 124, 58, 18, 12, 20, 29, 110, 10, 10, 15, 10, 136, 10, 104, 17, 32, 72, 28, 136, 22, 22, 70, 10, 0, 92, 136, 28, 78, 138, 54, 10, 32, 24, 136, 140, 140, 29, 24, 10, 128, 28, 132, 0, 120],
    [10, 62, 89, 10, 32, 84, 10, 31, 78, 72, 50, 89, 10, 55, 57, 75, 65, 16, 61, 10, 77, 44, 24, 46, 16, 82, 82, 25, 65, 60, 14, 16, 88, 21, 18, 33, 56, 44, 84, 16, 20, 20, 89, 48, 57, 10, 46, 12, 60, 0]]

  def Distance(self, from_node, to_node):
    return int(self.matrix[from_node][to_node])
def main():

  # Cities
  city_names = ["art-1","art-2","art-3","art-4","art-5","art-6","art-7","art-8","art-9","art-10","art-11","art-12","art-13","art-14","art-15","art-16","art-17","art-18","art-19","art-20","art-21","art-22","art-23","art-24","art-25","art-26","art-27","art-28","art-29","art-30","art-31","art-32","art-33","art-34","art-35","art-36","art-37","art-38","art-39","art-40","art-41","art-42","art-43","art-44","art-45","art-46","art-47","art-48","art-49","art-50"]
  tsp_size = len(city_names)
  num_routes = 1    # The number of routes, which is 1 in the TSP.
  # Nodes are indexed from 0 to tsp_size - 1. The depot is the starting node of the route.
  depot = 0

  # Create routing model
  if tsp_size > 0:
    routing = pywrapcp.RoutingModel(tsp_size, num_routes, depot)
    search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()

    # Create the distance callback, which takes two arguments (the from and to node indices)
    # and returns the distance between these nodes.
    dist_between_nodes = CreateDistanceCallback()
    dist_callback = dist_between_nodes.Distance
    routing.SetArcCostEvaluatorOfAllVehicles(dist_callback)
    # Solve, returns a solution if any.
    assignment = routing.SolveWithParameters(search_parameters)
    if assignment:
      # Inspect solution.
      # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
      route_number = 0
      index = routing.Start(route_number) # Index of the variable for the starting node.
      route = ''
      print("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")
      while not routing.IsEnd(index):
        # Convert variable indices to node indices in the displayed route.
        route += str(city_names[routing.IndexToNode(index)]) + ' -> '
        index = assignment.Value(routing.NextVar(index))
      route += str(city_names[routing.IndexToNode(index)])
      print( "Route:\n\n" + route)
    else:
      print('No solution found.')
  else:
    print('Specify an instance greater than 0.')

if __name__ == '__main__':
  main()
