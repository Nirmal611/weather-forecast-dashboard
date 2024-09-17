import requests

api_key = 'fd3e75819924aacc7af4bc398df85432'
def get_data(place , day=None , data=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={api_key}'
    temp =[]
    date =[]
    response = requests.get(url)
    data = response.json()
    data = data['list']
    first_date = int(data[0]['dt_txt'].split(' ')[0].split('-')[2])
    last_date = first_date + day
    for i in data:
        loop_date = int(i['dt_txt'].split(' ')[0].split('-')[2])
        if loop_date <= last_date :
            temp.append(i['main']['temp'])
            date.append(i['dt_txt'])
        else :
            break
    return temp, date

if __name__ == '__main__':
    get_data('tokyo')