// 1) What's the resulf of OR?
    // 2   




// 2) What's the result of OR'ed alerts?
    // 1 then 2






// 3) What is the result of AND?
    // null




// 4) What is the result of AND'ed alerts?
    // 1 then undefine d



// 5) The result of OR AND OR
    // 3   



// 6) Check the range between
    // if (90 >= userAge && userAge >= 14);


// 7) Check the range outside
    /* 
    My tries:
    if (userAge > 90 || userAge < 14) {

    }
    let outside = !(userAge < 90) 
    outside = (userAge < 14)
    if (outside) {}

    // or

    let outside = !(userAge < 90) ? true : (userAge < 14) ? true : false; 
    */
    // correct answer:
    // if (!(age >= 14 && age <= 90))
    // if (age < 14 || age > 90)