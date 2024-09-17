import requests

api_key = 'fd3e75819924aacc7af4bc398df85432'
def get_data(place='tokyo' , day='1', api_key):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    data = data['list']
    data = data[0:8*int(day)]

    temp =[row['main']['temp'] for row in data]
    date = [row['dt_txt'] for row in data]
    cloud = [row['weather'][0]['main'] for row in data]

    return temp, date , cloud

if __name__ == '__main__':
    get_data()