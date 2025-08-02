import random as r

st = input("Enter message in lower case : ")
words = st.split(" ")
coding = int(input("1 for Coding or 0 for Decoding : "))
if (coding==1):
  nwords = []
  k=0
  rand=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for word in words:
    if(len(word)>=3):
      r1 = ''.join(r.choices(rand, k=3))
      r2 = ''.join(r.choices(rand, k=3))
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))