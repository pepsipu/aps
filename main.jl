# using Polynomials
using Plots
using Distributed

println("goin")

# Add all available workers
addprocs(Sys.CPU_THREADS - 1)

@everywhere using PolynomialRoots
@everywhere using DistributedArrays

# Define a range of values for c
c_vals = range(-5, 5, length=10)

# Initialize the plot
p = plot(size=(800, 600), xlabel="Real Part", ylabel="Imaginary Part", xlims=(-5, 5), ylims=(-5, 5))

# Compute the roots for the entire range of c values in parallel
@sync @distributed for c in c_vals
    # Compute the roots for the current value of c
    roots_vals = roots([c, 0, -1, 2])
    print(roots_vals)
end

