Digits=[
        ["   ***   ","  *   *  "," *     * "," *     * "," *     * ","  *   *  ","   ***   "],
        ["   *   ","  **   ","   *   ","   *   ","   *   ","   *   ","  ***  "],
        [  "  ***  "," *   * "," *  *  ","   *   ","  *    "," *     "," ***** "],
        ["  ***  "," *   * ","     * ","   **  ","     * "," *   * ","  ***  "],
        ["    *   ","   **   ","  * *   "," *  *   "," ****** ","    *   ","    *   "],
        ["  ***  "," *     "," *     ","  ***  ","     * ","     * ","  ***  "],
        [ "  ***  "," *     "," *     "," ****  "," *   * "," *   * ","  ***  "],
        [" ***** ","     * ","    *  ","   *   ","  *    "," *     "," *     "],
        ["  ***  "," *   * "," *   * ","  ***  "," *   * "," *   * ","  ***  "],
        [ "  **** "," *   * "," *   * ","  **** ","     * ","     * ","     * "]
]
import sys
try:
    digits = sys.argv[1]
    row = 0 
    while row < 7: 
        line = "" 
        column = 0 
        while column < len(digits): 
            number = int(digits[column]) 
            digit = Digits[number]
            for i in digit[row]:
                if i == ' ':
                    line += ' '
                else:
                    line += str(number) 
            line += " " 
            column += 1 
        print(line) 
        row += 1 
except IndexError: 
    print("usage: bigdigits.py <number>") 
except ValueError as err: 
    print(err, "in", digits)
