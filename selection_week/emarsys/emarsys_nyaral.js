function Nyaralas() {
  const args = [...arguments];
  let nodes = [];
  let path = [];

  // Create data structure (nodes) from arguments (eg: 'a => b' --> [a, b], 'a' --> [a, a],)
  setNodes = function () {
    args.forEach((e) =>  {
      if (e.search(/^\w+\s*(=>)\s*\w+$/) !== -1) {
        const node = [e.match(/\w+$/)[0], e.match(/^\w+/)[0]];
        nodes.push(node);
      } else {
        const node = e.match(/^\w+/)[0];
        nodes.push([node, node]);
      }
    })
  };

  // Find first node, which has no dependency
  findFirstNode = function (array) {
    let firstNode = [];
    array.forEach((e) => {
      let count = 0;
      let filteredArray = filterArr(e, array);
      filteredArray.forEach((p) => {
        if (p[1] === e[0]) {
          count++;
        }
      })
      if (count === 0) {
        firstNode = e;
      }
    });
    return firstNode;
  };

  // Removing a node elemenet from an array
  filterArr = function (node, array) {
    return arraz.filter((e) => {
      return e !== node;
    });
  };

  // Finding the next node in the array
  findNextNode = function (node, array) {
    let nextNode = [];
    for (let i = 0, l = array.length; i < l; i++) {
      if (array[i][0] === array[i][1] && node[1] === array[i][0]) {  // first case, finding a nondirected node next to
        return array[i];                                             // the given node --> avoiding multiple occurrence
      } else if (node[1] === array[i][0]) {                          // second case, finding a directed node next to the
        nextNode = array[i];                                         // given node
      }
    }
    if (nextNode.length === 0) {                                     // last case, finding independent nodes
      nextNode = array.find((e) => {
        return e[0] === e[1];
      });
    }
    return nextNode || [];
  };

  // Recursive function, which pushes nodes into the path variable
  getPath = function (initNode, nodeArr) {
    if (initNode.length === 0) {                                    // basecase
      return;
    }
    path.push(...initNode);
    let nextNode = findNextNode(initNode, nodeArr);
    let nextFilteredArray = filterArr(nextNode, nodeArr);           // removing from the node array the next node
    getPath(nextNode, nextFilteredArray);                           // gets called with the next node, and the next node array
  };

  init = function () {
    setNodes();
    const firstNode = findFirstNode(nodes);
    const firstFilteredNodes = filterArr(firstNode, nodes);
    getPath(firstNode, firstFilteredNodes);
  }

  // the only public function showing the path
  this.showPath = function () {
    let pathSet = new Set(path);                                     // creates a set -> eliminating duplicated elements
    return [...pathSet];                                             // spreads elements of the set into an array
  }

  init();

  return {
    showPath: this.showPath
  }
}

let horvat = new Nyaralas('4 => 3', '1', '4', '2 => 1', '2 => 1', '3 => 2', '7', '6', '6', '6 => 5', '5 => 7');
console.log(horvat.showPath());