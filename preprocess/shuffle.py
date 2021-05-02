import random

fin = open("src-train.txt","r")
fout = open("shuffled/src-train.txt","w")

print("Reading src file....")
lines = fin.readlines()
print("Shuffling data...")
start_state = random.getstate()
random.shuffle(lines)
print("Writing shuffled data to file...")

fout.writelines(lines)

fin.close()
fout.close()

fin = open("tgt-train.txt","r")
fout = open("shuffled/tgt-train.txt","w")

print("Reading tgt file....")
lines = fin.readlines()
print("Shuffling data...")
random.setstate(start_state)
random.shuffle(lines)
print("Writing shuffled data to file...")

fout.writelines(lines)

fin.close()
fout.close()

