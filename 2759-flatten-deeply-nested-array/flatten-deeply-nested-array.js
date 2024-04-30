/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const flattenedArray = [];

    arr.forEach(item => {
        if (n > 0 && typeof item === "object" && item !== null) {
            flattenedArray.push(...flat(item, n - 1));
        } else {
            flattenedArray.push(item);
        }
    });

    return flattenedArray;
};