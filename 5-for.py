# lim_max = 10

# for var in range(0, lim_max):
#     print(var)

# for x in range(0, 10):
#     print(x)

var_est_list = [1, 2, 3, 4, 5, "pepe", "pepito"]

for var in var_est_list:
    if isinstance(var, int):
        print(var + 1)
else:
    print(var)

