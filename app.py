"""
Реализуйте следующее Web приложение на фреймворке Flask
1) создайте базу данных на движке SQLite при помощи Python, состоящей из одной таблицы
и заполните ее вашими данными (не менее 10 строк),
Таблицу можете выбрать любой тематики, например какие подарки необходимо купить
родным / коллегам на Новый Год. Указать ФИО, название подарка, стоимость и статус
(куплен / не куплен)
Проверьте наличие данных в вашей таблице написав SQL запрос через Python
SELECT * FROM ваша_таблица
2) возьмите файл базы данных созданной в задании 1) и выведите содержимое таблицы в
HTML форме, используя Flask фреймворк и вызов GET запроса через браузер

"""
# для работы используется БД из итоговой аттестации artist_listen_likes.db

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    conn = sqlite3.connect('artist_listen_likes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM artist_listen_likes")
    data = cur.fetchall()
    conn.close()
    return render_template('artist.html', data=data)

#запуск переменной app
if __name__ == '__main__':
  app.run(debug=True)








