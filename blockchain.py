from block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions
    It is implemented as a list of blocks
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def __repr__(self) -> str:
        return f'Blockchain: {self.chain}'

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))
    
def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)

if __name__ == '__main__':
    main()
