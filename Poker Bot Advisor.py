from random import randint
from time import sleep


class say():
  def __init__(self):
    self.move = 0
    self.m = 1
    self.N = 0
    print("Ready for operation!")
    
  def decision(self):
    self.N = randint(1,20)
    self.move = str(self.m)
    self.move = self.move+'.'
    sleep(1)
    input(">")
    if self.N == 20:
      self.m+=1
      print(self.move,"Fold")
    else:
      self.m+=1
      print(self.move,"Stay")
    self.decision()
    
O = say()
O.decision()