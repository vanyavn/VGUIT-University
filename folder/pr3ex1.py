import json
with open('data.json', 'rb') as infile: data = json.load(infile)
data_list = data['events_data']
a = 0
p = []
for i in range(len(data_list)):
    x = data_list[i]
    if x['action'] != '':
        a += 1
        p.append(x['client_id'])
s = set(p)
print(s)
print('\n\n\nКоличество клиентов (client_id), которые совершали какие-либо действия: ', len(s))