DATA WAREHOUSE PROJECT

Sparkify is a music streaming startup that collects data in S3. The purpose of this project will be to create a standardized redshift database via a redshift cluster.


The project steps are;

1. Create a database schema
2. Create the sql statements based on the schemas (sql_queries).
3. Finish the logic in create_tables.py We can run this when we want to drop    tables in case we need to restart in the future.
4. Create a redshift cluster. Once this is done you will need to add IAM role and database to the dwh.cfg.
5. Run the create_tables.py. once a redshift cluster has been created.
6. Finish the logic in etl.py to load data from s3 to staging tables. Run this script to load files into tables.
7. Create a script to ensure that the process is working correctly (counts.py)


SCHEMA

STAGING TABLES
--staging_events
--staging_songs

FACT TABLE
--songplays-this table record the events for the song play record. We filter records with the NextSong. The columns in this table are;

songplay_id,
start_time,
user_id, ##
level,
song_id,
artist_id,
session_id,
location, user_agent

DIMENSION TABLES

users - lists the unique uses in the app

user_id,
first_name,
last_name,
gender,
level

songs - lists the unique songs in our database

song_id,
title,
artist_id,
year,
duration

artists - lists the unique artists in the databases

artist_id,
name,
location,
lattitude,
longitude

time - timestap or records in songplay

start_time,
hour,
day,
week,
month,
year,
weekday
