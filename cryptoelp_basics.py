BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64_encode(bytes):
    """Transforms bytes into base64 encoded version."""
    ret = ""
    assert len(bytes) > 0

    extra = 0
    for i, c in enumerate(bytes):
        h = ord(c)
        if i % 3 == 0:
            # Use 6, extra 2
            ret += BASE64[h >> 2]
            extra = (h & 0b11) << 4
        elif i % 3 == 1:
            # Use Extra 2, 4 of next, extra 4
            ret += BASE64[extra | h >> 4]
            extra = (h & 0b1111) << 2
        elif i % 3 == 2:
            # Use extra 4, 8 to get two b64 bytes
            ret += BASE64[extra | h >> 6]
            ret += BASE64[h & 0b111111]
            extra = 0
    if i in (0, 1):
        ret += BASE64[extra]
        ret += "=" * (2 - i)
    return ret


def hex2bin(hex):
    return bin(int(hex, 16))[2:]

def pad(i, leftto=0, rightto=0):
    i = "0" * (leftto - len(i)) + i
    i = i + "0" * (rightto - len(i))
    return i

def bin_from_hex(h):
    assert len(h) == 1
    return pad(hex2bin(h), leftto=4)


def base64_decode(msg):
    """Returns decoded bytes of a base64 message."""
    ret = ""
    accum = 0
    for i, c in enumerate(msg):
        if c == "=":
            # We are outside the encoded area, so no just forget any future bytes
            return ret
        sextet = BASE64.index(c)
        if i % 4 == 0:
            # Save 6
            accum = sextet
        elif i % 4 == 1:
            # Use 6 from prev + 2 from next
            ret += chr(accum << 2 | sextet >> 4)
            accum = sextet & 0xf
        elif i % 4 == 2:
            # Use 4 from prev + 4 from next
            ret += chr(accum << 4 | sextet >> 2)
            accum = sextet & 0b11
        elif i % 4 == 3:
            ret += chr(accum << 6 | sextet)
            accum = 0
    return ret


def chars_to_hextets(s):
    """Returns a hex formatted version of a string."""
    ret = ""
    for c in s:
        o = pad(hex(ord(c))[2:], leftto=2)
        ret += o
    return ret


def hextets_to_chars(hextets):
    """Returns the chars represented by the  hextets."""
    ret = ""
    for i in range(0, len(hextets), 2):
        ret += chr(int(hextets[i:i+2], 16))
    return ret

def whatever2(abc):
    return 1


def fixed_xor(a, b):
    """Returns fixed xor on the bytes of each string (of same length)"""
    assert len(a) == len(b)

    ret = ""
    for i in range(len(a)):
        ac = ord(a[i])
        bc = ord(b[i])
        ret += chr(ac ^ bc)
    
    return ret


def single_byte_xor_decode(encoded, key):
    return fixed_xor(encoded, chr(key) * len(encoded))


def repeating_key_xor_encdec(msg, key):
    ret = []
    for i, enc in enumerate(msg):
        k = key[i % len(key)]
        ret.append(fixed_xor(k, enc))
    return "".join(ret)

def hamming_distance(a, b):
    dist = 0
    assert len(a) == len(b)
    for ac, bc in zip(a, b):
        diff_bits = ord(ac) ^ ord(bc)
        while diff_bits != 0:
            if diff_bits & 0b1:
                dist += 1
            diff_bits >>= 1
    return dist

