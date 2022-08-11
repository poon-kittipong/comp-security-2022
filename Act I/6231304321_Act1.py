import hashlib
import time

# substitution dict
sub_dict = {
  'a': ['@'],
  'o': ['0'],
  'O': ['0'],
  'l': ['I', '1'],
  'i': ['1'],
  'I': ['1']
}

# function to gen all possible substitution
def getAllSubstistution(password):
  all_sub = [""]

  for c in password:

    # get lowercase and uppercase of the character
    lower_list = [a+c.lower() for a in all_sub]
    upper_list = [a+c.upper() for a in all_sub]
    combined_list = lower_list + upper_list

    # sub character
    if c in sub_dict:
      for sub in sub_dict[c]:
        sub_list = [a+sub for a in all_sub]
        combined_list += sub_list
    
    # assign combined_list to the all_sub
    all_sub = combined_list

  return all_sub

# define hashed value to find
hash_to_find = 'd54cc1fe76f5186380a0939d2fc1723c44e8a5f7'
actual_password = ''

# import file
f = open("10k_common_password.txt", "r")
f_lines = f.read().splitlines()

# 1. ---------------
print('1. ------------------')
found_password = False
for line in f_lines:
  
  if found_password:
    continue
  
  # gen all possible password combination
  pass_combi = getAllSubstistution(line)


  for password in pass_combi:
    hashed_val = hashlib.sha1(password.encode()).hexdigest()

    if hashed_val == hash_to_find:
      print("Password (hashed with sha1) : ", password)
      actual_password = password
      found_password = True

    hashed_val = hashlib.md5(password.encode()).hexdigest()
    if hashed_val == hash_to_find:
      print("Password (hashed with md5) : ", password)
      actual_password = password
      found_password = True

# 2. ---------------
print('2. ------------------')

# start timer
start_time = time.time()
time_used = 0

f = open("10k_common_password.txt", "r")
f_lines = f.read().splitlines()

# create hash table
hash_sha1_table = dict()

# construct hash table
for line in f_lines:
  
  # gen all possible password combination
  pass_combi = getAllSubstistution(line)

  for password in pass_combi:
    hashed_val = hashlib.sha1(password.encode()).hexdigest()

    # assign value to hash table.
    hash_sha1_table[hashed_val] = password

time_used = time.time() - start_time
print('Time used to construct table (s): ', time_used)
print('Table size: ', len(hash_sha1_table))

# 3. ---------------
print('3. ------------------')
time_used = 0
entries = 0

f = open("10k_common_password.txt", "r")
f_lines = f.read().splitlines()

# create hash table
hash_sha1_table = dict()
all_gen_password = [""]

# construct hash table
for line in f_lines:
  
  # gen all possible password combination
  pass_combi = getAllSubstistution(line)
  all_gen_password += pass_combi

# start timer
start_time = time.time()

for password in all_gen_password:
  hashed_val = hashlib.sha1(password.encode()).hexdigest()

time_used = time.time() - start_time
print("all_gen_password length = ", len(all_gen_password))
print("Average time used (μs): ", time_used * 1e6 / len(all_gen_password))