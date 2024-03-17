#!/usr/bin/node
if (process.argv.length > 3) {
  const args = process.argv.map(Number);
  args.slice(2);
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
} else {
  console.log(0);
}
