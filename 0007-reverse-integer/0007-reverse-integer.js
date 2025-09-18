/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {

    let sign = x < 0 ? -1 : 1;
    
    let reversed = parseInt(Math.abs(x).toString().split('').reverse().join('')) * sign;
    

    if (reversed < -(2**31) || reversed > (2**31 - 1)) {
        return 0;
    }
    
    return reversed;
}

 
