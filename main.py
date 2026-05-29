import pandas as pd
import numpy
import matplotlib.pyplot as plt
import plotly.express as px
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
    comp_prod = pd.read_sql(" SELECT product, COUNT(complaint_id) AS count FROM consumer_complaints GROUP BY product ORDER BY count ASC LIMIT 10", conn)
    comp_prod.set_index('product').plot(kind='barh')
    plt.xlabel('number of complaints')
    plt.show()
    print(comp_prod)

# complaints per state 
    comp_state = pd.read_sql(" SELECT state, COUNT(complaint_id) AS count FROM consumer_complaints GROUP BY state ORDER BY count", conn)
    px.choropleth(comp_state, locations="state", locationmode='USA-states', color="count", template='plotly_dark', color_continuous_scale='blues').update_layout(geo_scope='usa').show()
    print(comp_state)

# worst response rate by compnany bar chart 
    comp_response = pd.read_sql(""" SELECT company, total, timely, (timely * 100.0 / total) AS pct
    FROM (
        SELECT company,
            COUNT(*) AS total,
            SUM(CASE WHEN timely_response = 'Yes' THEN 1 ELSE 0 END) AS timely
        FROM consumer_complaints
        GROUP BY company
        HAVING total > 100
        )
        ORDER BY pct ASC
        LIMIT 10 """, conn)
    comp_response.set_index('company')['pct'].plot(kind='barh')
    plt.xlabel("Timely response rate %")
    plt.show()

    # having a total of more then 1000 complaints are with large comapnies, and they have a massively positive response rate of 90%, which makes sense given their ability to resolve issues
    # i therefore for interesting data stuck with more then 100. it shows how companies can deal with complaints that are much smaller, and so one unresolved complain can show more impact in their timely response rate.
# i have printed out the actual total amount of complaints, because we also have mobiloans with supposedly no responses to their complaints. could indiciate non compliance, data collection issue, or company no longer operating. 

# monthly complaint trend 
# dispute rate by submission channel 
    conn.close()

if __name__ == "__main__":
    main()


