# Slideshow Creator

I was looking for a super simple tool to create a slideshow of images and videos for a wedding.

I couldn’t find one that was simple, free, and automated, so I built my own using [moviepy](https://github.com/Zulko/moviepy).

Hope it helps someone else too!

## Features

- Automatically generates a video slideshow from files in the medias/ folder
- Supports both images and videos
- Randomizes medias order
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

1. Place your images and videos in the `medias/` directory.

    > note that the order of the media will be randomised

    > you might want to run `mogrify -auto-orient *.jpg` in the medias/ folder, from experience it helps ensure no pictures get rotated after processing

2. Run the script:

        python3 main.py

3. Your generated slideshow will be saved as slideshow.mp4.
