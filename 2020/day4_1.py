input_passport = open("day4.in").read().splitlines()

passports = []
p = []
for line in input_passport:
    if line != "":
        for kk in line.split(" "):
            p.append(kk)
    else:
        passports.append(p)
        p = []
passports.append(p)

valid_passports = 0
invalid_passports = 0
for passs in passports:
    if (
        any("byr:" in s for s in passs) and
        any("iyr:" in s for s in passs) and
        any("eyr:" in s for s in passs) and
        any("hgt:" in s for s in passs) and
        any("hcl:" in s for s in passs) and
        any("ecl:" in s for s in passs) and
        any("pid:" in s for s in passs)
    ):
        valid_passports = valid_passports +1
        #print("YESSSSSSSS", passs)
    else:
        invalid_passports = invalid_passports +1
        #print("NOOOOOOOOO", passs)

#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID)

print("valid: ", valid_passports, " - invalid: ", invalid_passports)
