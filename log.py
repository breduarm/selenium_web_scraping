from colorama import Fore
from datetime import datetime

class Log:
    default_color: str = Fore.WHITE
    sistem_color: str = Fore.MAGENTA
    info_color: str = Fore.BLUE
    confirm_color: str = Fore.GREEN
    alert_color: str = Fore.YELLOW
    error_color: str = Fore.RED

    @staticmethod
    def s(message: str, show_time: bool = False) -> None:
        Log.__print_helpert__(Log.confirm_color, message, show_time)

    @staticmethod
    def i(message: str, show_time: bool = False) -> None:
        Log.__print_helpert__(Log.info_color, message, show_time)
    
    @staticmethod
    def d(message: str, show_time: bool = False) -> None:
        Log.__print_helpert__(Log.sistem_color, message, show_time)

    @staticmethod
    def w(message: str, show_time: bool = False) -> None:
        Log.__print_helpert__(Log.alert_color, message, show_time)

    @staticmethod
    def e(message: str, show_time: bool = False) -> None:
        Log.__print_helpert__(Log.error_color, message, show_time)

    @classmethod
    def __print_helpert__(cls, highliter_color: str, message: str, show_time) -> None:
        final_message: str = message
        if show_time: final_message = datetime.now().ctime() + ' : ' + message
        print(highliter_color + final_message + Log.default_color)