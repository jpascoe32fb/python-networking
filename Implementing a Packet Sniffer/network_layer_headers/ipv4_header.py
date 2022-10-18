from layer_header import LayerHeader
from struct import pack, unpack
import struct
class IPv4Header(LayerHeader):
    def __init__(self, pkt):
        # TODO: Replace the value of header_length with the length of an Ethernet header
        header_length = 1
        
        # TODO: If this header can be variable length, you will need to update the contents of 
        #       self.header_bytes once you know the full length of the header in order to ensure
        #       that all of the bytes associated with this header are saved. 
        #       You can leave it as is for now.
        self.header_bytes = pkt[:header_length]

        self.version = None
        self.IHL = None #is sizeOfHeader/4 (why default is 5 when size is 20)
        self.TOS = None
        self.total_length = None
        self.identification = None
        self.flags = None
        self.fragment_offset = None
        self.TTL = None
        self.transport_protocol = None
        self.checksum = None
        self.source_addr = None
        self.dest_addr = None
        self.options_bytes = None

        # TODO: Unpack the header and assign the values to the above variables
        #self.IHL = struct.unpack("!1s", pkt[:header_length])
        self.version = int.from_bytes(self.header_bytes, "big")
        self.IHL = (self.version & 15)
        self.version = self.version >> 4

        self.TOS, self.total_length, self.identification = struct.unpack("!1x B H H", pkt[:6])
        self.fragment_offset = struct.unpack("!6x H", pkt[:8])
        self.flags = (int(self.fragment_offset[0]) & 0xE000) >> 13
        self.fragment_offset = (int(self.fragment_offset[0]) & 0x1FFF)
        self.TTL, self.transport_protocol, self.checksum = struct.unpack("!8x B B H", pkt[:12])
        self.source_addr, self.dest_addr = struct.unpack("!12x I I", pkt[:20])


        # TODO: You do not need to unpack any options, if they are present in the header. However, if options 
        #       are present, store the bytes associated with them in self.options_bytes.
        header_length = self.IHL * 4
        self.options_bytes = pkt[20:header_length]
        self.header_bytes = pkt[:header_length]

    def protocol(self):
        return "IPv4"

    def header_bytes(self):
        return self.header_bytes

    def print_header(self):
        print("")
        print("IPv4 HEADER: ")
        line_width = (96+4)

        ####################################################################
        # Print first line
        print("-"*line_width)
        
        # Compose the contents of the first row of the header
        version_str = "VERSION: " + hex(self.version)
        white_space = (16 - len(version_str))//2
        first_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        ihl_str = "IHL: " + hex(self.IHL)
        white_space = (16 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        tos_str = "TOS: " + hex(self.TOS)
        white_space = (16 - len(tos_str))//2
        first_row_str += " "*white_space + tos_str + " "*white_space + "|"

        length_str = "LENGTH: " + hex(self.total_length)
        white_space = (47 - len(length_str))//2
        first_row_str += " "*white_space + length_str + " "*white_space + "|"

        # Print the first row of the header
        print(first_row_str)
        


        ####################################################################
        # Print a line divider
        print("-"*line_width)

        # Compose the contents of the second row of the header
        version_str = "IDENT: " + hex(self.identification)
        white_space = (48 - len(version_str))//2
        second_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        tos_str = "FLAGS: " + bin(self.flags)
        white_space = (16 - len(tos_str))//2
        second_row_str += " "*white_space + tos_str + " "*white_space + "|"

        length_str = "FRAG OFFSET: " + str(self.fragment_offset)
        white_space = (32 - len(length_str))//2
        second_row_str += " "*white_space + length_str + " "*white_space + "|"

        # Print the second line of the header
        print(second_row_str)


        ####################################################################
        # Print a line divider
        print("-"*line_width)
      
        # Compose the contents of the second row of the header
        version_str = "TTL: " + str(self.TTL)
        white_space = (24 - len(version_str))//2
        third_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        tos_str = "Protocol: " + hex(self.transport_protocol)
        white_space = (24 - len(tos_str))//2
        third_row_str += " "*white_space + tos_str + " "*white_space + "|"

        length_str = "CKSUM: " + hex(self.checksum)
        white_space = (48 - len(length_str))//2
        third_row_str += " "*white_space + length_str + " "*white_space + "|"

        # Print the second line of the header
        print(third_row_str)



        ####################################################################
        # Print a line divider
        print("-"*line_width)
      
        # Compose the contents of the second row of the header
        version_str = "SOURCE ADDR: " + self.format_IPv4_addr(self.source_addr)
        white_space = (98 - len(version_str))//2
        third_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        # Print the fourth line of the header
        print(third_row_str)



        ####################################################################
        # Print a line divider
        print("-"*line_width)
      
        # Compose the contents of the second row of the header
        version_str = "DEST ADDR: " + self.format_IPv4_addr(self.dest_addr)
        white_space = (98 - len(version_str))//2
        third_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        # Print the fourth line of the header
        print(third_row_str)



        ####################################################################
        # Print a line divider
        print("-"*line_width)

        return super().print_header()