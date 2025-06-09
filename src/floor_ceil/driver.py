from srs.floor_ceil.util import apply_floor_ceil_rint

if __name__ == "__main__":
    arr = list(map(float, input().split()))
    floor_vals, ceil_vals, rint_vals = apply_floor_ceil_rint(arr)
    print(floor_vals)
    print(ceil_vals)
    print(rint_vals)
