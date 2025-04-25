def tri_rec(k):
    if k > 0:
        result = k + tri_rec(k - 1)
        print(result)
    Else:
        result = 0
    return result

print("\n\n Example Results")
tri_rec(6)