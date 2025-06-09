from srs.merge_the_tools.util import merge_the_tools

if __name__ == "__main__":
    s = input().strip()
    k = int(input())
    result = merge_the_tools(s, k)
    for part in result:
        print(part)
