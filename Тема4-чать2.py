def sqrt_iterative(x, y0, tol=1e-10, max_iter=1000):
    """
    计算 sqrt(x) 的迭代方法：y_{i+1} = 0.5 * (y_i + x / y_i)
    """
    y = y0
    for i in range(max_iter):
        y_next = 0.5 * (y + x / y)
        if abs(y_next - y) < tol:
            break
        y = y_next
    return y, i + 1

def inv_sqrt_iterative(x, y0, tol=1e-10, max_iter=1000):
    """
    计算 1 / sqrt(x) 的迭代方法：y_{i+1} = y_i * (3 - x * y_i^2) / 2
    """
    y = y0
    for i in range(max_iter):
        y_next = y * (3 - x * y**2) / 2
        if abs(y_next - y) < tol:
            break
        y = y_next
    return y, i + 1

# 计算 sqrt(x)
print("1. 计算 sqrt(x)")
print("-" * 40)

x1 = 14.76
y0_1 = 3.8
result1, iter1 = sqrt_iterative(x1, y0_1)
print(f"x = {x1}, y0 = {y0_1}")
print(f"sqrt({x1}) ≈ {result1:.10f}, 迭代次数: {iter1}")
print(f"验证: {result1**2:.10f}")

print()

x2 = 0.142
y0_2 = 0.4
result2, iter2 = sqrt_iterative(x2, y0_2)
print(f"x = {x2}, y0 = {y0_2}")
print(f"sqrt({x2}) ≈ {result2:.10f}, 迭代次数: {iter2}")
print(f"验证: {result2**2:.10f}")

print("\n" + "="*60 + "\n")

# 计算 1 / sqrt(x)
print("2. 计算 1 / sqrt(x)")
print("-" * 40)

x3 = 17.32
y0_3 = 0.24
result3, iter3 = inv_sqrt_iterative(x3, y0_3)
print(f"x = {x3}, y0 = {y0_3}")
print(f"1/sqrt({x3}) ≈ {result3:.10f}, 迭代次数: {iter3}")
print(f"验证: {1/(result3**2):.10f} ≈ {x3}")

print()

x4 = 0.464
y0_4 = 1.5
result4, iter4 = inv_sqrt_iterative(x4, y0_4)
print(f"x = {x4}, y0 = {y0_4}")
print(f"1/sqrt({x4}) ≈ {result4:.10f}, 迭代次数: {iter4}")
print(f"验证: {1/(result4**2):.10f} ≈ {x4}")
