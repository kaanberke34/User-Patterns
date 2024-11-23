
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import seaborn as sns
import numpy as np
import os
import datetime
import math

def performDailyAnalysis():
    selected_date = ""
    while True:
        try:
            selected_date = input("Enter the date (YYYY-MM-DD): ")
            selected_date = datetime.datetime.strptime(selected_date, '%Y-%m-%d')
            selected_date = selected_date.strftime('%Y-%m-%d')
            break
        except ValueError:
            os.system('cls')
            print("Invalid Date Format!")
            print("Please enter the date in the format YYYY-MM-DD.")
    
    filtered_data = activity_data[activity_data["Date"] == selected_date]
    
    if filtered_data.empty:
        print("No records found for the specified date!")
        performDailyAnalysis()
    else:
        total_screen_time = 0
        screen_time_in_hours = []
        for duration in filtered_data["Duration (h:m:s)"]:
            h, m, s = duration.split(':')
            screen_time_in_hours.append(((int(h) * 60 + int(m)) * 60 + float(s)) / 3600)
            total_screen_time += ((int(h) * 60 + int(m)) * 60 + float(s)) / 3600
        total_screen_time = math.ceil(total_screen_time)
        print("Total Screen Time: " + str(total_screen_time) + " hours")

        filtered_data["Hours Spent"] = pd.Series(screen_time_in_hours)

        with matplotlib.backends.backend_pdf.PdfPages("DailyAnalysis_" + str(selected_date) + ".pdf") as pdf:
            activity_summary = filtered_data.groupby(["Activity Label"])["Hours Spent"].sum()
            plt.figure(figsize=(20, 6))
            sns.barplot(y=activity_summary.index.values, x=activity_summary.values)
            plt.title("Time Spent on Various Activities")
            plt.ylabel("Activity Labels")
            plt.xlabel("Hours Spent")
            pdf.savefig()
            plt.close()

            website_summary = filtered_data[filtered_data["Web Browser"] == 1].groupby(["Website"])["Hours Spent"].sum()
            plt.figure(figsize=(20, 6))
            sns.barplot(y=website_summary.index.values, x=website_summary.values)
            plt.title("Time Spent on Various Websites")
            plt.ylabel("Website Names")
            plt.xlabel("Hours Spent")
            pdf.savefig()
            plt.close()

def performWeeklyAnalysis():
    pass

def performMonthlyAnalysis():
    pass

def performYearlyAnalysis():
    pass

def displayMenu():
    print("------------------MENU-------------------")
    print(":\t1. Daily Analysis\t\t:")
    print(":\t2. Weekly Analysis\t\t:")
    print(":\t3. Monthly Analysis\t\t:")
    print(":\t4. Yearly Analysis\t\t:")
    print(":\t5. Exit\t\t\t\t:")
    print("-----------------------------------------")
    return input("Choose an option: ")

def initiateAnalysis():
    user_choice = displayMenu()
    while user_choice not in ['1', '2', '3', '4', '5']:
        os.system('cls')
        print("Invalid option! Please try again.\n")
        user_choice = displayMenu()
    
    if user_choice == '1':
        performDailyAnalysis()
    elif user_choice == '2':
        performWeeklyAnalysis()
    elif user_choice == '3':
        performMonthlyAnalysis()
    elif user_choice == '4':
        performYearlyAnalysis()
    else:
        print("Exiting! Thank you.")
        return

if __name__ == "__main__":
    os.system('cls')
    if not os.path.exists('UserActivityLog.csv'):
        print("Required file (UserActivityLog.csv) not found!")
        print("Ensure the file exists in the program's directory.")
    else:
        global activity_data

        activity_data = pd.read_csv('UserActivityLog.csv')
        initiateAnalysis()