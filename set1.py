from test_cryptoelp_basics import base64_decode, base64_encode, fixed_xor, hextets_to_chars, chars_to_hextets

####################
print("Challenge 1")

# The string:
C1HEXTETS = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
# Should produce:
C1EXPECTED = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

c1bytes = hextets_to_chars(C1HEXTETS)
assert C1EXPECTED == base64_encode(c1bytes)
print("Pass!")

####################
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

####################
print("Challenge 3")