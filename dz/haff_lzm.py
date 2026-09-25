import zlib, bz2, random

def good_set(n=10000):  return b'Z' * (n - 100) + b'W' * 100
def bad_set(n=10000):   return bytes(i % 256 for i in range(n)) # плохой только для lzw, для Хаффмана убрать надо переодичность (перемешать) 
def rand_set(n=10000):  return bytes(random.randint(0, 255) for _ in range(n))

def test(name, data):
    z = len(zlib.compress(data, 9))
    b = len(bz2.compress(data, 9))
    print(f"{name:<25} было={len(data):>6}  zlib={z:>6} ({z/len(data):.2f})  bz2={b:>6} ({b/len(data):.2f})")

print(f"{'Данные':<25} {'Было':>10}  {'zlib':>15}  {'bz2':>15}")
print('-' * 70)
test('Два символа ', good_set())
test('Равномерно 0..255 ', bad_set())
test('Случайные байты ', rand_set())
