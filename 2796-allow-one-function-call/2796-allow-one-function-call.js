/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let hasBeenCalled = false;
    
    return function(...args) {
        // We only proceed if the function has NOT been called before.
        if (!hasBeenCalled) {
            // 1. Mark it as called so this block never runs again.
            hasBeenCalled = true;
            
            // 2. Call the original function and return its result.
            // This line MUST be inside the 'if' block.
            return fn(...args);
        }
        // For any subsequent call, the 'if' block is skipped, 
        // and the function returns 'undefined' by default.
    };
};