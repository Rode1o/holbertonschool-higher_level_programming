#!/usr/bin/nodejs
// function that returns the reversed version of a list
exports.esrever = function (list) {
    const bufferRev = [];
    for (let i = list.length - 1; i >= 0; i--){
        bufferRev.push(list[i]);
    }
    return (bufferRev);
}
