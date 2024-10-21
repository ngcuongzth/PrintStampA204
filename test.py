def contains_whitespace(s):
    return " " in s


string = "2410180  09-0  003-7887-V000021"
if contains_whitespace(string):
    print("Co.")
else:
    print("Khong.")
