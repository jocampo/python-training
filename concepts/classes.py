from enum import Enum


def valid_phone_number(phone_number):
    return phone_number.isalnum()  # This will do for now


class PhoneNumberType(Enum):
    """Enum for phone number types"""
    HOME, MOBILE, WORK, FAX = range(4)


class Contact:
    """Some doc about Contact class"""
    def __init__(self, phone_numbers, name, email = ""):
        """
        :param phone_numbers: A list of :PhoneNumber
        :param name: Name String
        :param email: Email String
        """
        # Validations can be performed here before the binding of the data
        # And exceptions can be thrown if the params are invalid
        if phone_numbers is None or len(phone_numbers) < 1:
            raise ValueError("A contact must have at least 1 phone number")
        self._phone_numbers = phone_numbers
        self._name = name
        self._email = email

    def phone_number(self):
        return self._phone_number

    def name(self):
        return self._name

    def email(self):
        return self._email

    def add_phone_number(self, number, number_type=PhoneNumberType.HOME):
        if number in self._phone_numbers:
            raise ValueError("This contact already has that phone number")
        self._phone_numbers.append(PhoneNumber(number, number_type))

    def print_conact_summary(self):
        print("********CONTACT INFO************")
        print("FULL NAME: {}".format(self._name))
        print("EMAIL ADDR: {}".format(self._email))
        for phone_number in self._phone_numbers:
            print("{} NUMBER: {}".format(phone_number.pretty_number_type(), phone_number.number()))
        print("********************************")


class PhoneNumber:
    """A contact may have one or more numbers"""
    def __init__(self, number, number_type=PhoneNumberType.HOME):
        if valid_phone_number∫(number) is False:
            raise TypeError("You entered an invalid phone number")
        self._number = number
        self._number_type = number_type
        self._parsed_number_types = {
            PhoneNumberType.HOME: "Home",
            PhoneNumberType.MOBILE: "Mobile",
            PhoneNumberType.WORK: "Work",
            PhoneNumberType.FAX: "Fax",
        }

    def number(self):
        return self._number

    def number_type(self):
        return self._number_type

    def pretty_number_type(self):
        return self._parsed_number_types[self.number_type()]


jorge_contact = Contact([PhoneNumber("09606146261", PhoneNumberType.MOBILE), PhoneNumber("272000332", PhoneNumberType.WORK)], "Jorge Ocampo", "jocampo@belatrixsf.com")
jorge_contact.add_phone_number("0991111111", PhoneNumberType.HOME)
jorge_contact.print_conact_summary()

