# ETH_account_finder

## This is an ethereum account finder script made with python.
The main python file is "address_finder.py". This script uses a mnemonic and address to find the derivation path.
The way it works this script is that it takes two variables given by the programmer, in this case a mnemonic phrase of
12 words and an address related to this mnemonic. 

The program filters derivation paths from index 0 to index 10. Once the index reach 11, the script is going to reset 
and pass to the next account and so on until it reaches the address stablished in the code.
