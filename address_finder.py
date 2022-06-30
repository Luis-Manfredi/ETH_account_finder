from eth_account import Account

Account.enable_unaudited_hdwallet_features()

mnemonic = "task private clap excess trophy arrive shoot twelve insect shine embrace heavy"

# m/44'/60'/0'/0/10
# address = "0xd25233e5D4d496747256a162BBf1b47A3951E0f2"

# m/44'/60'/10'/0/6
# address = "0x4980b30b215b88F270b01aC706e0Ca327FEF0F01"

# m/44'/60'/1'/0/4
# address = "0xf4605C4BD8F43b71ACCD46723A886b1a8E63E514"

# m/44'/60'/34'/0/6
# address = "0x0C17a2D734ecFc1faAC1355c9aA2340c037B44Df"

# m/44'/60'/0'/1/1
# address = "0x4315D9BF9a15C7F7BaaBf9006bE94275c39eF9AE"

# m/44'/60'/10'/1/2
# address = "0x585D6E2A41b01dd71Cf1547a36Ce16D1C3A97CB6"

# m/44'/60'/42'/1/9 ----- 10 segundos tomó la búsqueda
address = "0x91fcC0ac8E88BDBE67c2E66e26Ef3036B4A1D9e8"

print("Finding matches...")
account = Account.from_mnemonic(mnemonic)
counter = 0
index = 0
chain = 0

while address != str(account.address):
    account = Account.from_mnemonic(mnemonic, "", "m/44'/60'/{}'/{}/{}".format(index, chain, counter))
    print(account.address)
    counter+=1
    if address == str(account.address):
        print("Address found! Your address derivation path is: " + "m/44'/60'/{}'/{}/{}".format(index, chain, counter - 1)) 
    elif counter == 11:
        counter = 0
        index+=1
    elif index == 50:
        chain+=1
        index = 0
        counter = 0
    
    
