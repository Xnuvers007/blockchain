import json
import hashlib
from time import time


class Blockchain(object):
   def __init__(xnvrs):
      xnvrs.chain = []
      xnvrs.pending_transactions = []
      xnvrs.xnvrs1_new_block(previous_hash="Pesan pertama digunakan untuk menghasilkan hash pertama", proof=100)


   def xnvrs1_new_block(xnvrs, proof, previous_hash=None):
      block = {
         "index": len(xnvrs.chain) + 1,
         "timestamp": time(),
         "transactions": xnvrs.pending_transactions,
         "proof": proof,
         "previous_hash": previous_hash or xnvrs.hash(xnvrs.chain[-1])
      }
      xnvrs.pending_transactions = []
      xnvrs.chain.append(block)
      return block
