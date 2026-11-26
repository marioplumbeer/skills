"""Narrate a plain-text story with Kokoro (ONNX), sentence by sentence, with pauses.

Usage: python3 -I tts.py <speed> <voice> <out.wav> <story.txt> <lang> [model_dir]
Prints the audio duration in seconds.
"""
import re
import sys

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

speed, voice, out, src, lang = float(sys.argv[1]), *sys.argv[2:6]
model_dir = sys.argv[6] if len(sys.argv) > 6 else "/home/claude/k"

kokoro = Kokoro(f"{model_dir}/kokoro.onnx", f"{model_dir}/voices.bin")
text = open(src, encoding="utf-8").read()
paragraphs = [p.strip().replace("\n", " ") for p in text.split("\n\n") if p.strip()]

chunks, sample_rate = [], 24000
for paragraph in paragraphs:
    for sentence in re.split(r"(?<=[.!?])\s+", paragraph):
        audio, sample_rate = kokoro.create(sentence, voice=voice, speed=speed, lang=lang)
        chunks.append(audio)
        chunks.append(np.zeros(int(sample_rate * 0.25)))  # pause between sentences
    chunks.append(np.zeros(int(sample_rate * 0.45)))  # pause between paragraphs

audio = np.concatenate(chunks)
sf.write(out, audio, sample_rate)
print(len(audio) / sample_rate)
