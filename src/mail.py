from imap_tools import MailBox, AND
from dataclasses import dataclass

@dataclass
class Email:
    """A minimal wrapper around an email text."""
    subject: str
    body: str

    def get(username: str, password: str) -> list['Email']:
        """Login with the username and password, and get a list of unread emails."""
        with MailBox('imap.gmail.com').login(username, password) as mailbox:
            msgs = mailbox.fetch(AND('UNSEEN'))
            return [ Email(msg.subject, msg.text) for msg in msgs ]