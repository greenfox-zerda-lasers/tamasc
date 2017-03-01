'use strict'

function Holiday() {
  const args = [...arguments];
  let nodes = [];
  let path = [];

  // Create data structure (nodes) from arguments (eg: 'a => b' --> [b, a], 'a' --> [a, a],)
  function setNodes () {
    args.forEach((e) =>  {
      if (e.search(/^\w+\s*(=>)\s*\w+$/) !== -1) {
        const node = [e.match(/\w+$/)[0], e.match(/^\w+/)[0]];
        nodes.push(node);
      } else {
        const node = e.match(/^\w+/)[0];
        nodes.unshift([node, node]);
      }
    });
  }

  // Find first node, which has no dependency
  function findFirstNode (array) {
    let firstNode = [];
    array.forEach((e) => {
      let count = 0;
      let filteredArray = filterArr(e, array);
      filteredArray.forEach((p) => {
        if (p[1] === e[0]) {
          count++;
        }
      });
      if (count === 0) {
        firstNode = e;
      }
    });
    return firstNode;
  }

  // Removing a node elemenet from an array
  function filterArr (node, array) {
    return array.filter((e) => {
      return e !== node;
    });
  }

  function findIndependentNode(node, array) {
    return array.find((e) => {
      return e[0] === e[1];
    });
  }

  // Finding the next node in the array
  function findNextNode (node, array) {
    let nextNode = [];
    for (let i = 0, l = array.length; i < l; i++) {
      if (array[i][0] === array[i][1] && node[1] === array[i][0]) {  // first case, finding a nondirected node next to
        return array[i];                                             // the given node --> avoiding multiple occurrence
      } else if (node[1] === array[i][0]) {                          // second case, finding a directed node next to the
        nextNode = array[i];                                         // given node
      }
    }
    if (nextNode.length === 0) {
      nextNode = findIndependentNode(node, array);
    }
    return nextNode || [];
  }

  // Recursive function, which pushes nodes into the path variable
  function getPath (initNode, nodeArr) {
    if (initNode.length === 0) {                                    // basecase
      return;
    }
    path.push(...initNode);
    let nextNode = findNextNode(initNode, nodeArr);
    let nextFilteredArray = filterArr(nextNode, nodeArr);
    getPath(nextNode, nextFilteredArray);
  }

  function removeDuplicates (nodeArray) {
    let nodeSet = new Set(nodeArray);                                // creates a set -> eliminating duplicated elements
    return [...nodeSet];                                             // spreads elements of the set into an array
  }

  function init () {
    setNodes();
    const firstNode = findFirstNode(nodes);
    const firstFilteredNodes = filterArr(firstNode, nodes);
    getPath(firstNode, firstFilteredNodes);
  };

  // the only public function showing the path
  this.showPath = function () {
    if (path.length === 0) {
      throw new Error('circular reference');
    }
    return removeDuplicates(path);
  };

  init();
};

module.exports = Holiday;
