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

pressumpted_valid_passports_lst=[]
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
        pressumpted_valid_passports_lst.append(passs)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

valid_passports = 0
invalid_passports = 0
for next_passport in pressumpted_valid_passports_lst:
    valid = True
    for i in next_passport:
        key = i.split(":")[0]
        value =  i.split(":")[1]

        if key == "byr":
            if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002: continue
            else: 
                valid = False
                motiu = "byr"
        elif key == "iyr":
            if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020: continue
            else:
                valid = False
                motiu = "iyr"
        elif key == "eyr":
            if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030: continue
            else: 
                valid = False
                motiu = "eyr"
        elif key == "hgt":
            if "cm" in value:
                split_value = value.replace("cm","")
                if int(split_value) >= 150 and int(split_value) <= 193: continue
                else: 
                    valid = False
                    motiu = "hgt"
            elif "in" in value:
                split_value = value.replace("in","")
                if int(split_value) >= 59 and int(split_value) <= 76: continue
                else:
                    valid = False
                    motiu = "hgt"
            else: valid = False
        elif key == "hcl":
            if len(value) == 7 and value[0] == "#": continue
            else:
                valid = False
                motiu = "hcl"
        elif key == "ecl":
            if (
                value == "amb" or
                value == "blu" or
                value == "brn" or
                value == "gry" or
                value == "grn" or
                value == "hzl" or
                value == "oth"
            ): continue
            else: 
                valid = False
                motiu = "ecl"
        elif key == "pid":
            if len(value) == 9: continue
            else:
                valid = False
                motiu = "pid"

    if valid:
        #print(next_passport)
        valid_passports = valid_passports +1
    else: print(motiu, next_passport)

print(valid_passports)
