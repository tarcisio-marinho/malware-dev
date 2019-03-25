#!/bin/bash/env python
# coding=UTF-8

import Crypto.Random 
import base64

def generate_key(bits, encode=False):
    generated = Crypto.Random.OSRNG.posix.DevURandomRNG()
    content = generated.read(bits)
    
    if(encode):
        return base64.b64encode(content)

    return content

if __name__ == "__main__":
    print(generate_key(32, True))
