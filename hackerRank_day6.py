# Given a string, , of length  that is indexed from  to ,
# print its even-indexed and odd-indexed characters as  space-separated strings
# on a single line (see the Sample below for more detail).
#
# Note: 0 is considered to be an even index.
#
# Example
#
#s = adbecf
# Print abc def

def process_string(s):
    even_chars = s[::2]  # Characters at even indices
    odd_chars = s[1::2]  # Characters at odd indices
    return f"{even_chars} {odd_chars}"

# Main code
if __name__ == "__main__":
    # Read the number of test cases
    t = int(input().strip())
    for _ in range(t):
        # Read each string and process it
        s = input().strip()
        print(process_string(s))

