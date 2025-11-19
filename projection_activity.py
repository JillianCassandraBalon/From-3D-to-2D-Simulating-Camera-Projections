import numpy as np
import matplotlib.pyplot as plt


points = np.array([
    [-1, -1, -1],
    [-1, -1, 1],
    [-1, 1, -1],
    [-1, 1, 1],
    [1, -1, -1],
    [1, -1, 1],
    [1, 1, -1],
    [1, 1, 1]
])


edges = [
    (0, 1), (0, 2), (0, 4), (1, 3), (1, 5),
    (2, 3), (2, 6), (3, 7), (4, 5), (4, 6),
    (5, 7), (6, 7)
]


def orthographic_projection(points):
    projected = points[:, :2]
    return projected


def perspective_projection(points, focal_length=2):
    projected = []
    for x, y, z in points:
        x_proj = (focal_length * x) / (z + focal_length)
        y_proj = (focal_length * y) / (z + focal_length)
        projected.append([x_proj, y_proj])
    return np.array(projected)


ortho_2d = orthographic_projection(points)
persp_2d = perspective_projection(points, focal_length=2)


fig, axs = plt.subplots(1, 2, figsize=(10, 5))
titles = ['Orthographic Projection', 'Perspective Projection']
projections = [ortho_2d, persp_2d]

for ax, proj, title in zip(axs, projections, titles):
    for edge in edges:
        p1, p2 = edge
        ax.plot([proj[p1, 0], proj[p2, 0]],
                [proj[p1, 1], proj[p2, 1]], 'bo-')
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect('equal')

plt.tight_layout()
plt.show()
