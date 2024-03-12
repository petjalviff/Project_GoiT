import re


class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
    

class Birthday(Field):
    def __init__(self, value: str) -> None:
        if self._is_valid_date(value):
            super().__init__(value)
        else:
            raise ValueError("Date must be in format dd.mm.yyyy")

    def _is_valid_date(self, value) -> bool:
        pattern = r'^\d{2}\.\d{2}\.\d{4}$'
        if re.match(pattern, value):
            return True
        return False
    
    
class Name(Field):
    def __init__(self, value: str) -> None:
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str) -> None:
        for char in value:
            if char.isalpha():
                raise ValueError("Phone number must contain only digits.")
        if len(value) < 10:
            raise ValueError("Phone number must be at least 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name: Name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if str(p) == old_phone:
                p.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p.value
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = '; '.join(str(p) for p in self.phones)
        birthday = f", Birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"


from datetime import datetime, timedelta

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(self):
        today = datetime.today().date()
        current_day = today.weekday()
        birthdays = {i: [] for i in range(7)}
        for record in self.data.values():
            if record.birthday:
                birthday = datetime.strptime(record.birthday.value, '%d.%m.%Y').date()
                birthday_this_year = birthday.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                delta_days = (birthday_this_year - today).days
                birthday_weekday = (today + timedelta(days=delta_days)).weekday()
                if delta_days <= current_day:
                    birthday_weekday = (birthday_weekday + 1) % 7
                birthdays[birthday_weekday].append(record.name.value)

        for day, names in birthdays.items():
            day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day]
            if names:
                print(f"{day_name}: {', '.join(names)}")


def handle_add(args, book):
    if len(args) != 2:
        return "Invalid command. Please provide name and phone."
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."

def handle_change(args, book):
    if len(args) != 2:
        return "Invalid command. Please provide name and new phone."
    name, new_phone = args
    record = book.find(name)
    if record:
        old_phone = record.find_phone(new_phone)
        if old_phone:
            record.remove_phone(old_phone)
        record.add_phone(new_phone)
        return "Phone number updated."
    else:
        return f"Contact '{name}' not found."

def handle_phone(args, book):
    if len(args) != 1:
        return "Invalid command. Please provide name."
    name = args[0]
    record = book.find(name)
    if record:
        phones = "; ".join(str(phone) for phone in record.phones)
        return f"Phone number(s) for {name}: {phones}"
    else:
        return f"Contact '{name}' not found."

def handle_all(book):
    if book.data:
        return "\n".join(str(record) for record in book.data.values())
    else:
        return "No contacts found."

def handle_hello():
    return "Hello! How can I assist you today?"


def handle_add_birthday(args, book):
    if len(args) != 2:
        return "Invalid command. Please provide name and birthday (DD.MM.YYYY)."
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        return f"Contact '{name}' not found."

def handle_show_birthday(args, book):
    if len(args) != 1:
        return "Invalid command. Please provide name."
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday: {record.birthday}"
    elif record:
        return f"{name} does not have a birthday set."
    else:
        return f"Contact '{name}' not found."

def handle_birthdays(book):
    book.get_birthdays_per_week()
    return ""

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

if __name__ == "__main__":
    book = AddressBook()
    print("Welcome to the Address Book Bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(handle_hello())
        elif command == "add":
            print(handle_add(*args, book))
        elif command == "change":
            print(handle_change(*args, book))
        elif command == "phone":
            print(handle_phone(*args, book))
        elif command == "all":
            print(handle_all(book))
        elif command == "add-birthday":
            print(handle_add_birthday(*args, book))
        elif command == "show-birthday":
            print(handle_show_birthday(*args, book))
        elif command == "birthdays":
            print(handle_birthdays(book))
        else:
            print("Invalid command.")

# the end