def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Finds a root using the Secant method.
    """
    for _ in range(max_iter):
        f_x0, f_x1 = f(x0), f(x1)
        if abs(f_x1 - f_x0) < 1e-12:
            raise ValueError("Denominator too small.")
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    raise ValueError("Secant method did not converge.")

if __name__ == "__main__":
    # Example function: f(x) = x^3 - 2x - 5
    f = lambda x: x**3 - 2*x - 5
    
    x1 = 1.5  # First guess
    x2 = 2.0  # Second guess
    
    try:
        print("Secant method root:", secant_method(f, x1, x2))
    except ValueError as e:
        print("Secant method error:", e)
