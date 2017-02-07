'use strict';

function QuickUnion(N) {
  this.N = N;
  this.IdArr = createIdArr(N);

  function createIdArr (N) {
    let arr = [];
    for (let i=0; i < N; i++) {
      arr.push(i);
    }
    return arr;
  };

  function findRoot (nodeId, IdArr) {
    while (nodeId !== IdArr[nodeId]) {
      nodeId = IdArr[nodeId];
    }
    return nodeId;
  };

  function unite(nodeId1, nodeId2) {
    let root1 = findRoot(nodeId1, this.IdArr);
    let root2 = findRoot(nodeId2, this.IdArr);
    this.IdArr[root1] = root2;
  };

  function find() {
    return;
  };

  function getGroups() {
    return;
  };

  return {
    IdArr: this.IdArr,
    unite: unite,
    find: find,
    getGroups: getGroups
  };
}


let o = new QuickUnion(5);
console.log(o.IdArr);
o.unite(2, 4);
console.log(o.IdArr);
