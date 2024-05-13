import sqlite3
from pathlib import Path
from contextlib import contextmanager
from nonebot import get_plugin_config
from  ..config import Config

plugin_config = get_plugin_config(Config)

KURO_DIR = plugin_config.KURO_DB_PATH
if isinstance(KURO_DIR, str):
    KURO_DIR = Path(KURO_DIR)
DATABASE = KURO_DIR / 'pns.db'

KURO_DIR.mkdir(parents=True, exist_ok=True)

class UserInfoManagement:
    _initialized = False
    def __init__(self):
        # 初始化数据库连接
        if not self._initialized:
            self.conn = sqlite3.connect(DATABASE)
            self._create_table_once()
            self._initialized = True
            print("数据库连接成功, 表已创建! ")
        else:
            self.conn = sqlite3.connect(DATABASE)
            print("数据库连接成功, 表已存在! ")

    @contextmanager
    def cursor(self):
        cur = self.conn.cursor()
        try:
            yield cur
        finally:
            cur.close()

    def close(self):
        self.conn.close()
        print("数据库关闭！")
    def _create_table_once(self):
        with self.cursor() as cur:
            cur.execute('''CREATE TABLE IF NOT EXISTS PNS_USER_INFO
                        (
                            bbs_id     INTEGER PRIMARY KEY,
                            qq_id      INTEGER,
                            pns_id     INTEGER,
                            mc_id      INTEGER,
                            user_token TEXT,
                            server_id  INTEGER
                        );''')
            self.conn.commit()
            return "success"
    def _get_data(self, qq_id):
        try:
            c = self.conn.cursor()
            sql = '''SELECT * FROM PNS_USER_INFO WHERE qq_id = ?'''
            c.execute(sql, (qq_id,))
            row = c.fetchone()
            return row
        except sqlite3.Error as e:
            raise e
        
    def _insert_data(self, user_id, data):
        bbs_id = data['userId']
        qq_id = user_id
        pns_id = data['pnsId']
        mc_id = data['mcId']
        user_token = data['token']
        server_id = data['serverId']
        try:
            c = self.conn.cursor()
            sql = '''INSERT INTO PNS_USER_INFO (bbs_id, qq_id, pns_id, mc_id, user_token, server_id) VALUES (?, ?, ?, ?, ?, ?)'''
            c.execute(sql, (bbs_id, qq_id, pns_id, mc_id, user_token, server_id))
            self.conn.commit()
            return "success"
        except Exception as e:
            raise e
        
    def _update_data(self, user_id, data):
        bbs_id = data['userId']
        qq_id = user_id
        pns_id = data['pnsId']
        mc_id = data['mcId']
        user_token = data['token']
        server_id = data['serverId']
        try:
            c = self.conn.cursor()
            params = (bbs_id, pns_id, mc_id, str(user_token), server_id, qq_id)
            sql = """UPDATE PNS_USER_INFO 
                    SET bbs_id = ?, pns_id = ?, mc_id = ?, 
                        user_token = ?, server_id = ? 
                    WHERE qq_id = ?"""

            c.execute(sql, params)
            self.conn.commit()
            return "success"
        except Exception as e:
            raise e
    
    def _getSpecificData(self, qq_id, field):
        try:
            c = self.conn.cursor()
            sql = '''SELECT {} FROM PNS_USER_INFO WHERE qq_id = ?'''.format(field)
            c.execute(sql, (qq_id,))
            row = c.fetchone()
            return row
        except Exception as e:
            raise e
        


            
