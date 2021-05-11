  #Copywrite Warning: Owner of the code is Gulcheera Academy(Khosiyat Sabirova)
                                                        #This code can be used by anyone for free, but the name "Gulcheera Academy" must be acknowledged 
import pandas as pd
import numpy as np
import matplotlib as plt
import re
import warnings
#%matplotlib inline

example_textData3=["30-538-917-33-62", "80 948 649 96 23","90.316. 221.23.19","https://www.apple.com","http://www.banana.net", "@this is great post", "#IT @my godfather http://bit.ly/3h63x  he did not deserve this","#culture_art Here is a post of modern art"]

#extract telephone nubers
def extract_telNumbers(inputText):
  telNumbers=[]

  for word in inputText:
    #You may change the regular expression patterns
    digit=re.findall(r"\d\d.\d\d\d.\d\d\d.\d\d.\d\d", word)
    #digit=re.findall(r"\d+", word)

    telNumbers.append(digit)
  return telNumbers
  #print(telNumbers)


extract_telNumbers(example_textData3)
