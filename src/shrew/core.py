import numpy as np
import numpy.typing as npt


def read_enroll_file(filename: str, levels_per_factor: list[int],
                     n_treatments: int) -> npt.ArrayLike:
    mat_shape = levels_per_factor.copy()
    mat_shape.append(n_treatments)
    mat_shape2 = tuple(mat_shape)
    enrolls = np.zeros(mat_shape2)

    with (open(filename) as f):
        f.readline()  # HEADER DATA
        for line in f:
            enrolls[tuple(map(
                int, line.split(',')))] = enrolls[tuple(map(int, line.split(',')))] + 1

    return enrolls
