import shrew
import random
import os


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

    # Load enrollments
    c = shrew.read_enroll_file(os.path.join('test', 'enroll2.txt'), [2, 2], 2)

    print(f'00: {c[0, 0, 0]}/{c[0, 0, 1]}')
    print(f'01: {c[0, 1, 0]}/{c[0, 1, 1]}')
    print(f'10: {c[1, 0, 0]}/{c[1, 0, 1]}')
    print(f'11: {c[1, 1, 0]}/{c[1, 1, 1]}')
    print()

    p_imb = 0.8
    print("Randomisation procedure: ")
    print(" - Deviation measure:   range")
    print(" - Factor weights:      unit")
    print(f' - Probability:         {p_imb}')
    print()

    print("New subject: 10")
    f = (1, 0)
    print(f'Subjects in levels "10": Control: {c[1, 0, 0]} vs Intervention: {c[1, 0, 1]}')

    n00 = c.sum(axis=1)[f[0], 0]
    n01 = c.sum(axis=1)[f[0], 1]
    print(f'Subjects in factor 0 Level 0: Control: {n00} vs Intervention: {n01}')

    n10 = c.sum(axis=0)[f[1], 0]
    n11 = c.sum(axis=0)[f[1], 1]
    print(f'Subjects in factor 1 level 0: Control: {n10} vs Intervention: {n11}')
    print()

    g0 = abs((n00 + 1) - n01) + abs((n10 + 1) - n11)
    g1 = abs(n00 - (n01 + 1)) + abs(n10 - (n11 + 1))
    print(f'Imbalance function if subject goes in control:      G0 = {g0}')
    print(f'Imbalance function if subject goes in intervention: G1 = {g1}')
    print()

    print("Randomising new subject:")
    if g0 == g1:
        p_control = 0.5
        print("Equal imbalance: p(control)=0.5.")
    elif g0 < g1:
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
