import numpy as np
import random


def main():
    print("Starting SHREW")
    print()

    random_seed = 37129472
    print(f'Using random seed {random_seed}')
    random.seed(a=random_seed)
    print()

    print("Experiment setup:")
    print("Factors(Levels): Age(<40/Y, 41-70/G, >70/O), sex(M,F), progression(1,2,3)")
    print()

    print("Treatments: Control / Intervention")
    print()

    print("Current enrollment status:")
    c = np.zeros((3, 2, 3, 2), dtype=int)
    c[0, 0, 0, 0] = 1  # YM1 c
    c[0, 0, 0, 1] = 0  # YM1 i

    c[1, 0, 0, 0] = 1  # GM1 c
    c[1, 0, 0, 1] = 3  # GM1 i

    c[2, 0, 0, 0] = 4  # OM1 c
    c[2, 0, 0, 1] = 2  # OM1 i

    c[0, 1, 0, 0] = 2  # YF1 c
    c[0, 1, 0, 1] = 1  # YF1 i

    c[1, 1, 0, 0] = 3  # GF1 c
    c[1, 1, 0, 1] = 1  # GF1 i

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

    print(f'Total: {c.sum()} subjects')
    print(f'YM1: {c[0, 0, 0, 0]}/{c[0, 0, 0, 1]} ; YM2: {c[0, 0, 1, 0]}/{c[0, 0, 1, 1]} ; '
          f'YM3: {c[0, 0, 2, 0]}/{c[0, 0, 2, 1]}')
    print(f'YF1: {c[0, 1, 0, 0]}/{c[0, 1, 0, 1]} ; YF2: {c[0, 1, 1, 0]}/{c[0, 1, 1, 1]} ; '
          f'YF3: {c[0, 1, 2, 0]}/{c[0, 1, 2, 1]}')
    print(f'GM1: {c[1, 0, 0, 0]}/{c[1, 0, 0, 1]} ; GM2: {c[1, 0, 1, 0]}/{c[1, 0, 1, 1]} ; '
          f'GM3: {c[1, 0, 2, 0]}/{c[1, 0, 2, 1]}')
    print(f'GF1: {c[1, 1, 0, 0]}/{c[1, 1, 0, 1]} ; GF2: {c[1, 1, 1, 0]}/{c[1, 1, 1, 1]} ; '
          f'GF3: {c[1, 1, 2, 0]}/{c[1, 1, 2, 1]}')
    print(f'OM1: {c[2, 0, 0, 0]}/{c[2, 0, 0, 1]} ; OM2: {c[2, 0, 1, 0]}/{c[2, 0, 1, 1]} ; '
          f'OM3: {c[2, 0, 2, 0]}/{c[2, 0, 2, 1]}')
    print(f'OF1: {c[2, 1, 0, 0]}/{c[2, 1, 0, 1]} ; OF2: {c[2, 1, 1, 0]}/{c[2, 1, 1, 1]} ; '
          f'OF3: {c[2, 1, 2, 0]}/{c[2, 1, 2, 1]}')
    print()

    p_imb = 0.8
    print("Randomisation procedure: ")
    print(" - Deviation measure:   range")
    print(" - Factor weights:      unit")
    print(f' - Probability:         {p_imb}')
    print()

    print("New subject: GM1")
    f = (1, 0, 0)
    print(f'Subjects in levels "GM1": Control: {c[1, 0, 0, 0]} vs Intervention: {c[1, 0, 0, 1]}')

    n00 = c.sum(axis=(1, 2))[f[0], 0]
    n01 = c.sum(axis=(1, 2))[f[0], 1]
    print(f'Subjects in level "G": Control: {n00} vs Intervention: {n01}')

    n10 = c.sum(axis=(0, 2))[f[1], 0]
    n11 = c.sum(axis=(0, 2))[f[1], 1]
    print(f'Subjects in level "M": Control: {n10} vs Intervention: {n11}')

    n20 = c.sum(axis=(0, 1))[f[2], 0]
    n21 = c.sum(axis=(0, 1))[f[2], 1]
    print(f'Subjects in level "1": Control: {n20} vs Intervention: {n21}')
    print()

    g0 = abs((n00 + 1) - n01) + abs((n10 + 1) - n11) + abs((n20 + 1) - n21)
    g1 = abs(n00 - (n01 + 1)) + abs(n10 - (n11 + 1)) + abs(n20 - (n21 + 1))
    print(f'Imbalance function if subject goes in control:      G0 = {g0}')
    print(f'Imbalance function if subject goes in intervention: G1 = {g1}')
    print()

    print("Randomising new subject:")
    if g0 == g1:
        p_control = 0.5
        print("Equal imbalance: p(control)=0.5.")
    if g0 < g1:
        p_control = p_imb
        print(f'Control has least imbalance: p(control)={p_control}.')
    else:
        p_control = 1.0 - p_imb
        print(f'Intervention has least imbalance: p(control)={p_control}.')

    random_number = random.random()  # random number in [0, 1)
    print(f'Random number: {random_number}')
    if random_number < p_control:
        # group = 0  # control
        print("Enrollment in CONTROL")
    else:
        # group = 1  # intervention
        print("Enrollment in INTERVENTION")

    print()
    print("SHREW has completed")


if __name__ == "__main__":
    main()
