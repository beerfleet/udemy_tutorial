import time

gen_start_time = time.time()
print(sum(n for n in range(50000000)))
gen_stop_time = time.time()

com_start_time = time.time()
print(sum([n for n in range(50000000)]))
com_stop_time = time.time()

print(f"Generator timing = {gen_stop_time - gen_start_time}")
print(f"Comprehension timing = {com_stop_time - com_start_time}")