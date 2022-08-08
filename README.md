# python-bricklink-api
Wrapper for the Bricklink API (v3)

See also
[BrickLink API Documentation (v3)](https://www.bricklink.com/v3/api.page)

## Install

``` bash
cd python-bricklink-api
python ./setup.py install
```

## Usage

### create API connection

``` python
import yaml
api_data = yaml.safe_load(open('bricklink_api_private.yml', 'r'))

from bricklink import api
bricklink_api = api.BrickLinkAPI(
  api_data['consumer_key'], api_data['consumer_secret'],
  api_data['token_value'], api_data['token_secret'])
```

### Get Info on a Set

``` python
set_id = '75313-1'
status, headers, response = bricklink_api.get('items/set/'+set_id)
print(response['data'])
```
#### Result

``` python
{'no': '75313-1', 'name': 'AT-AT - UCS', 'type': 'SET', 'category_id': 65,
'image_url': '//img.bricklink.com/SL/75313-1.jpg', 'thumbnail_url': '//img.bricklink.com/S/75313-1.jpg',
'weight': '10708.00', 'dim_x': '49.70', 'dim_y': '49.70', 'dim_z': '37.40', 'year_released': 2021, 'is_obsolete': False}
```

### Get Price Details on a Set

``` python
set_id = '75313-1'
#prices of sold used sets in the USA using USD (us dollars)
status, headers, response = bricklink_api.get('items/set/'+set_id+'/price?new_or_used=U&currency_code=USD&guide_type=sold&country_code=US')
for sale in response['data']['price_detail']:
   print('${0:.2f}'.format(float(sale['unit_price'])))
```
#### Result

```
$629.99
$558.00
$600.00
```

### Get List of Parts in a Set

``` python
set_id = '75313-1'
status, headers, response = bricklink_api.get('items/set/'+set_id+'/subsets')
print('There are {num_parts} unique parts in set ID {set_id}'.format(
  num_parts=len(response['data']), set_id=set_id))
```

#### Result

```
There are 670 unique parts in set ID 75313-1
```

### Get List of Minifigs in a Set

``` python
#show minifigs
set_id = '75313-1'
status, headers, response = bricklink_api.get('items/set/'+set_id+'/subsets')
#response['data'][0]['entries'][0]['item']['type']
items = 0
minifigs = 0
for part in response['data']:
  for entry in part['entries']:
   item = entry['item']
   if item['type'] == 'MINIFIG':
      minifigs += entry['quantity']
      print('{0}. {1}'.format(minifigs, item['name']))
   else:
      items += entry['quantity']

print('There are {num_parts} pieces and {minifigs} minifigs in set ID {set_id}'.format(
  num_parts=items, minifigs=minifigs, set_id=set_id))
```

#### Result

```
1. AT-AT Driver - Dark Red Imperial Logo, Cheek Lines, Frown
2. Luke Skywalker &#40;Pilot, Printed Legs, Visor Up / Down, Askew Front Panel&#41;
3. General Maximillian Veers - Dual Molded Legs
4. AT-AT Driver - Dark Red Imperial Logo, Female
5. Snowtrooper Commander, Printed Legs, Dark Tan Hands
6. Snowtrooper, Printed Legs, Dark Tan Hands - Female, Light Nougat Head
7. Snowtrooper, Printed Legs, Dark Tan Hands, Scowl
8. Snowtrooper, Printed Legs, Dark Tan Hands - Female, Reddish Brown Head
9. Snowtrooper, Printed Legs, Dark Tan Hands, Cheek Lines, Lopsided Grin

There are 6826 pieces and 9 minifigs in set ID 75313-1
```

