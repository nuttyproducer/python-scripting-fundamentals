"""meme-generator — bouw een ASCII-meme."""


def meme(boven, onder, breedte=32):
    boven = boven.upper()
    onder = onder.upper()
    rand = "=" * breedte

    print(rand)
    print(boven.center(breedte))
    print()
    print("(  :D  )".center(breedte))
    print()
    print(onder.center(breedte))
    print(rand)


def main():
    boven = input("Boven-tekst: ")
    onder = input("Onder-tekst: ")
    meme(boven, onder)


if __name__ == "__main__":
    main()
