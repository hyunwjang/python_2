#none = "" 으로 변경

items = ['오메가3', None ,'비타민3','오메가3', None ,'비타민3']

#리스트 내포전
result = []

for item in items:
    if item != None:
        result.append(item)
    else:
        result.append("")

print(result)

#리스트 내포후
result = [i if i != None else '' for i in items]
print(result)