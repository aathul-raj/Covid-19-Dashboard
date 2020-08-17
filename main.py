import requests
from bs4 import BeautifulSoup
from csv import writer

class covid:

    def load(self):

        self.response = requests.get('https://covidtracking.com/data')
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

        self.info = self.soup.find_all('td')

        self.cases = self.info[0].get_text()

        self.sick = self.info[3].get_text()

        self.recovered = self.info[4].get_text()

        self.deaths = self.info[5].get_text()

        self.totalTests = self.info[6].get_text()

        self.negative = self.info[1].get_text()

        self.totalTestsTemp = self.totalTests.replace(',', '')
        self.negativeTemp = self.negative.replace(',', '')

        self.positive = int(self.totalTestsTemp) - int(self.negativeTemp)

        self.positive = str(format (self.positive, ',d'))

    '''BELOW - col should be a string, accepted parameters are: "cases", "sick", "recovered", 
    "deaths", "totalTests", "positive", "negative"'''

    def get(self, col):
        if  col == "cases":
            return(self.cases)

        elif col == "sick":
            return(self.sick)

        elif col == "recovered":
            return(self.recovered)

        elif col == "deaths":
            return(self.deaths)

        elif col == "totalTests":
            return(self.totalTests)

        elif col == "positive":
            return(self.positive)

        elif col == "negative":
            return(self.negative)

#TODO: USE THIS TO MAKE ACTUAL TRACKER THAT CHECKS EVERY 5 MINUTES