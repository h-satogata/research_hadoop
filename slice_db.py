import sqlite3

conn_1 = sqlite3.connect('hadoop_hash_tag_date.db')
cursor_1 = conn_1.cursor()
conn_2 = sqlite3.connect('hadoop.db')
cursor_2 = conn_2.cursor()

def slice_db():
    timestamp_target = ""
    # 行数を獲得する
    try:
        cursor_1.execute("SELECT COUNT(tag) FROM hadoop_hash_tag_date")
        column_num_tuple = cursor_1.fetchone()
        column_num = column_num_tuple[0]

    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])

    # 1つ目のリリース以前のものにフラグをつける
    try:
        cursor_1.execute("SELECT author_date_unix_timestamp FROM hadoop_hash_tag_date WHERE id = '%d'", 1)
        timestamp_target_tuple = cursor_1.fetchone()
        timestamp_target = timestamp_target_tuple[0]
        cursor_2.execute("UPDATE data SET author_date_flag = '1' WHERE author_date_unix_timestamp < '%s'"
                         , timestamp_target)

    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])


    # dbをリリースごとにフラグをつける。author_date_unix_timestampを用いる
    for loop_num in range(0, column_num):
        try:
            cursor_1.execute("SELECT author_date_unix_timestamp FROM hadoop_hash_tag_date WHERE id = '%d'", loop_num+1)
            timestamp_target_tuple = cursor_1.fetchone()
            timestamp_target = timestamp_target_tuple[0]
            cursor_2.execute("UPDATE data SET author_date_flag = '%d' WHERE author_date_unix_timestamp < '%s'"
                             , loop_num+1, timestamp_target)

        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])



slice_db()

conn_1.commit()
conn_2.commit()

# 接続を閉じる
conn_1.close()
conn_2.close()
