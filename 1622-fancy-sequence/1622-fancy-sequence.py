class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.seq = []
        self.mult = 1   # cumulative multiplier
        self.add  = 0   # cumulative addend

    # Modular inverse via Fermat's little theorem (MOD is prime)
    def _inv(self, x: int) -> int:
        return pow(x, self.MOD - 2, self.MOD)

    def append(self, val: int) -> None:
        # Store the "raw" value so that raw * mult + add ≡ val (mod MOD)
        raw = (val - self.add) * self._inv(self.mult) % self.MOD
        self.seq.append(raw)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        # Applying m to every element:  (raw*mult + add)*m = raw*(mult*m) + (add*m)
        self.mult = self.mult * m % self.MOD
        self.add  = self.add  * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)