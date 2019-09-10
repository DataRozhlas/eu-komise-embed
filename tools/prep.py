#%%
import pandas as pd
import json

#%%
d = pd.read_excel('./data/ekomise.xlsx')
d.fillna('', inplace=True)

#%%
d['name'] = d.apply(lambda row: row['jm'] + ' ' + row['pri'], axis=1)

#%%
d.desc = d.desc.apply(lambda x: x.replace('\xa0', ' '))

#%%
out = list(d[['name', 'nat', 'fce', 'desc']].to_dict(orient='index').values())

#%%
with open('./data/data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(out, ensure_ascii=False))

#%%
out

#%%
