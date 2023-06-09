import pymysql.cursors
def add_AI_song(song_title, album_name):
    conn = pymysql.Connect(
        user="root",
        password="jyq123",
        port=3306,
        host="127.0.0.1",
        charset="utf8",
        db="jyq"

    )
    cursor=conn.cursor()
    sql = "select id from music_album where album_title = '" + album_name + "';"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    myresult = list(myresult)
    # print(type(myresult))
    # print(myresult)
    cursor.close()
    if len(myresult) == 0:
        return 0
    else:
        cursor=conn.cursor()
        album_id = str(myresult[0][0])
        sql = "INSERT into music_song(song_title, audio_file, is_favorite, album_id)values('" + song_title + "', './" + song_title + ".mp3', '0', '" + album_id + "');"
        # print(tmp)
        # # sql="INSERT into music_song(song_title, audio_file, is_favorite, album_id)values('AI2', './tes5.mp3', '0', '1')"
        cursor.execute(sql)
        conn.commit()
        return 1
        # print("finish")