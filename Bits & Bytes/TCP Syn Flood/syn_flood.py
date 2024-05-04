
def parse_IP_header( packet_header):
# 0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |Version|  IHL* |Type of Service|          Total Length         |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |         Identification        |Flags|      Fragment Offset    |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |  Time to Live |    Protocol   |         Header Checksum       |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                       Source Address                          |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                    Destination Address                        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                    Options                    |    Padding    |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 

    header_ = {
        'version': (packet_header[0] & 0xf0) >> 4,
        'header_length': (packet_header[0] & 0x0f) *4,
        'type_of_service': packet_header[1],
        'total_length': int.from_bytes( packet_header[2:4], byteorder='big'),
        'identification': int.from_bytes( packet_header[4:6], byteorder='big'),
        'flags': packet_header[6] & 0xf0,
        'fragmentation_offset': packet_header[7] | ( packet_header[6] & 0x0f),
        'time_to_live': packet_header[8],
        'protocol': packet_header[9],
        'header_checksum': int.from_bytes( packet_header[10:12], byteorder='big'),
        'source_address': "{0}.{1}.{2}.{3}".format( *packet_header[12:16]),
        'destination_address': "{0}.{1}.{2}.{3}".format( *packet_header[16:20])
    }

    return header_

def parse_TCP_header( packet_header):
#      0                   1                   2                   3   
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |          Source Port          |       Destination Port        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                        Sequence Number                        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                    Acknowledgment Number                      |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |  Data |           |U|A|P|R|S|F|                               |
#    | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
#    |       |           |G|K|H|T|N|N|                               |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |           Checksum            |         Urgent Pointer        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                    Options                    |    Padding    |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                             data                              |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    
    header_ = {
        'source_port': int.from_bytes( packet_header[0:2], byteorder='big'),
        'destination_port': int.from_bytes( packet_header[2:4], byteorder='big'),
        'sequence_number': int.from_bytes( packet_header[5:9], byteorder='big'),
        'acknowledgement_number': int.from_bytes( packet_header[9:13], byteorder='big'),
        'data_offset': (packet_header[13] & 0xf0) *4,
        'URG': (packet_header[13] & 0x20),
        'ACK': (packet_header[13] & 0x10),
        'PSH': (packet_header[13] & 0x08),
        'RST': (packet_header[13] & 0x04),
        'SYN': (packet_header[13] & 0x02),
        'FIN': (packet_header[13] & 0x01),
        'Window': int.from_bytes( packet_header[14:16], byteorder='big'),
        'checksum': "{:#x}".format(int.from_bytes( packet_header[16:18], byteorder='big')),
        'urgent_pointer': int.from_bytes( packet_header[18:20], byteorder='big')
    }

    return header_

def parse_pcap_record( pcap_record):
#                         1                   2                   3
#       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     0 |                      Timestamp (Seconds)                      |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     4 |            Timestamp (Microseconds or nanoseconds)            |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     8 |                    Captured Packet Length                     |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    12 |                    Original Packet Length                     |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    16 /                                                               /
#       /                          Packet Data                          /
#       /                        variable length                        /
#       /                                                               /
#       +---------------------------------------------------------------+

    pcap_ = {
        'timestamp': int.from_bytes( pcap_record[0:4], byteorder='little'),
        'timestamp_msec': int.from_bytes( pcap_record[4:8], byteorder='little'),
        'captured_packet_length': int.from_bytes( pcap_record[8:12], byteorder='little'),
        'original_packet_length': int.from_bytes( pcap_record[12:16], byteorder='little')
    }

    return pcap_

if __name__ == "__main__":
    with open( "synflood.pcap", mode="rb") as read_file:
        rf = read_file.read(24) #read the first 24 bytes as pcap file header
        assert rf[0:4] == b'\xd4\xc3\xb2\xa1' #pcap file header signature, big endian

        pcap_data = read_file.read()

        syn_pkt=ack_pkt=syn_ack_pkt =0
        start_slice=end_slice =0
        while (end_slice +16) <= len(pcap_data):
            start_slice = end_slice
            end_slice += 16
            pcap_record = parse_pcap_record( pcap_data[start_slice:end_slice])

            start_slice = end_slice
            end_slice +=4
            null_loopback = pcap_data[start_slice:end_slice] #Layer 2 header, null/loopback interface
            assert null_loopback == b'\x02\x00\x00\x00', "No loopback at [{0}:{1}]".format( start_slice, end_slice)
            
            start_slice = end_slice
            end_slice +=20
            ip_header = parse_IP_header( pcap_data[start_slice:end_slice])# first IP datagram
            if(  ip_header['header_length'] > 20): #re-calculate ip header if greater than 20 bytes
                end_slice = end_slice - 20 + ip_header['header_length']
                ip_header = parse_IP_header( pcap_data[start_slice:end_slice])

            start_slice = end_slice
            end_slice += (( pcap_record['captured_packet_length'] - 4) - ip_header['header_length'])
            tcp_header = parse_TCP_header( pcap_data[start_slice:end_slice])# first TCP datagram

            if tcp_header['SYN'] and not tcp_header['ACK']:
                syn_pkt+=1
            if tcp_header['ACK'] and not tcp_header['SYN']:
                ack_pkt+=1
            if tcp_header['ACK'] and tcp_header['SYN']:
                syn_ack_pkt+=1

        print("{0:,} total TCP handshakes initiated with SYN".format( syn_pkt))
        print("{0:.2f}% of connections acknowledged by server with SYN_ACK".format( (syn_ack_pkt / syn_pkt)*100))
        print("{0:.2f}% of handshakes completed by client with ACK".format( (ack_pkt / syn_pkt)*100))