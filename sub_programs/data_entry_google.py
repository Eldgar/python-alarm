from calendar import c
import math
import gspread
import datetime

#service account api keys from google for access to google sheets
service_account = gspread.service_account()
sheet = service_account.open("My_Exercise")

worksheet_pushups = sheet.worksheet("Pushups")
worksheet_squats = sheet.worksheet("Squats")

current_day = int(datetime.date.today().strftime("%d")) + 1
current_month = datetime.date.today().strftime("%m")


#converts month to letter column in google sheets
def get_month(current_month):
    if (current_month == '01'):
        return 'A'

    if (current_month == '02'):
        return 'B'

    if (current_month == '03'):
        return 'C'

    if (current_month == '04'):
        return 'D'

    if (current_month == '05'):
        return 'E'

    if (current_month == '06'):
        return 'F'

    if (current_month == '07'):
        return 'G'

    if (current_month == '08'):
        return 'H'

    if (current_month == '09'):
        return 'I'

    if (current_month == '10'):
        return 'J'

    if (current_month == '11'):
        return 'K'

    if (current_month == '12'):
        return 'L'




def update_workout(pushups, squats):
    worksheet_pushups.update(get_month(current_month) + str(current_day), str(pushups))
    worksheet_squats.update(get_month(current_month) + str(current_day), str(squats))
