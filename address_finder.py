import sys, time, threading
from eth_account import Account

Account.enable_unaudited_hdwallet_features()

'''
m/44'/60'/0'/0/10
address = "0xd25233e5D4d496747256a162BBf1b47A3951E0f2"

m/44'/60'/10'/0/6
address = "0x4980b30b215b88F270b01aC706e0Ca327FEF0F01"

m/44'/60'/34'/0/6
address = "0x0C17a2D734ecFc1faAC1355c9aA2340c037B44Df"

m/44'/60'/0'/1/1
address = "0x4315D9BF9a15C7F7BaaBf9006bE94275c39eF9AE"

m/44'/60'/10'/1/2
address = "0x585D6E2A41b01dd71Cf1547a36Ce16D1C3A97CB6"

m/44'/60'/42'/1/9 ----- 10 segundos tomó la búsqueda
address = "0x91fcC0ac8E88BDBE67c2E66e26Ef3036B4A1D9e8"

m/44'/60'/45'/2/0
address = "0xbc6833FD93667203be2eA4EED9A803ED62551776" 

m/44'/60'/45'/4/0
address = "0xF3a47abe58f0F2C643062bFAf9Ce8ba580Ed2C93"
'''

print("Finding matches...")
#Initialization
mnemonic = "task private clap excess trophy arrive shoot twelve insect shine embrace heavy"
address = "0xbc6833FD93667203be2eA4EED9A803ED62551776"  # m/44'/60'/45'/2/0
account = Account.from_mnemonic(mnemonic)

def searchAddress(account):
    # Variables initialization
    counter = 0
    index = 0
    chain = 0
    lines = 0
    maxLines = 2000
    while address != str(account.address) and lines < maxLines:
        account = Account.from_mnemonic(mnemonic, "", "m/44'/60'/{}'/{}/{}".format(index, chain, counter))
        # print(account.address)
        counter+=1
        lines+=1

        # Conditions
        if address == str(account.address):
            print("Address found! Your address derivation path is: " + "m/44'/60'/{}'/{}/{}".format(index, chain, counter - 1)) 
            print("Lines executed: " + str(lines))
        elif counter == 11:
            counter = 0
            index+=1
        elif index == 50:
            chain+=1
            index = 0
            counter = 0
        elif lines == maxLines:
            print("Couldn't find derivation path within the range :(")
            print("Lines executed: " + str(lines))
            break     

# Execution
searchAddress(account)   