from cryptoelp_basics import base64_decode, base64_encode, fixed_xor, hextets_to_chars, chars_to_hextets, single_byte_xor_decode, repeating_key_xor_encdec
from cryptoelp_scoring import score_english_ascii_simple

from collections import Counter

def challenge1():
    print("Challenge 1")

    # The string:
    C1HEXTETS = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    # Should produce:
    C1EXPECTED = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    c1bytes = hextets_to_chars(C1HEXTETS)
    assert C1EXPECTED == base64_encode(c1bytes)
    print("Pass!")

def challenge2():
    print("Challenge 2")

    # Fixed XOR
    # Write a function that takes two equal-length buffers and produces their XOR combination.

    # If your function works properly, then when you feed it the string:

    C2INPUT = "1c0111001f010100061a024b53535009181c"
    # ... after hex decoding, and when XOR'd against:
    C2XOR = "686974207468652062756c6c277320657965"
    # ... should produce:
    C2EXPECTED = "746865206b696420646f6e277420706c6179"

    fixed = fixed_xor(hextets_to_chars(C2INPUT), hextets_to_chars(C2XOR))
    fixed_c2h = chars_to_hextets(fixed)
    assert C2EXPECTED == fixed_c2h
    print("Pass")


def break_single_byte_xor(hextets):
    scores = Counter()
    for key in range(255):
        decoded = single_byte_xor_decode(hextets, key)
        scores[(chr(key), decoded)] = score_english_ascii_simple(decoded)

    return scores

def challenge3():
    print("Challenge 3")

    C3 = hextets_to_chars("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

    scores = break_single_byte_xor(C3)
    key, message = scores.most_common(1)[0][0]
    assert key == "X"
    assert message == "Cooking MC's like a pound of bacon"
    print("Pass")


def challenge4():
    print("Challenge 4")
    scores = Counter()
    for line in open("set1_challenge4.txt").readlines():
        chars = hextets_to_chars(line.strip())
        scores += break_single_byte_xor(chars)

    key, message = scores.most_common(1)[0][0]
    assert key == "5"
    assert message == "Now that the party is jumping\n"    

    print("Pass")


def challenge5():
    print("Challenge 5")
    stanza = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    encoded = repeating_key_xor_encdec(stanza, "ICE")
    assert chars_to_hextets(encoded) == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    print("Pass")

# challenge1()
# challenge2()
# challenge3()
# challenge4()
challenge5()