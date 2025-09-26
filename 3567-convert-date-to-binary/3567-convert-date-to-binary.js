/**
 * @param {string} date
 * @return {string}
 */
var convertDateToBinary = function(date) {
       const parts = date.split('-');
    
    
    const yearBinary = parseInt(parts[0], 10).toString(2);
    const monthBinary = parseInt(parts[1], 10).toString(2);
    const dayBinary = parseInt(parts[2], 10).toString(2);
    
    return `${yearBinary}-${monthBinary}-${dayBinary}`;
};