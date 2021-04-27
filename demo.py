import json, os
from solc import compile_standard
from web3 import Web3
from web3.middleware import geth_poa_middleware

ipc = os.path.expanduser("~/.ethereum/rinkeby/geth.ipc")

# the solc module uses this environment variable to locate the solidity compiler, which defaults to "solc"
os.environ['SOLC_BINARY'] = "solcjs"
w3 = Web3(Web3.IPCProvider(ipc))
w3.middleware_onion.inject(geth_poa_middleware, layer=0) # required when using a test network

FILENAME = "Greeter.sol"
CLASSNAME = "Greeter"
content = None
with open(FILENAME) as f:
    content = f.read()

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        FILENAME: {
            "content": content
        }
    },
    "settings":
        {
            "outputSelection": {
                "*": {
                    "*": [
                        "metadata", "evm.bytecode"
                        , "evm.bytecode.sourceMap"
                    ]
                }
            }
        }
})

bytecode = compiled_sol['contracts']['Greeter.sol']['Greeter']['evm']['bytecode']['object']
abi = json.loads(compiled_sol['contracts']['Greeter.sol']['Greeter']['metadata'])['output']['abi']
Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)
# tx_hash = Greeter.constructor().transact()
