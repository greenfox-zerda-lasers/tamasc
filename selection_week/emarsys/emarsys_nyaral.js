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
        this.nodes.push([node, node]);
      }
    })
  };

  this.findFirstNode = function (array) {
    let firstNode = [];
    array.forEach((e) => {
      let count = 0;
      let filteredArray = this.filterArr(e, array);
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

  this.filterArr = function (node, arr) {
    return arr.filter((e) => {
      return e !== node;
    });
  };

  this.findNextNode = function (node, array) {
    let nextNode = [];
    array.forEach((e) => {
      if (e[0] === e[1] && node[1] === e[0]) {
        // console.log('jeee node: ', node, ' nextNode: ', e);
        return 'asdas';
      } else if (node[1] === e[0]){
        nextNode = e;
      }
    });
    if (nextNode.length === 0) {
      nextNode = array.find((e) => {
        return e[0] === e[1];
      });
    }
    // console.log('node: ', node, ' nextNode: ', nextNode);
    return nextNode || [];
  };

  this.getPath = function (initNode, nodeArr) {
    if (initNode.length === 0) {
      console.log('return');
      return;
    }
    this.path.push(...initNode);
    let nextNode = this.findNextNode(initNode, nodeArr);
    console.log(initNode, nextNode);
    let nextFilteredArray = this.filterArr(nextNode, nodeArr);
    this.getPath(nextNode, nextFilteredArray);
  };

  this.init = function () {
    this.setNodes();
    const firstNode = this.findFirstNode(this.nodes);
    const firstFilteredNodes = this.filterArr(firstNode, this.nodes);
    this.getPath(firstNode, firstFilteredNodes);
  }

  this.init();
}

let horvat = new Nyaralas('b => a', 'x', 'v', 'v => x', 'a => v', 'm');
console.log(horvat.path);
