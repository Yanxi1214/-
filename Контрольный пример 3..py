def f3_system(t, x, y, z):
    dx_dt = -2*x + 5*z
    dy_dt = math.sin(t-1)*x - y + 3*z
    dz_dt = -x + 2*z
    return dx_dt, dy_dt, dz_dt

def solve_system_euler(f, t0, x0, y0, z0, a, b, n):
    h = (b - a) / n
    t_values = [t0]
    x_values = [x0]
    y_values = [y0]
    z_values = [z0]
    
    t = t0
    x = x0
    y = y0
    z = z0
    
    for i in range(n):
        dx, dy, dz = f(t, x, y, z)
        x = x + h * dx
        y = y + h * dy
        z = z + h * dz
        t = t + h
        
        t_values.append(t)
        x_values.append(x)
        y_values.append(y)
        z_values.append(z)
    
    return t_values, x_values, y_values, z_values

# Параметры
a, b = 0, 0.3
t0, x0, y0, z0 = 0, 2, 1, 1
n = 100  # h = 0.003

# Решение
t_vals, x_vals, y_vals, z_vals = solve_system_euler(f3_system, t0, x0, y0, z0, a, b, n)

# Вывод первых 10 точек
print("Система ДУ - Метод Эйлера (первые 10 точек):")
print("t\t\tx\t\ty\t\tz")
for i in range(0, min(11, len(t_vals)), 10):
    print(f"{t_vals[i]:.3f}\t\t{x_vals[i]:.6f}\t{y_vals[i]:.6f}\t{z_vals[i]:.6f}")
