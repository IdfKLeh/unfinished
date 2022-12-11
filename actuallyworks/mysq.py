# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:24:12 2022

@author: rimmy
"""


import sqlite3

def read_data(filename):
    data = []
    with open(filename,'r') as f:
        for line in f.readlines():
            values = [str(item) for item in line.split(',')]
            data.append(values)
    return data

def add_blog(title,genre,link):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("INSERT INTO blog (title, genre, link) VALUES (?, ?, ?)",(title,genre,link))
    conn.commit()
    conn.close()

def remove_blog(c, _id):
    c.execute("DELETE FROM blog WHERE id=?", (_id,))
    
def get_blog_list():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM blog")
    result = c.fetchall()
    conn.close()
    return result

if __name__ == '__main__':
    data = read_data('temp.txt')
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()  # 커서 생성
    c.execute("CREATE TABLE IF NOT EXISTS blog (id integer PRIMARY KEY, title text, genre text, link text)")
    for row in data:
        add_blog(row[1],row[2],row[3])

    c.execute('SELECT * FROM blog')
    all = c.fetchall()
    print(all)
    c.execute("DELETE FROM blog")
    conn.commit()
    conn.close()
