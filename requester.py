from pandas import Timestamp
from datetime import date
import constants

class Requester:

    def __init__(
            self,
            email: str,
            phone: str,
            first_name: str,
            last_name: str,
            birthday_timestamp: Timestamp,
            passport_number: str,
            passport_issue_date_timestamp: Timestamp,
            passport_expiration_date_timestamp: Timestamp,
            passport_issue_place: str,
            otp_code: str,
            status: str,
        ) -> None:
        # Login data
        self.email: str = email
        self.phone: str = phone

        # Personal data
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.birthday: date = birthday_timestamp.to_pydatetime().date()

        # Passport data
        self.passport_number: str = passport_number
        self.passport_issue_date: date = passport_issue_date_timestamp.to_pydatetime().date()
        self.passport_expiration_date: date = passport_expiration_date_timestamp.to_pydatetime().date()
        self.passport_issue_place: str = passport_issue_place

        # Others
        self.otp_code: str = otp_code
        self.status: str = status

    def is_from_quito(self) -> bool:
        return self.passport_issue_place == constants.QUITO
    
    def is_pending(self) -> bool:
        return self.status == constants.PENDING