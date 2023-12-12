export const removeItemOnce = (arr:any[], value:any) => {
    const index = arr.indexOf(value);
    if (index > -1) {
    arr.splice(index, 1);
    }
    return arr;
  }
     
  export const removeItemAll = (arr:any[], value:any) => {
    let i = 0;
    while (i < arr.length) {
      if (arr[i] === value) {
        arr.splice(i, 1);
      } else {
        ++i;
      }
    }
    return arr;
  }