class Account:
    num_accounts = 0

    def __init__(self, name):
        self.name = name
        self.__class__.num_accounts += 1

    def __del__(self):
        self.__class__.num_accounts -= 1


kim = Account("kim")
print(kim.num_accounts)
print(Account.num_accounts)

lee = Account("lee")
print(lee.num_accounts)
print(Account.num_accounts)

park = Account("park")
print(kim.num_accounts)
print(Account.num_accounts)

del kim
print(Account.num_accounts)

del lee
print(Account.num_accounts)

del park
print(Account.num_accounts)
