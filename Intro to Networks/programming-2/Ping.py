from socket import *
import os
import sys
import struct
import time
import select
import binascii

'''
Referred to: 
    - James W. Kurose, Keith W. Ross - Computer Networking: A Top-Down Approach
    - Project 2 Assignment (https://shastri.info/teaching/cs3640/assignments/programming-2.pdf)
'''

def checksum(str):
    # making the checksum of our packet
    #input: string of data 
    #output: computed checksum
    str = bytearray(str)
    csum = 0
    # number of bytes in the input string that can be paired
    countTo = (len(str) // 2) * 2

    #iterateing over each pair of bytes, computing 16-bit one's complement sum
    for count in range(0, countTo, 2):
        thisVal = str[count + 1] * 256 + str[count]
        csum = csum + thisVal
        csum = csum & 0xffffffff

    #if odd number of bytes in str, last byte is added to the checksum.
    if countTo < len(str):
        csum = csum + str[-1]
        csum = csum & 0xffffffff

    #calculating final checksum value
    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer 

def receivePing(my_socket, packet_id, timeout, dest_addr):
    # receiving an ICMP packet from socket
    # extracting RTT
    timeLeft = timeout
    
    while True:
        startTime = time.time()
        ready_sockets, _, _ = select.select([my_socket], [], [], timeLeft)
        diffInCurrandStartTime = time.time() - startTime
        
        if not ready_sockets:
            return "Request timed out."
        
        time_received = time.time()
        received_data, sender_address = my_socket.recvfrom(1024)
        #extracting ICMP header
        icmp_header = received_data[20:28]
        icmpType, code, checksum, packet_id_recv, sequence = struct.unpack("bbHHh", icmp_header)
        
        if (icmpType == 0 and packet_id_recv == packet_id):
            bytes_in_double = struct.calcsize("d")
            timeSent = struct.unpack("d", received_data[28:28 + bytes_in_double])[0]
            rtt = (time_received - timeSent)
            return rtt
        
        timeLeft -= diffInCurrandStartTime
        
        if timeLeft <= 0:
            return "Request timed out."

def send_icmp_packet(socket, dest_address, packet_id):
    #representing ICMP echo request
    icmp_echo_request = 8
    dummyChecksum = 0
    current_time = time.time()

    #arguments representing ICMP header fields
    #packed binary string created from the given arguments
    header = struct.pack("bbHHh", icmp_echo_request, 0, dummyChecksum, packet_id, 1)

    #current time in binary created 
    data = struct.pack("d", current_time)
    
    #complete ICMP echo request packet = header + data variables  
    packet = header + data
    # calculating the checksum value for packet
    checksumValue = checksum(packet)

    if sys.platform == "darwin":
        #ensuring checksumValue is truncated to a 16-bit value 
        #converting the checksumValue to network byte order
        checksumValue = htons(checksumValue) & 0xffff   #macOS
    else:
        checksumValue = htons(checksumValue)    #other OS

    header = struct.pack("bbHHh", icmp_echo_request, 0, checksumValue, packet_id, 1)
    #reconstructing using updated header + original data 
    newPacket = header + data
    socket.sendto(newPacket, (dest_address, 1))

def send_one_ping(destAddr, timeout):
    # Use Internet Control Message Protocol
    protocol = getprotobyname("icmp")
    
    # Create a raw socket
    Socket = socket(AF_INET, SOCK_RAW, protocol)
    
    # Get process ID for unique identifier
    myID = os.getpid() & 0xFFFF
    
    # Send an ICMP packet to the destination address
    send_icmp_packet(Socket, destAddr, myID)
    
    # Wait for a response with a given timeout
    delay = receivePing(Socket, myID, timeout, destAddr)
    
    # Close the socket and return the delay
    Socket.close()

    return delay

def ping(host, timeout=1):
    # timeout=1 means: If one second goes by without a reply from the server,
    # the client assumes that either the client's ping or the server's pong is lost
    dest = gethostbyname(host)
    print("Pinging " + dest)
    print("")
    # Send ping requests to a server separated by approximately one second
    loop = 0
    while loop < 5 :
        delay = send_one_ping(dest, timeout)
        print(delay)
        time.sleep(1) # wait one second
        loop += 1

    return delay


print("Ping to local host")
ping("127.0.0.1") #localHost

print('-----------------------')
print("Ping to North America")
ping("www.canada.ca") #Canada

print('-----------------------')
print("Ping to South America")
ping("www.visitbrasil.com") #Brazil

print('-----------------------')
print("Ping to Asia")
ping("www.china.org.cn") #China

print('-----------------------')
print("Ping to Australia")
ping("www.australia.gov.au") #Australia

print('-----------------------')
print("Ping to Europe")
ping("urjc.es") #Madrid, Spain
