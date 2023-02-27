'''Quick and easy search for a film to get it's rating.'''

import requests

key = '4847874d'

def search(title):
    try:
        r = requests.get(url=f'http://www.omdbapi.com/?apikey={key}&t={title}')
        data = r.json()
        for i in data['Ratings']:
            source = i['Source']
            rating = i['Value']
            print(f'{source} gave {title} this rating: {rating} \n')

    except:
        print('Error: Film not found.')

while True:
    usr_input = input('Enter which film are you interested in, or enter "q" to quit.')
    if usr_input.lower() != 'q':
        search(usr_input)
    else:
        break
