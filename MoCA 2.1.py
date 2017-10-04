#modules
import sqlite3
import csv
import datetime
import tkinter

#db connection
conn = sqlite3.connect('MoCA.db')
c = conn.cursor()

#create tables
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS Movies(
                    name TEXT,
                    director TEXT,
                    producer TEXT,
                    writer TEXT,
                    top_billed TEXT,
                    music TEXT,
                    cinematography TEXT,
                    editor TEXT,
                    release_date TEXT,
                    run_time REAL,
                    budget REAL,
                    box_office REAL,
                    mpaa_rating TEXT,
                    animated TEXT,
                    family_friendly TEXT)""")
    conn.commit()


def csv_data_entry():
    file_name = input("What is your file's name?")
    with open(file_name, 'r') as f:
        dr = csv.DictReader(f)
        to_table = [(i['name'], i['director'],
                     i['producer'],
                     i['writer'],
                     i['top_billed'],
                     i['music'],
                     i['cinematography'],
                     i['editor'],
                     i['release_date'],
                     i['run_time'],
                     i['budget'],
                     i['box_office'],
                     i['mpaa_rating'],
                     i['animated'],
                     i['family_friendly'])for i in dr]
        c.executemany("""INSERT INTO Movies IF NOT EXISTS(name, director, producer, writer,
                        top_billed, music, cinematography, editor, release_date, 
                        run_time, budget, box_office, mpaa_rating, animated, family_friendly ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""", to_table)


def manual_data_entry():
    print('Please input the following pieces of information:')
    name = input('What is the name of your movie?')
    director = input("Who is your movie's director?")
    producer = input("Who is your movie's producer?")
    writer = input("Who is your movie's writer?")
    top_billed = input("Who is your movie's top billed actor/actress?")
    music = input("Who did your movie's music?")
    cinematography = input("Who is your movie's cinematographer?")
    editor = input("Who is your movie's editor?")
    release_date = input("When was your movie released? (Format is DD-MM-YYYY)")
    run_time = input("How long, in minutes, is your movie?")
    budget = input("What was your movie's budget?")
    box_office = input("What was your movie's box office income?")
    mpaa_rating = input("What is your movies MPAA Rating?(G, PG, PG-13, R, NC-17")
    animated = input("Is your movie animated? (Y/N)")
    family_friendly = input("Is your movie family friendly? (G or PG rating)")
    c.execute("""INSERT INTO Movies(name, director, producer, writer,
                        top_billed, music, cinematography, editor, release_date, 
                        run_time, budget, box_office, mpaa_rating, animated, family_friendly) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""",
                        (name, director, producer, writer,
                        top_billed, music, cinematography, editor, release_date,
                        run_time, budget, box_office, mpaa_rating, animated, family_friendly))

create_table()
#csv_data_entry()
manual_data_entry()
conn.commit()
conn.close()