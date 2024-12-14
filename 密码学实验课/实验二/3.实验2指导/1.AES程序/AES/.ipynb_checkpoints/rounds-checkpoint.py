import time

def benchmark(iterations):
    start = time.time()
    for _ in range(iterations):
        p, c = get_meta()
        verify(p, c)
    end = time.time()
    print(f"执行{iterations}次加密，耗时: {end - start:.2f}秒")

# 测试不同次数的加密效率
benchmark(100)
benchmark(1000)
benchmark(10000)
