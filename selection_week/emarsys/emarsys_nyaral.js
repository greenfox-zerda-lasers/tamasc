function Nyaralas() {
  const args = [...arguments];
  this.nodes = [];
  this.path = [];

  this.setNodes = function () {
    args.forEach((e) =>  {
      if (e.search(/^\w+\s*(=>)\s*\w+$/) !== -1) {
        const node = [e.match(/\w+$/)[0], e.match(/^\w+/)[0]];
        this.nodes.push(node);
      } else {
        const node = e.match(/^\w+/)[0];
        this.nodes.push([node]);
      }
    })
  };
  // 
  // this.findFirstNode(array) {
  //   array.
  // }

  this.findNonDirectedNode = function(node, array) {
    let nextNode = [];
    array.forEach((e) => {
      let currentNode = (node.length > 1) ? node[1] : node[0];
      if (currentNode === e[0] && e.length === 1) {
        nextNode = e;
      }
    });
    return nextNode;
  };

  this.findIndependentNode = function (node, array) {
    return array.find((e) => {
      return e.length === 1;
    });
  };

  this.findDirectedNode = function (node, array) {
    let nextNode = [];
    array.forEach((e) => {
      if (e.length > 1 && node[node.length -1] === e[0]) {
        nextNode = e;
      }
    });
    return nextNode;
  };

  this.findNextNode = function (node, array) {
    let nextNode = this.findNonDirectedNode(node, array);
    if (!nextNode[0]) {
      nextNode = this.findDirectedNode(node, array);
    }
    if (!nextNode[0]) {
      nextNode = this.findIndependentNode(node, array);
    }
      return nextNode;
  };

  this.getPath = function (initNode, nodeArr) {
    console.log('node: ',initNode,'arr: ', nodeArr);
    this.path.push(...initNode);
    console.log('path: ', this.path);
    if (!initNode[0] || nodeArr.length === 0) {
      console.log('return');
      return;
    }
    let nextNode = this.findNextNode(initNode, nodeArr);
    let filteredArr = nodeArr.filter((e) => {
      return e !== nextNode;
    });
    console.log('nextNode: ', nextNode);
    this.getPath(nextNode, filteredArr);
  };

  this.init = function () {
    this.setNodes();
    this.getPath(this.nodes[3], this.nodes.filter((e) => {
      return e !== this.nodes[3];
    }));
  }

  this.init();
}

let horvat = new Nyaralas('b => a', 'x', 'v', 'v => x', 'a => v','d' , 'b', 'b', 'm => b');
// console.log(horvat.path);
// console.log(horvat.findDirectedNode(['v'], horvat.nodes));
// console.log(horvat.findIndependentNode(['v'], horvat.nodes));
// console.log(horvat.findDuplicatedNode(['v'], horvat.nodes));
