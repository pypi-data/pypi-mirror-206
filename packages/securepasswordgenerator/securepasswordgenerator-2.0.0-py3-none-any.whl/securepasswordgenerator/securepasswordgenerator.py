#!/usr/bin/env python
"""
MIT License

Copyright (c) 2023-present Ali Fayaz (Quill) (quillfires)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import secrets
import string


def generate_password(length=8, use_lower_case=True, use_upper_case=True, use_numbers=True, use_special=True, use_hex=False):
    characters = []
    if use_lower_case:
        characters.extend(string.ascii_lowercase)
    if use_upper_case:
        characters.extend(string.ascii_uppercase)
    if use_numbers:
        characters.extend(string.digits)
    if use_special:
        characters.extend(string.punctuation)
    if use_hex:
        characters.extend("123456789ABCDEF")
    return "".join(secrets.choice(characters) for _ in range(length))


def generate(length=8, use_lower_case=True, use_upper_case=True, use_numbers=True, use_special=True, use_hex=False):
    """
    Generate Normal Passwords - 8 characters that includes atleast 1 uppercase, 1 lower case, 1 special character and 1 number.
    """
    password = ""
    if length > 1000:
        print("ERROR: Requested password length is too large, please choose a reasonable value.")
        return
    if length > 4:
        while not password_checker(password, string.ascii_lowercase if use_lower_case else password) \
                or not password_checker(password, string.ascii_uppercase if use_upper_case else password) \
                or not password_checker(password, string.digits if use_numbers else password) \
                or not password_checker(password, string.punctuation if use_special else password) \
                or not password_checker(password, "123456789ABCDEF" if use_hex else password):
            password = generate_password(length, use_lower_case, use_upper_case, use_numbers, use_special, use_hex)
    else:
        password = generate_password(length, use_lower_case, use_upper_case, use_numbers, use_special, use_hex)

    return password


def decent():
    """
    Generate Memorable Passwords - Perfect for securing your computer or mobile device, or somewhere brute force is detectable.
    """
    password = generate_password(10, True, True, True, False, False)
    return password


def strong():
    """
    Generate Strong Passwords - Robust enough to keep your web hosting account secure.
    """
    password = generate_password(15, True, True, True, True, False)
    return password


def fort_knox():
    """
    Generate Fort Knox Passwords - Secure enough for almost anything, like root or administrator passwords.
    """
    password = generate_password(30, True, True, True, True, False)
    return password


def ci_key():
    """
    Generate CodeIgniter Encryption Keys - Can be used for any other 256-bit key requirement.
    """
    password = generate_password(32, True, True, True, False, False)
    return password


def wpa_160():
    """
    Generate 160-bit WPA Key
    """
    password = generate_password(20, True, True, True, True, False)
    return password


def wpa_504():
    """
    Generate 504-bit WPA Key
    """
    password = generate_password(63, True, True, True, True, False)
    return password


def wep_64():
    """
    Generate 64-bit WEP Keys
    """
    password = generate_password(5, False, False, False, False, True)
    return password


def wep_128():
    """
    Generate 128-bit WEP Keys
    """
    password = generate_password(13, False, False, False, False, True)
    return password


def wep_152():
    """
    Generate 152-bit WEP Keys
    """
    password = generate_password(16, False, False, False, False, True)
    return password


def wep_256():
    """
    Generate 256-bit WEP Keys
    """
    password = generate_password(29, False, False, False, False, True)
    return password


def password_checker(password, requirement):
    return any(char in password for char in requirement)


def main():
    parser = argparse.ArgumentParser(description="The Secure Password or Keygen Generator")
    parser.add_argument("length", nargs="?", type=int, default=8, help="Length of password (default is 8 characters)")
    parser.add_argument("-l", "--lower-case", action="store_true", help="Use lowercase characters")
    parser.add_argument("-u", "--upper-case", action="store_true", help="Use uppercase characters")
    parser.add_argument("-n", "--numbers", action="store_true", help="Use numbers")
    parser.add_argument("-s", "--special", action="store_true", help="Use special characters")
    parser.add_argument("-x", "--hex", action="store_true", help="Use hex characters")
    parser.add_argument("-p", "--password-strength", choices=["decent", "strong", "fort_knox", "wpa_160", "wpa_504", "wep_64", "wep_128", "wep_152", "wep_256"], help="Generate a password with a predefined strength")
    args = parser.parse_args()

    if args.password_strength:
        length, use_lower_case, use_upper_case, use_numbers, use_special, use_hex = {
            "decent": (10, True, True, True, False, False),
            "strong": (15, True, True, True, True, False),
            "fort_knox": (30, True, True, True, True, False),
            "wpa_160": (20, True, True, True, True, False),
            "wpa_504": (63, True, True, True, True, False),
            "wep_64": (5, False, False, False, False, True),
            "wep_128": (13, False, False, False, False, True),
            "wep_152": (16, False, False, False, False, True),
            "wep_256": (29, False, False, False, False, True)
        }[args.password_strength]
        password = generate_password(length, use_lower_case, use_upper_case, use_numbers, use_special, use_hex)
    else:
        if not args.lower_case and not args.upper_case and not args.numbers and not args.special and not args.hex:
            args.length=8
            args.lower_case=True
            args.upper_case=True
            args.numbers=True
            args.special=True
            args.hex=False
        password = ""
        if args.length > 1000:
            print("ERROR: Requested password length is too large, please choose a reasonable value.")
            return
        if args.length > 4:
            while not password_checker(password, string.ascii_lowercase if args.lower_case else password) \
                    or not password_checker(password, string.ascii_uppercase if args.upper_case else password) \
                    or not password_checker(password, string.digits if args.numbers else password) \
                    or not password_checker(password, string.punctuation if args.special else password) \
                    or not password_checker(password, "123456789ABCDEF" if args.hex else password):
                password = generate_password(args.length, args.lower_case, args.upper_case, args.numbers, args.special, args.hex)
        else:
            password = generate_password(args.length, args.lower_case, args.upper_case, args.numbers, args.special, args.hex)

    print(password)


if __name__ == "__main__":
    main()