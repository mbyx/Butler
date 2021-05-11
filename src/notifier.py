from dataclasses import dataclass
from database import Database
from typing import NoReturn
import arrow, Notification
from mail import Email


@dataclass
class Notifier:
    """The dameon that listens for plans and emails."""
    db: Database
    username: str
    password: str

    def listen(self) -> NoReturn:
        """Continuously loop while checking for due plans and unread email."""
        while True:
            # Check Plans
            plans = self.db.read()
            for plan in plans:
                if plan.due_date <= arrow.utcnow():
                    self.db.write(filter(lambda p: plan != p, plans))
                    Notification.toast('Butler', f'{plan.name} is due.')
            
            # Check Messages
            for mail in Email.get(self.username, self.password):
                Notification.toast(mail.subject, mail.body)