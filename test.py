import pymysql

while(True):
    print("***********************")
    print("         관리          ")
    print("***********************")
    print("1. 입력")
    print("2. 출력")
    print("3. 종료")

    n = int(input())
    if(n == 1):
        print("이름입력: ")
        name = input()
        print("value 입력")
        value = input()
        print("data 입력")
        data = input()
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='1234', db='testdb', charset='utf8')
        arr = (name, value, data)
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO student (name, value, number) VALUES (%s, %s, %s)"
                cursor.execute(sql, arr)
                result = cursor.fetchall()
                for row in result:
                    print(row)

            conn.commit()
        finally:
            conn.close()

    elif(n == 2):
        conn = pymysql.connect(host='127.0.0.1', user='root',
                               password='1234', db='testdb', charset='utf8')
        try:
            with conn.cursor() as cursor:

                sql = "SELECT * FROM student"

                cursor.execute(sql)
                # 결과 가져오기
                result = cursor.fetchall()
                for row in result:
                    print(row)

            conn.commit()
        finally:
            conn.close()
    elif(n == 3):
        break
