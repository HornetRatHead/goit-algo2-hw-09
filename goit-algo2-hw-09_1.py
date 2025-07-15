import random
import math

# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    solution = [random.uniform(b[0], b[1]) for b in bounds]
    value = func(solution)

    for _ in range(iterations):
        candidate = [max(min(solution[i] + random.uniform(-0.1, 0.1), bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        candidate_value = func(candidate)

        if candidate_value < value:
            if abs(value - candidate_value) < epsilon:
                break
            solution, value = candidate, candidate_value

    return solution, value

# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    solution = [random.uniform(b[0], b[1]) for b in bounds]
    value = func(solution)

    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)

        if candidate_value < value:
            if abs(value - candidate_value) < epsilon:
                break
            solution, value = candidate, candidate_value

    return solution, value

# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    solution = [random.uniform(b[0], b[1]) for b in bounds]
    value = func(solution)

    for _ in range(iterations):
        candidate = [max(min(solution[i] + random.uniform(-0.5, 0.5), bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        candidate_value = func(candidate)
        delta = candidate_value - value

        if delta < 0 or random.random() < math.exp(-delta / temp):
            if abs(value - candidate_value) < epsilon:
                break
            solution, value = candidate, candidate_value

        temp *= cooling_rate
        if temp < epsilon:
            break

    return solution, value

if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
