from thread_handler import ThreadHandler
from log import Log
import time
from requester import Requester
from pandas import DataFrame
import constants
import pandas

### Test of ThreadHandler
# def test_logic():
#     Log.s("this is a Test", True)
#     time.sleep(10)

# threads_name: list[str] = ['Thread 1', 'Thread 2', 'Thread 3', 'Thread 4', 'Thread 5']   # Number of browsers to spawn

# thread_handler = ThreadHandler(threads_name, test_logic)
# thread_handler.start_threads()

### Test of Pandas
df: DataFrame = pandas.read_excel(constants.EXCEL_PATH, sheet_name=constants.QUITO)
df_values = df.values
requesters: list[Requester] = []
for value in df_values:
    requester = Requester(*value)
    requesters.append(requester)

for index, requester in enumerate(requesters):
    Log.d(f"index = {index}  = {requester.first_name + requester.last_name}")