import os
import psycopg2 
import db

def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

def select_all_books():
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'SELECT ISBN, title, auther, publisher from book'
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return rows 

def insert_book(ISBN , title , auther , publisher):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'INSERT INTO book VALUES (default,%s,%s,%s,%s)'
    
    cursor.execute(sql,(ISBN,title,auther,publisher))
    
    connection.commit()
    cursor.close()
    connection.close() 
    
def delete_book(isbn):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'DELETE FROM book WHERE isbn = %s'

  cursor.execute(sql, (isbn,))

  connection.commit()

  cursor.close()
  connection.close()
  
def update_book(title,auther,publisher, isbn):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'UPDATE book SET title = %s, auther = %s, publisher = %s WHERE isbn = %s'

  cursor.execute(sql, (title,auther,publisher, isbn))

  connection.commit()

  cursor.close()
  connection.close()

def search_book(keyword):
  connection = get_connection()
  cursor = connection.cursor()
  sql = 'SELECT * FROM book WHERE title LIKE %s'
  
  pattern=f"%{keyword}%"
  
  cursor.execute(sql, (pattern,))
  
  rows = cursor.fetchall()

  cursor.close()
  connection.close()
  return rows