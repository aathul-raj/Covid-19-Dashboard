from main import covid
from os import system, name
from time import sleep
import datetime

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')
current_time = datetime.datetime.now()

def checkStats():
    if caseCheck > cases:
        caseCurve = "DOWN"
        return caseCurve
    
    else:
        caseCurve = "UP"
        return caseCurve


run = covid()
run.load()

cases = run.get("cases")
caseCheck = cases
sick = run.get("sick")
recovered = run.get("recovered")
deaths = run.get("deaths")
totalTests = run.get("totalTests")
positive = run.get("positive")
negative = run.get("negative")

print(f"PROGRAM STARTED AT: {current_time.month}/{current_time.day}/{current_time.year} at {current_time.hour}:{current_time.minute}")
print(f"Total US Cases: {cases}")
print(f"Total Currently Hospitalized: {sick}")
print(f"Total Recovered: {recovered}")
print(f"Total Deaths: {deaths}")
print(f"Total Tests: {totalTests}")
print(f"Total Tested Positive: {positive}")
print(f"Total Tested Negative: {negative}")

while True:
    if str(current_time.minute)[1] == '5':
        run.load()

        caseCheck = cases
        cases = run.get("cases")
        sick = run.get("sick")
        recovered = run.get("recovered")
        deaths = run.get("deaths")
        totalTests = run.get("totalTests")
        positive = run.get("positive")
        negative = run.get("negative")

    elif str(current_time.minute)[1] == '0':
        run.load()

        caseCheck = cases
        cases = run.get("cases")
        sick = run.get("sick")
        recovered = run.get("recovered")
        deaths = run.get("deaths")
        totalTests = run.get("totalTests")
        positive = run.get("positive")
        negative = run.get("negative")

    if caseCheck != cases:
        print("UPDATING . . . . .")
        sleep(2)
        clear()
        print(f"LAST UPDATED: {current_time.month}/{current_time.day}/{current_time.year} at {current_time.hour}:{current_time.minute}")
        print(f"Total US Cases: {cases}")
        print(f"  - {checkStats()} from {caseCheck}")
        print(f"Total Currently Hospitalized: {sick}")
        print(f"Total Recovered: {recovered}")
        print(f"Total Deaths: {deaths}")
        print(f"Total Tests: {totalTests}")
        print(f"Total Tested Positive: {positive}")
        print(f"Total Tested Negative: {negative}")