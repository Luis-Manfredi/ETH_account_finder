from eth_account import Account

Account.enable_unaudited_hdwallet_features()
# mnemonic = input("Add a mnemonic phrase of 12 words: ")
mnemonic = "task private clap excess trophy arrive shoot twelve insect shine embrace heavy"
num = int(input("Add the number of address you want to find: "))
address = "0xd25233e5D4d496747256a162BBf1b47A3951E0f2"
listOfAddresses = []
print()

for i in range(num+1):
    print("m/44'/60'/{}'/0/x".format(i) + "==========================")
    for e in range(num+1):
        acct = Account.from_mnemonic(mnemonic, "", "m/44'/60'/{}'/0/{}".format(i, e))
        myAccount = acct.address
        print(myAccount)
        listOfAddresses.append(myAccount)

    print("m/44'/60'/{}'/1/x".format(i) + "==========================")
    for e in range(num+1):
        acct = Account.from_mnemonic(mnemonic, "", "m/44'/60'/{}'/1/{}".format(i, e))
        myAccount = acct.address
        print(myAccount)
        listOfAddresses.append(myAccount)
    print()