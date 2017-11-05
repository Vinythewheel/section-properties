import numpy as np

def CHS(r, t, n):
    points = []
    facets = []
    holes = [(0,0)]

    for i in range(n):
        theta = i * 2 * np.pi * 1.0 / n

        x_out = r * np.cos(theta)
        y_out = r * np.sin(theta)

        x_in = (r - t) * np.cos(theta)
        y_in = (r - t) * np.sin(theta)

        points.append((x_out, y_out))
        points.append((x_in, y_in))

        if i != n - 1:
            facets.append((i * 2, i * 2 + 2))
            facets.append((i * 2 + 1, i * 2 + 3))
        else:
            facets.append((i * 2, 0))
            facets.append((i * 2 + 1, 1))

    return (points, facets, holes)

def RHS(d, b, t, r_out, n_r):
    points = []
    facets = []
    holes = [(b * 0.5, d * 0.5)]
    r_in = r_out - t

    # bottom left radius
    for i in range(n_r):
        theta = np.pi + i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = r_out + r_out * np.cos(theta)
        y_out = r_out + r_out * np.sin(theta)
        x_in = r_out + r_in * np.cos(theta)
        y_in = r_out + r_in * np.sin(theta)

        points.append((x_out, y_out))
        points.append((x_in, y_in))

    # bottom right radius
    for i in range(n_r):
        theta = 3.0 / 2 * np.pi + i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = b - r_out + r_out * np.cos(theta)
        y_out = r_out + r_out * np.sin(theta)
        x_in = b - r_out + r_in * np.cos(theta)
        y_in = r_out + r_in * np.sin(theta)

        points.append((x_out, y_out))
        points.append((x_in, y_in))

    # top right radius
    for i in range(n_r):
        theta = i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = b - r_out + r_out * np.cos(theta)
        y_out = d - r_out + r_out * np.sin(theta)
        x_in = b - r_out + r_in * np.cos(theta)
        y_in = d - r_out + r_in * np.sin(theta)

        points.append((x_out, y_out))
        points.append((x_in, y_in))

    # top left radius
    for i in range(n_r):
        theta = np.pi * 0.5 + i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = r_out + r_out * np.cos(theta)
        y_out = d - r_out + r_out * np.sin(theta)
        x_in = r_out + r_in * np.cos(theta)
        y_in = d - r_out + r_in * np.sin(theta)

        points.append((x_out, y_out))
        points.append((x_in, y_in))

    for i in range(len(points) / 2):
        if i != len(points) / 2 - 1:
            facets.append((i * 2, i * 2 + 2))
            facets.append((i * 2 + 1, i * 2 + 3))
        else:
            facets.append((i * 2, 0))
            facets.append((i * 2 + 1, 1))

    return (points, facets, holes)

def ISection(d, b, tf, tw, r, n_r):
    points = []
    facets = []
    holes = []

    points.append((0, 0))
    points.append((b, 0))
    points.append((b, tf))

    # bottom right radius
    for i in range(n_r):
        theta = 3.0 / 2 * np.pi * (1 - i * 1.0 / max(1, n_r - 1) * 1.0 / 3)

        x = b * 0.5 + tw * 0.5 + r + r * np.cos(theta)
        y = tf + r + r * np.sin(theta)

        points.append((x, y))

    # top right radius
    for i in range(n_r):
        theta = np.pi * (1 - i * 1.0 / max(1, n_r - 1) * 0.5)

        x = b * 0.5 + tw * 0.5 + r + r * np.cos(theta)
        y = d - tf - r + r * np.sin(theta)

        points.append((x, y))

    points.append((b, d - tf))
    points.append((b, d))
    points.append((0, d))
    points.append((0, d - tf))

    # top left radius
    for i in range(n_r):
        theta = np.pi * 0.5 * (1 - i * 1.0 / max(1, n_r - 1))

        x = b * 0.5 - tw * 0.5 - r + r * np.cos(theta)
        y = d - tf - r + r * np.sin(theta)

        points.append((x, y))

    # bottom left radius
    for i in range(n_r):
        theta = -np.pi * i * 1.0 / max(1, n_r - 1) * 0.5

        x = b * 0.5 - tw * 0.5 - r + r * np.cos(theta)
        y = tf + r + r * np.sin(theta)

        points.append((x, y))

    points.append((0, tf))

    for i in range(len(points)):
        if i != len(points) - 1:
            facets.append((i, i + 1))
        else:
            facets.append((len(points) - 1, 0))

    return (points, facets, holes)

def PFC(d, b, tf, tw, r, n_r):
    points = []
    facets = []
    holes = []

    points.append((0, 0))
    points.append((b, 0))
    points.append((b, tf))

    # bottom right radius
    for i in range(n_r):
        theta = 3.0 / 2 * np.pi * (1 - i * 1.0 / max(1, n_r - 1) * 1.0 / 3)

        x = tw + r + r * np.cos(theta)
        y = tf + r + r * np.sin(theta)

        points.append((x, y))

    # top right radius
    for i in range(n_r):
        theta = np.pi * (1 - i * 1.0 / max(1, n_r - 1) * 0.5)

        x = tw + r + r * np.cos(theta)
        y = d - tf - r + r * np.sin(theta)

        points.append((x, y))

    points.append((b, d - tf))
    points.append((b, d))
    points.append((0, d))

    for i in range(len(points)):
        if i != len(points) - 1:
            facets.append((i, i + 1))
        else:
            facets.append((len(points) - 1, 0))

    return (points, facets, holes)

def Angle(d, b, t, r, n_r):
    points = []
    facets = []
    holes = []

    points.append((0, 0))
    points.append((b, 0))
    points.append((b, t))

    # bottom right radius
    for i in range(n_r):
        theta = 3.0 / 2 * np.pi * (1 - i * 1.0 / max(1, n_r - 1) * 1.0 / 3)

        x = t + r + r * np.cos(theta)
        y = t + r + r * np.sin(theta)

        points.append((x, y))

    points.append((t, d))
    points.append((0, d))

    for i in range(len(points)):
        if i != len(points) - 1:
            facets.append((i, i + 1))
        else:
            facets.append((len(points) - 1, 0))

    return (points, facets, holes)

def Flat(d, b):
    points = [(0,0), (b, 0), (b, d), (0, d)]
    facets = [(0,1), (1,2), (2,3), (3,0)]
    holes = []

    return (points, facets, holes)

def Round(r, n):
    points = []
    facets = []
    holes = []

    for i in range(n):
        theta = i * 2 * np.pi * 1.0 / n

        x = r * np.cos(theta)
        y = r * np.sin(theta)

        points.append((x, y))

        if i != n - 1:
            facets.append((i, i + 1))
        else:
            facets.append((i, 0))

    return (points, facets, holes)

def Tee(d, b, tf, tw, r, n_r):
    points = []
    facets = []
    holes = []

    points.append((b * 0.5 - tw * 0.5, 0))
    points.append((b * 0.5 + tw * 0.5, 0))

    # top right radius
    for i in range(n_r):
        theta = np.pi * (1 - i * 1.0 / max(1, n_r - 1) * 0.5)

        x = b * 0.5 + tw * 0.5 + r + r * np.cos(theta)
        y = d - tf - r + r * np.sin(theta)

        points.append((x, y))

    points.append((b, d - tf))
    points.append((b, d))
    points.append((0, d))
    points.append((0, d - tf))

    # top left radius
    for i in range(n_r):
        theta = np.pi * 0.5 * (1 - i * 1.0 / max(1, n_r - 1))

        x = b * 0.5 - tw * 0.5 - r + r * np.cos(theta)
        y = d - tf - r + r * np.sin(theta)

        points.append((x, y))

    for i in range(len(points)):
        if i != len(points) - 1:
            facets.append((i, i + 1))
        else:
            facets.append((len(points) - 1, 0))

    return (points, facets, holes)

def Cee(d, b, l, t, r_out, n_r):
    points = []
    facets = []
    holes = []
    r_in = r_out - t

    # bottom left radius out
    for i in range(n_r):
        theta = np.pi + i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = r_out + r_out * np.cos(theta)
        y_out = r_out + r_out * np.sin(theta)

        points.append((x_out, y_out))

    # bottom right radius out
    for i in range(n_r):
        theta = 3.0 / 2 * np.pi + i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = b - r_out + r_out * np.cos(theta)
        y_out = r_out + r_out * np.sin(theta)

        points.append((x_out, y_out))

    points.append((b, l))
    points.append((b - t, l))

    # bottom right radius in
    for i in range(n_r):
        theta = 2 * np.pi - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_in = b - r_out + r_in * np.cos(theta)
        y_in = r_out + r_in * np.sin(theta)

        points.append((x_in, y_in))

    # bottom left radius in
    for i in range(n_r):
        theta = 3.0 / 2 * np.pi - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_in = r_out + r_in * np.cos(theta)
        y_in = r_out + r_in * np.sin(theta)

        points.append((x_in, y_in))

    # top left radius in
    for i in range(n_r):
        theta = np.pi - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_in = r_out + r_in * np.cos(theta)
        y_in = d - r_out + r_in * np.sin(theta)

        points.append((x_in, y_in))

    # top right radius in
    for i in range(n_r):
        theta = np.pi * 0.5 - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_in = b - r_out + r_in * np.cos(theta)
        y_in = d - r_out + r_in * np.sin(theta)

        points.append((x_in, y_in))

    points.append((b - t, d - l))
    points.append((b, d - l))

    # top right radius out
    for i in range(n_r):
        theta = i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = b - r_out + r_out * np.cos(theta)
        y_out = d - r_out + r_out * np.sin(theta)

        points.append((x_out, y_out))

    # top left radius out
    for i in range(n_r):
        theta = 0.5 * np.pi + i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = r_out + r_out * np.cos(theta)
        y_out = d - r_out + r_out * np.sin(theta)

        points.append((x_out, y_out))

    for i in range(len(points)):
        if i != len(points) - 1:
            facets.append((i, i + 1))
        else:
            facets.append((len(points) - 1, 0))

    return (points, facets, holes)

def Zed(d, b1, b2, l, t, r_out, n_r):
    points = []
    facets = []
    holes = []
    r_in = r_out - t

    # bottom left radius out
    for i in range(n_r):
        theta = np.pi + i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = r_out + r_out * np.cos(theta)
        y_out = r_out + r_out * np.sin(theta)

        points.append((x_out, y_out))

    # bottom right radius out
    for i in range(n_r):
        theta = 3.0 / 2 * np.pi + i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = b1 - r_out + r_out * np.cos(theta)
        y_out = r_out + r_out * np.sin(theta)

        points.append((x_out, y_out))

    points.append((b1, l))
    points.append((b1 - t, l))

    # bottom right radius in
    for i in range(n_r):
        theta = 2 * np.pi - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_in = b1 - r_out + r_in * np.cos(theta)
        y_in = r_out + r_in * np.sin(theta)

        points.append((x_in, y_in))

    # bottom left radius in
    for i in range(n_r):
        theta = 3.0 / 2 * np.pi - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_in = r_out + r_in * np.cos(theta)
        y_in = r_out + r_in * np.sin(theta)

        points.append((x_in, y_in))

    # top right radius out
    for i in range(n_r):
        theta = i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = t - r_out + r_out * np.cos(theta)
        y_out = d - r_out + r_out * np.sin(theta)

        points.append((x_out, y_out))

    # top left radius out
    for i in range(n_r):
        theta = np.pi * 0.5 + i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_out = t - b2 + r_out + r_out * np.cos(theta)
        y_out = d - r_out + r_out * np.sin(theta)

        points.append((x_out, y_out))

    points.append((t - b2, d - l))
    points.append((t - b2 + t, d - l))

    # top left radius in
    for i in range(n_r):
        theta = np.pi - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_in = t - b2 + r_out + r_in * np.cos(theta)
        y_in = d - r_out + r_in * np.sin(theta)

        points.append((x_in, y_in))

    # top right radius in
    for i in range(n_r):
        theta = 0.5 * np.pi - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x_in = t - r_out + r_in * np.cos(theta)
        y_in = d - r_out + r_in * np.sin(theta)

        points.append((x_in, y_in))

    for i in range(len(points)):
        if i != len(points) - 1:
            facets.append((i, i + 1))
        else:
            facets.append((len(points) - 1, 0))

    return (points, facets, holes)

def Cruciform(d, b, t, r, n_r):
    points = []
    facets = []
    holes = []

    points.append((-t * 0.5, -d * 0.5))
    points.append((t * 0.5, -d * 0.5))

    # bottom right radius
    for i in range(n_r):
        theta = np.pi - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x = 0.5 * t + r + r * np.cos(theta)
        y = -0.5 * t - r + r * np.sin(theta)

        points.append((x, y))

    points.append((0.5 * b, -t * 0.5))
    points.append((0.5 * b, t * 0.5))

    # top right radius
    for i in range(n_r):
        theta = 1.5 * np.pi - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x = 0.5 * t + r + r * np.cos(theta)
        y = 0.5 * t + r + r * np.sin(theta)

        points.append((x, y))

    points.append((t * 0.5, 0.5 * d))
    points.append((-t * 0.5, 0.5 * d))

    # top left radius
    for i in range(n_r):
        theta = -i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x = -0.5 * t - r + r * np.cos(theta)
        y = 0.5 * t + r + r * np.sin(theta)

        points.append((x, y))

    points.append((-0.5 * b, t * 0.5))
    points.append((-0.5 * b, -t * 0.5))

    # bottom left radius
    for i in range(n_r):
        theta = np.pi * 0.5 - i * 1.0 / max(1, n_r - 1) * np.pi * 0.5

        x = -0.5 * t - r + r * np.cos(theta)
        y = -0.5 * t - r + r * np.sin(theta)

        points.append((x, y))

    for i in range(len(points)):
        if i != len(points) - 1:
            facets.append((i, i + 1))
        else:
            facets.append((len(points) - 1, 0))

    return (points, facets, holes)
