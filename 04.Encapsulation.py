'''
4.Encapsulation
#Encapsulation means hiding internal details of a class and only exposing what’s necessary. It helps to protect important data from being changed directly and keeps the code secure and organized.

Example: Locker PIN
(Your locker has a PIN that only you can change using buttons.
No one can directly touch or see the PIN inside.
This is like hiding sensitive info and allowing only safe, controlled access using methods like get_pin() or set_pin().)

Example Code:
--------------
# Define class
class Locker:
    def _init_(self, pin):
        self.__pin = pin            # Private variable

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if isinstance(new_pin, int) and 1000 <= new_pin <= 9999:
            self.__pin = new_pin
        else:
            print("Invalid PIN")

# Create object and test access
locker = Locker(1234)                   # Object with private data
print("Old PIN:", locker.get_pin())
locker.set_pin(4321)
print("New PIN:", locker.get_pin())

Output:
       Old PIN: 1234
       New PIN: 4321
'''
