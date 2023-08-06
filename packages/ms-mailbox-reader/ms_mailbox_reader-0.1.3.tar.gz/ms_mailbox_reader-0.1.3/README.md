# ms-mailbox-reader
A python package for windows which allows easy readnig of email 
messages from a local mailbox. Tested with Outlook and Microsoft Exchange. 


### Basic Usage
```python
from ms_mailbox_reader.client import MsExchangeClient, MessageFilter

msClient = MsExchangeClient()
last_n_hours = datetime.now() - timedelta(hours=2)
filter_params = MessageFilter(sender_email="@mydomain.com",
                              received_since = last_n_hours,
                              limit=25)

messages = msClient.get_outlook_messages(filter_params)

for message in messages:
    print(message.sender_name)
    print(message.body)
    print("=====================")
```