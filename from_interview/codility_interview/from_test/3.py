import operator
def tariff(h, m, s):
    all = s + m * 60 + h * 60 * 60
    if all < 5 * 60:
        return 3 * all
    else:
        if s != 0:
            return (m + 1) * 150
        else:
            return m * 150
def solution(s):
    # print(s)
    lines = s.splitlines()
    # print(lines)
    hours, minutes, secs = 0, 0, 0
    num = {}
    for i in lines:
        # print(i)
        hours = int(i[0:2])
        minutes = int(i[3:5])
        secs = int(i[6:8])
        number = str(i[9:20])
        if str(number) in num:
            # print('before=', num[number])
            temp = num[number] + tariff(hours, minutes, secs)
            num[number] = temp
            # print('after=',num[number])
        else:
            num[number] = tariff(hours, minutes, secs)
        # print(num)
        # print(number)
    # print('final=', num)
    # print('max val=',max(num.items(), key=operator.itemgetter(1))[0])
    del num[max(num.items(), key=operator.itemgetter(1))[0]]
    # print('final=', num)
    return sum(num.values())


test = '00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090\n00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090'
print('res=', solution(test))