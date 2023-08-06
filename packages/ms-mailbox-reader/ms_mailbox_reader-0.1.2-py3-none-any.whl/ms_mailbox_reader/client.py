import re


class MsExchangeClient:
    def __init__(self):
        pass

    def extract_content_before_from_pattern(self, message_body):
        pattern = r"From: .*?<.*?>"
        match = re.search(pattern, message_body)

        if match:
            end_index = match.start()
            text_before_match = message_body[:end_index]
        else:
            text_before_match = message_body

        return text_before_match

    def get_outlook_messages():
        # Create an instance of the Outlook Application
        outlook = win32com.client.Dispatch(
            "Outlook.Application").GetNamespace("MAPI")

        # Get the default Inbox folder
        inbox = outlook.GetDefaultFolder(6)  # 6 represents the Inbox folder

        # Calculate the time 5 hours ago
        n_hours_ago = datetime.now() - timedelta(hours=12)
        # Format the time as an Outlook date string
        n_hours_ago_str = n_hours_ago.strftime('%m/%d/%Y %H:%M %p')

        ebsco_ou = "FYDIBOHF23SPDLT"
        # Get all messages in the Inbox folder received in the last 5 hours
        # from someone with an ebsco.com email address and not a calendar item
        filter_condition = f"[ReceivedTime] >= '{n_hours_ago_str}' AND [MessageClass] = 'IPM.Note'"
        messages = inbox.Items.Restrict(filter_condition)

        # Iterate through the messages and print their subject and received time if it's a conversation with someone from ebsco.com
        for message in messages:
            try:
                sender_email = message.SenderEmailAddress
                if ebsco_ou in sender_email:
                    print(f"Subject: {message.Subject}")
                    print(f"From: {message.Sender}")
                    print(f"Received Time: {message.ReceivedTime}")
                    print("------")
                    print(
                        f"Body: {extract_original_message_content(message.Body)}")
                    print(f"============================")
            except Exception as e:
                print(f"Error: {e}")
                print("------")
