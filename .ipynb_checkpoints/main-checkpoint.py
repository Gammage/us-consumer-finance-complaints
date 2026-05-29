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
    # print(schema)

# inspect some of the data
    preview = pd.read_sql("SELECT * FROM consumer_complaints LIMIT 5", conn)
    # print(preview)

# what are the tags of this data
    issue = pd.read_sql("SELECT issue FROM consumer_complaints", conn)
    print(issue)

# top complained about products 
    comp_prod = pd.read_sql("SELECT product", conn)
    print(comp_prod)
# complaints per state 
# worst response rate by compnany bar chart 
# monthly complaint trend 
# dispute rate by submission channel 

    conn.close()

if __name__ == "__main__":
    main()


