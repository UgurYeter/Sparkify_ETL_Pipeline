import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    # song_id, title, artist_id, year, duration
    # open song file
    print('started!')
    df = pd.read_json(filepath, orient='records', lines=True)

    for i, row in df.iterrows():
        # insert song record
        song_data = (row['song_id'], row['title'], row['artist_id'],
                     row['year'], row['duration'])
        cur.execute(song_table_insert, song_data)
        # insert artist record
        artist_data = (row['artist_id'], row['artist_name'], row['artist_location'],
                   row['artist_latitude'], row['artist_longitude'])
        cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df[df['page'] == 'NextSong']
    data_to_load = []
    for i in range(len(df.values)):
        # convert timestamp column to datetime
        t = pd.to_datetime(df.values[i][15], unit='ms')
        seconds_series = pd.Series(t)
        # insert time data records
        time_data = [seconds_series[0], seconds_series.dt.hour[0], seconds_series.dt.day[0],
                     seconds_series.dt.week[0], seconds_series.dt.month[0], seconds_series.dt.year[0],
                     seconds_series.dt.weekday[0]]
        # insert time data records
        data_to_load.append(time_data)

    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    time_df = pd.DataFrame(data=data_to_load, columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # insert user records
    for i, row in df.iterrows():
        user_id = str(row['userId'])
        if user_id != "":
            cur.execute(user_select, [user_id])
            user_exists = cur.fetchall()
            # persist only if user does not exist!
            if len(user_exists) == 0:
                user_data = (user_id, row['firstName'], row['lastName'], row['gender'], row['level'])
                cur.execute(user_table_insert, user_data)

    # insert songplay records
    for index, row in df.iterrows():
        song_variables = (row.song, row.artist, row.length)
        # get songid and artistid from song and artist tables
        cur.execute(song_select, song_variables)
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
        # insert songplay record
        songplay_data = (row.sessionId, row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()