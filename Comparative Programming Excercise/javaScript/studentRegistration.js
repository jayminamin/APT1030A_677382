const readline = require('readline-sync');

const name = readline.question("Enter student name: ");
const units = parseInt(readline.question("Enter number of registered units: "));

const status = units > 7 ? "Overload – Approval Required" : "Registration Accepted";

console.log("\n--- Final Summary ---");
console.log(`Student Name: ${name}`);
console.log(`Units: ${units}`);
console.log(`Status: ${status}`);
