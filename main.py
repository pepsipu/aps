import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from multiprocessing import Pool

# Define the polynomial as a function of c

# Define a range of values for c
c_vals = np.linspace(-5000, 5000, 500000)

# Compute the roots for the entire range of c values in parallel
def compute_roots(c):
    # Compute the roots for the current value of c
    roots_vals = Polynomial([c, 4 + c, 3 + c, -4, 3, 1, -1, 2]).roots()

    # Return the roots as a tuple with the current value of c
    return (c, roots_vals)


if __name__ == "__main__":
    with Pool() as pool:
        root_trajectories = pool.map(compute_roots, c_vals)

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set(xlabel="Real Part", ylabel="Imaginary Part", xlim=(-5, 5), ylim=(-5, 5))

    # Plot the root trajectories
    for i in range(len(root_trajectories[0][1])):
        x = [np.real(root_trajectories[j][1][i]) for j in range(len(root_trajectories))]
        y = [np.imag(root_trajectories[j][1][i]) for j in range(len(root_trajectories))]
        ax.plot(
            x,
            y,
            color=["blue", "red", "green", "orange", "purple"][i % 5],
        )

    # Set the title to the current value of c
    ax.set_title("roots as c varies")

    # Save the plot to the local directory
    plt.savefig("root_curve.png")
