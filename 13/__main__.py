import schedule
import time
from lib.classes.CsvSource import CsvSource
from lib.classes.TxtSource import TxtSource

def check_for_new_files():
    csv_source.create_path()
    csv_source.check_for_new_files()
    txt_source.create_path()
    txt_source.check_for_new_files()

csv_source = CsvSource()
txt_source = TxtSource()


schedule.every(5).seconds.do(check_for_new_files)

while True:
    schedule.run_pending()
    time.sleep(1)