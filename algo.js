// greater Than y
// given two parameters, Y and some array, return the number of values in the array that are greater than y

function greaterThanY(y, arr){
    var count=0;
    for(let i=0; i<arr.length; i++){
        if(arr[i]>y){
            count++;
        }
    }
    return count
}

console.log(greaterThanY(5, [2,4,6,8,10]))

// Average - Create a function that takes a list and returns the average of all the values.
// Example: average([1,2,3,4]) should return 2.5

// declare a function and accept a list of numbers
    // store a total, start at zero
    // loop through the list
        // add values to total
    // return total/length of array

function average(arr){
    var total=0;
    for(let i=0; i<arr.length; i++){
        total += arr[i]
    }
    return total/arr.length
}

console.log(average([1,2,3,4]))