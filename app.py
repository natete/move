import os
import shutil
from datetime import datetime


def create_date(file_name):
    file_date = file_name.split("_")[1]

    return datetime.strptime(file_date, '%d.%m.%Y').date()


def move_files_by_date():
    today = datetime.now().date()

    origin_path = "archivos"
    destination_path = "destination"

    dirs = os.scandir(origin_path)

    for file_entry in dirs:

        file_name, file_extension = os.path.splitext(os.path.basename(file_entry))

        file_date = create_date(file_name)

        if file_date < today:
            year_path = os.path.join(destination_path, file_date.strftime('%Y'))

            if not os.path.isdir(year_path):
                os.mkdir(year_path)

            month_path = os.path.join(year_path, file_date.strftime('%m'))

            if not os.path.isdir(month_path):
                os.mkdir(month_path)

            shutil.copy(file_entry, month_path)


move_files_by_date()
