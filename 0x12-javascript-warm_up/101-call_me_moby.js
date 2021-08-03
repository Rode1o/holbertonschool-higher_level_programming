#!/usr/bin/node
// function that executes x times a function.

function callMeMoby (x, thefunction) {
    for (let i = 0; i < x; i++) {
        thefunction();
    }
}
module.exports = {
    callMeMoby: callMeMoby
};
