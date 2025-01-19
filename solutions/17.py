nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def numberToWords(num: int) -> str:
    if num < 10:
        return nums[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        return tens[num // 10] + ("" if num % 10 == 0 else nums[num % 10])
    elif num == 1000:
        return "onethousand"
    else:
        if num % 100 == 0:
            return nums[num // 100] + "hundred"
        return nums[num // 100] + "hundredand" + numberToWords(num % 100)
s = ""
for i in range(1, 1001):
    s += numberToWords(i)
print(len(s))