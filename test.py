import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import pandas as pd
import etl as et

conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
cur = conn.cursor()


def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    return all_files




def main():
    song_files = get_files('data/log_data')
    #
    filepath = song_files[0]
    df = pd.read_json(filepath, orient='records',lines=True)

    # for i, row in df.iterrows():
    #   song_data = [row['song_id'], row['title'], row['artist_id'], row['year'], row['duration']]
    #   cur.execute(song_table_insert, song_data)

    # for i, row in df.iterrows():
    #   artist_data = [row['artist_id'], row['artist_name'], row['artist_location'], row['artist_latitude'], row['artist_longitude']]
    #   cur.execute(artist_table_insert, artist_data)


    # user_df = pd.read_json(filepath, orient='records',lines=True)
    # user_df[user_df['page'] == 'NextSong']
    # column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')
    # data_to_load = []
    # for i in range(len(df.values)):
    #     t = pd.to_datetime(df.values[i][15], unit='ms')
    #     seconds_series = pd.Series(t)
    #     time_data = [seconds_series[0], seconds_series.dt.hour[0], seconds_series.dt.day[0],
    #                        seconds_series.dt.week[0], seconds_series.dt.month[0], seconds_series.dt.year[0],
    #                        seconds_series.dt.weekday[0]]
    #     data_to_load.append( time_data)
    # print(data_to_load[0])
    # time_df = pd.DataFrame(data=data_to_load, columns=column_labels)
    # print(time_df.to_string())
    # for i, row in time_df.iterrows():
    #     print(cur.execute(time_table_insert, list(row)))

    # for i, row in user_df.iterrows():
    #   user_id = row['userId']
    #   if user_id != "":
    #     user_data = [user_id, row['firstName'], row['lastName'], row['gender'], row['level']]
    #     cur.execute(user_table_insert, user_data)

    et.process_log_file(cur,filepath)
    # cur.execute(song_select, ['Bitter End', 'Insatiable (Instrumental Version)', 266.39628])
    # print(cur.fetchall())

    # for index, row in df.iterrows():
    #     # get songid and artistid from song and artist tables
    #     #     print(row.song)
    #     #     print( row.artist )
    #     #     print( row.length)
    #     #     print( type(row.length))
    #     cur.execute(song_select, (row.song, row.artist, row.length))
    #     results = cur.fetchone()
    #     if results:
    #         songid, artistid = results
    #     else:
    #         songid, artistid = ('A', 'B')
    #
    #     print(songid)
    #     songplay_data = [row.sessionId, row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location,
    #                      row.userAgent]
    #     print(songplay_data)
    #     cur.execute(songplay_table_insert, songplay_data)
    #
    # conn.commit()
    # conn.close()


if __name__ == "__main__":
    main()