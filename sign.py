from web3lib import get_goerli_test_web3

transaction = {
    'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
    'value': 1000000000,
    'gas': 2000000,
    'gasPrice': 2_000_000_000,
    'nonce': 0,
    'chainId': 5
}
key = '0x7c7fb042692bd4e82d79b2db5d7bda5f562a5d268dab66fc6c620646b993ba3d'
w3 = get_goerli_test_web3()
signed = w3.eth.account.sign_transaction(transaction, key)
tx = w3.eth.send_raw_transaction(signed.rawTransaction)
print(tx)
