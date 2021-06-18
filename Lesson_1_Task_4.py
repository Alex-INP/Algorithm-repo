import string
from datetime import datetime as DT

num_min = int(input())
num_max = int(input())
num_min_f = float(input())
num_max_f = float(input())
sim_min = input()
sim_max = input()
ind_si_min = string.ascii_lowercase.index(sim_min)
ind_si_max = string.ascii_lowercase.index(sim_max)


print(round((num_max - num_min) * int(DT.now().second) / 60 + num_min))

print((num_max_f - num_min_f) * int(DT.now().second) / 60 + num_min_f)

print(string.ascii_lowercase[round((ind_si_max - ind_si_min) * int(DT.now().second) / 60 + ind_si_min)])