def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Finds a root using the Newton-Raphson method.
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:
            raise ValueError("Derivative too close to zero.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Newton-Raphson did not converge.")

if __name__ == "__main__":
    # Example function: f(x) = x^3 - 2x - 5
    f = lambda x: x**3 - 2*x - 5
    df = lambda x: 3*x**2 - 2  # Derivative
    
    x0 = 2.0  # Initial guess
    try:
        print("Newton-Raphson root:", newton_raphson(f, df, x0))
    except ValueError as e:
        print("Newton-Raphson error:", e)
