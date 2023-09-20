import json
with open('data.json', 'rb') as infile: data = json.load(infile)
data_list = data['events_data']
d = 0
for i in range(len(data_list)):
    x=data_list[i]
    if (x['action'] != '') and (x['client_id'] == 60459):
        print(x)
        d += 1
    else: d += 0
print('Колличество действий: ', d)