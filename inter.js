//  
function func(arr1, arr2){
  let flatted = [arr1, arr2].flat()
  sorted = flatted.sort((a, b) => a - b)
  if (flatted.length % 2 === 0) {
    let num1 = sorted[(Math.floor(sorted.length / 2)) - 1]
    console.log("num1: ", num1)
    let num2 = sorted[(Math.floor(sorted.length / 2))]
    console.log("num2: ", num2)
    return (num1 + num2) / 2
  }

  return sorted[Math.floor(sorted.length / 2)]
}
// func([5,4,7,8,9,15], [5,81,2,4,50])
//  7
//  5
// [5,7]
console.log(func([1,4,7,8,9], [5,81,2,4,50]))
console.log(func([5,4,7,8], [5,81,2,4,50]))