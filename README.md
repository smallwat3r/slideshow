# Slideshow Creator

A minimal tool to create video slideshows by chaining images and videos using [moviepy](https://github.com/Zulko/moviepy).

## Features

- Automatically generates a video slideshow from files in the media/ folder
- Supports both images and videos
- Randomizes media order
- Smooth fade transitions

## Default settings

- Output filename: slideshow.mp4
- Image duration: 3 seconds
- Fade duration (in/out): 0.5 seconds
- Frame rate: 24 FPS
- Audio: Disabled

You can customize these settings in the `config.py` file.

## Installation

Install `moviepy` via pip:

    pip install moviepy

## Usage

1. Place your images and videos in the `media/` directory.
    > note that the order of the media will be randomised.

2. Run the script:

    python3 main.py

3. Your generated slideshow will be saved as slideshow.mp4.
