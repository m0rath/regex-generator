import re
import sys

try:
    inputString = str(sys.argv[1])
except Exception:
    print("Required string argument")
    exit(1)

listRegexExpression = ["\d", "\w", "\s", "[a-z]", "\W", "\D", "\S"]
specialChars = ["\-", "\$", "\&", "\+", "\,", "\:", "\;", "\=", "\?", "\@", "\#", "\|", "\'", "\"", "\<", "\>", "\.",
                "\^", "\*", "\(", "\)", "\%", "\!"]

# Variable declaration
regexString, storeState, storeLastState, updatedRegexString, st_var = "", "", "", "", ""
hasSlash, count = 0, 0
flag, st_flag = False, False

# generating basic regex
for x in inputString:
    for y in listRegexExpression:
        if "\\" + x in specialChars:
            for sc in specialChars:
                if "\\" + x == sc:
                    regexString = regexString + sc
                    break
            break
        elif re.match(y, x):
            regexString = regexString + y
            break

# Optimising Regex
for x in range(len(regexString)):
    if regexString[x] == "\\":
        hasSlash = 1
        continue
    if regexString[x] == "[":
        st_var = st_var + regexString[x]
        st_flag = True
        continue
    if st_flag:
        st_var = st_var + regexString[x]
        if regexString[x] != "]":
            continue

    if hasSlash == 1:
        hasSlash = 0
        temp_str = "\\" + regexString[x]
    elif st_flag:
        temp_str = st_var
        st_flag = False
        st_var = ""
    else:
        temp_str = regexString[x]

    if storeLastState == "" or storeLastState != temp_str:  # or str in specialChars
        updatedRegexString = updatedRegexString + temp_str
        count = 0
        flag = False
    elif storeLastState == temp_str:
        if not flag: updatedRegexString = updatedRegexString + "+"
        flag = True
    else:
        count = count + 1
    storeLastState = temp_str

print("Basic Regex: ", regexString)
print("Optimized Regex: ", updatedRegexString)
print("Alternate Regex: ", updatedRegexString.replace('+', '*'))

