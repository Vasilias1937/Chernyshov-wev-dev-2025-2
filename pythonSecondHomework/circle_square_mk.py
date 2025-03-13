import random

def circle_square_mk(r, n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            inside_circle += 1
    return (inside_circle / n) * (2 * r) ** 2

if __name__ == '__main__':
    r = 1
    n = 10000
    estimated_area = circle_square_mk(r, n)
    actual_area = 3.141592653589793
    print(f"Estimated area: {estimated_area}")
    print(f"Actual area: {actual_area}")
    print(f"Error: {abs(estimated_area - actual_area)}")
