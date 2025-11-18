import csv
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

purchases = {}
with open(os.path.join(base_dir, 'purchase_log.txt'), 'r', encoding='utf-8') as purchase_file:
    for line in purchase_file:
        purchase = json.loads(line.strip())
        user = purchase.get('user_id')
        category = purchase.get('category')
        if user and category:
            purchases[user] = category

with open(os.path.join(base_dir, 'visit_log__1_.csv'), 'r', encoding='utf-8') as visits_file, \
     open(os.path.join(base_dir, 'funnel.csv'), 'w', encoding='utf-8-sig', newline='') as funnel_file:  

    reader = csv.reader(visits_file)
    writer = csv.writer(funnel_file, delimiter=';')

    writer.writerow(['user_id', 'source', 'category'])
    next(reader)  

    for user_id, source in reader:
        if user_id in purchases:
            writer.writerow([user_id, source, purchases[user_id]])
