"""
九九乘法表 - 详细注释版
适合初学者理解每一行代码的作用
"""

print("=" * 50)
print("九九乘法表")
print("=" * 50)
print()

for i in range(1, 10):
    for j in range(1, i + 1):
        result = i * j
        print(f"{j}×{i}={result}", end="\t")
    print()

print()
print("=" * 50)
print("乘法表输出完成！")
print("=" * 50)
