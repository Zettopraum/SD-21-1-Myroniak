import sqlite3

# Підключення до бази даних (або створення нової)

def create_table():
    with sqlite3.connect('article.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')

# Вставка запису
def insert_article(title, text):
    with sqlite3.connect('article.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO articles (title, content) VALUES (?, ?)', (title, text))
        connection.commit()

# Вибірка запису
def get_article(article_id=None):
    with sqlite3.connect('article.db') as connection:
        cursor = connection.cursor()
        if article_id is None:
            cursor.execute('SELECT * FROM articles')
        else:
            cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
        return cursor.fetchall()

# Видалення запису
def delete_article(article_id):
    with sqlite3.connect('article.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM articles WHERE id = ?', (article_id,))
        connection.commit()

# Закриття підключення
def enter():
    create_table()
    while True:
        print('Команда:' '\n' 'add - додати' '\n' 'watch - переглянути' '\n' 'remove - видалит' '\n' 'exit - вийти')
        comands = input('Ведіть команду: ')
        if comands == "add":
            title = input('Ведіть заголовок статті: ')
            text = input('Веддіть текст статті: ')
            insert_article(title, text)
            print('Стаття додана')
            
        elif comands == "watch":
            article = get_article()
            if article:
                print('Всі статті')
                for article in article:
                    print(article)
            else: 
                print('Немає статті')
        elif comands == 'remove':
            article_id = int(input())
            delete_article(article_id)
            print('Статтю видалено')                    
        elif comands == 'exit':
                break
        else:
                print('Ведіть правильну команду: ')
            
enter()