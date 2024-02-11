#topological sort
from collections import defaultdict, deque
def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    queue = deque(node for node in graph if in_degree[node] == 0)
    result = []

    while queue:
        current_node = queue.popleft()
        result.append(current_node)

        for neighbor in graph[current_node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph):
        # The graph contains a cycle, so topological sorting is not possible
        return None
    else:
        return result
graph={'Robot':['Mechanics','Electronics'],
       'Mechanics':['Actuators','Position and Orientation'],
       'Actuators':['Battery','DC Motor','DC Servo Motor','DC Stepper Motor'],
       'Battery':['Alkaline battery','Li-ion battery','LIPO battery'],
       'Alkaline battery':[],
       'Li-ion battery':[],
       'LIPO battery': [],
       'DC Motor': [],
       'DC Servo Motor': [],
       'DC Stepper Motor': [],
       'Position and Orientation':['Feedback'],
       'Feedback':['IMU','Control'],
       'IMU':['MPU 6050','MPU 9250'],
       'MPU 6050':[],
       'MPU 9250':[],
       'Control':['Fuzzy Logic','LQR Controller','PID Controller'],
       'Fuzzy Logic':[],
       'LQR Controller':[],
       'PID Controller':[],
       'Electronics':['Microcontroller'],
       'Microcontroller': ['Arduino Uno', 'Arduino_nano', 'ESP32', 'ESP8266'],
       'Arduino Uno': [],
       'Arduino_nano': [],
       'ESP32': [],
       'ESP8266': [],
       }
topological_order = topological_sort(graph)
if topological_order is None:
    print("The graph contains a cycle, topological sorting is not possible.")
else:
    print("Topological Order:", topological_order)

'''
graph={'Robot':['Mechanics','Electronics'],
       'Mechanics':['Actuators','Position and Orientation'],

       'Actuators':['Battery','DC Motor','DC Servo Motor','DC Stepper Motor'],
       'Battery':['Alkaline battery','Li-ion battery','LIPO battery'],

       'Position and Orientation':['Feedback'],
       'Feedback':['IMU','Control']
       'IMU':['MPU 6050','MPU 9250'],

       'Control':['Fuzzy Logic','LQR Controller','PID Controller'],
       
       'Electronics':['Microcontroller'],
       'Microcontroller': ['Arduino Uno', 'Arduino_nano', 'ESP32', 'ESP8266'],

       }
'''