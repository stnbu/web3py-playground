#!/usr/bin/env python3

# 7c7fb042692bd4e82d79b2db5d7bda5f562a5d268dab66fc6c620646b993ba3d


import os
import os
import sys
import time
import pprint
from eth_account import Account
#from web3.providers.eth_tester import EthereumTesterProvider
from web3 import Web3
#from eth_tester import PyEVMBackend
from solcx import compile_source
from web3.middleware import geth_poa_middleware

def get_goerli_test_account():
   return Account.from_key(os.getenv('PRIVATE_KEY'))

def get_goerli_test_web3():
   ipc = os.path.expanduser(os.path.expanduser("~/.ethereum/goerli/geth.ipc"))
   #os.environ['SOLC_BINARY'] = "solcjs"
   w3 = Web3(Web3.IPCProvider(ipc))
   w3.middleware_onion.inject(geth_poa_middleware, layer=0) # required when using a test network
   return w3
   
#  send_raw_transaction()

def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).constructor().transact()
    address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
    return address
