import pandas as pd
import numpy
import matplotlib.pyplot as plt
import sqlite3

def main():

    conn = sqlite3.connect("./data/database.sqlite")

#list all tables (see what exists)
    tables = pd.read_sql("SELECT name from sqlite_master WHERE type='table'", conn)
    print(tables)

# pick a table name from step 1, then inspect columns
    schema = pd.read_sql("PRAGMA table_info(consumer_complaints)", conn)
    print(schema)

    conn.close()

if __name__ == "__main__":
    main()
