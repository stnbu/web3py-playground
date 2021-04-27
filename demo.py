import json
from solc import compile_standard
from web3 import Web3
from web3.middleware import geth_poa_middleware

#export SOLC_BINARY=/usr/local/bin/solcjs
#pip3 install py-solc

ipc = "/home/mburr/.ethereum/rinkeby/geth.ipc"
w3 = Web3(Web3.IPCProvider(ipc))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "Greeter.sol": {
            "content": '''
                pragma solidity ^0.8.0;

                contract Greeter {
                  string public greeting;

                  constructor() public {
                      greeting = 'Hello';
                  }

                  function setGreeting(string memory _greeting) public {
                      greeting = _greeting;
                  }

                  function greet() view public returns (string memory) {
                      return greeting;
                  }
                }
              '''
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
