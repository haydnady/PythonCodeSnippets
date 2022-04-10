       

def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    bulls = 0
    cows = 0
    modString = ""
    
    if 1 <= len(secret) and len(secret) <= 1000 and \
       1 <= len(guess) and len(guess) <= 1000 and \
       len(secret) == len(guess) and \
       secret.isdigit() and \
       guess.isdigit():  # Constraints

        for idx, value in enumerate(secret):
            # Finds match and location is correct
            if (value in guess) and (value == guess[idx]):
                bulls += 1
                # x out the values that should no longer be matched
                guess = guess[:idx] + "x" + guess[idx+1:]
                modString += "x"

            else:
                modString += value

        if modString != guess:  # If strings are the same, break, there are no wrong location matches
            for idx, value in enumerate(modString):
                # Finds match and location is NOT correct
                if (value in guess) and (value != guess[idx]):
                    cows += 1

                    print("modString", modString, "letter", value, "guess letter", guess[idx], "guess", guess)
                    print("-------------------------", idx)
                    # x out the values that should no longer be matched
                    guess = guess[:guess.index(value)] + "x" + guess[guess.index(value)+1:]

    return str(bulls) + "A" + str(cows) + "B"


print("==============>", getHint("1807", "7810"))
assert getHint("1807", "7810") == "1A3B"

print("==============>", getHint("1123", "0110"))
assert getHint("1123", "0110") == "1A1B"

print("==============>", getHint("1123", "1111"))
assert getHint("1123", "1111") == "2A0B"

print("==============>", getHint("1123", "0111"))
assert getHint("1123", "0111") == "1A1B"

print("==============>", getHint("1123", "1123"))
assert getHint("1123", "1123") == "4A0B"

print("==============>", getHint("1122", "2211"))
assert getHint("1122", "2211") == "0A4B"

print("==============>", getHint("2962", "7236"))
assert getHint("2962", "7236") == "0A2B"

print("==============>", getHint("011", "110"))
assert getHint("011", "110") == "1A2B"

print("==============>", getHint("11", "01"))
assert getHint("11", "01") == "1A0B"

print("==============>", getHint("11", "10"))
assert getHint("11", "10") == "1A0B"

print("==============>", getHint("12", "23"))
assert getHint("12", "23") == "0A1B"

print("==============>", getHint("1", "1"))
assert getHint("1", "1") == "1A0B"

print("==============>", getHint("0765860239", "5736153483"))
assert getHint("0765860239", "5736153483") == "1A4B"