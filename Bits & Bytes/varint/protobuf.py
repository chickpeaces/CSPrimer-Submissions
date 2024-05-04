def encode( data):
    """
    take the 7 lsb's 
    if there is more of the int, add the continuation_bit
    shift the data to the right 7
    """
    output = []
    _data = int.from_bytes(data, byteorder='big')

    while True:
        if( (_data >> 7) > 0):
            output.append( _data & 0x7f | 0x80)
        elif( (_data >> 7) <= 0):
            output.append( _data & 0x7f)
            break
        _data = _data >> 7
        
    return bytes(output)
    
def decode( data):
    """
    take the 7 msb's (little endian byte order)
    check continuation bit
        as long as c_bit is 1 
            take the next 7 lsb's as binary
            concatenate the 7 lsb's with all the other binary data
    """
    output = []
    _data = int.from_bytes( data, byteorder='little')

    while True:
        if( _data >> 7 > 0):
            output.append(format( _data & 0x7f, '07b'))
            _data = _data >> 8
        elif( _data >> 7 <=0):
            output.append(format( _data & 0x7f, 'b'))
            break
    
    output_bin = '0b'
    output.reverse()
    for item in output:
        output_bin = output_bin + item
    
    return int(output_bin, base=2)

if __name__ == '__main__':

    files = ['1.uint64', '2.uint64', '150.uint64', '281474976710657.uint64', 'maxint.uint64']
    for file in files:
        with open( file, 'rb') as _file:
            read_data = _file.read()
        
        assert int.from_bytes(read_data, byteorder='big') == decode(encode(read_data))
        
        # print("raw binary value: ", read_data)
        # print("uint64 value:", int.from_bytes(read_data, byteorder='big'))
        # print("encode: ", encode(read_data))
        # print("decode: ", decode(encode(read_data)))
        # print()
    
    # for n in range(1 << 30): # test a range of binary numbers
        # print('\r',n, end='')
        # assert decode(encode( n.to_bytes(8, byteorder='big'))) == n
    
    