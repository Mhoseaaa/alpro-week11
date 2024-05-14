def cek_tuple_sama(t):
    return all(x == t[0] for x in t)

tA = tuple(map(int, input("Masukkan tuple: ").split()))
result = cek_tuple_sama(tA)
print(result)