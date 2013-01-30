from webiopi.utils import route
from webiopi.i2c import I2C

class PCF8574(I2C):
    def __init__(self, addr=0x20):
        I2C.__init__(self, addr, "PCF8574")
        
    @route("GET", "%(channel)d/value", "%d")
    def input(self, channel):
        mask = 1 << channel
        d = self.readByte()
        return (d & mask) == mask 

    @route("POST", "%(channel)d/value/%(value)d", "%d")
    def output(self, channel, value):
        mask = 1 << channel
        b = self.readByte()
        if value:
            b |= mask
        else:
            b &= ~mask
        self.writeBytes(b)
        return self.input(channel)  
