import random

# Objective function
def f(x):
    return -x**2 + 10*x

# Hill climbing algorithm
def hill_climb(start, step_size=0.1, max_iterations=1000):
    current_x = start
    current_value = f(current_x)

    for _ in range(max_iterations):
        # Check neighbors
        neighbors = [current_x + step_size, current_x - step_size]
        neighbor_values = [f(x) for x in neighbors]

        # Find best neighbor
        best_value = max(neighbor_values)
        best_neighbor = neighbors[neighbor_values.index(best_value)]

        # Move if better
        if best_value > current_value:
            current_x = best_neighbor
            current_value = best_value
        else:
            break  # Stop if no improvement

    return current_x, current_value

# Run the algorithm
start = random.uniform(0, 10)
best_x, best_value = hill_climb(start)

print(f"Starting at x = {start:.2f}")
print(f"Best solution: x = {best_x:.2f}, f(x) = {best_value:.2f}")
