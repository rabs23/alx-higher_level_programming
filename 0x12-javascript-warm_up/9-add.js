#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
add(a, b);
