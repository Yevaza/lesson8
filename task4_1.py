import re
def extract_domains(emails):
    return [re.search(r'@([a-zA-Z0-9.-]+)', email).group(1) for email in emails if re.search(r'@([a-zA-Z0-9.-]+)', email)]

email=[input("Почта: ")]
result_domains = extract_domains(email)
print(result_domains)