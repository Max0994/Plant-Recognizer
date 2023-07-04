Plant Recognizer
Description
The Plant Recognizer project allows for the identification of plants and distinguishing them from weeds or wild grass. The main objective of the project is to create a system capable of real-time weed detection and applying necessary solutions for their elimination. This enables cultivated plants to grow more healthily, ultimately increasing crop yields. The most challenging part of the project lies in developing code that can accurately differentiate between different plant species.

The project aims to optimize herbicide usage by minimizing waste. Typically, a significant amount of herbicide is required to eradicate weeds or wild grass. With the Plant Recognizer, it is possible to save approximately 60-70% of the herbicide used. Additionally, based on this neural network, robots can be developed in the future to assist in crop harvesting.

Please note that the project is currently in the prototype stage. In the future, I would create an application with a user-friendly interface where users can select plant species for identification. Furthermore, I would develop a physical prototype of the system.

Usage Instructions
You can interact with the Telegram bot @PlantRecognizerBot to identify plant species. Alternatively, you can place several images in the data/test/ folder and run classify_image.py. The console will display the analysis results for each image along with the plant's name. There is also a classify_stream.py file, which ideally should perform analysis using a webcam. However, due to limited time, I was unable to thoroughly test this functionality.

To train the model, you can run main.py, but please note that the model is already trained, so running this script is not necessary for immediate use. Please be aware that the prototype was trained using approximately 200 images, whereas a real project would utilize a much larger dataset.


Plant Recognizer (RU)
Описание
Проект Plant Recognizer позволяет идентифицировать растения и отличать их от диких трав или сорняков. Основная цель проекта заключается в создании системы, способной определять сорняки в режиме реального времени и применять необходимые решения для их уничтожения. Это позволяет выращиваемым растениям расти более здорово, увеличивая урожай. Самая сложная часть проекта заключается в разработке кода, способного точно различать разные виды растений.

Проект направлен на оптимизацию использования гербицидов путем минимизации их расходования. Обычно для уничтожения сорняков или диких трав требуется значительное количество гербицида. С помощью Plant Recognizer можно сэкономить примерно 60-70% используемого гербицида. Кроме того, в будущем на основе данной нейронной сети можно создать роботов, помогающих собирать урожай.

Пожалуйста, учтите, что на данный момент проект находится в стадии прототипа. В будущем я бы создал приложение с удобным интерфейсом, где пользователи могли бы выбирать виды растений для идентификации. Кроме того, я бы создал физический прототип системы.

Инструкции по использованию
Вы можете взаимодействовать с ботом Telegram @PlantRecognizerBot для идентификации видов растений. В качестве альтернативы вы можете поместить несколько изображений в папку data/test/ и запустить classify_image.py. Консоль отобразит результаты анализа для каждого изображения вместе с названием растения. Также имеется файл classify_stream.py, который, по идее, должен выполнять анализ с использованием веб-камеры. Однако из-за ограниченного времени я не смог полностью протестировать эту функциональность.

Для обучения модели вы можете запустить main.py, но обратите внимание, что модель уже обучена, поэтому запуск этого скрипта не требуется для немедленного использования. Пожалуйста, учтите, что прототип был обучен с использованием примерно 200 изображений, в то время как в реальном проекте было бы использовано гораздо большее количество данных.
