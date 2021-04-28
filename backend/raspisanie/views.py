from django.shortcuts import render
import psycopg2

# Create your views here.
TEMP = []


def index(request):
    global TEMP
    headers_f = ['Факультет']
    headers_k = ['Курс']
    f = request.GET.get("f")
    k = request.GET.get("k")
    conn = psycopg2.connect(dbname='ghettodb', user='ghettopg',
                            password='penEg1342', host='localhost')
    cur = conn.cursor()
    cur.execute("SELECT id, faculty FROM facultys")
    faculty = cur.fetchall()
    cur.execute("SELECT id, full_name FROM teachers;")
    prepod = cur.fetchall()
    cur.execute("SELECT * FROM audiences;")
    aud = cur.fetchall()
    course = list()
    if f is not None:
        if f == '1' or f == '2' or f == '6':
            cur.execute("SELECT id, course FROM courses")
            course = cur.fetchall()
        else:
            cur.execute("SELECT id, course FROM courses\
                        LIMIT 4")
            course = cur.fetchall()
        headers_f.append(faculty[int(f) - 1])
        data = {
            'faculty': faculty,
            'course': course,
            'headers_f': headers_f,
            'temp': TEMP,
        }
        if k is None:
            TEMP.append(f)
            return render(request, "courses.html", context=data)

    if k is not None:
        TEMP.append(k)
        headers_k.append(course[int(k) - 1])
        cur.execute("SELECT GP.id, GP.group_\
                    FROM courses AS CR\
                    JOIN groups_ AS GP\
                    ON GP.course = CR.id\
                    JOIN facultys AS FC\
                    ON FC.id = GP.faculty\
                    WHERE CR.id = {} AND FC.id = {}".format(k, f))
        group_ = cur.fetchall()
        data = {
            'faculty': faculty,
            'course': course,
            'group_': group_,
            'headers_k': headers_k,
            'headers_f': headers_f,
            'temp': TEMP,
        }
        return render(request, "groups.html", context=data)
    data = {
        'faculty': faculty,
        'prepod': prepod,
        'aud': aud,
    }
    return render(request, "selector.html", context=data)


def shedule(request):
    TEMP.clear()
    g = request.GET.get("g")
    weeks = list()
    conn = psycopg2.connect(dbname='ghettodb', user='ghettopg',
                            password='penEg1342', host='localhost')
    cur = conn.cursor()
    for week in range(1, 3):
        days = list()
        for i in range(1, 7):
            cur.execute("SELECT D.day,DS.subject, PR.time_str,\
                TC.full_name, AD.name, TP.type,\
                POS.position, WE.parity, GP.group_\
                FROM shedule AS RP\
                JOIN days AS D \
                ON D.id = RP.day\
                JOIN subjects AS DS\
                ON DS.id = RP.subject AND\
                D.id = {}\
                JOIN classes as PR\
                ON PR.id = RP.class\
                JOIN teachers AS TC\
                ON TC.id = RP.teacher\
                JOIN positions_of_teacher AS POS\
                ON POS.id = TC.position\
                JOIN audiences AS AD\
                ON AD.id = RP.audience\
                JOIN type_of_classes AS TP\
                ON TP.id = RP.type_of_class\
                JOIN weeks as WE\
                ON WE.id = RP.week\
                JOIN groups_ as GP\
                ON GP.id = RP.group_\
                WHERE RP.group_ = {} AND RP.week = {}\
                ORDER BY start_time".format(i, g, week))
            day = cur.fetchall()
            try:
                days.append(day)
            except Exception as e:
                print(e)
                continue
        weeks.append(days)
    return render(request, "index.html", context={'weeks': weeks})


def prepod(request):
    p = request.GET.get("p")
    conn = psycopg2.connect(dbname='ghettodb', user='ghettopg',
                            password='penEg1342', host='localhost')
    cur = conn.cursor()
    weeks = list()
    for week in range(1, 3):
        days = list()
        for i in range(1, 7):
            cur.execute("SELECT D.day,DS.subject, PR.time_str, TC.full_name, AD.name, TP.type, POS.position, WE.parity\
                        FROM shedule AS RP\
                        JOIN days AS D \
                        ON D.id = RP.day\
                        JOIN subjects AS DS\
                        ON DS.id = RP.subject AND\
                        D.id = {}\
                        JOIN classes as PR\
                        ON PR.id = RP.class\
                        JOIN teachers AS TC\
                        ON TC.id = RP.teacher\
                        JOIN positions_of_teacher AS POS\
                        ON POS.id = TC.position\
                        JOIN audiences AS AD\
                        ON AD.id = RP.audience\
                        JOIN type_of_classes AS TP\
                        ON TP.id = RP.type_of_class\
                        JOIN weeks as WE\
                        ON WE.id = RP.week\
                        WHERE TC.id = {} AND RP.week = {}\
                        ORDER BY start_time".format(i, p, week))
            day = cur.fetchall()
            try:
                days.append(day)
            except Exception as e:
                print(e)
                continue
        weeks.append(days)
    return render(request, "index.html", context={'weeks': weeks})


def audience(request):
    a = request.GET.get("a")
    conn = psycopg2.connect(dbname='ghettodb', user='ghettopg',
                            password='penEg1342', host='localhost')
    cur = conn.cursor()
    weeks = list()
    for week in range(1, 3):
        days = list()
        for i in range(1, 7):
            cur.execute("SELECT D.day, DS.subject, PR.time_str, TC.full_name,\
                         AD.name, TP.type, POS.position, WE.parity, GR.group_\
                        FROM shedule AS RP\
                        JOIN days AS D\
                        ON D.id = RP.day\
                        JOIN subjects AS DS\
                        ON DS.id = RP.subject AND\
                        D.id = {}\
                        JOIN classes as PR\
                        ON PR.id = RP.class\
                        JOIN teachers AS TC\
                        ON TC.id = RP.teacher\
                        JOIN positions_of_teacher AS POS\
                        ON POS.id = TC.position\
                        JOIN audiences AS AD\
                        ON AD.id = RP.audience\
                        JOIN type_of_classes AS TP\
                        ON TP.id = RP.type_of_class\
                        JOIN weeks as WE\
                        ON WE.id = RP.week\
                        JOIN groups_ as GR\
                        ON GR.id = RP.group_\
                        WHERE AD.id = {} AND RP.week = {}\
                        ORDER BY start_time".format(i, a, week))
            day = cur.fetchall()
            try:
                days.append(day)
            except Exception as e:
                print(e)
                continue
        weeks.append(days)
    return render(request, "index.html", context={'weeks': weeks})
