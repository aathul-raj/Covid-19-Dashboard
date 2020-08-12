import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://covidtracking.com/data')

soup = BeautifulSoup(response.text, 'html.parser')


info = soup.find_all('td')

cases = info[0].get_text()

hospitalized = info[3].get_text()

recovered = info[4].get_text()

deaths = info[5].get_text()

totalTests = info[6].get_text()

negative = info[1].get_text()

totalTestsTemp = totalTests.replace(',', '')
negativeTemp = negative.replace(',', '')

positive = int(totalTestsTemp) - int(negativeTemp)

positive = str(format (positive, ',d'))

print(f"Total US cases: {cases}")

print(f"Patients currently hospitalized: {hospitalized}")

print(f"Total recovered: {recovered}")

print(f"Death count: {deaths}")

print(f"Total tested: {totalTests}")

print(f"Positive: {positive}")

print(f"Negative: {negative}")