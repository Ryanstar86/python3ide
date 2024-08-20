import bip39

def generate_mnemonic():
    mnemonic = bip39.generate_mnemonic()
    return mnemonic