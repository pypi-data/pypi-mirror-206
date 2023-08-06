# ms-mailbox-reader
A python package for windows which allows easy reading of email 
messages from a local mailbox. Tested with Outlook + Microsoft Exchange on a Windows 11 PC. 


### Basic Usage
```python
from ms_mailbox_reader.client import MsExchangeClient, MessageFilter

# Create the message reader
message_reader = MsOutlookMessageReader()

# Timedelta representing the last two hours
last_n_hours = datetime.now() - timedelta(hours=2)

# Create a filter to limit returned messages to a max of 25, 
# those which were sent from @mydomain.com and 
# received in the last two hours
filter_params = MessageFilter(sender_email="@mydomain.com",
                              received_since = last_n_hours,
                              limit=25)

# Get the message list
messages = message_reader.get_outlook_messages(filter_params)

# Do stuff with the messages
for message in messages:
    print(message.sender_name)
    print(message.body)
    print("=====================")
```