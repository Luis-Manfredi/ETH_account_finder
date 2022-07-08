# ETH_account_finder

## This is an ethereum account finder script made with python.
The main python file is "address_finder.py". This script uses a mnemonic and address to find the derivation path.

The way it works this script is that it takes two variables given by the programmer, in this case a mnemonic phrase of
12 words and an address related to this mnemonic. The program filters derivation paths from index 0 to index 10. Once 
the index reach 11, the script is going to reset this index and pass to the next account and so on until it reaches the 
address stablished in the code.

### En español:
El script principal es "address_finder.py". Este script usa una frase mnemotécnica y una dirección para encontrar la
ruta de derivación. 

La manera en que funciona este script es que toma dos variables dadas por el programador, en este caso una frase
mnemotécnica de 12 palabras y una dirección relacionada con dicha frase. El programa filtra las rutas de derivación del 
índice 0 al índice 10. Una vez que el índice alcance la posición 11, el script va a reestablecer la variable índice y va 
pasar hacia la siguiente cuenta, así sucesivamente hasta encontrar la dirección asignada en el código por el programador.
