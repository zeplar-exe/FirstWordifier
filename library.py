from moviepy import *
from moviepy.editor import *
import whisper_timestamped

import numpy as np
import os
import tempfile

def first_wordify(video_file: str, language: str="en", output_file: str="out.mp4", model="base.en"):
    video = VideoFileClip(video_file)
    audio = video.audio

    waveform_file = tempfile.TemporaryFile(suffix=".wav")
    waveform_filename = waveform_file.name
    waveform_file.close()

    print(f"Extracting waveform audio to {waveform_filename}.")

    audio.write_audiofile(waveform_filename)
    waveform = waveform_filename

    print("Loading whisper model.")
    
    model = whisper_timestamped.load_model(model)
    result = whisper_timestamped.transcribe(model, waveform_filename, language=language, remove_punctuation_from_words=True, remove_empty_words=True, beam_size=5, best_of=5, temperature=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0))

    words = {}
    occurances = []

    print("Iterating segments.")

    for segment in result["segments"]:
        for word in segment["words"]:
            w = word["text"].lower()

            if w not in words:
                start = word["start"]
                end = word["end"]
                length = end - start
                margin = length / 4

                words[w] = video.subclip(max(0, start - margin), min(end + margin, video.duration))
            else:
                occurances.append(word)
    
    print(f"Detected {len(words)} distinct words.")

    clips = []
    head = 0

    print("Editing video.")

    for occurance in occurances:
        word = occurance["text"].lower()
        start = occurance["start"]
        end = occurance["end"]

        clips.append(video.subclip(head, start))
        clips.append(words[word])

        head = end
    
    clips.append(video.subclip(head))

    print(f"Exporting to {output_file}")
    final = concatenate_videoclips(clips)
    final.write_videofile(output_file)

    os.remove(waveform_filename)
    video.close()
    audio.close()