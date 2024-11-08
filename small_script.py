import json

with open('data\\points_position.json') as json_data:
    data = json.load(json_data)


for i in range(1,len(data) + 1):
    data[str(i)]['img'] = 'https://content.instructables.com/FA0/V1OC/LG3ZIIZQ/FA0V1OCLG3ZIIZQ.png?auto=webp&frame=1&width=320&md=MjAyMy0wNC0wNiAwMzo0MTowOS4w'
    data[str(i)]['text'] = f'zagadka{i}'
    data[str(i)]['ans'] = f'answer{i}'


with open('data\\balda.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)