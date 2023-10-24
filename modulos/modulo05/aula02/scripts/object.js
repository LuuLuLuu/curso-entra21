// 1) Hello, Object
// const user = {};
// user['name'] = 'John';
// user['surname'] = 'Smith';
// user['name'] = 'Peter';
// delete user.name;




// 2) Check for emptiness
// My attempt:
// const schedule = {};
// const isEmpty = (element) => {
//     return(element === '' || element === null) ? true : false;
// }
// (function(x){
//     return isEmpty(x) ? alert(true) : alert(false);
// })(schedule);

// The answer:
// function isEmpty(obj) {
//     for (let key in obj) {
//       // if the loop has started, there is a property
//       return false;
//     }
//     return true;
//   }




// 3) Sum object properties
let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
  }
salaries.reduce((acumulador, elemento) => , 0)