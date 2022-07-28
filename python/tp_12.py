word = tuple(input("What's in your mind? : "))

hist = {}

for key in word:
  hist[key] = hist.get(key,0)+1

hist
