'''
6. Abstraction
#Abstraction hides complex details and exposes only essential info. (or)
#Abstraction is about showing only what’s needed and hiding how it works inside.

Example: Message Sender
You have a general message sender. Whether it's email or SMS, the user only sees send_message(), not how it works inside.

Example code:
---------------
# Define parent class
class MessageSender:
    def send_message(self, message):
        print("Sending message:", message)

# Define child classes
class EmailSender(MessageSender):
    pass

class SMSSender(MessageSender):
    pass

# Create objects and call method
email = EmailSender()
sms = SMSSender()

email.send_message("Welcome to our platform!")
sms.send_message("Your OTP is 1234.")

Output:
 Sending message: Welcome to our platform!
 Sending message: Your OTP is 1234.
'''
