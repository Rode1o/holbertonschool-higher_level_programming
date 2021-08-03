#!/usr/bin/node
// script that prints a square

const size = process.argv[2];

if (!parseInt(size)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < size; j++) {
    console.log('X'.repeat(size));
  }
}
