
def truncate_line(truncate_at, string_line):

    byte_count= 0
    for char in string_line:
        utf8_byte_len= len(char.encode('utf-8'))
        if (byte_count+ utf8_byte_len) > truncate_at:
            break
        byte_count+= utf8_byte_len

    ba_string= bytearray(string_line, 'utf-8')
    final_string= str(ba_string[:byte_count], encoding='utf-8')

    return final_string

if __name__ == "__main__":
    with open('cases', 'rb') as read_file:
        read_line= read_file.readlines()
        for line in read_line:
            print(truncate_line(int(line[0]), str(line[1:], encoding='utf-8').strip()))