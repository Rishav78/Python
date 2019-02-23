import re

str  = input("Enter Any Line: ")
# print(re.findall(r"\d",str))
# print(re.findall("\s",str))
# print(re.findall("\S",str))
# print(re.findall("ri..a",str))
# if re.findall("^rishav",str):
#     print("Yes string start with rishav")
# else:
#     print("No")
# print(re.findall("[a-m]",str),end="\n\n")
# print(re.findall("r*",str))
# print(re.findall("r+",str))
# print(re.findall("r{2}",str))
# print("yes",re.findall("r{2}|r{1}",str))
# print(re.findall(r"\brish",str))
# print(re.findall(r"\D",str))
# print(re.findall(r"ri\B",str))
# print(re.findall(r"\w",str))
# print(re.findall(r"\W",str))

# print(re.search("rish",str))
# print(re.search(r"\br.*",str).span())

# print(re.findall(r"ri?",str))

v=re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', str)
if v:
    print("verified")
    print(v.group(1))
    print(v.group(2))
    print(v.group(3))