
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

for _ in range(100):  # Increase iterations for more intersections
    # Random dimensions for rectangles
    width_horizontal = np.random.uniform(4, 8)
    height_horizontal = np.random.uniform(1, 2)
    width_vertical = np.random.uniform(1, 2)
    height_vertical = np.random.uniform(4, 8)

    # Random intersection point, allowing for a broader range to fill the plot
    intersect_x = np.random.uniform(-20, 40)
    intersect_y = np.random.uniform(-20, 40)

    # Adjust positions for varied intersections
    horizontal_rect_bottom_left = (intersect_x - width_horizontal / 2, intersect_y)  # Center around intersection point
    vertical_rect_bottom_left = (intersect_x, intersect_y - height_vertical / 2)

    # Random alpha and color
    alpha_horizontal = np.random.uniform(0.4, 0.6)
    alpha_vertical = np.random.uniform(0.4, 0.6)
    color_horizontal = str(np.random.uniform(0.0, 1.0))
    color_vertical = str(np.random.uniform(0.0, 1.0))

    # Add patches for each set of rectangles
    ax.add_patch(plt.Rectangle(horizontal_rect_bottom_left, width_horizontal, height_horizontal, alpha=alpha_horizontal, color=color_horizontal))
    ax.add_patch(plt.Rectangle(vertical_rect_bottom_left, width_vertical, height_vertical, alpha=alpha_vertical, color=color_vertical))

# Set axis limits to encompass the broader range of intersections
ax.set_xlim(-30, 60)
ax.set_ylim(-30, 60)

plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.show()
