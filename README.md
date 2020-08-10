# ETL project for Sparkify
Sparkify provides a musing streaming platform for their users, and there are log files of this service which displays users' activity details. Users' activity details show when a user logs in to the system and which songs and artists are preferred.

 ## Goals
- To provide a structured storage of existing log files which allows to query activities of users and information about users themselves and songs.
- Enriching log data while structuring by using song data on [Million Song Dataset](http://millionsongdataset.com/)
- Using the song and log datasets, creating a star schema optimized for queries on song play analysis.

## Project Structure
As ETL processes consist of extract, transform and load steps, as an example of ETL process this project consists of 3 main steps.Before starting with extract process, since the goal of the project extracting data in log and song files into Postgres database, Postgres database and tables must be in place. To prepare the local project setup one can run `docker-compose up` command to run a local Postgres container which defined in the `docker-compose.yml`.
Assuming the database is ready to accept connections from the application, next step would be the run `python3 ./create_tables.py` command to create tables which the application will load data into. `create_tables.py` file has the necessary code to create drop tables if they exist and recreate them, be careful with this command if you do not want to lose existing data and tables.
The have the ETL pipeline up and running, one should run  `python3 ./etl.py` command which will start the application's data pipeline which reads data from files under `./data/song_data` and `./data/log_data` folders and triggers related functions in the `etl.py` file.



## Data Model
Data model will include 5 tables, all tables named with plural words.
`songplays` table is the fact table and `users`, `songs`, `artist`, `times` are the dimension tables.

![Data Model](./docs/DataModelv1.png)
