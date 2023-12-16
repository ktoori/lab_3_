Инструкция по файлам:
main.py - Загрузка csv файла в PostgreSQL
psycopg2_.py и прочие файлы с названиями библиотек - время выполнения запросов через указанную библиотеку
Pandas_.py - время работы Pandas через подключение к PostgreSQL
Pandas2_.py - время работы Pandas через read_csv

Таблица с временем работы четырёх запросов для каждой библиотеки:
![image](https://github.com/ktoori/lab_3_/assets/152300646/5be9a5df-1da2-4b50-b437-9a0e5575ab99)

Сравнительные графики:
![image](https://github.com/ktoori/lab_3_/assets/152300646/87a10852-6ee0-4fa2-96de-184c5946ae27)

**Psycopg2**
Плюсы: 
- Удобно работать с PostgreSQL.
- Поддерживает основные функции.
- Простая реализация запросов.
Недостатки:
- Медленная по сравнению с некоторыми библиотеками, но не сильно проигрывает SQLite. Предполагаю, что из-за работы с PostgreSQL, потому что время уходит на отправку запроса на сервер, его чтение и обработку.
**SQLite**
Плюсы:
- Есть возможность работать с bd файлом, сама себе база данных и СУБД.
Недостатки: 
- Пришлось переписывать запросы, т.к. не может обработать запрос с EXTRACT, при это в описании оишбки упоминания этому не было, пришлось искать методом тыка и заменять на strftime.
- Достаточно медленная.
- Не различает регистры, поэтому столбцы Airport_fee и airport_fee считала за один, из-за чего возникала ошибка...
**DuckDB**
Плюсы:
- Очень быстро работает.
- Красивый вывод в виде таблички, если использовать .show().
- Создаёт свой duckdb файл за две строчки, легко и быстро! Но есть и возможность подключиться к PostgreSQL.
- Простая реализация запросов.
Недостатки:
- Не нашла)
**Pandas**
Плюсы:
- Позволяет загрузить csv в PostgreSQL ссовместно SQLAlchemy.
- Может работать и с PostgreSQL и с csv файлом.
- Достаточная быстрая, если читать файл через read_csv
Минусы:
- Для работы с csv файлом нужно переписывать sql запросы под функции библиотеки.
**SQLAlchemy**
Плюсы:
- Благодаря creat_engine можно подключаться к PostgreSQL, создавать там базы данных с нуля или из csv файлов
Минусы:
- Сложновато понять, как писать запросы, но есть лазейка для ленивых(меня) в виде text(q).
- По скорости не сильно проигрывает SQLite.
  














  
