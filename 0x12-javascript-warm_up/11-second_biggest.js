#!/usr/bin/node
// find biggest num in array

const args = process.argv;

function max (array) {
  let i = 3;
  let maxInt = parseInt(array[2]);

  for (; i < array.length; i++) {
    if (parseInt(array[i]) > maxInt) {
      maxInt = parseInt(array[i]);
    }
  }
  return maxInt;
}
if (args.length <= 3) {
  console.log(0);
} else {
  console.log(max(args));
}
