# Transcriber

This program transcribes .mp4 or .mp3 files to .srt subtitle files, which can then be imported to video editing softwares directly. 

Setup:
```
pip install -r requirements.txt
```
Requirements:
- ffmpeg
- openai-whisper
- moviepy

Usage:
```
python main.py
```

To do list:
- [ ] add progress bar
- [ ] add transcribers from other sources
- [ ] cross-check the results between sources
