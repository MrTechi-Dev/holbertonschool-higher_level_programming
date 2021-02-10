#!/usr/bin/node
// reverse list
exports.esrever = function (list) {
  const reverseList = [];
  for (let i = 0; i <= list.length - 1; i++) {
    reverseList.unshift(list[i]);
  }
  return reverseList;
};
