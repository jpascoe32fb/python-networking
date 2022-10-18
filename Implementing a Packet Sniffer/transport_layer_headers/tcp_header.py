from layer_header import LayerHeader
from struct import pack, unpack
import struct
class TCPHeader(LayerHeader):
    def __init__(self, pkt):
        # TODO: Replace the value of header_length with the length of an Ethernet header
        header_length = 20
        
        # TODO: If this header can be variable length, you will need to update the contents of 
        #       self.header_bytes once you know the full length of the header in order to ensure
        #       that all of the bytes associated with this header are saved. 
        #       You can leave it as is for now.
        self.header_bytes = pkt[:header_length]

        self.source_port = None
        self.dest_port = None
        self.SEQ = None
        self.ACK = None
        self.data_offset = None
        self.NS_flag = None
        self.CWR_flag = None
        self.ECE_flag = None
        self.URG_flag = None
        self.ACK_flag = None
        self.PSH_flag = None
        self.RST_flag = None
        self.SYN_flag = None
        self.FIN_flag = None
        self.window_size = None
        self.checksum = None
        self.urg_pointer = None
        self.options_bytes = None

        # TODO: Unpack the header and assign the values to the above variables
        self.source_port, self.dest_port, self.SEQ = struct.unpack("!H H I", pkt[:8])
        self.ACK, self.NS_flag, self.FIN_flag = struct.unpack("!8x I 1s 1s", pkt[:14])
        print(self.NS_flag)
        self.data_offset = (int(self.NS_flag[0]) & 0xF0) >> 4
        self.NS_flag = (int(self.NS_flag[0]) & 0x01)
        self.CWR_flag = (int(self.FIN_flag[0]) & 0x80)
        self.ECE_flag = (int(self.FIN_flag[0]) & 0x40)
        self.URG_flag = (int(self.FIN_flag[0]) & 0x20)
        self.ACK_flag = (int(self.FIN_flag[0]) & 0x10)
        self.PSH_flag = (int(self.FIN_flag[0]) & 0x08)
        self.RST_flag = (int(self.FIN_flag[0]) & 0x04)
        self.SYN_flag = (int(self.FIN_flag[0]) & 0x02)
        self.FIN_flag = (int(self.FIN_flag[0]) & 0x01)
        self.window_size, self.checksum, self.urg_pointer = struct.unpack("!14x H H H", pkt[:header_length])
        # TODO: You do not need to unpack any options, if they are present in the header. However, if options 
        #       are present, store the bytes associated with them in self.options_bytes.
        header_length = self.data_offset * 4
        self.options_bytes = pkt[20:header_length]
        self.header_bytes = pkt[:header_length]

    def protocol(self):
        return "TCP"

    def header_bytes(self):
        return self.header_bytes

    def print_header(self):
        print("")
        print("TCP HEADER: ")
        line_width = (96+4)

        ####################################################################
        # Print first line
        print("-"*line_width)
        
        # Compose the contents of the first row of the header
        version_str = "SOURCE PORT: " + str(self.source_port)
        white_space = (48 - len(version_str))//2
        first_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        ihl_str = "DEST PORT: " + str(self.dest_port)
        white_space = (48 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        # Print the first row of the header
        print(first_row_str)
        


        ####################################################################
        # Print first line
        print("-"*line_width)
        
        # Compose the contents of the first row of the header
        version_str = "SEQ NUMBER: " + str(self.SEQ)
        white_space = (96 - len(version_str))//2
        first_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        # Print the first row of the header
        print(first_row_str)


        ####################################################################
        # Print first line
        print("-"*line_width)
        
        # Compose the contents of the first row of the header
        version_str = "ACK NUMBER: " + str(self.ACK)
        white_space = (96 - len(version_str))//2
        first_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        # Print the first row of the header
        print(first_row_str)


        ####################################################################
        # Print first line
        print("-"*line_width)
        
        # Compose the contents of the first row of the header
        version_str = "OFFSET: " + str(self.data_offset)
        white_space = (16 - len(version_str))//2
        first_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        ihl_str = "  ---  |"
        first_row_str += ihl_str

        ihl_str = "NS:" + ("1" if self.NS_flag else "0")
        white_space = (5 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        ihl_str = "CWR:" + ("1" if self.CWR_flag else "0")
        white_space = (5 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        ihl_str = "ECE:" + ("1" if self.ECE_flag else "0")
        white_space = (5 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        ihl_str = "URG:" + ("1" if self.URG_flag else "0")
        white_space = (5 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        ihl_str = "ACK:" + ("1" if self.ACK_flag else "0")
        white_space = (5 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        ihl_str = "PSH:" + ("1" if self.PSH_flag else "0")
        white_space = (5 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        ihl_str = "RST:" + ("1" if self.RST_flag else "0")
        white_space = (5 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        ihl_str = "SYN:" + ("1" if self.SYN_flag else "0")
        white_space = (5 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        ihl_str = "FIN:" + ("1" if self.FIN_flag else "0")
        white_space = (5 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        ihl_str = "WIN:" + str(self.window_size)
        white_space = (20 - len(ihl_str))//2
        first_row_str += " "*white_space + ihl_str + " "*white_space + "|"

        # Print the first row of the header
        print(first_row_str)



        ####################################################################
        # Print first line
        print("-"*line_width)
        
        # Compose the contents of the first row of the header
        version_str = "CHECKSUM: " + str(self.checksum)
        white_space = (48 - len(version_str))//2
        first_row_str = "|" + " "*white_space + version_str + " "*white_space + "|"

        # Compose the contents of the first row of the header
        version_str = "URG POINTER: " + str(self.urg_pointer)
        white_space = (48 - len(version_str))//2
        first_row_str += " "*white_space + version_str + " "*white_space + "|"

        # Print the first row of the header
        print(first_row_str)

        ####################################################################
        # Print a line divider
        print("-"*line_width)

        return super().print_header()