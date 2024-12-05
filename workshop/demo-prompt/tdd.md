## Demo :: TDD with API

### Step 1
```
As javascript developer, i want to generate unit test with TypeScript and JEST from this code
"""
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
"""

```

### Step 2 :: Steps to Create project
* please, create steps to create project TypeScript + Jest with vite

### Step 3 :: Add more test cases
* Add more test cases for edge cases
* Add more test cases for security issue cases (Injection and Cross-Site Script)

### Step 4 :: More ..
* try to refactor
* try to explain