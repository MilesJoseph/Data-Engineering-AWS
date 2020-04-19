import configparser
import psycopg2
from sql_queries import select_counts_queries


def get_results(cur, conn):
    """
    Get the counts in each table
    """
    for query in select_counts_queries:
        print('Running ' + query)
        cur.execute(query)
        results = cur.fetchone()

        for row in results:
            print("   ", row)


def main():
    """
    run this to determine if queries were correct and gather results
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    get_results(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
