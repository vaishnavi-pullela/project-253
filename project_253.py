# --------------253 Proj----------------
from web3 import Web3
import time
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x249F26b88E9291051f5685D58C12aF69779B72B5'
James_account = '0xc3Eddbe9FF70011eBb6026E1D9EdE03f366bA5F9'
Ryan_account  = '0x9F2d82eA614Dc50B7bc306603f1aabD8a4b99Df5'


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
    'nonce': nonce1,
    'to':James_account,
    'value':web3_ganache_connection.to_wei(5, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x4cf48f0d53f24492736a8f21cb2fb647c1872e957118e836be1be1f4a2034f1b'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash1))



# -----------------
print("Wait for few seconds Transaction is in progress...") 
time.sleep(5)
# -----------------



nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    'nonce':nonce2,
    'to':Ryan_account,
    'value':web3_ganache_connection.to_wei(5, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0x8f530e2552dc3704312c6b377f364f043c26e7a2eb51685e22382e7e05b3ac81'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash2))



