import numpy as np


def main():
    print("Starting SHREW")
    print()
    print()

    print("Experiment setup:")
    print("Factors(Levels): Age(<40/Y, 41-70/G, >70/O), sex(M,F), progression(1,2,3)")
    print()

    print("Treatments: Control / Intervention")
    print()

    print("Current enrollment status:")
    print("Total: 51 subjects")
    print("YM1: 1/0 ; YM2: 0/0 ; YM3: 0/0")
    print("YF1: 2/1 ; YF2: 2/1 ; YF3: 0/1")
    print("GM1: 1/2 ; GM2: 0/1 ; GM3: 0/2")
    print("GF1: 4/2 ; GF2: 3/3 ; GF3: 2/0")
    print("OM1: 5/2 ; OM2: 3/1 ; OM3: 0/3")
    print("OF1: 2/1 ; OF2: 1/2 ; OF3: 0/3")
    c = np.zeros((3, 2, 3, 2))
    c[0, 0, 0, 0] = 1  # YM1 c
    c[0, 0, 0, 1] = 0  # YM1 i

    c[1, 0, 0, 0] = 1  # GM1 c
    c[1, 0, 0, 1] = 2  # GM1 i

    c[2, 0, 0, 0] = 5  # OM1 c
    c[2, 0, 0, 1] = 2  # OM1 i

    c[0, 1, 0, 0] = 2  # YF1 c
    c[0, 1, 0, 1] = 1  # YF1 i

    c[1, 1, 0, 0] = 4  # GF1 c
    c[1, 1, 0, 1] = 2  # GF1 i

    c[2, 1, 0, 0] = 2  # OF1 c
    c[2, 1, 0, 1] = 1  # OF1 i

    c[0, 0, 1, 0] = 0  # YM2 c
    c[0, 0, 1, 1] = 0  # YM2 i

    c[1, 0, 1, 0] = 0  # GM2 c
    c[1, 0, 1, 1] = 1  # GM2 i

    c[2, 0, 1, 0] = 3  # OM2 c
    c[2, 0, 1, 1] = 1  # OM2 i

    c[0, 1, 1, 0] = 2  # YF2 c
    c[0, 1, 1, 1] = 1  # YF2 i

    c[1, 1, 1, 0] = 3  # GF2 c
    c[1, 1, 1, 1] = 3  # GF2 i

    c[2, 1, 1, 0] = 1  # OF2 c
    c[2, 1, 1, 1] = 2  # OF2 i

    c[0, 0, 2, 0] = 0  # YM3 c
    c[0, 0, 2, 1] = 0  # YM3 i

    c[1, 0, 2, 0] = 0  # GM3 c
    c[1, 0, 2, 1] = 2  # GM3 i

    c[2, 0, 2, 0] = 0  # OM3 c
    c[2, 0, 2, 1] = 3  # OM3 i

    c[0, 1, 2, 0] = 0  # YF3 c
    c[0, 1, 2, 1] = 1  # YF3 i

    c[1, 1, 2, 0] = 2  # GF3 c
    c[1, 1, 2, 1] = 0  # GF3 i

    c[2, 1, 2, 0] = 0  # OF3 c
    c[2, 1, 2, 1] = 3  # OF3 i
    print()

    print("Randomisation procedure: ")
    print(" - Deviation measure:   range")
    print(" - Factor weights:      unit")
    print(" - Probability:         0.8/0.2")
    print()

    print("New subject: GM1")
    f = (1, 0, 0)

    n00 = c.sum(axis=(1, 2))[f[0], 0]
    n01 = c.sum(axis=(1, 2))[f[0], 1]

    n10 = c.sum(axis=(0, 2))[f[1], 0]
    n11 = c.sum(axis=(0, 2))[f[1], 1]

    n20 = c.sum(axis=(0, 1))[f[2], 0]
    n21 = c.sum(axis=(0, 1))[f[2], 1]
    print()

    g0 = abs((n00 + 1) - n01) + abs((n10 + 1) - n11) + abs((n20 + 1) - n21)
    g1 = abs(n00 - (n01 + 1)) + abs(n10 - (n11 + 1)) + abs(n20 - (n21 + 1))

    print(g0)
    print(g1)


if __name__ == "__main__":
    main()
