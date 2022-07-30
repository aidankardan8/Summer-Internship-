from pathlib import Path

from requests import Session






# constants for use in any def or class statements below
resource = 'https://oceandata.sci.gsfc.nasa.gov/cgi/getfile/'
query = {
   'appkey': '28093ae92eeef85c583d305040ff9ef4aeddc381',
}
parent = Path('Level 3 Pull')

def get_oceandata(asset):

   # retrieve the content of a data file (asset) from the api
   with Session() as session:
       response = session.get(
           url=resource + asset,
           params=query,
           )

   # write retrieved content to local file under `parent`
   path = parent/asset
   path.parent.mkdir(parents=True, exist_ok=True)
   with path.open('wb') as stream:
       stream.write(response.content)


chlorophyll_data_daily=['A2016113.L3b_DAY_CHL.nc','A2016105.L3b_DAY_CHL.nc',
'A2016106.L3b_DAY_CHL.nc','A2016107.L3b_DAY_CHL.nc',
'A2016108.L3b_DAY_CHL.nc','A2016109.L3b_DAY_CHL.nc',
'A2016110.L3b_DAY_CHL.nc','A2016111.L3b_DAY_CHL.nc',
'A2016112.L3b_DAY_CHL.nc','A2016114.L3b_DAY_CHL.nc',
'A2016115.L3b_DAY_CHL.nc','A2016116.L3b_DAY_CHL.nc',
'A2016117.L3b_DAY_CHL.nc','A2016118.L3b_DAY_CHL.nc',
'A2016119.L3b_DAY_CHL.nc','A2016120.L3b_DAY_CHL.nc',
'A2016121.L3b_DAY_CHL.nc'
]

chlorophyll_data_8D=['A20161132016120.L3b_8D_CHL.nc',
'A20161052016112.L3b_8D_CHL.nc','A20161212016128.L3b_8D_CHL.nc']


# execute the loop
for item in chlorophyll_data_daily:
   (get_oceandata(item))

for item in chlorophyll_data_8D:
   (get_oceandata(item))
