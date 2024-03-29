// // Using map() to double each element in an array
const numbers = [1, 2, 3, 4, 5];
// const doubledNumbers = numbers.map(num => num * 2);
const odd1 = numbers.map(num => num % 2 !== 0);
console.log(odd1)
// console.log(doubledNumbers); // Output: [2, 4, 6, 8, 10]




// // Using reduce() to sum all elements in an array
// const sum = numbers.reduce((acc, curr) => acc + curr, 0);
// console.log(acc)
// console.log(curr)
// console.log(sum); // Output: 15

// // // Using filter() to get odd numbers from an array
const oddNumbers = numbers.filter(num => num % 2 !== 0);
console.log(oddNumbers); // Output: [1, 3, 5]
