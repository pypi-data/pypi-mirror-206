"""
 * FFT Multiplication
 *
 * @author      Moin Khan
 * @copyright   Moin Khan
 *
 * @link https://mo.inkhan.dev
 *
 */
 """

import cmath


def __fft_recursive(a: list) -> list:
    """
    FFT of a given coefficients list

    :param a: list - List of input coefficients representation
    :returns list - list of output value representation
    """

    n = len(a)
    if n == 1:
        return a
    omega_n = cmath.exp(2 * cmath.pi * 1j / n)
    omega = 1
    a0 = [a[i] for i in range(0, n, 2)]
    a1 = [a[i] for i in range(1, n, 2)]
    y0 = __fft_recursive(a0)
    y1 = __fft_recursive(a1)
    y = [0] * n
    for i in range(n // 2):
        y[i] = y0[i] + omega * y1[i]
        y[i + n // 2] = y0[i] - omega * y1[i]
        omega *= omega_n
    return y


def __ifft_recursive(y: list) -> list:
    """
    Inverse FFT of a given value list

    :param y: list - List of input value representation
    :returns list - list of output coefficients representation
    """

    n = len(y)
    if n == 1:
        return y
    omega_n = cmath.exp(-2 * cmath.pi * 1j / n)
    omega = 1
    y0 = [y[i] for i in range(0, n, 2)]
    y1 = [y[i] for i in range(1, n, 2)]
    a0 = __ifft_recursive(y0)
    a1 = __ifft_recursive(y1)
    a = [0] * n
    for i in range(n // 2):
        a[i] = a0[i] + omega * a1[i]
        a[i + n // 2] = a0[i] - omega * a1[i]
        omega *= omega_n
    return a


def multiply(p: list, q: list) -> list:
    """
    Multiply two polynomial using FFT

    :param p: list - List of input value representation
    :param q: list - List of input value representation
    :returns list - Result of multiplication
    """

    n = 1
    while n < len(p) + len(q) - 1:
        n *= 2
    p += [0] * (n - len(p))
    q += [0] * (n - len(q))

    fp = __fft_recursive(p)
    fq = __fft_recursive(q)

    fr = [fp[i] * fq[i] for i in range(n)]
    r = __ifft_recursive(fr)

    result = [round(x.real) / n for x in r][:len(p) + len(q) - 1]
    return result


def direct_multiply(p: list, q: list) -> list:
    """
    Multiply two polynomial directly

    :param p: list - List of input value representation
    :param q: list - List of input value representation
    :returns list - Result of multiplication
    """

    n = 1
    while n < len(p) + len(q) - 1:
        n *= 2

    result = [0.0] * n

    for i, p_i in enumerate(p):
        for j, q_j in enumerate(q):
            result[i + j] += p_i * q_j

    return result
