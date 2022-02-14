import sqlite3 as sq
import datetime


class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True


loged = False


def get_timestamps(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))


def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()


def home(user):
    print("Login, Register")
    a = input("What would you like to do: ")
    if(a == "register" or a == "Register"):
        register()
    elif(a == "Login" or a == "login"):
        return login(user)
    else:
        print("Choose a valid option")
        home('')


def register():
    n = input("Name: ")
    u1 = input("Username: ")
    p = input("Password: ")
    u = User(n, u1, p)
    print("Welcome, " + u.name)
    with sq.connect("saper.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            name TEXT PRIMARY KEY NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
            )""")
        cur.execute("""
            INSERT INTO users(name, username, password)  VALUES (?,?,?);
        """, (n, u1, p))

    home(u)


def login(user):
    lu = input("Username: ")
    l2 = input("Password")
    with sq.connect("saper.db") as con:
        cur = con.cursor()
        pas = cur.execute('SELECT password FROM users WHERE name=?', (lu, )).fetchone()
        for value in pas:
            if(l2 == value):
                loged = True
                print("Welcome, " + lu)
                return costs()
            else:
                print("Incorrect username or password")
                login(user)


def costs():
    with sq.connect("saper.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS costs1 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            food REAL,
            clothing REAL,
            transportation REAL,
            paymant_date INTEGER
            )""")
        print('hello')
        print('select and enter an expense category or see your expenses ')
        inp = input('1)food\n, 2)clothing\n, 3)transportation\n or 4)expenses '
                    '')
        if(inp == 'food'):
            inf = input('enter how much was spent')
            ints = input('select date 1)today or enter 2)another date, to enter your date year-month-day ')
            if (ints == 'today'):
                cur.execute("""
                        INSERT INTO costs1(food, paymant_date)  VALUES (?,?);
                                    """, (inf, datetime.date.today()))
                con.commit()
            elif (ints == 'another date'):
                inte = input('enter your date year-month-day ')
                cur.execute("""
                        INSERT INTO costs1(food, paymant_date)  VALUES (?,?);
                                    """, (inf, inte))
                con.commit()
        elif (inp == 'clothing'):
            inc = input('enter how much was spent')
            ints = input('select date 1)today or enter 2)another date, to enter your date year-month-day ')
            if (ints == 'today'):
                cur.execute("""
                            INSERT INTO costs1(clothing, paymant_date)  VALUES (?,?);
                                    """, (inc, ints))
                con.commit()
            elif (ints == 'another date'):
                inte = input('enter your date year-month-day ')
                cur.execute("""
                            INSERT INTO costs1(clothing, paymant_date)  VALUES (?,?);
                                    """, (inc, inte))
                con.commit()
        elif (inp == 'transportation'):
            intr = input('enter how much was spent')
            ints = input('select date 1)today or enter 2)another date, to enter your date year-month-day ')
            if (ints == 'today'):
                cur.execute("""
                            INSERT INTO costs1(transportation, paymant_date)  VALUES (?,?);
                                    """, (intr, datetime.date.today()))
                con.commit()
            elif (ints == 'another date'):
                inte = input('enter your date year-month-day ')
                cur.execute("""
                            INSERT INTO costs1(transportation, paymant_date)  VALUES (?,?);
                                    """, (intr, inte))
                con.commit()
        elif (inp == 'expenses'):
            intv = input('view all expenses or by category\n '
                         'enter categories or 1)allexpenses\n '
                         'or to delete all data enter 2)delete\n '
                         'View spending statistics: , per year, per month, per day.\n '
                         'to do this, enter 3)statisticsemd\n ')
            if (intv == 'allexpenses'):
                cur.execute(""" SELECT * FROM costs1 """)
                rows = cur.fetchall()
                for q in rows:
                    print(q)
                print('#, food, clothing, transportation')
            elif (intv == 'statisticsemd'):
                intc = input('choose which statistics you want to see\n '
                      '1) for the year. enter year\n '
                      '2) per month. enter month\n '
                      '3) per day. enter day\n ')
                if (intc == 'year'):
                    inte = input('enter year')
                    res = cur.execute(""" SELECT * FROM costs1 """).fetchall()
                    for item in res:
                        it4 = item[4]
                        it42 = it4[:4]
                        if (it42 == inte):
                            print(item)

                    print('#, food, clothing, transportation')
                elif (intc == 'month'):
                    intm = input('enter month')
                    res = cur.execute(""" SELECT * FROM costs1 """).fetchall()
                    for item in res:
                        it4 = item[4]
                        it42 = it4[5:7]
                        if (it42 == intm):
                            print(item)
                    print('#, food, clothing, transportation')
                elif (intc == 'day'):
                    intd = input('enter day')
                    res = cur.execute(""" SELECT * FROM costs1 """).fetchall()
                    for item in res:
                        it4 = item[4]
                        it42 = it4[-2:]
                        if (it42 == intd):
                            print(item)
                    print('#, food, clothing, transportation')
            #datetime.strptime(date_string, format) - преобразует строку в datetime (так же, как и функция strptime из модуля time).
            elif (intv == 'categories'):
                intc = input("enter the category you want to view 1)food,\n 2)clothing,\n 3)transportation  ")
                if (intc == 'food'):
                    cur.execute(""" SELECT food FROM costs1 WHERE food=food""")
                    rows = cur.fetchall()
                    for q in rows:
                        print('food', q)
                    print('---- cash')
                elif (intc == 'clothing'):
                    cur.execute(""" SELECT clothing FROM costs1 WHERE clothing=clothing""")
                    rows = cur.fetchall()
                    for q in rows:
                        print('clothing', q)
                    print('---- cash')
                elif (intc == 'transportation'):
                    cur.execute(""" SELECT transportation FROM costs1 WHERE transportation=transportation""")
                    rows = cur.fetchall()
                    for q in rows:
                        print('transportation', q)
                    print('---- cash')
                else:
                    print('what you entered is wrong')
            elif(intv == 'delete'):
                cur.execute(""" DELETE FROM costs1 """)
                cur.execute(""" DELETE FROM users """)
                print('We have deleted', cur.rowcount, 'records from the table.')
                con.commit()
            else:
                print('what you entered is wrong')
        else:
            print("Choose a valid option")
            costs()
        costs()

# if loged == False:



if __name__ == '__main__':
    home('')
