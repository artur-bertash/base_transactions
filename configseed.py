import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

ABIS_DIR = os.path.join(ROOT_DIR, 'abis')

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')
WOOFI_ABI = os.path.join(ABIS_DIR, 'woofi.json')

private_key = '0xdb2a1dde0eae643315991ba5d4451176a5a5b1c23e2abd2ddcebd5faa7ba3ed9'
seed = 'ancient silly crisp paper nut explain kid nominee choice basic account crystal'
address = '0x30b0aCD3045b511c86Dc319F8DcAf483A30EbC19'
eth_rpc = 'https://mainnet.infura.io/v3/'
arb_rpc = 'https://rpc.ankr.com/arbitrum/'
base_rpc = 'https://base.llamarpc.com'
