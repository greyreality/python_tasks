def create(child, parent):
    dic = {}
    if child != 'global':
        dic['parent'] = parent
        dic['namespace'] = child
        dic['value'] = []
        return dic
    else:
        return None


def add(namespace, value):
    for i in spaces:
        if i['namespace'] == namespace:
            i['value'].append(value)

def get(namespace, value):
    o = 0
    for i in spaces:
      #  print(o,'-',i['namespace'])
        o+=1
        if i['namespace'] == namespace:
          #  print(value in i.get('value'))
            if value in i.get('value'):
              #  print('return ',i.get('namespace'))
                return str(i.get('namespace'))
            elif i['parent'] != 'None':
                    return get(i['parent'], value)
    return None

count = input()
i = 0
spaces = []
get_array = []
global_dic = {}
global_dic['namespace'] = 'global'
global_dic['parent'] = 'None'
global_dic['value'] = []
spaces.append(global_dic)

while i < int(count):
    cmd, namesp, arg = input().split()
    if cmd == 'add':
        add(namesp, arg)
        #print('added',spaces)
    elif cmd == 'create':
        result = create(namesp, arg)
        if result != None:
            spaces.append(result)
       # print('created', spaces)
    elif cmd == 'get':
        got = get(namesp, arg)
        get_array.append(got)
        # print('got=',got)
        # print('array=', get_array)
    i += 1
else:
    for k in range(0,len(get_array)):
        print(str(get_array[k]))

