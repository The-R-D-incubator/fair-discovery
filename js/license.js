/**
 * Fair Discovery License Architect
 * Generates a business-standard license key
 */
function generateKey(type = 'LIFETIME') {
    const prefix = type === 'LIFETIME' ? 'FD-LIFE' : 'FD-YEAR';
    const segment1 = Math.random().toString(36).substring(2, 6).toUpperCase();
    const segment2 = Math.random().toString(36).substring(2, 6).toUpperCase();
    const segment3 = Math.random().toString(36).substring(2, 6).toUpperCase();
    
    return `${prefix}-${segment1}-${segment2}-${segment3}`;
}

// Log for testing (Architect's check)
console.log("New License Ready: ", generateKey());
