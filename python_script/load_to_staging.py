import mysql.connector
import mysql.connector.errorcode as errcode
import csv
import logging

csv_file='D:\VSCode\DataWarehouse\csvfile\preprocessed_data.csv'

# logging config
logging.basicConfig(level=logging.INFO, filename='log_file.log', format='%(asctime)s - %(levelname)s - %(message)s')

def staging(csv_file):
    try:
        conn = mysql.connector.connect(host='localhost', user='nhannguyen', password='admin', database='staging', autocommit=True)
        print("Connection is established")
    except mysql.connector.Error as err:
        if err.errno == errcode.ER_ACCESS_DENIED_ERROR:
            print('Something was wrong with the username or password!')
        elif err.errno == errcode.ER_BAD_DB_ERROR:
            print("Database does not exist!")
        else:
            print(err)
    else:
        cur = conn.cursor()
        print('loading...')
        
        with open(csv_file, 'r', encoding='utf-8') as csvfile:
            csv_data=csv.reader(csvfile)
            for row in csv_data:
                cur.callproc('load_data' , row)

        cur.close()
        conn.close()
        print('Done.')

staging(csv_file)