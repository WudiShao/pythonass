import csv

##PART A
h = input("Please enter your filename: ").strip('\'')

def select_day():
    #h is the file name and m is the specific month
    rainfall = {}
    count = 0
    with open(h) as f:
        f_csv = csv.reader(f)
        header = next(f_csv)
        for row in f_csv:
            count = count +1
            if row[-3] is '':
                continue
            if row[-3] is not '':
                rainfall[int(row[2]),int(row[3]),int(row[4])] = (float(row[-3]),row[-2])
            #create rainfall dict
    return rainfall

def delete_month():
    rainfall = select_day()
    e = 0
    #e will represent the start date of a observation period
    K = []
    #K will represent the month should be delete
    delete_month = []
    for key in rainfall:
        value = rainfall[key]
        if value[1] is '' and '1':
            continue
        else:
            e = key[2] - int(value[1])
            if e >= 0:
                continue
            elif key[1] != 1:
                K = [(key[0],key[1]),(key[0],key[1]-1)]
            else:
                K = [(key[0],key[1]),(key[0],12)]
            delete_month = delete_month.__add__(K)
            #put all the month that should be delete into a list
    return delete_month

def delete_year():
    rainfall = select_day()
    e = 0
    K = []
    delete_year = []
    for key in rainfall:
        value = rainfall[key]
        if value[1] is '' and '1':
            continue
        else:
            e = key[2] - int(value[1])
            if e >= 0:
                continue
            elif key[1] != 1:
                continue
            else:
                K = [key[0],key[0]-1]
                #if the time period is through January and December,we need to
                #delete two year data
            delete_year = delete_year.__add__(K)
    return delete_year

def monthly_rainfall():
    month_rainfall = {}
    sum = 0
    m = 0
    dm = delete_month()
    rainfall = select_day()
    for key in rainfall:
        value = rainfall[key]
        if (key[0],key[1]) in dm:
            continue
        #if the month should be delete,the rainfall of that month should not be count
        elif (key[0],key[1]) in month_rainfall:
                sum = round(sum + value[0],2)
                month_rainfall[(key[0],key[1])] = sum
        else:
            sum = 0
            sum = round(sum + value[0],2)
            month_rainfall[(key[0],key[1])] = sum
        #print(month_rainfall)
    return month_rainfall

def specific_month_rainfall():
    m = int(input('specific month = '))
    month_specific_rainfall = {}
    month_rainfall = monthly_rainfall()
    for key in month_rainfall:
        #calculate the sum of the specific month
        if key[1] == m:
            if (key[0],m) in month_specific_rainfall:
                value = month_rainfall[key]
                sum = round(sum + value,2)
                month_specific_rainfall[(key[0],m)]=sum
            else:
                sum = 0
                value = month_rainfall[key]
                sum = round(sum + value,2)
                month_specific_rainfall[(key[0],m)] = sum
        else:
            continue
    return (month_specific_rainfall,m)

def year_rainfall():
    year_rainfall={}
    sum = 0
    rainfall = select_day()
    dy = delete_year()
    for key in rainfall:
        value = rainfall[key]
        if key[0] in dy:
            continue
        if key[0] in year_rainfall:
            sum = round(sum + value[0],2)
            year_rainfall[key[0]] = sum
        else:
            sum = 0
            sum = round(sum + value[0],2)
            year_rainfall[key[0]] = sum
    return year_rainfall

def select_single_day():
    rainfall = select_day()
    single_day = {}
    for key in rainfall:
        value = rainfall[key]
        if value[-1] is not '1':
            continue
        else:
            single_day[key] = value[0]
    #print(len(single_day))
    return single_day

##PART B
def start_year():
    sy = int(input('Start year:'))
    return sy

def end_year():
    ey = int(input('End year:'))
    return ey

def start_month():
    sm = int(input('Start month:'))
    return sm

def end_month():
    em = int(input('End month:'))
    return em

def start_day():
    sy = start_year()
    sm = start_month()
    sd = int(input('Start day:'))
    return (sy,sm,sd)

def end_day():
    ey = end_year()
    em = end_month()
    ed = int(input('End day:'))
    return (ey,em,ed)


#the time period in all methods
def order_k():
    #time kinds
    need = input('which function do you want? \n     A:Aggregating observations \n     F:find threshold values and dates\nplease input A or F:')
    if need == 'A':
        fun = input('which aggregation do you want?\n     m: total for each month\n     sp: total for a specific month of the year\n     y:total for each year\nplease input m or sp or y:')
        if fun == 'm':
            s = monthly_rainfall()
            print (s)
        elif fun == 'sp':
            s = specific_month_rainfall()
            print (s)
        elif fun == 'y':
            s = year_rainfall()
            print (s)
        else:
            order_k()
    if need == 'F':
        tk=input('Which data kinds your want check?\n     Y:Year\n     M:Month \n     D:Day\nplease input Y or M or D : ')
        max_min = input('which value you want to find: max value(max) or min value(min)? \nplease input max or min:')
        while max_min == 'max':
            while tk=='Y'or tk=='M'or tk=='D':
                if tk == 'Y':
                    b = method_year_max()
                    return b
                elif tk == 'M':
                    b = method_month_max()
                    return b
                elif tk == 'D':
                    b = method_day_max()
                    return b
            else:
                order_k()
        while max_min == 'min':
            while tk=='Y'or tk=='M'or tk=='D':
                if tk == 'Y':
                    #method_a_month_min()
                    b = method_year_min()
                    return b
                elif tk == 'M':
                    b = method_month_min()
                    return b
                elif tk == 'D':
                    #method_a_day_min()
                    b = method_day_min()
                    return b
            else:
                order_k()

#the time friquency in all methods
def f_time():
    #frequency kinds
    fk=input("Please select a frequency kind \n      Y:year, M:month or D:day\nplease input Y or M or D: ")
    if fk == 'Y':
        y = int(input('year(s): '))
        return y
    elif fk == 'M':
        m = int(input('month(s): '))
        return m
    elif fk == 'D':
        d = int(input('day(s): '))
        return d
    else:print("error")

def transfer_list_y():
    a = year_rainfall()
    s = start_year()
    e = end_year()
    sp = ep = 0
    less_e = []
    greater_s = []
    date_list = list(a.keys())
    rain_list = list(a.values())
    if s in date_list:
        sp == date_list.index(s)
    else:
        for i in date_list:
            if i <s:
                continue
            else:
                greater_s = greater_s.__add__([i])
        sp = date_list.index(greater_s[0])
    if e in date_list:
        ep = date_list.index(e)
    else:
        for i in date_list:
            if i<e:
                less_e = less_e.__add__([i])
            else:
                continue
        ep = date_list.index(less_e[-1])
    rl = rain_list[sp:ep]
    return rl

def transfer_list_m():
    tin=input("please input A:all month or S:specific month: ")
    if tin == 'A':
        monthly_rainfall()
        a = monthly_rainfall()
        s = start_year()
        e = end_year()
        ms = start_month()
        me = end_month()
    elif tin == 'S':
        (a,ms) = specific_month_rainfall()
        me=ms
        s = start_year()
        e = end_year()
    else:
        print("error")
    date_list = list(a.keys())
    rain_list = list(a.values())
    less_e = []
    greater_s = []
    sp = ep = 0
    if (s,ms) in date_list:
         sp == date_list.index((s,ms))
    else:
         for i in date_list:
             if i[0]<= s and i[1]<=ms:
                 continue
             elif i[0]==s and i[1]==ms:
                 greater_s = greater_s.__add__([i])
             elif i[0]==s and i[1]>ms:
                 greater_s = greater_s.__add__([i])
             elif i[0]>s:
                 greater_s = greater_s.__add__([i])
         sp = date_list.index(greater_s[0])
    if (e,me) in date_list:
        ep = date_list.index((e,me))
    else:
        for i in date_list:
            if i[0]<e:
                less_e = less_e.__add__([i])
            elif i[0] == e and i[1] < me:
                less_e = less_e.__add__([i])
            elif i[0] == e and i[1] == me:
                less_e = less_e.__add__([i])
        ep = date_list.index(less_e[-1])
   #sp = date_list.index((s,ms))
   #ep = date_list.index((e,es))
    rl = rain_list[sp:ep]
    return (rl,a)

def transfer_list_d():
    a = select_single_day()
    s = start_day()
    e = end_day()
    sp = ep = 0
    less_e = []
    greater_s = []
    date_list = list(a.keys())
    rain_list = list(a.values())
    if s in date_list:
        sp == date_list.index(s)
    else:
        for i in date_list:
            if i[0]<= s[0] and i[1]<=s[1] and i[2]<=s[2]:
                continue
            elif i[0]==s[0] and i[1]==s[1] and i[2]>s[2]:
                greater_s = greater_s.__add__([i])
            elif i[0]==s[0] and i[1]>s[1]:
                greater_s = greater_s.__add__([i])
            elif i[0]>s[0]:
                greater_s = greater_s.__add__([i])
        sp = date_list.index(greater_s[0])
    if e in date_list:
        ep = date_list.index(e)
    else:
        for i in date_list:
            if i[0]<e[0]:
                less_e = less_e.__add__([i])
            elif i[0] == e[0] and i[1] < e[1]:
                less_e = less_e.__add__([i])
            elif i[0] == e[0] and i[1] == e[1] and i[2]<e[2]:
                less_e = less_e.__add__([i])
        ep = date_list.index(less_e[-1])
    rl = rain_list[sp:ep]
    return rl

def method_month_max():
    a=transfer_list_m()
    a0=a[0]
    a1=a[1]
    ft=f_time()
    d = {v: k for k, v in a1.items()}
    for i in range(len(a1)):
        if i-ft>=0:
            if i+ft<=len(a1):
                b=a0[i]
                j=a0[(i-(ft-1)):(i-1)]
                k=a0[(i+1):(i+ft-1)]
                jm=j.sort()
                km=k.sort()
                while b>j[-1] and b>k[-1]:
                    print('method a:rainfall:', b, 'date:', d[b])
                    break
   #int n
    n = N = 0
    D = []
    dn=int(len(a0)/ft)
    b=a0.sort()
    bmax=a0[-dn]
    bmax_above = a0[-dn:]
    while n<len(bmax_above):
        N = bmax_above[n]
        X = [d[N]]
        D = D.__add__(X)
        n = n+1
    dic_output = dict(zip(D,bmax_above))
   #print(bmax)
   #c=specific_month_rainfall()
    print('method b:max rainfall:',bmax,'date:',d[bmax],';','date equal or exceed:',dic_output)

def method_month_min():
    a=transfer_list_m()
    a0=a[0]
    a1=a[1]
    ft=f_time()
    d = {v: k for k, v in a1.items()}
    for i in range(len(a1)):
        if i-ft>=0:
            if i+ft<=len(a1):
                b=a0[i]
                j=a0[(i-(ft-1)):(i-1)]
                k=a0[(i+1):(i+ft-1)]
                jm=j.sort()
                km=k.sort()
                while b<j[0] and b<k[0]:
                    print('method a:rainfall:', b, 'date:', d[b])
                    break
    n = N = 0
    D = []
    dn=int(len(a0)/ft)
    b=a0.sort()
    bmin=a0[dn-1]
    bmin_less = a0[:dn]
    while n<len(bmin_less):
        N = bmin_less[n]
        X = [d[N]]
        D = D.__add__(X)
        n = n+1
    dic_output = dict(zip(D,bmin_less))
   #print(bmax)
   #c=specific_month_rainfall()
    print('method b:min rainfall:',bmin,'date:',d[bmin],';','date equal or exceed:',dic_output)

def method_day_max():
    a = transfer_list_d()
    ft = f_time()
    c=select_single_day()
    d=dict(zip(c.values(),c.keys()))
    for i in range(len(a)):
       if i - ft >= 0:
           if i + ft <= len(a):
               b = a[i]
               j = a[(i - (ft - 1)):(i - 1)]
               k = a[(i + 1):(i + ft - 1)]
               jm = j.sort()
               km = k.sort()
               while b > j[-1] and b > k[-1]:
                   print('method a:rainfall:', b, 'date:', d[b])
                   break
    list=a
    n = N = 0
    D = []
    #int n
    dn=int(len(list)/ft)
    b=list.sort()
    bmax=list[-dn]
    bmax_above = list[-dn:]
    #print(bmax)
    while n<len(bmax_above):
        N = bmax_above[n]
        X = [d[N]]
        D = D.__add__(X)
        n = n+1
    dic_output = dict(zip(D,bmax_above))
    print('method b:max rainfall:',bmax,'date:',d[bmax],';','date equal or exceed:',dic_output)

def method_day_min():
    a = transfer_list_d()
    ft = f_time()
    c=select_single_day()
    d=dict(zip(c.values(),c.keys()))
    for i in range(len(a)):
       if i - ft >= 0:
           if i + ft <= len(a):
               b = a[i]
               j = a[(i - (ft - 1)):(i - 1)]
               k = a[(i + 1):(i + ft - 1)]
               jm = j.sort()
               km = k.sort()
               while b < j[0] and b < k[0]:
                   print('method a:rainfall:', b, 'date:', d[b])
                   break
    list=a
    #int n
    dn=int(len(list)/ft)
    b=list.sort()
    bmin=list[dn-1]
    n = 0
    D = []
    #print(bmax)
    bmin_less = list[:dn]
    while n<len(bmin_less):
        N = bmin_less[n]
        X = [d[N]]
        D = D.__add__(X)
        n = n+1
    dic_output = dict(zip(D,bmin_less))
    print('method b:min rainfall:',bmin,'date:',d[bmin],';','date equal or exceed:',dic_output)

def method_year_max():
    a=transfer_list_y()
    ft=f_time()
    c = year_rainfall()
    d = dict(zip(c.values(), c.keys()))
    for i in range(len(a)):
       if i-ft>=0:
           if i+ft<=len(a):
               b=a[i]
               j=a[(i-(ft-1)):(i-1)]
               k=a[(i+1):(i+ft-1)]
               jm=j.sort()
               km=k.sort()
               while b>j[-1] and b>k[-1]:
                   print('method a:rainfall:', b, 'date:', d[b])
                   break
    list=a
    #int n
    dn=int(len(list)/ft)
    b=list.sort()
    bmax=list[-dn]
    n = 0
    D = []
    bmax_above = list[-dn:]
    while n<len(bmax_above):
        N = bmax_above[n]
        X = [d[N]]
        D = D.__add__(X)
        n = n+1
    dic_output = dict(zip(D,bmax_above))
    print('method b:max rainfall:',bmax,'date:',d[bmax],';','date equal or exceed:',dic_output)

def method_year_min():
    a=transfer_list_y()
    ft=f_time()
    c = year_rainfall()
    d = dict(zip(c.values(), c.keys()))
    for i in range(len(a)):
       if i-ft>=0:
           if i+ft<=len(a):
               b=a[i]
               j=a[(i-(ft-1)):(i-1)]
               k=a[(i+1):(i+ft-1)]
               jm=j.sort()
               km=k.sort()
               while b<j[0] and b<k[0]:
                   print('method a:rainfall:', b, 'date:', d[b])
                   break
    list=a
    #int n
    dn=int(len(list)/ft)
    b=list.sort()
    bmin=list[dn-1]
    n = 0
    D = []
    #print(bmax)
    bmin_less = list[:dn]
    while n<len(bmin_less):
        N = bmin_less[n]
        X = [d[N]]
        D = D.__add__(X)
        n = n+1
    dic_output = dict(zip(D,bmin_less))
    print('method b:min rainfall:',bmin,'date:',d[bmin],';','date equal or exceed:',dic_output)
