var intToRoman = function(num) {
    // Define the Roman numeral mappings
    const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

    let result = '';

    // Iterate over the values and symbols
    for (let i = 0; i < values.length; i++) {
        // Repeat the symbol as many times as it fits into num
        while (num >= values[i]) {
            num -= values[i];
            result += symbols[i];
        }
    }

    return result;
};

console.log(intToRoman(3749)); // Output: "MMDCCXLIX"
