from util import generate_hacker_rank_logo

def main():
    thickness = int(input().strip())
    if thickness % 2 == 0:
        print("Thickness must be an odd number.")
        return
    logo = generate_hacker_rank_logo(thickness)
    print(logo)

if __name__ == "__main__":
    main()
