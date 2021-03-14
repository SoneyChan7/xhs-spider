import pymysql.cursors
import pymysql
# from pymysql import err


db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    db = 'xhs',
    cursorclass=pymysql.cursors.DictCursor
)

def insert_notes_id(note_id,uid, kw):
    with db.cursor() as cursor:
        sql = 'INSERT INTO `notes_id_tab`(`note_id`, `uid`, `kw`) VALUES (%s, %s, %s)'
        try:
            cursor.execute(sql,(note_id, uid, kw))
            db.commit()
        except:
            db.rollback()

def get_note_id():
    with db.cursor() as cursor:
        sql = 'SELECT `note_id` ,`kw` FROM `notes_id_tab`'
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except:
            db.rollback()

def insert_notes_info(note_id, content, uid, likes, share, star, comment, kw):
    with db.cursor() as cursor:
        sql = 'INSERT INTO `notes_info_tab`(`id`, `content`, `uid`, `likes`, `share`, `star`,`comment`,`kw`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            cursor.execute(sql, (note_id, content, uid, likes, share, star, comment, kw))
            db.commit()
        except:
            db.rollback()
