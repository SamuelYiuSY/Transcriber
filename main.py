import whisper
from moviepy.editor import VideoFileClip
from datetime import timedelta
import os


# ask for input
standardPrompt = "Please input filename, or type \"--help\" to see additional options"
helpPrompt = "usage: <filename> [option] "\
             "this place is reserved for future uses"

print(standardPrompt)
inp = input(">")
loopFlag = True
while loopFlag:
    if inp == "--help":
        print(helpPrompt)
        print(standardPrompt)
        inp = input(">")
    else:
        # handle inputs with arguments
        if len(inp.split()) == 2:
            filename = inp.split()[0]
            option = inp.split()[1]
        else:
            filename = inp
        # check whether filename is valid
        if filename[-4:] == ".mp3" or filename[-4:] == ".mp4":
            loopFlag = False
        else:   # loop
            print(f"Invalid filename! {standardPrompt}")
            inp = input(">")

# convert mp4 to mp3
if filename[-4:] == ".mp4":
    print(f"converting {filename} into a mp3 file")
    video = VideoFileClip(filename)
    video.audio.write_audiofile(str(filename[:-4])+".mp3")

model = whisper.load_model("base")
print("Whisper model loaded.")
result = model.transcribe(filename)

transcriptTextfileName = f"{filename[:-4]}_transcript.srt"

# delete file with the same transcript name
if os.path.exists(transcriptTextfileName):
    os.remove(transcriptTextfileName)

# separate each segments and write to a .srt file
srtSegment = []
for eachSegment in result["segments"]:
    startTime = f"0{str(timedelta(seconds=int(eachSegment['start'])))},000"
    endTime = f"0{str(timedelta(seconds=int(eachSegment['end'])))},000"
    text = eachSegment["text"]
    id = eachSegment["id"] + 1
    srtSegment.append(f"{id}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n")
with open(transcriptTextfileName, "a") as textFile:
    for eachSrtSegment in srtSegment:
        textFile.write(eachSrtSegment)


print(f"Done, your transcript is saved as {transcriptTextfileName}")
