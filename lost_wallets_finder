import api_requests
import cryptography
import threading
import time

def find_lost_wallets():
    """
    Scans blockchains for lost wallets using the Blockchair API.
    """
    url = 'https://api.blockchair.com/bitcoin/raw/address/'

    for address in addresses:
        full_url = url + address
        response = api_requests.make_api_request(full_url)

        if response:
            balance = response['balance']
            if balance > 0:
                print(f'Found a lost wallet with address {address} and balance {balance}!')

def generate_seed():
    """
    Generates a new mnemonic seed using the cryptography library.
    """
    seed = cryptography.generate_mnemonic()
    print(f'Generated a new mnemonic seed: {seed}')

if __name__ == '__main__':
    addresses = []
    n_threads = 4

    # Get user input for addresses
    while True:
        address = input('Enter a Bitcoin address to scan (or "done" to continue): ')
        if address.lower() == 'done':
            break
        addresses.append(address)

    # Create a thread for each address
    threads = []
    for i in range(n_threads):
        thread = threading.Thread(target=find_lost_wallets)
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print('\nScan complete!')

    # Generate a new mnemonic seed
    generate_seed()