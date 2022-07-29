from pathlib import Path

from requests import Session


# constants for use in any def or class statements below
oceandata = 'https://oceandata.sci.gsfc.nasa.gov/ob/getfile/'
cmr = 'https://cmr.earthdata.nasa.gov/search/granules.json'
aqua_modis_oc = 'C1442922848-OB_DAAC'
query = {
   'appkey': '28093ae92eeef85c583d305040ff9ef4aeddc381',
}


def query_cmr(polygon, temporal):
   '''Query the EarthData CMR for Aqua-MODIS granules within the
   given spatial (as a polygon) and temporal bounds.'''

   with Session() as session:
      response = session.get(
         url=cmr,
         params={
            'collectionConceptId': aqua_modis_oc,
            'polygon': polygon,
            'temporal': temporal,
            'page-size': 1000,
         },
      )
   assets = [
      i['producer_granule_id'] for i in response.json()['feed']['entry']
   ]
   return assets


def get_oceandata(asset, parent):
   '''Download an asset from the OB.DAAC'''

   # early return if asset exists at path
   path = parent/asset
   if path.exists():
      return

   # retrieve the content of a data file (asset) from the api
   with Session() as session:
       response = session.get(
           url=oceandata+asset,
           params=query,
           )

   # write binary response to file under parent directory
   path.parent.mkdir(parents=True, exist_ok=True)
   with path.open('wb') as stream:
       stream.write(response.content)


if __name__ == '__main__':

   # spatial and temporal bounds for MODIS data search
   sable_island = (
      '-70,60,'
      '-70,40,'
      '-50,40,'
      '-50,60,'
      '-70,60'
   )
   late_april_2016 = '2016-04-12T00:00:00Z/P20D'

   # create a list of NetCDF files within the given bounds
   assets = query_cmr(sable_island, late_april_2016)

   # download each asset into a local directory
   parent = Path('data')
   for item in assets:
      get_oceandata(item, parent)
