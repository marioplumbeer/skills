---
name: plumbeer-kids-story-audio
description: >-
  Use when the user wants a children's story as audio: a bedtime story, a kids audio
  story, "tell/narrate a story about X", or a story plus speech/MP3. Writes an original
  story tailored to the child's age (mandatory, never assumed), topic and target length
  in minutes, narrates it with a natural neural voice in the requested language
  (Portuguese by default when the user writes in Portuguese), and delivers an MP3 whose
  real duration is within about 5% of the target. Not for adult audiobooks or for
  narrating a text the user already wrote.
license: MIT
compatibility: >-
  Cloud workspace with Python, ffmpeg, apt and pip, and access to GitHub (model download,
  ~325 MB). Not tested offline.
metadata:
  author: plumbeer
  version: "1.0"
  category: creative
---

# Kids Story Audio

## Overview

Write an original children's story and deliver it as a natural-sounding MP3. Age drives
the writing style and narration speed, length drives the word count, and the voice is a
neural Kokoro model so the result does not sound robotic or choppy.

## Confirmation

Before writing, confirm with the user:
- Age of the child (**required, no default**: if missing, ask before anything else; never infer it)
- Topic, and any "only X" constraint (e.g. only airplanes means every character is an airplane)
- Length in minutes (default 5), language (default: the language the user wrote in) and voice

Present these as a one-line plan and ask "Proceed?". Start only after approval. If the
user already gave age, topic and length in the request, restate them and proceed unless
they object.

## Instructions

### Phase 1 — Write the story

Save plain text to `story.txt`: one paragraph per block, blank line between blocks.

- Target words = minutes x 145 (measured at speed 0.93: 705 words = 4m50s; 1358 words at 0.875 = 9m46s).
- Age 2-4: very short sentences, repetition, sound words, 1-2 characters, gentle plot. Speed 0.85.
- Age 5-7: arc of wish, obstacle, help from friends, lesson; 3-5 characters; light humor. Speed 0.90.
- Age 8-12: richer plot, a real problem to solve, more description. Speed 1.0.
- Always original characters (no brands, known characters or songs), kind tone, nothing frightening, and a calm bedtime-style ending. The lesson comes through the plot, not a sermon.
- Write for the ear: no lists, parentheses, stage directions or emojis; no quotation marks (use "disse X"); sentences under about 20 words; end with "Fim."
- Check the count with `wc -w story.txt`.

### Phase 2 — Set up the voice

Follow [references/voice-setup.md](references/voice-setup.md). Always use Kokoro; the
robotic fallback is only for when the model cannot be downloaded, and the user must be told.

### Phase 3 — Synthesize and calibrate

```bash
python3 -I scripts/tts.py <speed> <voice> out.wav story.txt <lang>
```

The script prints seconds. Sentence-by-sentence synthesis with pauses is what removes the
choppy feel, so do not replace it with one call on the whole text. Use a long timeout: 10
minutes of audio takes several minutes.

If the duration is off by more than 5%, rerun once with speed multiplied by
(current / target), clamped to 0.85-1.05. If still off, edit the story instead of pushing speed.

### Phase 4 — Deliver

```bash
ffmpeg -y -loglevel error -i out.wav -af "loudnorm=I=-16:TP=-1.5" -ar 44100 -ac 1 -b:a 128k Title.mp3
```

Send the MP3 with `SendUserFile` (attach) with title and real duration as caption. Reply
in 2-3 sentences: premise, lesson, voice. Offer another voice or speed, and the story text
on request. Do not paste the whole story.

## Gotchas

- Age missing means ask. Writing for the wrong age is the costliest mistake because it forces a full rewrite and re-synthesis.
- HuggingFace is blocked, so voice models from there fail. Use the GitHub release files.
- Keep scripts outside the directory holding generated files, and run Python with `-I`.
- Do not claim the target length; report the measured duration.
- Voices outside the table in the setup reference are untested: say so before using one.
