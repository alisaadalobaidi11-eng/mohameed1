import secrets
import string

SPECIAL = "!@#$%^&*_-"
ALPHABET = string.ascii_letters + string.digits + SPECIAL

def generate_password(length=14):
    while True:
        pw = ''.join(secrets.choice(ALPHABET) for _ in range(length))
        if (
            any(c.islower() for c in pw) and
            any(c.isupper() for c in pw) and
            any(c.isdigit() for c in pw) and
            any(c in SPECIAL for c in pw)
        ):
            return pw

def main():
    passwords = set()
    target = 100_000

    while len(passwords) < target:
        passwords.add(generate_password())

    with open("passwords.txt", "w", encoding="utf-8") as f:
        for pw in sorted(passwords):
            f.write(pw + "\n")

    print("Done: 100000 strong unique passwords saved to passwords.txt")

if __name__ == "__main__":
    main()
