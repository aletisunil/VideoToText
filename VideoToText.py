import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from os import path
#from pydub import AudioSegment
#from os import path
#from ffprobe import FFProbe
#from pydub import AudioSegment

#For video to wav audio
audio_file_name = "transcribed_speech.wav"
video_file_name = "Dns.mp4"
audioclip = AudioFileClip(video_file_name)
audioclip.write_audiofile(audio_file_name)


""" For mp3 audio to wav audio
sound = AudioSegment.from_mp3("04.mp3")
sound.export("transcript.wav", format="wav")
audio_file_name = "transcript.wav"
"""

with contextlib.closing(wave.open(audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
total_duration = math.ceil(duration / 60)
r = sr.Recognizer()
f = open("transcription.txt", "a")
for i in range(0, total_duration):
    with sr.AudioFile(audio_file_name) as source:
        audio = r.record(source, offset=i*60, duration=60)
        f.write(r.recognize_google(audio))
        print(r.recognize_google(audio))
        f.write(" ")
f.close()
print("\n\nDone")