import pug
import soup
import random
import time

random.seed(time.time())
letters = "qwertyuiopasdfghjklzxcvbnm"
number = random.randint(1, 100)
word = "okak"
run = True
sas = 1
sas1 = 1

while (run):
    S1 = soup.stage1(sas, sas1, number)
    S2 = soup.stage2(letters, word)

    if isinstance(S1, tuple):
        sas, sas1 = S1
    elif S1 is not None:
        S3 = S2 + str(S1)
        print(S3)
        run = False
    


