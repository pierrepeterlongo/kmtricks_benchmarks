"""Given an estimated kmer count provided
by ntcard*
Provide a threshold t >=1 being the smallest value such that
the number of canonical kmers occurring t times is smaller
than X% of the total number of canonical kmers F0

* example:
    F1      38532109434
    F0      8573134738
    1       5471333409
    2       1482413356
    3       419175858
    4       236675241
F1 is the total number of kmers (of positions where a kmer occurs)
F0 is the number of distinct canonical kmers
1 is the number of distinct canonical kmers seen once
2 is the number of distinct canonical kmers seen twice
...

"""
import sys
import logging


def determine_t(ntcard_file_name: str, X: float) -> int:
    """Compute and returns t


    Given an estimated kmer count provided
    a ntcard file, provide a threshold t >=1 being the smallest value such that
    the number of canonical kmers occurring t times is smaller
    than X% of the total number of canonical kmers F0


    Args:
        ntcard_file_name (str): file name containing the kmer count
        X (int): percentage X value ([0-100])

    Returns:
        int: t
    """
    with open(ntcard_file_name) as ntcard_file:
        _ = ntcard_file.readline()  # F1 value, unused
        F0 = int(ntcard_file.readline().strip().split()[-1])
        threshold = F0*X/float(100)
        logging.info(f"{X}% of {F0} is {threshold}")
        while True:
            line = ntcard_file.readline()
            if not line:
                raise ValueError(f"Cannot provide t given ntcard file\
                                 {ntcard_file_name}, and X value {X}%")
            line = line.strip().split()
            multiplicity = int(line[0])
            nb_kmers = int(line[1])
            if nb_kmers <= threshold:
                logging.info(f"{multiplicity}, with {nb_kmers} kmers, is the answer")
                return multiplicity


if __name__ == "__main__":
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        logging.error(f"Usage: python {sys.argv[0]} ntcard_file_name X verbose")
        logging.error("\
                Given an estimated kmer count provided\n\
                by ntcard*\n\
                Provide a threshold t >=1 being the smallest value such that\n\
                the number of canonical kmers occurring t times is smaller\n\
                than X% of the total number of canonical kmers F0\n\
            \n\
                * example:\n\
                    F1      38532109434\n\
                    F0      8573134738\n\
                    1       5471333409\n\
                    2       1482413356\n\
                    3       419175858\n\
                    4       236675241\n\
                F1 is the total number of kmers (of positions where a kmer occurs)\n\
                F0 is the number of distinct canonical kmers\n\
                1 is the number of distinct canonical kmers seen once\n\
                2 is the number of distinct canonical kmers seen twice\n\
                ...")
        exit(1)
    verbose = False
    if len(sys.argv) == 4 and sys.argv[-1] == "verbose":
        verbose = True

    if verbose:
        logging.basicConfig(format="%(levelname)s: %(message)s",
                            level=logging.DEBUG)
        logging.info("Verbose output.")
    else:
        logging.basicConfig(format="%(levelname)s: %(message)s")

    print(f"{determine_t(sys.argv[1], float(sys.argv[2]))}")
