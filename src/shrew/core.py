import numpy as np
import numpy.typing as npt


def read_enroll_file(filename: str, levels_per_factor: list[int],
                     n_treatments: int) -> npt.NDArray[np.int_]:
    mat_shape = levels_per_factor.copy()
    mat_shape.append(n_treatments)
    mat_shape2 = tuple(mat_shape)
    enrolls = np.zeros(mat_shape2, dtype=int)

    print(f'Reading enrollment file: {filename}')
    with open(filename) as f:
        print('HEADER DATA in enrollment file:')
        print(f.readline())
        for line in f:
            enrolls[tuple(
                map(int, line.split(',')))] = enrolls[tuple(map(int, line.split(',')))] + 1
    print(f'Successfully read {enrolls.sum()} enrolled subjects')
    print()
    return enrolls
