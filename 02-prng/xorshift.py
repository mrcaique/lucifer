class Xorshift:
    """
    Xorshift
    Is a subset of linear-feedback shift registers (LFSRs). Xorshift generate
    numbers in the sequence by repeatedly taking the exclusive or of a number
    with a bit-shifeted version of itself.

    Parameters:
        low: botton limit in the sequence;
        up: upper limit in the sequence
    """
    def __init__(self, low, up):
        self.low = low
        self.up = up

    """
    Generate the random number. The constants, or magic numbers, have to be
    choosen carefully to guarantee a long period of numbers. In this case,
    was picked these three numbers as defined in Marsaglia's paper.

    Parameters:
        seed: seed to start the generation;
        n : interval of the sequence.

    See:
        http://www.jstatsoft.org/v08/i14/paper
    """
    def generate(self, seed, n):
        for _ in range(n):
            x = seed
            x = x * self.low
            x = x^(x << 24)
            x = x^(x >> 9)
            x = x^(x << 35)
            x = x % self.up
            seed = x
        return x
