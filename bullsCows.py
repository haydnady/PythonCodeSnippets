# def getHint(secret, guess):
#     """
#     :type secret: str
#     :type guess: str
#     :rtype: str
#     """
#     countC = 0
#     correctValues = 0
#     count = 0
    
#     for i in secret:

#         if i in guess:
#             if i != guess[count]:
#                 correctValues += 1

#             if i == guess[count]:
#                 countC += 1

#         count += 1   
#     return str(countC) + "A" + str(correctValues) + "B"
        

def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    countC = 0
    correctValues = 0
    count = 0
    tempList = ""
    
    for i in secret:
        if i in guess:

            # Finds match and location is correct
            if i == guess[count]:
                countC += 1

                guess = guess[:guess.index(i)] + "x" + guess[guess.index(i)+1:]
                tempList += "x"

            else:
                tempList += i

        else:
            tempList += i

        count += 1

    count = 0
    for ii in tempList:
        if ii in guess:

            print("tempList", tempList, "letter", ii, "guess letter", guess[count], "guess", guess)
            print("-------------------------", count)

            # Finds match and location is NOT correct
            if ii != guess[count]:
                guess = guess[:guess.index(ii)] + "x" + guess[guess.index(ii)+1:]
                correctValues += 1

        count += 1

    return str(countC) + "A" + str(correctValues) + "B"


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