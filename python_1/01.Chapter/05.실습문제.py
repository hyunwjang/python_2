a = ['apple','watch', 'apolo','star', 'abocado']

# for i in a:
#     if a.startswith('a'):
#         print(i)
c = []
for i in a:
    if i.startswith('a'):
        c.append(i)
        
print(c)

b = [i for i in a if i.startswith('a')]
print(b)