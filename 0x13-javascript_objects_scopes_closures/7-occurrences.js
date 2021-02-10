#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const number = list.filter(item => item === searchElement).length;
  return number;
};
