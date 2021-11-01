import random

while True:
  print("akmens, skeres, papirits - aiziet!")
  izveele = input("Izvēlies - akmens(A), skeres(S), papirits(P):")
  print("Tu izvēlējies " + izveele)

  defizveeles = ['A','S','P']
  pretIzveele = random.choice(defizveeles)

  print("Es izvēlējos: " + pretIzveele)

  if pretIzveele == izveele:
    print("Neizšķirts!")



  elif pretIzveele == "S" and izveele == "P": print('lol')
  elif pretIzveele == "A" and izveele == "S": print('lol')
  elif pretIzveele == "P" and izveele == "A": print('lol')