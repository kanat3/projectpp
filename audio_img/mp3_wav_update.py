from os import path
from pydub import AudioSegment
import os
for k in range (0,76565):
  src = "{}{}{}".format("C:/Users/localadmin/Desktop/clips/",files[k], ".mp3")
  dst = "{}{}{}".format("C:/Users/localadmin/Desktop/test/",files[k], ".wav")
  # convert wav to mp3 
  sound = AudioSegment.from_mp3(src)
  sound.export(dst, format="wav")
