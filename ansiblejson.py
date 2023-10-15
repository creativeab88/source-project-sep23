#! python3

import json, os

os.system('ansible localhost -m setup >> ans2.txt')


file = open("ans2.txt","r")

x = file.read()


# print(x)
print(len(x))

# need to remove msg from beginning of x to first {
x = x.replace('localhost | SUCCESS => ','')

print(len(x))

print(x[0:25])
ansSetupData = json.loads(x)
# ansSetupData = json.load(file)


a = ansSetupData["ansible_facts"]

print('Some Ansible facts are:')
print(a["ansible_os_family"])
print(a["ansible_processor"])
# print(a[8])
# print(a[11])
