#! /usr/bin/env python3
from math import nan
import struct

def conceal( six_byte_msg):

    empty_payload_nan= bytearray( struct.pack( "<d", nan))
    struct.pack_into( "<6s", empty_payload_nan, 0, six_byte_msg.encode('utf-8'))

    return struct.unpack( "<d", empty_payload_nan)[0]

def extract( loaded_nan):

    payload_nan= bytearray( struct.pack( "<d", loaded_nan))
    payload_msg= struct.unpack_from( "<6s", payload_nan, 0)

    return payload_msg[0].decode('utf-8')

if __name__ == "__main__":
    sneaky_nan= conceal("hello!")
    print( sneaky_nan)

    payload= extract( sneaky_nan)
    print( payload)