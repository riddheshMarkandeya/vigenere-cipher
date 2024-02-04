alphabet_to_index = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25, "_":26}
index_to_alphabet = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z", 26:"_"}

# table = [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"],
# ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A"],
# ["C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B"],
# ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C"],
# ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D"],
# ["F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E"],
# ["G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F"],
# ["H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G"],
# ["I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H"],
# ["J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I"],
# ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
# ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],
# ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"],
# ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
# ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"],
# ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
# ["Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"],
# ["R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"],
# ["S", "T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"],
# ["T", "U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"],
# ["U", "V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"],
# ["V", "W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"],
# ["W", "X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"],
# ["X", "Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"],
# ["Y", "Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"],
# ["Z", "_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"],
# ["_", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]]

def text_to_indexes(text):
  vals = []
  for c in text:
    vals.append(alphabet_to_index[c])
  return vals

def indexes_to_text(indexes):
  vals = []
  for i in indexes:
    vals.append(index_to_alphabet[i])
  return "".join(vals)

def encrypt(plaintext, secret):
  plaintext = plaintext.upper().replace(" ", "_")
  secret = secret.upper().replace(" ", "_")

  plaintext_index = text_to_indexes(plaintext)
  secret_index = text_to_indexes(secret)
  
  secret_length = len(secret_index)
  j = 0
  cipher_index = []
  for i in plaintext_index:
    cipher_index.append((i + secret_index[j]) % 27)
    j = j + 1
    
    if j == secret_length:
      j = 0

  return indexes_to_text(cipher_index)

def decrypt(ciphertext, secret):
  ciphertext = ciphertext.upper()
  secret = secret.upper().replace(" ", "_")

  ciphertext_index = text_to_indexes(ciphertext)
  secret_index = text_to_indexes(secret)
  
  secret_length = len(secret_index)
  j = 0
  plaintext_index = []
  for i in ciphertext_index:
    plaintext_index.append((i - secret_index[j]) % 27)
    j = j + 1
    
    if j == secret_length:
      j = 0

  return indexes_to_text(plaintext_index).replace("_", " ")

if __name__ == "__main__":
  secret = input("Enter secret: ")
  choice = input("Enter 0 for Encryption or 1 for Decryption: ")
  if choice == "0":
    plaintext = input("Enter plaintext: ")
    print("CipherText: ", encrypt(plaintext, secret))
  if choice == "1":
    ciphertext = input("Enter ciphertext: ")
    print("PlainText: ", decrypt(ciphertext, secret))

