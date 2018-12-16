import schedule
import time

import os, sys, time, shutil
import schedule

from datetime import datetime

today = datetime.now().date()



def create_date(file):
    date_file = file.split("_")[1].split(".")[:3]
    date_file = "/".join(date_file)
    date_file = datetime.strptime(date_file, '%d/%m/%Y').date()
    return date_file


path = "archivos/"
pathi = os.getcwd()

dirs = os.listdir(path)
def mover():
    for file in dirs:
        print(path + file)

        if str(create_date(file)) < str(today):
            if str(create_date(file).year) not in os.listdir():
                os.mkdir(str(create_date(file).year))
                npath = str(create_date(file).year) + "/"

                if create_date(file).month not in os.listdir(npath):
                    os.chdir(npath)
                    os.mkdir(str(create_date(file).month))
                    os.chdir(pathi)
                    shutil.copy(path + file, npath+str(create_date(file).month))

                else:
                    shutil.copy(path + file, npath+str(create_date(file).month))


            else:
                npath = str(create_date(file).year) + "/"
                if create_date(file).month not in os.listdir(npath):
                    os.chdir(npath)
                    os.mkdir(str(create_date(file).month))
                    os.chdir(pathi)
                    shutil.copy(path + file, npath+str(create_date(file).month))

                else:
                    shutil.copy(path + file, npath+str(create_date(file).month))




# schedule.every().day.at("09:00").do(mover)
# schedule.every().day.at("12:00").do(mover)
# schedule.every().day.at("15:00").do(mover)
# schedule.every().day.at("18:30").do(mover)
#
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
mover()
