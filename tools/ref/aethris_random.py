#!/usr/bin/env python3
"""Referenzimplementierung von FAethrisRandom (PCG32 XSH-RR) für Tests und den Balancing-Simulator.
Ausgaben müssen bitgenau mit AethrisCore/Public/Math/AethrisRandom.h übereinstimmen."""
M64 = (1 << 64) - 1
M32 = (1 << 32) - 1

class AethrisRandom:
    def __init__(self, seed=0x853C49E6748FEA9B, stream=0xDA3E39CB94B95BDB):
        self.seed(seed, stream)

    def seed(self, seed, stream):
        self.state = 0
        self.inc = ((stream << 1) | 1) & M64
        self.next_u32()
        self.state = (self.state + seed) & M64
        self.next_u32()

    def next_u32(self):
        old = self.state
        self.state = (old * 6364136223846793005 + self.inc) & M64
        xorshifted = (((old >> 18) ^ old) >> 27) & M32
        rot = old >> 59
        return ((xorshifted >> rot) | (xorshifted << ((32 - rot) & 31))) & M32

    def next_bounded(self, bound):
        threshold = ((-bound) & M32) % bound
        while True:
            r = self.next_u32()
            if r >= threshold:
                return r % bound

    def range_inclusive(self, lo, hi):
        return lo + self.next_bounded(hi - lo + 1)

    def chance_permille(self, p):
        if p <= 0: return False
        if p >= 1000: return True
        return self.next_bounded(1000) < p

    def fork(self, sub_stream_id):
        new_seed = (self.next_u32() << 32) | self.next_u32()
        return AethrisRandom(new_seed, ((self.inc >> 1) ^ (sub_stream_id * 0x9E3779B97F4A7C15)) & M64)

if __name__ == "__main__":
    r = AethrisRandom(42, 54)
    # Bekannte PCG32-Referenzwerte für seed=42, stream=54
    print([hex(r.next_u32()) for _ in range(6)])
