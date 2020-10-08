# сохраняет спектограмму n-файла из папки с wav-аудио
import os
from os import path
from pydub import AudioSegment
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import pylab
from PIL import Image
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#загружаем все имена файлов в files формата 'name.mp3'
directory = 'D:/test'
files = os.listdir(directory)
for k in range (0,76564):
    filename = "{}{}".format("D:/test/",files[k])
    y, sr = librosa.load(filename)
    fig, ax = plt.subplots()
    # trim silent edges
    whale_song, _ = librosa.effects.trim(y)
    librosa.display.waveplot(whale_song, sr=sr);
    n_fft = 2048
    D = np.abs(librosa.stft(whale_song[:n_fft], n_fft=n_fft, hop_length=n_fft+1))
    hop_length = 256
    D = np.abs(librosa.stft(whale_song, n_fft=n_fft, hop_length=hop_length))
    librosa.display.specshow(D, sr=sr, y_axis='linear');
    DB = librosa.amplitude_to_db(D, ref=np.max)
    librosa.display.specshow(DB, sr=sr, hop_length=hop_length, y_axis='log');
    pylab.axis('off')
    plt.gca().set_axis_off()
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    save_path = "{}{}{}".format('D:/image/', files[k], '.png')
    plt.savefig(save_path)
    plt.clf()
