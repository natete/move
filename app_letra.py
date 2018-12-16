
import os, sys, time, shutil


from datetime import datetime

today = datetime.now().date()


def create_date(file):
    date_file = file.split("_")[1].split(".")[:3]
    date_file = "/".join(date_file)
    date_file = datetime.strptime(date_file, '%d/%m/%Y').date()
    return date_file

def month(file):
    if create_date(file).month not in os.listdir():
        os.mkdir(str(create_date(file).month))
        pathf = os.getcwd()
        pathf += "/" + str(create_date(file).month)
        os.chdir(pathi)
        shutil.copy(path + file, pathf)

    else:
        pathf = os.getcwd()
        pathf += "/" + str(create_date(file).month)
        shutil.copy(path + file, pathf)

path = "archivos/"
pathi = os.getcwd()

dirs = os.listdir(path)


def mover_letra(dirs):

    for file in dirs:

        os.chdir(pathi)
        if str(create_date(file)) < str(today):
            if file[0] not in os.listdir():
                os.mkdir(file[0])
                npath = file[0] + "/"
                os.chdir(npath)
                if str(create_date(file).year) not in os.listdir():
                    os.mkdir(str(create_date(file).year))
                    npath = str(create_date(file).year) + "/"
                    os.chdir(npath)
                    month(file)


                else:
                    npath = str(create_date(file).year) + "/"
                    os.chdir(npath)
                    month(file)

            else:
                os.chdir(file[0]+"/")
                if str(create_date(file).year) not in os.listdir():
                    os.mkdir(str(create_date(file).year))
                    npath = str(create_date(file).year) + "/"
                    os.chdir(npath)
                    month(file)


                else:
                    npath = str(create_date(file).year) + "/"
                    os.chdir(npath)
                    month(file)



mover_letra(dirs)