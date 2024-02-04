import matplotlib.pyplot as plt
import numpy as np
import random

def draw_rotated_rectangle_filled(ax, origin, height, width, angle, alpha):
    """
    Draw a filled, rotated rectangle with specified transparency.
    """
    rad = np.deg2rad(angle)
    corners = np.array([
        [0, 0], [width, 0], [width, height], [0, height],
    ])
    R = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad), np.cos(rad)]
    ])
    rotated_corners = np.dot(corners, R) + origin
    ax.fill(*zip(*rotated_corners), color='grey', alpha=alpha)

def spawn_branches_filled(ax, origin, height, width, angle=0, depth=0):
    if depth > 4: return
    alpha = random.uniform(0.5, 0.7)
    draw_rotated_rectangle_filled(ax, origin, height, width, angle, alpha)
    num_branches = random.randint(2, 4)
    for _ in range(num_branches):
        branch_height = height * random.uniform(0.3, 0.7)
        branch_width = width * random.uniform(0.3, 0.7)
        branch_angle = random.uniform(-90, 90) + angle
        branch_origin_offset = random.uniform(0, height)
        branch_origin = origin + np.array([
            branch_origin_offset * np.sin(np.deg2rad(angle)), 
            branch_origin_offset * np.cos(np.deg2rad(angle))
        ])
        spawn_branches_filled(ax, branch_origin, branch_height, branch_width, branch_angle, depth + 1)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs = axs.flatten()
for ax in axs:
    ax.set_aspect('equal')
    ax.axis('off')
    generate_overlayed_trees_single_cell(ax)

def generate_overlayed_trees_single_cell(ax):
    origin = np.array([0, 0])
    height = 10
    width = 2
    angle = 0
    for _ in range(3):
        spawn_branches_filled(ax, origin, height, width, angle)

for ax in axs:
    generate_overlayed_trees_single_cell(ax)

plt.show()