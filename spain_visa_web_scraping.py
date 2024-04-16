from requester import Requester
from thread_handler import ThreadHandler
from bls_spain_visa_web_scraper import BLSSpainVisaWebScraper
from pandas import DataFrame
import constants
import pandas

df: DataFrame = pandas.read_excel(constants.EXCEL_PATH, sheet_name=constants.GUAYAQUIL)
df_values = df.values
requesters: list[Requester] = []

# for value in df_values:
#     requester = Requester(*value)
#     if requester.is_pending():
#         requesters.append(requester)

value = df_values[0]
requester = Requester(*value)
requesters.append(requester)
requesters.append(requester)
requesters.append(requester)
requesters.append(requester)
requesters.append(requester)

###############################################################
    
threads_name: list[str] = []
scrapers_func = []

for requester in requesters:
    thread_name_formatted: str = f'Thread of {requester.first_name} {requester.last_name} requester'
    threads_name.append(thread_name_formatted)
    scraper = BLSSpainVisaWebScraper(requester)
    scrapers_func.append(scraper.scrape)
    
thread_handler = ThreadHandler(threads_name, scrapers_func)
thread_handler.start_threads()

###############################################################

# Last ERROR
# raise exception_class(message, screen, stacktrace, alert_text)  # type: ignore[call-arg]  # mypy is not smart enough here
# selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: Please confirm all the information and VAS for your application.
# Message: unexpected alert open: {Alert text : Please confirm all the information and VAS for your application.}
#   (Session info: chrome=106.0.5249.91)