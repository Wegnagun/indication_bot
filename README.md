#  Шаблон для создания проекта телеграм бота  

---------------
## Автор  
[Александр Фокин](https://github.com/Wegnagun)

--------------- 
### Стек технологий:  (Сюда добавлять библиотеки)
Python 3.9, aiogram 3.1.1, python-dotenv 1.0.0  

### Установка: 
#### Windows
`python -m venv venv `  
`venv/Scripts/activate `  
`pip install --upgrade pip `  
`pip install -r requirements.txt `  

#### Структура .env файла:  
`TOKEN=Здесь должен быть Ваш боттокен` добавьте и иные ваши секреты    

### Описание взаимодействия с ботом (Вставил описание структуры шаблона)

+ bot.py - основной исполняемый файл - точка входа в бот
+ .env - файл с переменными окружения (секретными данными) для конфигурации бота
+ .env.example - файл с примерами секретов для GitHub (пока не использую...)
+ .gitignore - файл, сообщающий гиту какие файлы и директории не отслеживать
+ 📁 config_data - директория с модулем конфигурации бота  
    - config.py - модуль для конфигурации бота
+ 📁 database - пакет для работы с базой данных.  
  - database.py - модуль с шаблоном нашей "игрушечной" базы данных (ситуативно)
+ 📁 filters - пакет с самописными фильтрами
  - filters.py - модуль с фильтрами, которые мы напишем под конкретные задачи бота
+ 📁 handlers - пакет с обработчиками
  - other_handlers.py - модуль с обработчиком любых сообщений пользователя,  
  которые не попали в другие обработчики
  - user_handlers.py - модуль с хэндлерами пользователей. Все основные  
  обработчики апдейтов бота будут в этом модуле
+ 📁 keyboards - пакет с клавиатурами бота
+ 📁 lexicon - директория для хранения словарей бота
  - lexicon.py - файл со словарем соответствий команд и запросов отображаемым  
  текстам. То есть, например, если пользователь отправил команду /start - ему  
  должен прийти обратно какой-то текст. Этот текст может меняться со временем  
  или в зависимости от языка пользователя. Удобно хранить такие соответствия в  
  отдельном файле.
+ 📁 services - пакет со вспомогательными инструментами для работы бота
