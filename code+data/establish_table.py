import sqlite3
import csv

def csv_to_db(csv_file, db_file):
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    #建立table => PredictionEmployee
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PredictionEmployee (
            yyyy INTEGER,
            PerNo INTEGER,
            最新離職預測 INTEGER,
            sex INTEGER,
            工作分類 INTEGER,
            職等 INTEGER,
            廠區代碼 INTEGER,
            管理層級 INTEGER,
            工作資歷1 INTEGER,
            工作資歷2 INTEGER,
            工作資歷3 INTEGER,
            工作資歷4 INTEGER,
            工作資歷5 INTEGER,
            專案時數 INTEGER,
            專案總數 INTEGER,
            當前專案角色 INTEGER,
            特殊專案佔比 INTEGER,
            工作地點 INTEGER,
            訓練時數A INTEGER,
            訓練時數B INTEGER,
            訓練時數C INTEGER,
            生產總額 INTEGER,
            榮譽數 INTEGER,
            是否升遷 INTEGER,
            升遷速度 INTEGER,
            近三月請假數A INTEGER,
            近一年請假數A INTEGER,
            近三月請假數B INTEGER,
            近一年請假數B INTEGER,
            出差數A INTEGER,
            出差數B INTEGER,
            出差集中度 INTEGER,
            年度績效等級A INTEGER,
            年度績效等級B INTEGER,
            年度績效等級C INTEGER,
            年齡層級 INTEGER,
            婚姻狀況 INTEGER,
            年資層級A INTEGER,
            年資層級B INTEGER,
            年資層級C INTEGER,
            任職前工作平均年數 INTEGER,
            最高學歷 INTEGER,
            畢業學校類別  INTEGER,
            畢業科系類別 INTEGER,
            眷屬量 INTEGER,
            通勤成本 INTEGER,
            歸屬部門 INTEGER
        )
    ''')
    conn.commit()

    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 

        # 將每一行插入到資料庫表中
        for row in csv_reader:
            cursor.execute('''
            INSERT INTO PredictionEmployee (
            yyyy, PerNo, 最新離職預測, sex, 工作分類, 
            職等, 廠區代碼, 管理層級, 工作資歷1, 工作資歷2,
            工作資歷3, 工作資歷4, 工作資歷5, 專案時數,
            專案總數, 當前專案角色, 特殊專案佔比,
            工作地點, 訓練時數A, 訓練時數B, 訓練時數C,
            生產總額, 榮譽數, 是否升遷, 升遷速度,
            近三月請假數A, 近一年請假數A, 近三月請假數B,
            近一年請假數B, 出差數A, 出差數B, 出差集中度,
            年度績效等級A, 年度績效等級B, 年度績效等級C,
            年齡層級, 婚姻狀況, 年資層級A, 年資層級B,
            年資層級C, 任職前工作平均年數, 最高學歷,
            畢業學校類別, 畢業科系類別, 眷屬量,
            通勤成本, 歸屬部門
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
          row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21],
          row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32],
          row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41], row[42], row[43],
          row[44], row[45], row[46]))
    
    conn.commit()
    conn.close()


csv_file = 'file/test.csv'
db_file = 'employee_management.db'
csv_to_db(csv_file, db_file)
