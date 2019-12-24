import sqlite3

conn = sqlite3.connect('hadoop_hash_tag_date.db')
cursor = conn.cursor()

def slice_db():
    # 行数を獲得する
    try:
        cursor.execute("SELECT COUNT(tag) FROM hadoop_hash_tag_date")
        column_num_tuple = cursor.fetchone()
        column_num = column_num_tuple[0]

    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])


    # dbをリリースごとにスライスする。author_dateを用いる
    for loop_num in range(0, column_num):
        try:
            cursor.execute("DROP TABLE IF EXISTS hadoop_slice_%s", )
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS hadoop_hash_tag_date (hash TEXT, tag TEXT PRIMARY KEY, author_date TEXT)")

            key_list = sorted(list(hash_dict.keys()))
            #        print(len(hash_dict))
            #        print(len(set([hash_dict[key] for key in key_list])))
            data = [{'hash': hash_dict[key], 'tag': tag_dict[key], 'author_date': authordate_dict[key]} for key in
                    key_list]
            cursor.executemany("INSERT INTO hadoop_hash_tag_date VALUES (:hash, :tag, :author_date)",
                               data)

        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])



slice_db()