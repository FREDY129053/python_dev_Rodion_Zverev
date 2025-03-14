# Выполнение тестового задания для практики FarPost

### Инстуркция по запуску:
1. Склонировать репозиторий через ```git clone```
2. Перейти в склонированный репозиторий
3. Запустить Docker и с помощью ```docker-compose up --build -d``` запустить проект
4. Перейти на страницу документации - http://localhost:8080/docs

### Инструменты и библиотеки
- В качестве базы данных был выбран **PostgreSQL 16**
- Для реализации эндпоинтов была выбрана библиотека **Fast API**
- Для удобного подключения к БД и работы с ней была выбрана ORM **Tortoise**

### База данных
#### 1. Изменения

Для подсчета кол-ва комментариев база данных авторов была расширена, путем добавления таблицы **comments**.

Comments:
- id - int, primary key. Уникальный идентификатор.
- text - varchar(255). Текст комментария.
- author_id - int, foreign key в таблицу **users** к полю id. Указывает на автора комментария.
- post_id - int, foreign key в таблицу **posts** к полю id. Указывает к какому посту принадлежит комментарий.

В таблице **users** поля *email* и *login* сделал уникальными на всякий случай.

#### 2. Данные

В ходе разработки базы данных была заполнена некоторыми данными.
     
  1. База данных авторов(**authors_database**) 
      - Таблица **users**
        
        ![users data](<Снимок экрана (1901)-1.png>)
      
      - Таблица **blogs**
        
        ![blogs data](<Снимок экрана (1902).png>)

      - Таблица **posts**

        ![posts data](<Снимок экрана (1903).png>)

      - Таблица **comments**

        ![comments data](<Снимок экрана (1908).png>)
  
  2. База данных логов(**logs_database**)

      - Таблица **logs**

        ![logs data](<Снимок экрана (1905).png>)

      - Таблица **event_type**

        ![event_type data](<Снимок экрана (1906).png>)

      - Таблица **space_type**
        
        ![space_type data](<Снимок экрана (1907).png>)

### Endpoints

*/api/coments*:
- возвращает список данных о комментариях, которые писал пользователь к разным постам.
- принимает **user_login** - логин пользователя из БД.
- если пользователя нет в БД, то возвращает ошибку 404.
- если пользователь не писал комментарии(например пользователь *login_10*), то возвращает пустой массив.

*/api/general*:
- возвращает список логов пользователя за **каждый день**. Поскольку в ТЗ не говорилось как ограничивать поле *datetime* при выборке, то я ограничился датой в формате "YYYY-MM-DD", получив активность за каждый записанный день.
- если нет логов от пользователя(*login_3* например), то возвращает пустой массив.
- принимает 2 параметра: **user_login** или/и **user_id**.

    1. Если передается **user_login**, то идет обращение в первую БД(authors_database), чтобы узнать ID пользователя по логину. Далее идет выборка по этому ID в таблице **logs**.

    2. Если передается **user_id**, то выборка сразу идет по таблице **logs**. 

    3. Если передается **user_login** и **user_id** вместе, то выборка идет по первому пункту и в случае провала идет как во втором случае.

Такая реализация была предпринята, т.к. в ТЗ сказано, что "*user_id может содержать идентификаторы пользователи из разных БД...*", то при передачи только **user_login** мы не можем получить user_id из других(неизвестных) БД.

Была идея передавать просто одно поле(str | int) и проверять: если это число, то это **user_id**, иначе это логин. Но, в теории, возможна ситуация, что логин будет "123" и **user_id** из другой БД прилетит 123 и тогда как искать. К тому же, такое можно сделать, если ограничить *login*, чтобы он был не числом.

Вывод даты может немного отличаться, быть на день меньше, потому что *datetime.datetime* в Python это *timestamp with timezone* в PostgreSQL

Так же, для более удобной проверки кейса, было решено добавить 2 эндпоинта метода **POST** для занесения данных в БД:

1. */api/comments* - занесение комментариев в таблицу **comments**.
 
    Принимает:
      - **text** - текст комментария.
      - **author** - логин автора комментария.
      - **post** - id поста, к которому принадлежит комментарий.

2. */api/general* - создание записи лога в таблицу **logs**.

    Принимает:
      - **datetime** - время лога(datetime.datetime из Python).
      - **user_id** - id пользователя.
      - **event_type** - тип события. На его основе заполняется ячейка **space_type**.

### Спасибо, что дочитали)
