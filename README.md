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

#### 06.10.2020
1. Посмотрела видосики про загрузку датасетов и их подготовку
2. Скорректировала код для спектограммы, теперь функция загружает чистое изображение (без всех шкал)
3. Нашла функцию, которая переводит изображение в тензор (это же так говорится??) и показывает его расширение.
#### 07.10.2020
1. я.ботала.матан.
2. https://pythonprogramming.net/loading-custom-data-deep-learning-python-tensorflow-keras/ - пример загрузки датасета 
3. Желаю здоровья мудрому человеку с данного сайта https://stackoverflow.com/questions/11837979/removing-white-space-around-a-saved-image-in-matplotlib
т.к он решил проблему с белым окном вокруг спектограммы.
4. О, загрузила картиночки с jupiter на git
5. Теперь есть код, который сохраняет необходимые графики n-ого кол-ва файлов 
#### 08.10.2020
1. Ноутбук загрузил всего лишь 14к изображений по аудио. *плак*
2. Русскоязычный код загрузки/подготовки данных на примере котов и собак (постоянно теряю ссылку) https://github.com/sozykin/dlpython_course/blob/master/computer_vision/cats_and_dogs/data_preparation.ipynb
3. Добралась до csv-файлов, удалила ненужные столбцы и оставила только те названия аудио, в которых есть данные и о возрасте и о поле.
Придётся чистить папки с wav аудио и с изображениями? Или заново конвертировать? А, или просто буду проверять имя файла на наличие в списке csv 
4. Отредактировала файлы test, train, загрузила код на git. Проверила test и train на совпадения, всё хорошо.
#### 09.10.2020
1. Исправила ошибку с недостатком памяти при сохранении спектограммы (необходимо было закрыть окно графика с помощью функции plt.close())
2. Загружена половина датасета ~38к
3. Изменена модель свёрточной нейронной сети под изображение 432x288, добавлены новые слои Conv2D() и Dropout()
4. https://www.tensorflow.org/tutorials/load_data/images?hl=ru загрузка датасета *а смысл........*
5. Отредактировала train, test, validated файлы, в train отсутсвуют возраста двух категорий, скорее всего validated буду обучать модель
#### 10.10.2020
1. Проверила датасет на потерю данных или ещё чего, всё совпадает, cool
2. Отредактировала train, test, validated файлы, загрузла код
3. Ура, фулл dataset
#### 11.10.2020 - 12.10.2020
1. Отсортировала изображения по папкам
2. Загрузила код на гит
#### 14.10.2020 
1. Посмотрела видосик https://www.youtube.com/watch?v=q7ZuZ8ZOErE
2. Сломала анаконду.................
3. Некоторые пакеты получили в названии "-", к примеру -aplotlib, пришлось переустановить анаконду
4. Ого, я что-то загрузила. Чота долго обучается))
5. Тут про визуализацию данных и про методы против переобучения https://habr.com/ru/post/458170/
6. Тут говорят, что попробовать, если точность низкая https://ru.stackoverflow.com/questions/834469/keras-низкая-точность-нейронной-сети
#### 15. 10. 2020
1. Ноутбук обучил модель, которая предсказывает гендер по голосу, на одной эпохе. Обучалась часа 3. 
2. Загрузила датасет в модель, которая предсказывает возраст по голосу. Ещё не обучала, но на первой эпохе точность 0.1951, т.е чистое угадывание, 
в отличие от предыдущей модели, где точность на начале обучения была под 0,79
3. Проверила первую модель после обучения на первой эпохе на тестовых данных, loss: 1.9131 - accuracy: 0.8745,
на обучающей выборке loss: 3.0752 - accuracy: 0.7983, на val данных val_loss: 1.8196 - val_accuracy: 0.8807
4. Загрузила код на гит.
5. Больше ничего не успела.
#### 25.10.2020
1. Итак, снова я, снова здесь. 
2. Я тоже хочу пользоваться процессором ноутбука, поэтому самое время перейти на гугл колаб
3. Да начнутся мои страдания
4. Мини-заметочка: поменяла пути к test и validation data, теперь валидационные данные в размере 13к, тестовые в размере 4к
#### 26.10.2020
1. Снова проблемы... Почему-то некоторые папки в датасете были удалены, ну да ладно.
2. Дописала полноценный код копирования спектограмм по папкам.
3. Вот так выглядият мои папки на примере train 
<img src="data:image/png;base64,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" /> 

