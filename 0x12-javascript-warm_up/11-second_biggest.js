#!/usr/bin/node
// find biggest num in array

const args = process.argv;

function max (array) {
  let i = 3;
  let maxInt = parseInt(array[2]);
  let secondBig;

  for (; i < array.length; i++) {
    if (parseInt(array[i]) > maxInt) {
      secondBig = maxInt;
      maxInt = parseInt(array[i]);
    }
  }
  return secondBig;
}
if (args.length <= 3) {
  console.log(0);
} else {
  console.log(max(args));
}
