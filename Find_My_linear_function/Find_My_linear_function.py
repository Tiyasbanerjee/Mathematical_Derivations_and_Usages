import matplotlib.pyplot as plt

def split_points(points):
   l = []
   point = points[1:-1]
   point = point.split(",")
   try:
       l.append(int(point[0]))
       l.append(int(point[1]))
   except ValueError:
       print("Error: plz input numbers.")
       exit()
   return l

while True:
  first_point = input("Enter the first point in this format:---- (x1,y1): ")
  second_point = input("Enter the second point in this format:---- (x2,y2): ")
  if first_point[0] == "(" and first_point[-1] == ")" and second_point[0] == "(" and second_point[-1] == ")" and "," in first_point and "," in second_point:
      first_point = split_points(first_point)
      second_point = split_points(second_point)
      break
  else:
      print("Error due to wrong value input .Please enter exactly two values for each point.")


slope = (second_point[1]-first_point[1])/(second_point[0]-first_point[0])   # m = (y2-y1)/(x2-x1)
y_intercept = first_point[1] - slope*first_point[0]     # b = y1 - m*x1
print(f"The linear function is: y = {slope}*x + {y_intercept}")

def linear_function(x):
    return slope*x + y_intercept

def calculate_max_x():
    max_x = max(abs(first_point[0]), abs(second_point[0]))
    return max_x*2


def plot_graph():
    x_values = [i for i in range(-calculate_max_x(), calculate_max_x())]
    y_values = [linear_function(x) for x in x_values]

    # Create figure & axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot line & points
    ax.plot(x_values, y_values, label=f'y = {slope}*x + {y_intercept}')
    ax.scatter([first_point[0], second_point[0]],
               [first_point[1], second_point[1]],
               color='red')

    # Titles & labels
    ax.set_title('Graph of the Linear Function')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Axes at (0,0)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Style
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()

    plt.show()

plot_graph()
