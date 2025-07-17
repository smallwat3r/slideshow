# some images can be re-oriented after processing, in order to
# avoid this, it looks like running this command in the medias
# folder before running this helps:
#     mogrify -auto-orient *.jpg

import os
import random
import logging
from typing import assert_never

from moviepy import (
    ImageClip,
    VideoFileClip,
    concatenate_videoclips,
    vfx,
)

from config import Config as C

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    all_files = [
        os.path.join(C.media_folder, f)
        for f in os.listdir(C.media_folder)
        if f.lower().endswith(C.image_exts + C.video_exts)
    ]
    random.shuffle(all_files)
    total_files = len(all_files)
    clips = []

    for i, fpath in enumerate(all_files):
        ext = os.path.splitext(fpath)[1].lower()
        if ext in C.image_exts:
            clip = ImageClip(fpath).with_duration(C.image_duration)
        elif ext in C.video_exts:
            clip = VideoFileClip(fpath)
        else:
            assert_never(ext)

        clip = clip.with_effects(
            [
                vfx.Resize(height=C.target_height),
                vfx.FadeIn(C.fade_duration),
                vfx.FadeOut(C.fade_duration),
            ]
        )
        clips.append(clip)
        logger.info("Processed file %d on %d", i, total_files)

    if clips:
        final_video = concatenate_videoclips(clips, method="compose")
        final_video.write_videofile(
            C.output_video,
            fps=C.final_fps,
            audio=C.audio,
            threads=C.threads,
        )
    else:
        logger.error("No valid media files found.")


if __name__ == "__main__":
     main()
