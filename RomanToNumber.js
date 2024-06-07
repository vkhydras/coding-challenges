var intToNumber = function(s) {
    const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

    let i = 0;
    let num = 0;

    while (i < s.length) {
        for (let j = 0; j < symbols.length; j++) {
            const symbol = symbols[j];
            const value = values[j];
            if (s.startsWith(symbol, i)) {
                num += value;
                i += symbol.length;
                break;
            }
        }
    }

    return num;
};

console.log(intToNumber("MMDCCXLIX")); // Output: 2749
