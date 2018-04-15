class LCG:
    """
    Linear Congruential Generator (LCG)
    LCG is a very simple pseudo-random number generator, all LCGs use the
    following formula:
        r_{n+1} = a * r_{n} + c (mod m)
    Where:
        * r_{0} is a seed;
        * r_{1}, r_{2}, r_{3}, ..., are the random numbers;
        * a, c and m are constants.
    According to a m value, the generator goes to numbers from size of 1 to
    m bits.
    """
    def __init__(self, a, c, power):
        """
        Initialize LCG with the parameters:
            a: constant;
            c: constant;
            power: defines what power of two will be the modulus;
        """
        self.a = a
        self.c = c
        self.modulus = power

    def generate(self, seed, n):
        """
        Generates a random number as specified in LCG formula.

        Parameter:
            seed: Seed to start the generation;
            n: interval of the sequence 

        Returns:
            A random number with 'modulus' bits
        """
        for _ in range(n):
            result = (self.a * seed + self.c) % self.modulus
            seed = result
        return result
