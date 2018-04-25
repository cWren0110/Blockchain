# -*- coding: utf-8 -*-

import hashlib as hasher
import datetime as date


class SnakeCoin:
    def __init__(self):
        self.__blockchain__ = [self.__create_genesis_block__()]
    
    def __str__(self):
        output = [str(block) for block in self.__blockchain__]
        return '\n'.join(output)
    
    def __len__(self):
        return len(self.__blockchain__)
        
    def __create_genesis_block__(self):
        ''' Manually construct a block with
            index zero and arbitrary previous hash'''
        return self.Block(0, date.datetime.now(), "Genesis Block", "0")
    
    def __next_block__(self, last_block):
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = "Hey! I'm block " + str(this_index)
        this_hash = last_block.hash
        return self.Block(this_index, this_timestamp, this_data, this_hash)
    
    def add_block(self):
        block_to_add = self.__next_block__(self.__blockchain__[-1])
        self.__blockchain__.append(block_to_add)
        
    class Block:
        def __init__(self, index, timestamp, data, previous_hash):
            self.index = index
            self.timestamp = timestamp
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.hash_block()
        
        def __str__(self):
            return self.hash
        
        def hash_block(self):
            sha = hasher.sha256()
            sha.update((str(self.index) + 
                        str(self.timestamp) + 
                        str(self.data) + 
                        str(self.previous_hash)).encode())
            return sha.hexdigest()

def main():
    sc = SnakeCoin()
    print('Raw SnakeCoin')
    print(sc)
    while(len(sc)!=5):
        sc.add_block()
    print('Updated SnakeCoin')
    print(sc)
    
if __name__ == '__main__':
    main()