
def setStartDate(d):
    if d['month'] < 12:
        d['day'] = 1
        d['month'] += 1
    elif d['month'] == 12:
        d['day'] = 1
        d['month'] = 1
        d['year'] += 1
    return d


def setEndDate(d):
    d['day'] = 1
    return d


def incrementDate(d):
    if d['month'] < 12:
        d['month'] += 1
    else:
        d['month'] = 1
        d['year'] += 1
    return d


def zellerCongruence(y, m, d):
    if m <= 2:
        m += 12
        y -= 1
    return (d + (13 * (m + 1)) // 5 + y + y // 4 - y // 100 + y // 400) % 7


def countingSundaysAll(i_d, f_d):
    if i_d['day'] != 1:
        i_d = setStartDate(i_d)
    if f_d['day'] != 1:
        f_d = setEndDate(f_d)
    counterSudays = 0
    while True:
        if (zellerCongruence(i_d['year'], i_d['month'], i_d['day']) == 1):
            counterSudays += 1
        i_d = incrementDate(i_d)
        if (f_d['year'] == i_d['year'] and f_d['month'] == i_d['month']):
            if (zellerCongruence(i_d['year'], i_d['month'], i_d['day']) == 1):
                counterSudays += 1
            break
    return counterSudays


T = int(input())

for _ in range(T):
    Y1, M1, D1 = list(map(int, input().split(' ')))
    initial_date = {'year': Y1, 'month': M1, 'day': D1}
    Y2, M2, D2 = list(map(int, input().split(' ')))
    final_date = {'year': Y2, 'month': M2, 'day': D2}
    result = countingSundaysAll(initial_date, final_date)
    print(result)
