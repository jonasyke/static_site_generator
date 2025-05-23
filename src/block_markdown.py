from enum import Enum
import re

def d(stuff):
    print(F"_______debug_______")
    print(stuff)
    print(F"_______debug_______")

class BlockType(Enum):
    paragraph = 'paragraph'
    heading = 'heading'
    list = 'list'
    code = 'code'
    quote = 'quote'
    unordered_list = 'unordered_list'
    ordered_list = 'ordered_list'

def block_to_block_type(block):
    lines = block.split('\n')
    if len(lines) == 1:
        line = lines[0]

        if re.match(r'^#{1,6}\s+', line):
            return BlockType.heading

        elif line.startswith('>'):
            return BlockType.quote

        elif re.match(r'^-\s+', line):
            return BlockType.unordered_list

        elif re.match(r'^1\.\s+', line):
            return BlockType.ordered_list

        elif line.startswith('```') and line.endswith('```'):
            return BlockType.code

        else:
            return BlockType.paragraph
    
    if all(line.startswith('>') for line in lines):
        return BlockType.quote
    
    elif all(re.match(r'^-\s+', line) for line in lines):
        return BlockType.unordered_list
    
    elif all(
        re.match(rf'^{i+1}\.\s+', lines[i]) for i in range(len(lines))
    ):
        return BlockType.ordered_list
    
    elif lines[0].startswith('```') and lines[-1].startswith('```'):
        return BlockType.code
    
    else:
        return BlockType.paragraph

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks = [block.strip() for block in blocks]
    blocks = [block for block in blocks if block]
    return blocks

