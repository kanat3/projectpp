#### 21.09.2020
1. Доделаны флаер и Диаграмма Ганта

#### 23.09.2020
1. Закинула флаер и Диаграмму Ганта на диск

#### 24.09.2020
1. Закинула файл с содержанием некоторых статей на диск
2. Наконец-то написала что-то в git'е по workflow

#### 25.09.2020
1. Загрузила библиотеки librosa, matplotlib
2. Нашла какой-то код wav to mel-spect

#### 25.09.2020
1. Код работает!! Ой....

#### 27.09.2020
1. Код строит mel-спектограмму без ошибок

#### 28.09.2020
1. Стырила код отсюда https://pythonbasics.org/convert-mp3-to-wav/
2. Теперь код может конвертировать любое кол-во файлов mp3 в wav
3. Датасет наконец-то в формате wav

#### 29.09.2020
1. https://github.com.cnpmjs.org/OmarHory/VoiceGenderRecognition - отсюда беру модель
#### 04.09.2020 - 05.09.2020
1. Переделала код для конвертации mp3 в wav.
2. Сконвертировала все файлы датасета

#### 06.09.2020
1. Посмотрела видосики про загрузку датасетов и их подготовку
2. Скорректировала код для спектограммы, теперь функция загружает чистое изображение (без всех шкал)
3. Нашла функцию, которая переводит изображение в тензор (это же так говорится??) и показывает его расширение.
#### 07.09.2020
1. я.ботала.матан.
2. https://pythonprogramming.net/loading-custom-data-deep-learning-python-tensorflow-keras/ - пример загрузки датасета 
3. Желаю здоровья мудрому человеку с данного сайта https://stackoverflow.com/questions/11837979/removing-white-space-around-a-saved-image-in-matplotlib
т.к он решил проблему с белым окном вокруг спектограммы.
4. О, загрузила картиночки с jupiter на git
5. Теперь есть код, который сохраняет необходимые графики n-ого кол-ва файлов 
#### 08.09.2020
1. Ноутбук загрузил всего лишь 14к изображений по аудио. *плак*
2. Русскоязычный код загрузки/подготовки данных на примере котов и собак (постоянно теряю ссылку) https://github.com/sozykin/dlpython_course/blob/master/computer_vision/cats_and_dogs/data_preparation.ipynb
3. Добралась до csv-файлов, удалила ненужные столбцы и оставила только те названия аудио, в которых есть данные и о возрасте и о поле.
Придётся чистить папки с wav аудио и с изображениями? Или заново конвертировать? А, или просто буду проверять имя файла на наличие в списке csv 
4. Отредактировала файлы test, train, загрузила код на git. Проверила test и train на совпадения, всё хорошо.
#### 09.09.2020
1. Исправила ошибку с недостатком памяти при сохранении спектограммы (необходимо было закрыть окно графика с помощью функции plt.close())
2. Загружена половина датасета ~38к
3. Изменена модель свёрточной нейронной сети под изображение 432x288, добавлены новые слои Conv2D() и Dropout()
4. https://neurohive.io/ru/tutorial/cnn-na-pytorch/ (на почитать)
