import numpy as np

from ape.optimization import NaiveEvolutionStrategy


def test_convergence_quadratic():
    def quadratic(x):
        return x[0]**2 + x[1]**2

    limit = np.array([1, 1])
    mean = np.random.uniform(-limit, limit)
    cov = np.identity(2)
    mu = 12
    size = mu//2
    iterations = 100
    tol = 1e-12

    es = NaiveEvolutionStrategy(mu, size, 2, mean, cov)
    es.optimize(func=quadratic, iterations=iterations)
    mean, _ = es.estimate()

    assert np.linalg.norm(mean) < tol
