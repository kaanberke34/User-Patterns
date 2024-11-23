
import win32gui
import uiautomation as ui_auto
import time
import datetime
import os
import csv

def fetchCurrentWindowActivity():
    current_window = win32gui.GetForegroundWindow()
    window_title = str(win32gui.GetWindowText(current_window))
    if "https://" in window_title or "http://" in window_title:
        window_title = "Browser Pop-up"
    activity_label = window_title.split(' - ')[-1]

    return current_window, activity_label, window_title

def retrieveWebsiteURL(window):
    try:
        control_element = ui_auto.ControlFromHandle(window)
        edit_box = control_element.EditControl()
        website_url = str(edit_box.GetValuePattern().Value).split('/')[0]
    except:
        website_url = "-"
    
    return website_url

def isLogFilePresent():
    return os.path.exists('UserActivityLog.csv')

def initializeLogFile():
    file_exists = isLogFilePresent()
    if file_exists:
        file_exists = not os.stat("UserActivityLog.csv").st_size == 0

    with open('UserActivityLog.csv', 'a', newline="") as log_file:
        log_writer = csv.writer(log_file)
        if not file_exists:
            print("Preparing the log file for activity tracking...")
            log_writer.writerow(["Date", "Activity Label", "Web Browser", "Website", "Start Time", "End Time", "Duration (h:m:s)"])
            time.sleep(2)
            print("Log file setup complete: UserActivityLog.csv")

def logActivityData(activity_date, activity_label, is_browser, website, start_time, end_time):
    initializeLogFile()
    with open('UserActivityLog.csv', 'a', newline="") as log_file:
        log_writer = csv.writer(log_file)
        log_writer.writerow([activity_date, activity_label, is_browser, website, start_time, end_time, (end_time - start_time)])

if __name__ == "__main__":
    os.system('cls')
    current_date = datetime.date.today()

    activity_start_time = datetime.datetime.now()
    previous_activity = ""
    previous_website = ""

    browsers_list = ["Google Chrome", "Mozilla Firefox"]

    initializeLogFile()
    while True:
        try:
            window, activity_label, window_title = fetchCurrentWindowActivity()
            activity_end_time = datetime.datetime.now()
            current_website = "-"
            if activity_label in browsers_list:
                current_website = retrieveWebsiteURL(window)
                if window_title.split(" - ")[0] == "New Tab":
                    current_website = "google.com"
            
            if previous_activity == "":
                previous_activity = activity_label
                if activity_label in browsers_list:
                    previous_website = current_website
            
            elif activity_label != previous_activity or (activity_label in browsers_list and current_website != previous_website) or datetime.date.today() != current_date:
                if previous_activity in browsers_list:
                    logActivityData(current_date, previous_activity, 1, previous_website, activity_start_time, activity_end_time)
                else:
                    logActivityData(current_date, previous_activity, 0, "-", activity_start_time, activity_end_time)

                previous_website = current_website
                activity_start_time = activity_end_time
                previous_activity = activity_label
                current_date = datetime.date.today()
        except KeyboardInterrupt:
            print("Would you like to exit? (Enter 'Y' or 'y' to confirm)")
            user_input = input("Choice: ")
            if user_input.lower() == "y":
                if previous_activity in browsers_list:
                    logActivityData(current_date, previous_activity, 1, previous_website, activity_start_time, activity_end_time)
                else:
                    logActivityData(current_date, previous_activity, 0, "-", activity_start_time, activity_end_time)
                print("Exiting!")
                break
            else:
                print("Continuing...")
                continue
        except UnicodeEncodeError:
            previous_activity = ""
            activity_start_time = activity_end_time
            continue