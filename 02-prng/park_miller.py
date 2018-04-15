from lcg import LCG

class Park_miller(LCG):
    """
    Park-Miller Number Generator
    Is a linear congruential generator (LCG) that operates in multiplicative
    group of integers modulo n, the general formula is:
        x_{k+1} = g * x{k} (mod n)
    Where:
        n: a prime number or a power of a prime number;
        g: is a element of a higher multiplicative order modulo n;
        x_{0}: seed and is coprime to n.

    In other words, a PMNG is a LCG where c = 0.
    """
    def __init__(self, g, n):
        super().__init__(g, 0, n)

    """
    Generates the random number.

    Parameters:
        seed: Seed to start the generation;
        n: interval of the sequence.
    """
    def generate(self, seed, n):
         return super().generate(seed, n)
