import time

from backend.chain.block import Block, GENESIS_DATA
from backend.config import MINE_RATE, SECONDS

def test_mine_block():
    last_block = Block.genesis()

    data = 'test'
    block = Block.mine_block(last_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash
    assert block.hash[0:block.difficulty] == '0' * block.difficulty

def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    assert genesis.timestamp == GENESIS_DATA['timestamp']
    assert genesis.last_hash == GENESIS_DATA['last_hash']
    assert genesis.hash == GENESIS_DATA['hash']
    assert genesis.data == GENESIS_DATA['data']

def test_quickly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'testing')
    mined_block = Block.mine_block(last_block, 'blocks')

    assert mined_block.difficulty == last_block.difficulty + 1

def test_slowly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'testing')

    time.sleep(MINE_RATE / SECONDS)

    mined_block = Block.mine_block(last_block, 'blocks')
