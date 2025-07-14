import re

# number = "+254 701 234 567 and +254-701-234-567 +254|789|123|456"
# pattern = r"\+\d{3}(\s|-)+\d{3}(\s|-)+\d{3}(\s|-)+\d{3}"

# matches = re.findall(pattern,number)
# print(matches)

# email = "Sonnyboi3000@gmail.com shadrackjoseph.omondi@eldoretnovapioneer.com"
# pattern = r"[a-zA-Z0-9.]+\@[a-z A-Z]+\.[com|co\.ke]$"

# matches = re.findall(pattern,email)
# print(matches)

password = "Afcon2027!"
pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}"

matches  = re.findall(pattern, password)
print(matches)
