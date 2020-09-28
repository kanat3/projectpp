from os import path
from pydub import AudioSegment
import os
#загружаем все имена файлов в files формата 'name.mp3'
directory = 'C:/Users/localadmin/Desktop/clips'
files = os.listdir(directory)
#удаляем символы, записанные в переменную bad_chars, во всех файлах
bad_chars = ["'"," "]
for k in range (0,76565):
  files[k] = ''.join(i for i in files[k] if not i in bad_chars) 
#имена конвертирумых файлов [0,1,2...].wav
  export_name = [0]*76565
for k in range (0,76565):
  export_name[k] = k
#конвертируем
for k in range (0,76565):
  src = "{}{}".format("C:/Users/localadmin/Desktop/clips/",files[k])
  dst = "{}{}{}".format("C:/Users/localadmin/Desktop/test/",export_name[k], ".wav")
  # convert wav to mp3 
  sound = AudioSegment.from_mp3(src)
  sound.export(dst, format="wav")
