### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  def check_for_ace(self, card): 
    if card.value = 1: #should be checking with ==
      return True
    else #missing :
      return False
   

  dif highest_card(self, card1 card2):  #should be def, missing comma between card1 and card2.
  if card1.value > card2.value: #should be indented
    return card  #should be card1 and comparing the value of it
  else:
    return card2 #should be card2.value
  


def cards_total(self, cards):  #the function needs to be indented
  total # total = 0
  for card in cards:
    total += card.value 
    return "You have a total of" + total #need to be in f string, total in {} and " after total, the whole line needs to be unindented once.
  
```
