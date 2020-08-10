# DROP TABLES

songplay_table_drop = "drop TABLE IF EXISTS songplays"
user_table_drop = "drop TABLE IF EXISTS users"
song_table_drop = "drop TABLE IF EXISTS songs"
artist_table_drop = "drop TABLE IF EXISTS artists"
time_table_drop = "drop TABLE IF EXISTS times"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(songplay_id varchar PRIMARY KEY, start_time varchar, user_id varchar NOT NULL, level varchar NOT NULL, song_id varchar, artist_id varchar, session_id int NOT NULL, location varchar, user_agent varchar);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id varchar PRIMARY KEY, first_name varchar NOT NULL, last_name varchar NOT NULL, gender varchar NOT NULL, level varchar NOT NULL)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar NOT NULL, artist_id varchar NOT NULL, year int, duration decimal NOT NULL)
""")

artist_table_create = ("""

CREATE TABLE IF NOT EXISTS artists( artist_id varchar PRIMARY KEY, name varchar NOT NULL, location varchar, latitude decimal, longitude decimal)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS times (start_time timestamp PRIMARY KEY, hour int, day int NOT NULL, week int NOT NULL, month int NOT NULL, year int NOT NULL, weekday int NOT NULL)
""")

# # INSERT RECORDS

songplay_table_insert = ("""

insert into songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
values(%s, %s, %s,%s,%s,%s, %s, %s,%s) ON CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert = ("""
insert into users (user_id, first_name, last_name, gender, level) values (%s, %s, %s,%s,%s) ON CONFLICT (user_id) DO NOTHING

""")

song_table_insert = ("""
insert into songs(song_id, title, artist_id, year, duration) values (%s, %s, %s,%s,%s) ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
insert into artists (artist_id, name, location, latitude, longitude) values (%s, %s, %s,%s,%s) ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
insert into times (start_time, hour, day, week, month, year, weekday) values  (%s, %s, %s,%s, %s, %s,%s) ON CONFLICT (start_time) DO NOTHING
""")

# # FIND SONGS

song_select = ("""

select s.song_id, a.artist_id from songs s, artists a where a.name = %s and s.title = %s and s.duration = %s and
a.artist_id = s.artist_id
""")

user_select = ("""
SELECT * FROM users WHERE user_id = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]