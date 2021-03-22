#!/usr/bin/node
// find biggest num in array

const args = process.argv;

function secondMax (arr) {
  const array = arr.slice(2, arr.length);
  let i = 0;
  for (; i < array.length; i++) {
    array[i] = parseInt(array[i]);
  }
  array.sort(function (a, b) { return b - a; });
  return array[1];
}

if (args.length <= 3) {
  console.log(0);
} else {
  console.log(secondMax(args));
}
