import numpy as np
import matplotlib.pyplot as plt


base = [5, 2, 3, 4, -2, -1, 0, -3, 1]
actor = [2, 3, 1, -2, 5, -1, 2]

# Define the function to compute the roots
def compute_roots(c):
    # Compute the roots of the polynomial for the given value of c
    # p = np.poly1d(base) * np.poly1d(actor) * c
    p = np.poly1d(base) + c * np.poly1d(actor)
    roots = p.roots
    # Sort the roots by their real part
    roots = sorted(roots, key=lambda x: x.real)
    # Return the real and imaginary parts of the roots as a tuple
    return [(r.real, r.imag) for r in roots]


def poly(p, var_string="x"):
    res = ""
    first_pow = len(p) - 1
    for i, coef in enumerate(p):
        power = first_pow - i

        if coef:
            if coef < 0:
                sign, coef = (" - " if res else "- "), -coef
            elif coef > 0:  # must be true
                sign = " + " if res else ""

            str_coef = "" if coef == 1 and power != 0 else str(coef)

            if power == 0:
                str_power = ""
            elif power == 1:
                str_power = var_string
            else:
                str_power = var_string + "^" + str(power)

            res += sign + str_coef + str_power
    return res


# Define the range of c values to compute roots for
c_vals = np.linspace(-100, 100, 40000)

# Compute the roots for each value of c
results = []
for c in c_vals:
    results.append(compute_roots(c))

# Transpose the results array so that we can plot each root separately
results = np.transpose(results, (1, 0, 2))

# Create a 3D plot of the roots as a function of c
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
for i in range(len(results)):
    ax.plot(
        c_vals,
        [results[i][j][0] for j in range(len(results[i]))],
        [results[i][j][1] for j in range(len(results[i]))],
        alpha=0.7,
        linewidth=2,
    )
ax.set_xlim(-10, 10)
ax.set_ylim(-6, 6)
ax.set_zlim(-6, 6)
ax.set_xlabel("Actor Strength (c)")
ax.set_ylabel("Real part of roots")
ax.set_zlabel("Imaginary part of roots")
# title the graph based on the actor and base polynomial, converting the array to a polynomial
ax.set_title(f"Root Bus of Base ({poly(base)}) and Actor ({poly(actor)})")

plt.show()
