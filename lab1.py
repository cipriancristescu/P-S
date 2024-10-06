import numpy as np
import matplotlib.pyplot as plt

# Choose number of chords to draw in the simulation:
num_chords = 10000

def draw_circle_and_triangle(ax):
    circle = plt.Circle((0, 0), 1, color='w', linewidth=2, fill=False)
    ax.add_patch(circle)  # Draw circle
    ax.plot([np.cos(np.pi / 2), np.cos(7 * np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(7 * np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(np.pi / 2), np.cos(- np.pi / 6)],
            [np.sin(np.pi / 2), np.sin(- np.pi / 6)], linewidth=2, color='g')
    ax.plot([np.cos(- np.pi / 6), np.cos(7 * np.pi / 6)],
            [np.sin(- np.pi / 6), np.sin(7 * np.pi / 6)], linewidth=2, color='g')


def bertrand_simulation(method_number):
    # Simulation initialisation parameters
    count = 0
    triangle_side_length = np.sqrt(3)  # Latura triunghiului echilateral înscris

    # Figure initialisation
    plt.style.use('dark_background')  # use dark background
    ax = plt.gca()
    ax.cla()  # clear things for fresh plot
    ax.set_aspect('equal', 'box')
    ax.set_xlim((-1.2, 1.2))  # Set x axis limits
    ax.set_ylim((-1.2, 1.2))  # Set y axis limits

    # Repeat the following simulation num_chords times:
    for _ in range(num_chords):
        # Step 1: Construct chord coordinates according to chosen method
        x1, y1, x2, y2 = bertrand_methods[method_number]()

        # Step 2: Compute length of chord and compare it with triangle side
        chord_length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if chord_length > triangle_side_length:
            count += 1

        # Plot the first 1000 chords
        if _ < 1000:
            color = 'b' if chord_length > triangle_side_length else 'r'
            ax.plot([x1, x2], [y1, y2], color=color, alpha=0.1)

    # Display probability after each simulation
    probability = count / num_chords
    draw_circle_and_triangle(ax)
    plt.title(f'Method {method_number}: Probability = {probability:.4f}')
    plt.show()


def bertrand1():
    """Generate random chords using "Method 1":

    Pairs of (uniformly-distributed) random points on the unit circle are
    selected and joined as chords.

    """
    theta1 = 2 * np.pi * np.random.random()
    theta2 = 2 * np.pi * np.random.random()

    x1, y1 = np.cos(theta1), np.sin(theta1)
    x2, y2 = np.cos(theta2), np.sin(theta2)

    return x1, y1, x2, y2


def bertrand2():
    """Generate random chords using "Method 2":

    Select a random point inside the unit circle, and construct a chord
    such that this point is its midpoint.

    """
    # Generate random radius and angle for the midpoint
    r = np.sqrt(np.random.random())  # To ensure uniform distribution in circle area
    theta = 2 * np.pi * np.random.random()

    x_mid, y_mid = r * np.cos(theta), r * np.sin(theta)

    # Choose a random angle for the chord direction
    chord_angle = 2 * np.pi * np.random.random()
    dx, dy = np.cos(chord_angle), np.sin(chord_angle)

    # Determine the endpoints of the chord
    chord_length = np.sqrt(1 - r**2)
    x1, y1 = x_mid + chord_length * dx, y_mid + chord_length * dy
    x2, y2 = x_mid - chord_length * dx, y_mid - chord_length * dy

    return x1, y1, x2, y2


def bertrand3():
    """Generate random chords using "Method 3":

    Select a random radius and a random point along this radius, and
    construct a chord such that this point is its midpoint.

    """
    # Generate a random angle for the radius
    theta = 2 * np.pi * np.random.random()

    # Generate a random point along the radius
    r = np.random.random()

    # Coordinates of the midpoint on the radius
    x_mid, y_mid = r * np.cos(theta), r * np.sin(theta)

    # The chord should be perpendicular to the radius at the midpoint
    chord_angle = theta + np.pi / 2
    dx, dy = np.cos(chord_angle), np.sin(chord_angle)

    # Determine the endpoints of the chord
    chord_length = np.sqrt(1 - r**2)
    x1, y1 = x_mid + chord_length * dx, y_mid + chord_length * dy
    x2, y2 = x_mid - chord_length * dx, y_mid - chord_length * dy

    return x1, y1, x2, y2


bertrand_methods = {
    1: bertrand1,
    2: bertrand2,
    3: bertrand3
}

# Run the simulation for each method
for method in range(1, 4):
    bertrand_simulation(method)
