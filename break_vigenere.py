import vigenere as v

ciphertext = "tyxvahlvowsrahsoervceispsqlj_hxgyqfjtqgi_j___bafebacoewvowsohvs_nvet_dgo_tghidzvbklvodsjuhsjwdsmerwdnvkn_jgvrvv_ilxvhzevnelvodsohvsyhrfyeqga_yan_dgo_rloatcdnxsxujsmaj__rqgi_j___wtytqlcajsreq_wvvshauxvokjvpekdtzgi_kfwsitdlrugeqlceqxidqtidqtdmqga_ihtidzvidswlbsdtisailxvvrjdeja_sqan_afjwbxzgvsjfqlceqxiecqvadwvtyan_afjwbxzgvsyadsjnbqvbvszehaqeusdnqlceqydrilvidkoadv__wjjmqlceqvjnlxmtvwvsfqvhvfyeqao_zkveik_njawlqlcajsohvsyodn_rjxz_iht_sxvthxwtvwvwzlc_j___klhoilvlzu_rrddto".upper()

digraphs = {}
for i in range(len(ciphertext) - 1):
  key = ciphertext[i] + ciphertext[i+1]
  if key not in digraphs:
    digraphs[key] = 0
  
  digraphs[key] = digraphs[key] + 1

digraphs = dict(sorted(digraphs.items(), key=lambda item: item[1], reverse=True))

print(digraphs)

def print_distances(digraph):
  positions = []
  for i in range(len(ciphertext) - 1):
    key = ciphertext[i] + ciphertext[i+1]
    if key == digraph:
      positions.append(i)

  distances = [positions[0]]
  for i in range(1, len(positions)):
    distances.append(positions[i] - positions[i-1])

  print(distances)

# print_distances("__")
print_distances("VS")
print_distances("EQ")
print_distances("QL")
print_distances("LC")

# 68, 52
# secret length is probably 4

period = 4

segments = [[] for i in range(period)]
for i in range(len(ciphertext)):
  segments[i % period].append(ciphertext[i])

print(segments)

fequencies = [{} for i in range(period)]
for i in range(period):
  temp = {}
  for char in segments[i]:
    if char not in temp:
      temp[char] = 0
    temp[char] += 1
    
  fequencies[i] = dict(sorted(temp.items(), key=lambda item: item[1], reverse=True))

print(fequencies)

# _,Q,S,V 
print(v.alphabet_to_index["_"], v.alphabet_to_index["Q"], v.alphabet_to_index["S"], v.alphabet_to_index["V"])
print(-1 % 27)

# _,Q,S,V 26,16,18,21 -> 0,17,19,22

print(v.index_to_alphabet[0], v.index_to_alphabet[17], v.index_to_alphabet[19], v.index_to_alphabet[22])

print(v.decrypt(ciphertext, "ARTW"))

# print(v.decrypt(ciphertext, "FOUR"))
