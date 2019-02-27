import click
import requests
import json

@click.command()
@click.argument('city',nargs=1)
def weather(city):
    resp = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=9a06355669d434a7e3720d56c7139930" % format(city),
        params={'units':'metric'}
    )
    data =resp.json()
    message="City : {}\nTemprature : {}\nMax_Temorature : {}\nMin_Temorature : {}\nHumidity : {}".format(city+","+data['sys']['country'], data['main']['temp'], data['main']['temp_max'], data['main']['temp_min'], data['main']["humidity"])
    click.echo(message)

if __name__=="__main__":
    weather()