import re
def split_string(string, separators):
    return [substring for substring in re.split('|'.join(map(re.escape, separators)),string) if substring]
s=(input("Предложение: "))
separators = [',', '.', '-', '!']
result= split_string(s, separators)
print(result)