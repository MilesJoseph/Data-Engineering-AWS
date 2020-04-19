import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Load data from S3 into staging tables
    """
    print('Insert data from S3 to staging table')
    for query in copy_table_queries:
        print('Running ' + query)
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Select data from staging for counts
    """
    print('Insert data to counts table from staging')
    for query in insert_table_queries:
        print('Running ' + query)
        cur.execute(query)
        conn.commit()


def main():
    """
    Extracting song from log for use in both tables
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
