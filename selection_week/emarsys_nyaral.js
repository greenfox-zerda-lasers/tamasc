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

  this.findNonDirectedNode = function (node, array) {
    let nextNode = [];
    array.forEach((e) => {
      if (e.length === 1 && e[0] === node) {
        nextNode = e;
      }
    });
    if (!nextNode) {
      return array.find((e) => {
        return e.length === 1;
      });
    }
    return nextNode;
  };

  this.findDirectedNode = function (node, array) {
    let nextNode = [];
    array.forEach((e) => {
      if (e.length > 1) {
        nextNode = e;
      }
    });
    return nextNode;
  };

  this.findNextNode = function (node, array) {
    if (array.some(e) => {return (e.length === 1 && !!node[1] && node[1] === e[0])}) { // non directed node, which is 
      return
    }
    if (this.findDirectedNode(node, array).length === 2) {
      return this.findDirectedNode(node, array);
    } else if (this.findNonDirectedNode(node, array).length === 1) {
      return this.findNonDirectedNode(node, array);
    } else {
      return;
    }
  };

  this.getPath = function (initNode, nodeArr) {
    console.log('node: ',initNode,'arr: ', nodeArr);
    console.log('path', this.path);
    if (!initNode || nodeArr.length === 0) {
      console.log('return');
      return;
    }
    let nextNode = this.findNextNode(initNode, nodeArr);
    let filteredArr = nodeArr.filter((e) => {
      return e !== nextNode;
    });
    this.path.push(...initNode);
    this.getPath(nextNode, filteredArr);
  };

  this.init = function () {
    this.setNodes();
    this.temp = this.nodes;
    this.getPath(this.nodes[3], this.nodes.filter((e) => {
      return e !== this.nodes[3];
    }));
  }

  this.init();
}

let horvat = new Nyaralas('b => a', 'x', 'v', 'v => x', 'a => v');
// console.log(horvat.path);

// console.log(horvat.path);
// console.log(horvat.findDirectedNode('v', horvat.nodes));
// console.log(horvat.findNonDirectedNode('v', horvat.nodes));
