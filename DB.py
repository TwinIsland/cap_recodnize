import sqlite3


conn = sqlite3.connect('./DB.db')
c = conn.cursor()

def newDB():
    c.execute('''CREATE TABLE CAPLIB (
    ADDR TEXT NOT NULL UNIQUE ,
    WORD TEXT NOT NULL 
    )''')

    conn.commit()

def add_to_DB(addr,word):
    c.execute('''INSERT INTO CAPLIB(ADDR,WORD) VALUES (?,?)''',[addr,word])


def disp_DB():
    content = c.execute('''SELECT ADDR,WORD FROM CAPLIB''')
    count = 0

    for i in content:
        if count > 15:
            print('...')
            break

        print('ADDR: ' + i[0],end='    ')
        print('WORD: ' + i[1])
        count += 1

def reconstruct():
    try:
        c.execute('''DROP TABLE CAPLIB''')
    except Exception:
        print()
    conn.commit()
    newDB()


def save_change():
    conn.commit()

def getWord(addr):
    '''

    :param addr: ./train/1.jpg
    :return: word
    '''
    return list(c.execute('''SELECT WORD FROM CAPLIB WHERE ADDR=?''',[addr]))[0][0]


