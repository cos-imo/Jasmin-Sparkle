import numpy as np

class CraxPython_t:

    def __init__(self):
        self.rcon = [0xB7E15162, 0xBF715880, 0x38B4DA56, 0x324E7738, 0xBB1185EB]
        pass

    def crax(self, x, y, key):
        self.x = np.uint32(x)
        self.y = np.uint32(y)

        for i in range(0, 10):   
            self.x = np.uint32(self.x)
            self.y = np.uint32(self.y)

            self.x ^= i 
            self.x = np.uint32(self.x)

            if ((i%2)==0):
                self.x ^= key[0]
                self.y ^= key[1]
            else:
                self.x ^= key[2]
                self.y ^= key[3]

            self.x = np.uint32(self.x)
            self.y = np.uint32(self.y)

            rcon = np.uint32(self.rcon[i%5])

            self.x, self.y = self.alzette(rcon, self.x, self.y)
        self.x ^= key[0]
        self.y ^= key[1]

        return np.uint32(self.x), np.uint32(self.y)

    def alzette(self, c, x, y):
        self.c = np.uint32(c)
        self.x = np.uint32(x)
        self.y = np.uint32(y)

        offset_1 = [31, 17, 0, 24]
        offset_2 = [24, 17, 31, 16]

        offset_1 = [np.uint32(element) for element in offset_1]
        offset_2 = [np.uint32(element) for element in offset_2]

        for i in range(0, 4):   
            self.round(offset_1[i], offset_2[i])

        return np.uint32(self.x), np.uint32(self.y)

    def round(self, offset_1, offset_2):
        self.x += self.rotate_bits(self.y, offset_1)
        self.y ^= self.rotate_bits(self.x, offset_2)
        self.x ^= self.c
        self.x = np.uint32(self.x)
        self.y = np.uint32(self.y)

    def rotate_bits(self, bits, offset):
        return np.uint32(np.uint32((bits >> offset))|np.uint32((bits << (32 - offset))) & 0xFFFFFFFF)

