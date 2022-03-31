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
    occurance = []
    
    for i in secret:
        if i in guess:

            # Finds match and location is correct
            if i == guess[count]:
                # print("-------------------------", count)
                countC += 1
                occurance.append(i)

            # Finds match and location is NOT correct
            if i != guess[count] and secret.index(i) != guess.index(i) and i not in occurance:
                # print("++++++++++++++++++++++++++", count)
                correctValues += 1


            count += 1

    return str(countC) + "A" + str(len(occurance)) + "B"


print("==============>", getHint("2962", "7236"))
assert "==============>", getHint("2962", "7236") == "0A2B"

print("==============>", getHint("11", "01"))
assert "==============>", getHint("11", "01") == "1A0B"
# assert "==============>", getHint("0765860239", "5736153483")
# assert "==============>", getHint("1807", "7810")
# assert "==============>", getHint("1123", "0110")
# assert "==============>", getHint("1123", "0111")
print("==============>", getHint("1123", "0111"))
assert "==============>", getHint("1123", "1111") == "1A1B"
# assert "==============>", getHint("1123", "1123")
# assert "==============>", getHint("1122", "2211")
# assert "==============>", getHint("11", "10")
# assert "==============>", getHint("1", "1")

# 
# 
# print("==============>", getHint("0765860239", "5736153483"))
# print("==============>", getHint("1807", "7810"))
# print("==============>", getHint("1123", "0110"))
# 
# print("==============>", getHint("1123", "1111"))
# print("==============>", getHint("1123", "1123"))
# print("==============>", getHint("1122", "2211"))
# print("==============>", getHint("11", "10"))
# print("==============>", getHint("1", "1"))