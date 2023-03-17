import numpy as np
import imageio

'''
 plot_planet - returns a 3d sphere with all the planets belong to the solar system and the sun. 
 
 Prototype: plot_planet('planet', ax)
 
 Input:
        'planet' [string] can be one of the 9 planets or the sun. Notice that the name must be all in small letters, 
        for example 'earth' or 'venus'
        ax [1 x 1] number of the axis of the plot
        
Output:
        3D sphere representing the planet centred in the origin of the plot

 AUTHOR: Giovanni Facchinetti, 2023
 
'''
def plot_planet(planet_name, ax):
    # Define planet properties
    planets = {
        'sun': {
            'radius': 695700.0,  # km
            'color': 'yellow',
            'texture': 'https://www.solarsystemscope.com/textures/download/8k_sun.jpg'
        },
        'mercury': {
            'radius': 2439.7,  # km
            'color': 'gray',
            'texture': 'https://www.solarsystemscope.com/textures/download/8k_mercury.jpg'
        },
        'venus': {
            'radius': 6051.8,  # km
            'color': 'orange',
            'texture': 'https://www.solarsystemscope.com/textures/download/8k_venus_surface.jpg'
        },
        'earth': {
            'radius': 6371.0,  # km
            'color': 'blue',
            'texture': 'https://www.solarsystemscope.com/textures/download/8k_earth_daymap.jpg'

        },
        'mars': {
            'radius': 3389.5,  # km
            'color': 'red',
            'texture': 'https://www.solarsystemscope.com/textures/download/8k_mars.jpg'
        },
        'jupiter': {
            'radius': 69911.0,  # km
            'color': 'brown',
            'texture': 'https://www.solarsystemscope.com/textures/download/8k_jupiter.jpg'
        },
        'saturn': {
            'radius': 58232.0,  # km
            'color': 'goldenrod',
            'texture': 'https://www.solarsystemscope.com/textures/download/8k_saturn.jpg'
        },
        'uranus': {
            'radius': 25362.0,  # km
            'color': 'cyan',
            'texture': 'https://www.solarsystemscope.com/textures/download/2k_uranus.jpg'
        },
        'neptune': {
            'radius': 24622.0,  # km
            'color': 'blueviolet',
            'texture': 'https://www.solarsystemscope.com/textures/download/2k_neptune.jpg'
        },
        'pluto': {
            'radius': 1188.3,  # km
            'color': 'gray',
                    },
    }

    # Get planet properties
    planet = planets.get(planet_name)
    if planet is None:
        raise ValueError(f'Invalid planet name: {planet_name}')

    # Create planet
    u, v = np.mgrid[0:2 * np.pi:100j, 0:np.pi:100j]
    x = planet['radius'] * np.cos(u) * np.sin(v)
    y = planet['radius'] * np.sin(v) * np.sin(u)
    z = planet['radius'] * np.cos(v)

    if 'texture' in planet:
        # Load the image from the internet URL
        image_url = planet['texture']
        image = imageio.imread(image_url)

        # Flip the image vertically
        image = np.flipud(image)
        # Set the texture coordinates based on the sphere coordinates
        phi = np.arctan2(y, x)
        theta = np.arccos(z / planet['radius'])

        # Convert texture coordinates to pixel coordinates
        texture_x = (phi + np.pi) / (2 * np.pi) * image.shape[1]
        texture_y = (np.pi - theta) / np.pi * (image.shape[0] - 1)

        # Make sure the image array is large enough
        image = np.pad(image,
                       [(max(0, int(texture_y.max() - image.shape[0])) // 2,
                         max(0, int(texture_y.max() - image.shape[0])) // 2 + max(0, int(texture_y.max() - image.shape[
                             0])) % 2),
                        (0, max(0, int(texture_x.max() - image.shape[1]))),
                        (0, 0)], mode='edge')

        # Sample the texture at the given coordinates
        texture = image[np.clip(texture_y.astype(int), 0, image.shape[0] - 1), np.clip(texture_x.astype(int), 0,
                                                                                       image.shape[1] - 1)]
        # Plot the textured sphere
        ax.plot_surface(x, y, z, facecolors=texture / 255.0, shade=True)

    else:
        # Plot the solid-colored sphere
        ax.plot_surface(x, y, z, rstride=1, cstride=1, color=planet['color'], alpha=0.5)
