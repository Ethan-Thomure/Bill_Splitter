from random import choice
class Friend:
    def __init__(self):
        self.name = input()
        self.portion = 0

    def __dict__(self):
        return {self.name: self.portion}


class Party:
    def __init__(self):
        self.party_count = 0
        self.party_dict = {}
        self.bill = 0
        self.lucky_one = ""

        self.set_party_count()
        print()
        if self.party_count < 2:
            print("No one is joining for the party")
        else:
            self.set_party_members()
            print()
            self.set_bill()
            print()
            self.lucky()
            self.disperse_bill()

    def set_party_count(self):
        self.party_count = int(input("Enter the number of friends joining (including you):\n"))

    def set_party_members(self):
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(self.party_count):
            friend = Friend()
            self.party_dict.update(friend.__dict__())

    def set_bill(self):
        self.bill = int(input("Enter the total bill value:\n"))

    def disperse_bill(self):
        if self.lucky_one == "":
            disbursement = round(float(self.bill) / float(self.party_count), 2)
            self.party_dict = {key: disbursement for key in self.party_dict.keys()}
        else:
            disbursement = round(float(self.bill) / float(self.party_count - 1), 2)
            self.party_dict = {key: (disbursement if key != self.lucky_one else 0) for key in self.party_dict.keys()}

    def lucky(self):
        is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if is_lucky.lower() == "yes":
            self.lucky_one = choice(list(self.party_dict.keys()))
            print(self.lucky_one + " is the lucky one!")
        else:
            print("No one is going to be lucky")

    def print_party(self):
        if self.party_count > 0:
            print(self.party_dict)


if __name__ == "__main__":
    party = Party()
    print()
    party.print_party()
