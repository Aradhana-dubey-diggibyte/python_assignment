from srs.mutations.util import mutate_string

if __name__ == "__main__":
    string = input().strip()
    position, character = input().strip().split()
    position = int(position)
    result = mutate_string(string, position, character)
    print(result)
