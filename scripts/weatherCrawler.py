import requests as r
from bs4 import BeautifulSoup

for year in range(2017, 2018):

    csvFile = open(str(year) + '.csv', 'a')

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0:
        months[1] = 29

    for i, month in enumerate(months):

        for day in range(1,month+1):
            print(day, i+1, year)
            request = r.get('https://www.wunderground.com/history/airport/BIRK/' + str(year) + '/' + str(i+1) + '/' + str(day) + '/DailyHistory.html?req_city=Reykjavik&req_state=&req_statename=Iceland&reqdb.zip=&reqdb.magic=&reqdb.wmo=')
            soup = BeautifulSoup(request.content, 'html.parser')

            meanTemp    = ''
            maxTemp     = ''
            minTemp     = ''
            avgHumid    = ''
            perci       = ''
            seaLevPre   = ''
            windSpeed   = ''
            maxWindSpeed= ''
            visibility  = ''

            if soup.find(text='Mean Temperature'):
                textItem = soup.find(text='Mean Temperature').parent
                meanTemp = textItem.parent.findNext('span', {'class': 'wx-value'}).text

            if soup.find(text='Max Temperature'):
                textItem = soup.find(text='Max Temperature').parent
                maxTemp = textItem.parent.findNext('span', {'class': 'wx-value'}).text

            if soup.find(text='Min Temperature'):
                textItem = soup.find(text='Min Temperature').parent
                minTemp = textItem.parent.findNext('span', {'class': 'wx-value'}).text

            if soup.find(text='Average Humidity'):
                textItem = soup.find(text='Average Humidity').parent
                avgHumid = textItem.parent.findNext('td').text

            if soup.find(text='Precipitation'):
                textItem = soup.find(text='Precipitation').parent
                perci = textItem.parent.findNext('span', {'class': 'wx-value'}).text

            if soup.find(text='Sea Level Pressure'):
                textItem = soup.find(text='Sea Level Pressure').parent
                seaLevPre = textItem.parent.findNext('span', {'class': 'wx-value'}).text

            if soup.find(text='Wind Speed'):
                textItem = soup.find(text='Wind Speed').parent
                windSpeed = textItem.parent.findNext('span', {'class': 'wx-value'}).text

            if soup.find(text='Max Wind Speed'):
                textItem = soup.find(text='Max Wind Speed').parent
                maxWindSpeed = textItem.parent.findNext('span', {'class': 'wx-value'}).text

            if soup.find(text='Visibility'):
                textItem = soup.find(text='Visibility').parent
                visibility = textItem.parent.findNext('span', {'class': 'wx-value'}).text

            csvFile.write(str(day) + '/' + str(i+1) +  '/' + str(year) + ',' + meanTemp + ',' + maxTemp + ',' + minTemp + ',' + avgHumid + ',' + perci + ',' + seaLevPre + ',' + windSpeed + ',' + maxWindSpeed + ',' + visibility + '\n')


    csvFile.close()
