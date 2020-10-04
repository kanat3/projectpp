from os import path
from pydub import AudioSegment
#загружаем все имена файлов в files формата 'name.mp3'
directory = 'C:/Users/localadmin/Desktop/clips'
files = os.listdir(directory)
print(files)
for k in range (0,76565):
  src = "{}{}{}".format("C:/Users/localadmin/Desktop/clips/",files[k], ".mp3")
  dst = "{}{}{}".format("C:/Users/localadmin/Desktop/test/",files[k], ".wav")
  # convert wav to mp3 
  sound = AudioSegment.from_mp3(src)
  sound.export(dst, format="wav")
