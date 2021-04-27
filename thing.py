#!/usr/bin/env python3

import os
from eth_account import Account

key = os.getenv('PRIVATE_KEY')

account = Account.from_key(key)

print(account.key)
