import sqlite3 as lite
import sys

con = lite.connect('C:/Users/batsh/Documents/IS 211/week12database.db')

with con:

    cur = con.cursor()

    # cur.execute(""" DROP TABLE songs;""")
    cur.execute(""" CREATE TABLE users (
                                          user_id integer PRIMARY KEY,
                                            name_authorized text NOT NULL
                                    
                                        ); """
                )

    cur.execute(""" CREATE TABLE students (
                                             student_id integer PRIMARY KEY,
                                               name text NOT NULL

                                           ); """
                )

    cur.execute(""" CREATE TABLE quizzes (
                                                 quiz_id integer PRIMARY KEY,
                                                   quiz_name text NOT NULL

                                               ); """
                )

    cur.execute(""" CREATE TABLE scores (
                                                    score_id integer PRIMARY KEY,
                                                      score integer NOT NULL,
                                                      student_id integer,
                                                      quiz_id integer,
                                                      user_id integer

                                                  ); """
                )


