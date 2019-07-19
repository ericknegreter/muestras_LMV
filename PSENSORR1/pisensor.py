import struct
import smbus2
import time

bus = smbus2.SMBus(1)

address = 0x29

def get_data():
    return bus.read_i2c_block_data(address, 0, 8);

def get_float(data, index):
    bytes = data[4*index:(index+1)*4]
    return struct.unpack('f', bytes)

while True:
    time.sleep(1);
    data = get_data()
    print(get_float(data, 0))
    print(get_float(data, 1))
