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
        if self.party_count < 1:
            print("No one is joining for the party")
        else:
            self.set_party_members()
            print()
            self.set_bill()
            print()
            # self.disperse_bill()
            self.lucky()

    def set_party_count(self):
        self.party_count = int(input("Enter the number of friends joining (including you):\n"))

    def set_party_members(self):
        if self.party_count < 1:
            print("No one is joining for the party")
        else:
            print("Enter the name of every friend (including you), each on a new line:")
            for i in range(self.party_count):
                friend = Friend()
                self.party_dict.update(friend.__dict__())

    def set_bill(self):
        self.bill = int(input("Enter the total bill value:\n"))

    def disperse_bill(self):
        dispersment = round(float(self.bill) / float(self.party_count), 2)
        for key in self.party_dict.keys():
            self.party_dict.update({key: dispersment})

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
