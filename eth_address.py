from eth_account import Account

Account.enable_unaudited_hdwallet_features()
mnemonic = input("Add a mnemonic phrase of 12 words: ")
num = int(input("Add the number of address you want to find: "))
print()

for i in range(num+1):
    print("m/44'/60'/{}'/0/0".format(i) + "==========================")
    for e in range(num+1):
        acct = Account.from_mnemonic(mnemonic, "", "m/44'/60'/{}'/0/{}".format(i, e))
        myAccount = acct.address
        print(myAccount)
        
    print("m/44'/60'/{}'/0/1".format(i) + "==========================")
    for e in range(num+1):
        acct = Account.from_mnemonic(mnemonic, "", "m/44'/60'/{}'/1/{}".format(i, e))
        myAccount = acct.address
        print(myAccount)
    print()