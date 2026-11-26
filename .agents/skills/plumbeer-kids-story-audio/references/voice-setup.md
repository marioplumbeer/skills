# Voice setup (Kokoro via GitHub releases)

HuggingFace is blocked in the cloud workspace; GitHub and apt are reachable. Always use
Kokoro with the model files from the kokoro-onnx GitHub release.

```bash
apt-get update -q && apt-get install -y -q espeak-ng
pip install --break-system-packages -q kokoro-onnx soundfile
mkdir -p /home/claude/k && cd /home/claude/k
curl -sL -o kokoro.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -sL -o voices.bin  https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
```

The model is ~325 MB (about a minute). Files persist for the session; skip if present.

## Voices and `lang` codes

| Language | lang | Voices (first is default) |
|---|---|---|
| Portuguese (BR) | pt-br | pf_dora, pm_alex, pm_santa |
| English (US) | en-us | af_heart, af_bella, am_michael |
| Spanish | es | ef_dora, em_alex |
| French | fr-fr | ff_siwis |
| Italian | it | if_sara, im_nicola |

If the language is not listed, say so and offer the story text only.

## Fallback (robotic, choppy)

Only if Kokoro cannot be downloaded:

```bash
apt-get install -y -q espeak-ng mbrola mbrola-br2
espeak-ng -v mb-br2 -s 175 -p 55 -g 12 -f story.txt -w out.wav   # ~175 wpm
```

Warn the user that this voice sounds robotic.
