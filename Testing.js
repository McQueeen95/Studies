// hello this first javaScript code to me so be nice please i still learning


//console.log("hello");
//to print string we use "" or ' ' its the same 

/*  Concatenating two strings together is actually pretty simple!

"Hello," + " New York City"
Returns: "Hello, New York City" */ 

/*  It is called implicit type coercion and it's a feature of JavaScript.
JavaScript multiplies the 5*10 to become 50 and then changes the number 50 into the string "50",
  so you're adding together the same data type. This then gets combined with the string "Hello".
 You'll learn more about why this happens later in this lesson. */ 

/* To access an individual character, you can use the character's location in the string, called its index. Just put the index of the character inside square brackets (starting with [0] as the first character) immediately after the string. For example:

"James"[0];
Returns: "J" */ 

/*Escaping characters
In JavaScript, you use the backslash to escape other characters.

Escaping a character tells JavaScript to ignore the character's special meaning and just use the literal value of the character. This is helpful for characters that have special meanings like in our previous example with quotes "…".

Because quotes are used to signify the beginning and end of a string, you can use the backslash character to escape the quotes in order to access the literal quote character.

"The man whispered, \"please speak to me.\""
Returns: The man whispered, "please speak to me." */

//console.log("The man whispered, \"please speak to me.\"");

/*Special characters
Quotes aren’t the only special characters that need to be escaped, there’s actually quite a few. However, to keep it simple, here’s a list of some common special characters in JavaScript.

Code	Character
\\	\ (backslash)
\"	'' (double quote)
\'	' (single quote)
\n	newline
\t	tab
The last two characters listed in the table, newline \n and tab \t, are unique because they add additional whitespace to your Strings.
A newline character will add a line break and a tab character will advance your line to the next tab stop.*/

// to print this ("The file located at "C:\\Desktop\My Documents\Roster\names.txt" contains the names on the roster.")
// we write this ("The file located at \"C:\\\\Desktop\\My Documents\\Roster\\names.txt\" contains the names on the roster.")

// Pick a string. Your string can have any number of characters.
//var my_string = "a";

// Calculate the ASCII value of the first character, i.e. the character at the position 0. 
//var ASCII_value = my_string.charCodeAt(0);

// Let us print
//console.log(ASCII_value);

// null refers to the "value of nothing", while undefined refers to the "absence of value".
/* // calculating the square root of a negative number will return NaN
Math.sqrt(-10)

// trying to divide a string by 5 will return NaN
"hello"/5 */ 

/*What is NaN?
NaN stands for "Not-A-Number" and it's often returned indicating an error with number operations.
For instance, if you wrote some code that performed a math calculation,
and the calculation failed to produce a valid number, NaN might be returned.*/

//"1" == 1
//Returns: true

//0 == false
//Returns: true. The == operator is unable to differentiate 0 from false.

//' ' == false
//Returns: true. Both the operands on either side of the == operator are first converted to zero, before comparison.

/*  you do not need to specify data types. Instead,
when your code is interpreted by the JavaScript engine it will automatically be converted into the "appropriate" data type.
This is called implicit type coercion */

/* Strict equality
Instead, in JavaScript it’s better to use strict equality to see if numbers, strings, or booleans, etc.
  are identical in type and value without doing the type conversion first.
  To perform a strict comparison, simply add an additional equals sign = to the end of the == and != operators.*/

/*"1" === 1 // return false */

/* "3" > 1 is true because 3 is greater than 1 (implicit type coercion)
true >= 0 is true because 1 greater than or equal to 0 (implicit type coercion)
1 !== false is true because 1 does not equal false (strict equality)
3 === 3 is true because 3 equals 3 (strict equality) */ 



/* short-circuiting because it describes the event when later arguments in a logical expression are not considered because the first argument already satisfies the condition.*/

/*var balance = 325.00;
var checkBalance = true;
var isActive = false;

if(checkBalance){
  if(isActive && balance > 0){
    console.log("Your balance is $"+balance.toFixed(2)+".");
  }
  else if(isActive == false){
    console.log("Your account is no longer active.");
  }
  else if(balance == 0){
    console.log("Your account is empty.");
  }
  else{
    console.log("Your balance is negative. Please contact bank.");
  }
}
else{
  console.log("Thank you. Have a nice day!");
}*/

/*var flavor = "strawberry";
var vessel = "cone";
var toppings = "cookies";

if((flavor === "vanilla" || flavor ==="chocolate" ) && (vessel ==="cone" || vessel === "bowl" ) && (toppings ==="sprinkles" || toppings === "peanuts") ){
  
    
      console.log("I'd like two scoops of "+flavor+" ice cream in a "+vessel+" with "+toppings+".")
    
  
}*/

/*var shirtWidth = 23;
var shirtLength = 30;
var shirtSleeve = 8.71;

if((shirtWidth < 20 && shirtWidth >= 18) && (shirtLength >=28 && shirtLength < 29) && (shirtSleeve <8.38 && shirtSleeve>=8.13)){
  console.log("S");
}
else if((shirtWidth < 22 && shirtWidth >= 20) && (shirtLength >=29 && shirtLength < 30) && (shirtSleeve <8.63 && shirtSleeve>=8.38)){
  console.log("M");
}
else if((shirtWidth < 24 && shirtWidth >= 22) && (shirtLength >=30 && shirtLength < 31) && (shirtSleeve <8.88 && shirtSleeve>=8.63)){
  console.log("L");
}
else if((shirtWidth < 26 && shirtWidth >= 24) && (shirtLength >=31 && shirtLength < 33) && (shirtSleeve <9.63 && shirtSleeve>=8.88)){
  console.log("XL");
}
else if((shirtWidth < 28 && shirtWidth >= 26) && (shirtLength >=33 && shirtLength < 34) && (shirtSleeve <10.13 && shirtSleeve>=9.63)){
  console.log("2XL");
}
else if((shirtWidth >= 28) && (shirtLength >= 34) && (shirtSleeve>=10.13)){
  console.log("3XL");
}
else{
  console.log("NA");
}*/

// Every value in JavaScript has an inherent boolean value. When that value is evaluated in the context of a boolean expression, the value will be transformed into that inherent boolean value.

/*
if ("") {
    console.log("the value is truthy");
} else {
    console.log("the value is falsy");
} // return "the value is falsy"
*/

/*
Here’s the list of all of the falsy values:
the Boolean value false
the null type
the undefined type
the number 0
the empty string ""
the odd value NaN (stands for "not a number", check out the NaN MDN article)
That's right, there are only six falsy values in all of JavaScript!
and the truthly values are anything not in falsy list.
*/
/*var isGoing , color ;
if(isGoing === true){
  console.log("go")
}
else if (isGoing === false){
  console.log("dont")
}*/

/*The ternary operator provides you with a shortcut alternative for writing lengthy if...else statements.

conditional ? (if condition is true) : (if condition is false)*/

/*var eatsPlants = false;
var eatsAnimals = true;


var category = eatsPlants && eatsAnimals ? "omnivore" : (eatsPlants?"herbivore":(eatsAnimals?"carnivore":"undefined"));


console.log(category);*/

/*var education = 'no high school diploma';
var salary = 0;

switch(education){
  case "no high school diploma" : salary = 25.636;
  console.log("In 2015, a person with "+education+" earned an average of "+salary+"/year.");
  break;
  case "a high school diploma" : salary = 35.256;
  console.log("In 2015, a person with "+education+" earned an average of "+salary+"/year.");
  break;
  case "an Associate's degree" : salary = 41,496;
  console.log("In 2015, a person with "+education+" earned an average of "+salary+"/year.");
  break;
  case "a Bachelor's degree" : salary = 59,124;
  console.log("In 2015, a person with "+education+" earned an average of "+salary+"/year.");
  break;
  case "a Master's degree" : salary = 69,732;
  console.log("In 2015, a person with "+education+" earned an average of "+salary+"/year.");
  break;
  case "a Professional degree" : salary = 89,960;
  console.log("In 2015, a person with "+education+" earned an average of "+salary+"/year.");
  break;
  case "a Doctoral degree" : salary = 84,396;
  console.log("In 2015, a person with "+education+" earned an average of "+salary+"/year.");
}*/

/*var x = 1;

function addTwo() {
  var x = x + 2;
}

addTwo();
x = x + 1;
console.log(x); // return 2 , that x = 2 */

/*var x = 1;

function addTwo() {
  x = x + 2;
}

addTwo();
x = x + 1;
console.log(x); //return 4 , that x = 4 */

/*
What you've learned so far:
If an identifier is declared in global scope, it's available everywhere.
If an identifier is declared in function scope, it's available in the function it was declared in (even in functions declared inside the function).
When trying to access an identifier, the JavaScript Engine will first look in the current function. If it doesn't find anything, it will continue to the next outer function to see if it can find the identifier there. It will keep doing this until it reaches the global scope.
Global identifiers are a bad idea. They can lead to bad variable names, conflicting variable names, and messy code. 
*/

/*sayHi("Julia");

function sayHi(name) {
  console.log(greeting + " " + name);
  var greeting;
} // return undefined Julia

sayHi("Julia");

function sayHi(name) {
  console.log(greeting + " " + name);
  var greeting = "Hello";
} // return undefined Julia

function sayHi(name) {
  var greeting = "Hello";
  console.log(greeting + " " + name);
}

sayHi("Julia"); 
// return Hello Julia*/

// variable assignments are not hoisted

/*buildTriangle(3);

function makeLine(length){
  var line ="";
  for(var i = 0 ; i < length ; i++){
    line+="* ";
  }
  return line +"\n";
}
function buildTriangle(width){
  var Triangle="";
  for(var i = 1 ; i <= width ; i++){
    Triangle+=makeLine(i);
  }
  return Triangle;
}*/

/*
Function expressions and hoisting
Deciding when to use a function expression and when to use a function declaration can depend on a few things, and you will see some ways to use them in the next section. But, one thing you'll want to be careful of is hoisting.

All function declarations are hoisted and loaded before the script is actually run. Function expressions are not hoisted, since they involve variable assignment, and only variable declarations are hoisted. The function expression will not be loaded until the interpreter reaches it in the script.*/

/*
// anonymous function expression
var doSomething = function(y) {
  return y + 1;
}; unnamed(anonymous)

// named function expression
var doSomething = function addOne(y) {
  return y + 1;
}; named
*/
//var x = ["abcd",1,true,undefined,null,"all of data type"];

// here u can find all functions of Arrays [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array]

/*
Following is the syntax of splice() method: arrayName.splice(arg1, arg2, item1, ....., itemX); where,

arg1 = Mandatory argument. Specifies the starting index position to add/remove items. You can use a negative value to specify the position from the end of the array e.g., -1 specifies the last element.

arg2 = Optional argument. Specifies the count of elements to be removed. If set to 0, no items will be removed.

item1, ....., itemX are the items to be added at index position arg1

docoment about splice[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice]
*/

/*
forEach() => [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach]
map() => [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map]


/*var x = function(num){
  return num + 5;
}
console.log(x(5));*/

/*function sum(num){
  return num+5;
};
console.log(sum(5));*/

/*console.log(buildTriangle(10));

function makeLine(length){
  var line ="";
  for(var i = 0 ; i < length ; i++){
    line+="* ";
  }
  return line +"\n";
}
function buildTriangle(width){
  var Triangle="";
  for(var i = 1 ; i <= width ; i++){
    Triangle+=makeLine(i);
  }
  return Triangle;
}*/

/*function cat(){
  //console.log(meow(2)); meow is not a function , he can't see it becase its an anonymous function
  console.log(purr());
  var meow = function(max){
    var mess="";
    for(var i = 0 ; i < max ; i++){
      mess+=" meow ";
    }
    return mess;
  }
  function purr(){
    return "purrrr";
  }
}
cat();*/


/*function movies(anyfunc, name) {
  anyfunc(name);
}

// call the movies function, pass in the function and name of movie
movies(function displayFavorite(movieName) {console.log("My favorite movie is " + movieName);}, "Finding Nemo");
*/

/*var laugh = function(numOfHaha){
  var ha = "";
  for(var i = 0 ; i < numOfHaha ; i++){
    ha+="ha";
  }
  return ha+"!";
}

console.log(laugh(10));*/

/*var cry = function crying(){
  console.log("boohoo!");
}
cry(); // return boohoo!*/

/*function emotions(myString, haFunc) {
  console.log("I am " + myString + ", " + haFunc(5));
}

emotions("happy" ,function(numOfHaha){
  var ha = "";
  for(var i = 0 ; i < numOfHaha ; i++){
    ha+="ha";
  }
  return ha+"!";
}); */

/*var y = [[1,2,3] , ["mona" , "&" , "world"] , [true,false],[]];

for (var i = 0 ; i < y.length ; i++){
  for(var z = 0 ; z < y.length ; z++){
    if(y[i][z] == undefined){
      break;
    }
    else{
      console.log(y[i][z]);
    }
  }
}*/

/*var captain = "Mal";
var second = "Zoe";
var pilot = "Wash";
var companion = "Inara";
var mercenary = "Jayne";
var mechanic = "Kaylee";

var crew = [captain,second,pilot,companion,mercenary,mechanic];
console.log(crew);


console.log(crew.push("nice mate"))*/

/*var rainbow = ['Red', 'Orange', 'Blackberry', 'Blue'];

rainbow.splice(2,1,"Yellow","Green");
rainbow.splice(5,0,"Purple");
console.log(rainbow);*/

/*var team = ["Oliver Wood", "Angelina Johnson", "Katie Bell", "Alicia Spinnet", "George Weasley", "Fred Weasley", "Harry Potter"];

function hasEnoughPlayers(array){
  if(array.length < 7)
    return false ;
  else
    return true;
}
console.log(hasEnoughPlayers(team));*/

/*var h = ["a","b","c"]

console.log(h.join(''));*/


/*words = ["cat", "in", "hat"];
words.forEach(function(word, num, all) {
  console.log("Word " + num + " in " + all.toString() + " is " + word);
});*/

/*var test = [12, 929, 11, 3, 199, 1000, 7, 1, 24, 37, 4,
  19, 300, 3775, 299, 36, 209, 148, 169, 299,
  6, 109, 20, 58, 139, 59, 3, 1, 139];

test.forEach((element,index) => {
  if(element % 3 === 0){
    test[index]+=100;
  }
});
test.forEach(function(element,index){
  if(element%3===0){
    test[index]+=100;
  }
})
console.log(test);*/

/*var donuts = ["jelly donut", "chocolate donut", "glazed donut"];

var improvedDonuts = donuts.map(function(donut) {
  donut += " hole";
  donut = donut.toUpperCase();
  return donut;
});

console.log(donuts);
console.log(improvedDonuts)
*/

/*var bills = [50.23, 19.12, 34.01,100.11, 12.15, 9.90, 29.11, 12.99,10.00, 99.22, 102.20, 100.10, 6.77, 2.22];

//var totals = bills.map(element => Number((element+((15/100)*element)).toFixed(2)))

var totals = bills.map(function(element){
  element= Number((element+((15/100)*element)).toFixed(2));
  return element;
})

console.log(bills);
console.log(totals);
*/


/*var numbers = [
  [243, 12, 23, 12, 45, 45, 78, 66, 223, 3],
  [34, 2, 1, 553, 23, 4, 66, 23, 4, 55],
  [67, 56, 45, 553, 44, 55, 5, 428, 452, 3],
  [12, 31, 55, 445, 79, 44, 674, 224, 4, 21],
  [4, 2, 3, 52, 13, 51, 44, 1, 67, 5],
  [5, 65, 4, 5, 5, 6, 5, 43, 23, 4424],
  [74, 532, 6, 7, 35, 17, 89, 43, 43, 66],
  [53, 6, 89, 10, 23, 52, 111, 44, 109, 80],
  [67, 6, 53, 537, 2, 168, 16, 2, 1, 8],
  [76, 7, 9, 6, 3, 73, 77, 100, 56, 100]
];

for(var r = 0 ; r < numbers.length ; r++){
  for(var c = 0 ; c < numbers.length; c++){
    if(numbers[r][c] % 2 === 0)
      numbers[r][c] = "even";
    else
      numbers[r][c] = "odd";
  }
}*/

/*var umbrella = {
  color: "pink",
  isOpen: true,
  open: function() {
      if (umbrella.isOpen === true) {
          return "The umbrella is already opened!";
      } else {
          umbrella.isOpen = true;
          return "Julia opens the umbrella!";
      }
  },
  close: function(){
      if (umbrella.isOpen === true){
        umbrella.isOpen=false;
        return "Julia closes the umbrella!";
      }
      else{
        return "The umbrella is already closed!";
      }
  }
};

console.log(umbrella["isOpen"]);
console.log(umbrella.isOpen);
*/

/*var garage = {
  fireTruck:{
    model:"Mercedis",
    color:"red",
    wheels:6,
    isEMG:false,
    setEMG:function(status){
      this.isEMG = status;
      if(status === true)
        return "fireTruck in its way to the fire";
      else
        return "false alarm calm down";
    }
  },
  raceCar:{
    model:"BMW",
    color:"Black",
    hp:600,
    McQueen:function nice(){
      return "Kachoowwww";
    }
  }
};

console.log(garage.fireTruck.model);
console.log(garage.fireTruck.setEMG(true))
console.log(garage.raceCar.McQueen())*/


/*var breakfast = {
  name: "The Lumberjack",
  price: "$"+9.95,
  ingredients: ["eggs","sausage","toast","hashbrowns","pancakes"]
};
// console.log(breakfast.name)
// console.log(breakfast.price)
// console.log(breakfast.ingredients)
console.log(breakfast)*/

/*var savingsAccount = {
  balance: 1000,
  interestRatePercent: 1,
  deposit: function addMoney(amount) {
      if (amount > 0) {
          savingsAccount.balance += amount;
      }
  },
  withdraw: function removeMoney(amount) {
      var verifyBalance = savingsAccount.balance - amount;
      if (amount > 0 && verifyBalance >= 0) {
          savingsAccount.balance -= amount;
      }
  },
  printAccountSummary:function(){
    return "Welcome!\nYour balance is currently $"+this.balance+" and your interest rate is "+this.interestRatePercent+"%.";
  }
};

console.log(savingsAccount.printAccountSummary());
*/

/*var facebookProfile = {
  name:"McQueen",
  friends:9500,
  messages: ["hufff, OKAAAYY here we go focus","Speed,I am speed","1 Winner 42 Losers , I eat losers on breakfast","BREAKFAST! , maybe i should have breakfast","no no foucs , I am fast than faster","I AM LIGHTNING"],
  postMessage: function(meesage){
    this.messages.push(meesage);
  },
  deleteMessage: function(index){
    this.messages.splice(index,1);
  },
  addFriend: function(){
    ++(this.friends);
  },
  removeFriend: function(){
    if(this.friends > 0)
    --(this.friends);
  }
};

/*var donuts = [
  { type: "Jelly",
    cost: 1.22
  },
  { type: "Chocolate",
    cost: 2.45 
  },
  { type: "Cider",
    cost: 1.59 
  },
  { type: "Boston Cream",
    cost: 5.99 
  }
];

donuts.forEach((element,index) => {
  console.log(donuts[index].type+" donuts cost $"+element.cost+" each")
});

donuts.forEach(function(donut){
  console.log(donut.type+" donuts cost $"+donut.cost+" each")
});*/

/*
console.log("yaso" != "yaso")
var x = 1;
function addTwo(){
  x  = x +2 ;
}
addTwo();
x = x + 1 ;
console.log(x)
*/
/*
let and const
Variables declared with let and const eliminate this specific issue of hoisting because they’re scoped to the block, not to the function.
Previously, when you used var, variables were either scoped globally or locally to an entire function scope.

If a variable is declared using let or const inside a block of code (denoted by curly braces { }),
then the variable is stuck in what is known as the temporal dead zone until the variable’s declaration is processed. 
This behavior prevents variables from being accessed only until after they’ve been declared.
*/

/*
let and const also have some other interesting properties.

Variables declared with let can be reassigned, but can’t be redeclared in the same scope.
Variables declared with const must be assigned an initial value,
but can’t be redeclared in the same scope, and can’t be reassigned.
*/

/*const student = {
  name: 'Richard Kalehoff',
  guardian: 'Mr. Kalehoff'
};

const teacher = {
  name: 'Mrs. Wilson',
  room: 'N231'
}*/

/*let note = teacher.name + ',\n\n' +
  'Please excuse ' + student.name + '.\n' +
  'He is recovering from the flu.\n\n' +
  'Thank you,\n' +
  student.guardian;

  console.log(note);*/

  // Template Literals : are essentially string literals that include embedded expressions.

  // let message = `${student.name} please see ${teacher.name} in ${teacher.room} to pick uup`
  // console.log(message)
  /*let note = `${teacher.name},

  Please excuse ${student.name}.
  He is recovering from the fluu.
  
  Thank you,
  ${student.guardian}`
  console.log(note);*/
/*
  const cheetah = {
    name: 'Cheetah',
    scientificName: 'Acinonyx jubatus',
    lifespan: '10-12 years',
    speed: '68-75 mph',
    diet: 'carnivore',
    summary: 'Fastest mammal on land, the cheetah can reach speeds of 60 or perhaps even 70 miles (97 or 113 kilometers) an hour over short distances. It usually chases its prey at only about half that speed, however. After a chase, a cheetah needs half an hour to catch its breath before it can eat.',
    fact: 'Cheetahs have “tear marks” that run from the inside corners of their eyes down to the outside edges of their mouth.'
};

// creates an animal trading card
function createAnimalTradingCardHTML(animal) {
    const cardHTML = `<div class="card">
        <h3 class="name">${animal.name}<h3>
        <img src="${animal.name}.jpg" alt="${animal.name}" class="picture">
        <div class="description">
            <p class="fact"> ${animal.fact}<p>
            <ul class="details">
                <li><span class="bold">Scientific Name</span>: ${animal.scientificName}</li>
                <li><span class="bold">Average Lifespan</span>: ${animal.lifespan}</li>
                <li><span class="bold">Average Speed</span>: ${animal.speed}</li>
                <li><span class="bold">Diet</span> ${animal.diet}</li>
            </ul>
            <p class="brief">${animal.summary}</p>
        </div>
    </div>`;
    return cardHTML;
}

console.log(createAnimalTradingCardHTML(cheetah));
*/

/*
Destructuring: 
borrows inspiration from languages like Perl and Python by allowing you to specify the elements you want to extract from an array or object on the left side of an assignment. 
It sounds a little weird, but you can actually achieve the same result as before, but with much less code;
and it's still easy to understand.
*/

/*onst point = [10, 25, -34];
const [x, y, z] = point;
const [a, ,c] = point
console.log(x, y, z);
console.log(a,c);

const gemstone = {
  type: 'quartz',
  color: 'rose',
  carat: 21.29
};

//const {type, color, carat} = gemstone;

//console.log(type, color, carat);
let {color} = gemstone;
console.log(color , gemstone.color);*/

/*const circle = {
  radius:10,
  color:"red",
  getArea: function(){
    return Math.PI*this.radius*this.radius;
  },
  getCircumference: function(){
    return 2*this.radius*Math.PI;
  }
};

let {radius,getArea,getCircumference}=circle;

console.log(getArea()); // print Nan because Calling getArea() will return NaN. When you destructure the object and store the getArea() method into the getArea variable, it no longer has access to this in the circle object which results in an area that is NaN.
*/

/*const things = ['red', 'basketball', 'paperclip', 'green', 'computer', 'earth', 'udacity', 'blue', 'dogs'];
let [one, , ,two, , , ,three, ] = things;
//console.log(one,two,three);
const colors = `List of Colors
1. ${one}
2. ${two}
3. ${three}`;
console.log(colors);*/


/*let type = 'quartz';
let color = 'rose';
let carat = 21.29;
const gemstone = {
  type: type,
  color: color,
  carat: carat,
  methodName:function(){
    //....
  }
};
// bad way to make object like this 
// const gemstone = {type,
//       color,
//       carat,
//       methodName(){
//         // body 
//       }
//     };
console.log(gemstone);*/
// the right way,

/*let buttons = [1,2,3,4,5,6,7,8];

for (const i in digits){
  console.log(digits[i]);
} // for .. in loop

for (const button of buttons){
  console.log(button);
}// for .. of loop
*/

// Array.prototype.decimalfy = function() {
//   for (i = 0; i < this.length; i++) {
//     this[i] = this[i].toFixed(2);
//   }
// };

// function Initcap(word){
//   return word.charAt(0).toUpperCase()+word.slice(1);
// }

//const days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];


// for (const day of days){
//   console.log(Initcap(day));
// }

//console.log(...days);

// spread operator


// const fruits = ["apples", "bananas", "pears"];
// const vegetables = ["corn", "potatoes", "carrots"];

// const produce = [...fruits,...vegetables];

// console.log(...produce);

// Rest parameter

/*const order = [20.17, 18.67, 1.50, "cheese", "eggs", "milk", "bread"];
const [total, subtotal, tax, ...items] = order;
console.log(total, subtotal, tax, items);
console.log(items)*/

/*function Rest(...items){
  for(const item of items){
    console.log(item);
  }
}

Rest("cheese","potato","pizza","cola");*/

// variadic function

/*function sum(...nums) {
  let total = 0;  
  for(const num of nums) {
    total += num;
  }
  return total;
}

console.log(sum(1,3,4,5,3,6,100,42,432));*/

/*function average(...nums){
  let total =0;
  let numOfThem = 0
  for(const num of nums){
    total+=num;
  }
  if(nums.length === 0){
    return 0;
  }
  else{
  return total/nums.length;
  }
}

console.log(average(2, 6));
console.log(average(2, 3, 3, 5, 7, 10));
console.log(average(7, 1432, 12, 13, 100));
console.log(average());*/
// =====================================================
// DOM
/*
The DOM is standardized by the W3C. There are a number of specifications that make up the DOM, here are few:

Core Specification
Events Specification
Style Specification
Validation Specification
Load and Save Specification
*/

// console.log("hello, let's get started!");

// document.getElementById('footer');
// Parameters
// id
// The ID of the element to locate. The ID is case-sensitive string which is unique within the document; only one element may have any given ID.

// Return value
// An Element object describing the DOM element object matching the specified ID, or null if no matching element was found in the document.

// (https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById)
// for more info


// select all elements that have the class "accent-color"
// document.getElementsByClassName('accent-color');

// select all "span" elements
// document.getElementsByTagName('span');
// Further Research
// .getElementsByClassName(https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName) on MDN
// .getElementsByTagName(https://developer.mozilla.org/en-US/docs/Web/API/Element/getElementsByTagName) on MDN

// ======================================================================================================

// Node Interface(OOP)

//const a = document.getElementById('para');
//Node.Instance_properties
//a.baseURI ==> return the URL of your page
//Node.Instance_methods
//a.appendChild() ==> Adds the specified childNode argument as the last child to the current node
// for all properties and methods (https://developer.mozilla.org/en-US/docs/Web/API/Node)

// element Interface(OOP)
// for more details(https://developer.mozilla.org/en-US/docs/Web/API/Element)
//$0.className ==> the name of its $0 class
//$0.hasAttribute('class'); ==> true if its$0 has class

/*
you can use the document object to select an element, then you can call.
getElementsByClassName() on that element to receive a list of elements with the class name that are descendents of that specific element!
*/ 
// selects the DOM element with an ID of "sidebar"
// const sidebarElement = document.getElementById('sidebar');

// searches within the "sidebar" element for any elements with a class of "sub-heading"
// const subHeadingList = sidebarElement.getElementsByClassName('sub-heading');

//To check out all of the different interfaces, click here:(https://developer.mozilla.org/en-US/docs/Web/API)

/*
// find and return the element with an ID of "header"
document.querySelector('#header');

// find and return the first element with the class "header"
document.querySelector('.header');

// find and return the first <header> element
document.querySelector('header');

// to find more than something
document.querySelector('p#id'); ==> this find p and has id = #id

more details in here(https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
*/

/*
The querySelectorAll Method
The .querySelector() method returns only one element from the DOM (if it exists). 
However, there are definitely times when you will want to get a list of all elements with a certain class or all of one type of element (e.g. all <tr> tags). 
We can use the .querySelectorAll() method to do this!

// find and return a list of elements with the class "header"
document.querySelectorAll('.header');

// find and return a list of <header> elements
document.querySelectorAll('header');
for more details(https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)
*/
/*const nodeListOfElements = document.querySelectorAll('h2');
for(let i = 0; i < nodeListOfElements.length;i++){
  console.log('i is ' + i );
  console.log(nodeListOfElements[i]);
}// so this will loop over every item in the nodeListOfElements list*/

//E.X
/*Write the .querySelectorAll() code to find all paragraph elements that are descendents of elements that have the class: articles
document.querySelectorAll('.articles p');
*/

//======================================================================================
// CREATING CONTENT WITH JAVASCRIPT


//E.X:

const a = document.querySelector('.card') // get first class that's name is 'card'
const b = document.getElementsByClassName('card')[0]// get first class thats called 'card'

// // to use it ==>
// b.innerHTML //  >>> gets the html content

//.outerHTML represents the HTML element itself, as well as its children.

//<h1 id="pick-me">Greetings To <span>All</span>!</h1>

const innerResults = document.querySelector('#pick-me').innerHTML;
console.log(innerResults); // logs the string: "Greetings To <span>All</span>!"

const outerResults = document.querySelector('#pick-me').outerHTML;
console.log(outerResults); // logs the string: "<h1 id="pick-me">Greetings To <span>All</span>!</h1>"

// document.querySelector('.card').textContent ==> Node.textContent
/*
textContent gets the content of all elements, including <script> and <style> elements. 
In contrast, innerText only shows "human-readable" elements.
textContent returns every element in the node. 
In contrast, innerText is aware of styling and won't return the text of "hidden" elements.
Moreover, since innerText takes CSS styles into account, reading the value of innerText triggers a reflow to ensure up-to-date computed styles. 
(Reflows can be computationally expensive, and thus should be avoided when possible.)
Both textContent and innerText remove child nodes when altered, but altering innerText in Internet Explorer (version 11 and below) also permanently destroys all descendant text nodes. 
It is impossible to insert the nodes again into any other element or into the same element after doing so.
*/

/*
We just saw that passing text that contains HTML characters to .textContent will not display the content as HTML. Instead, it will still display everything as text - even the HTML characters!

If you'd like to update an element, including its HTML, then you need to use the .innerHTML property:
*/
// .innerText and .textContent
/*
.innerText will get the visible text of the element. This is an important distinction! If CSS is used to hide any text inside that element, .innerText will not return that text, while .textContent will return it. And it's not just the hiding/showing nature of CSS that .innerText adheres to, .innerText will also honor changes to things like capitalization.

.textContent and .innerText. .textContent completely ignores any CSS styling and returns all of the element's HTML just as it's listed in the HTML. On the other hand, the .innerText property will take CSS styling into consideration and will return the text that is visibly rendered on the page.
*/

//=============================================================================
document.createElement('p');
// more details (https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)

const newSpan = document.createElement('span');
newSpan.textContent ="this new span , okk!";
const elementWeWantToModify = document.querySelector('#id')
elementWeWantToModify.appendChild(newSpan) // from elementWeWan... we append the new span at the end of element..
//  When you're using the .appendChild() method, it must be called on an existing element
​// for more details on appendChild() >> (https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)

// another ex. of .appendChild()
const one = document.createElement('p'); // we created the paragraph element


const text = document.createTextNode('sorry I forgot to add this p in the html , so I add it by javaScript'); // we created
one.appendChild(text); // we append the text node to the element 
// or we just update the text by .textContent
one.textContent = "'sorry I forgot to add this p in the html , so I add it by javaScript"

document.body.appendChild(one) // we append the element inculding the text to the DOM (body)
// for more details on document.createTextNode(https://developer.mozilla.org/en-US/docs/Web/API/Document/createTextNode)

//const mainHeading = document.querySelector('#main-heading');
const otherHeading = document.querySelector('#other-heading');
const excitedText = document.createElement('span');

excitedText.textContent = '!!!';
mainHeading.appendChild(excitedText); // text gonna be added here first
otherHeading.appendChild(excitedText); // then it gonna be added here
// can't be at two places in the same time (The .appendChild() method will move an element from its current position to the new position.)

// element.insertAdjacentHTML(position,text)
// two arguments are (the location of the HTML) and (the HTML text that is going to be inserted)

// first arg. 
/*
beforebegin – inserts the HTML text as a previous sibling
afterbegin – inserts the HTML text as the first child
beforeend – inserts the HTML text as the last child
afterend – inserts the HTML text as a following sibling
*/
// EX.
/*

<!-- beforebegin -->
<p>
    <!-- afterbegin -->
    Existing text/HTML content
    <!-- beforeend -->
</p>
<!-- afterend -->

*/
// more details (https://developer.mozilla.org/en-US/docs/Web/API/Element/insertAdjacentHTML)
// how we use it >>

const main = document.querySelector('#main-heading');
const htmlTextToAdd = '<h2>Skydiving is fun!</h2>';

main.insertAdjacentHTML('afterend', htmlTextToAdd);

// some notes
/*
if an element already exists in the DOM and this element is passed to .appendChild(), the .appendChild() method will move it rather than duplicating it
an element's .textContent property is used more often than creating a text node with the .createTextNode() method
the .insertAdjacentHTML() method's second argument has to be text, you can't pass an element
*/
//========================================================================================
// Node.removeChild()
//<parent-element>.removeChild(<child-to-remove>);
parent.removeChild(parent.firstElementChild);

// EX 2
let g = document.querySelector('#child');
g.parentElement.removeChild(g) // by accessing the child only we remove it
// an element uses itself to remove itself from its parent
// more details(https://developer.mozilla.org/en-US/docs/Web/API/Node/removeChild)

//element.remove()
document.querySelector('#child').remove();
// more details here (https://developer.mozilla.org/en-US/docs/Web/API/Element/remove)
//The difference is that with .removeChild() must be called on the parent of the element being removed and must be passed the child to be removed, while .remove() can be called directly on the element to delete.

//about .firstChild and .firstElementChild 
/*
The difference between .firstChild and .firstElementChild, is that .firstElementChild will always return the first element, while .firstChild might return whitespace (if there is any) to preserve the formatting of the underlying HTML source code.
*/


//=========================================================================================================================
// details about specificity of CSS (https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)

// to access an element's style attribute use:
// HTMLElement.style.property = 'value'; // to set one style at a time
let u = document.querySelector('.class');
u.style.fontSize = '20px';
//HTMLElement.style.cssText='prop:value; prop2:value2;....; '
let h = document.querySelector('#id');
h.style.cssText='color:red; background-color: black; font-size:20px;';
// HTMLElement.setAtttibute('style','prop:value; ; ;')
h.setAttribute('style','font-size:20px;');

// EX for set ID by setAttribue()
// const mainHeading = document.querySelector('h1');

// add an ID to the heading's sibling element
mainHeading.nextElementSibling.setAttribute('id', 'heading-sibling');

// use the newly added ID to access that element
document.querySelector('#heading-sibling').style.backgroundColor = 'red';


// const mainHeading = document.querySelector('#main-heading');

// store the list of classes in a variable
// const listOfClasses = mainHeading.className;

// logs out the string "ank-student jpk-modal"
console.log(listOfClasses);
// The .className property returns a space-separated string of the classes. This isn't the most ideal format, unfortunately. We can, however, convert this space-separated string into an array using the JavaScript string method, .split():

const arrayOfClasses = listOfClasses.split(' ');

// logs out the array of strings ["ank-student", "jpk-modal"]
console.log(arrayOfClasses);

// .classList
<h1 id="main-heading" class="ank-student jpk-modal">Learn Web Development at Udacity</h1>
const mainHeading = document.querySelector('#main-heading');

// store the list of classes in a variable
const listOfClasses = mainHeading.classList;

// logs out ["ank-student", "jpk-modal"]
console.log(listOfClasses);

/*
The .classList property has a number of properties of its own. Some of the most popularly used ones are:

.add() - to add a class to the list
.remove() - to remove a class from the list
.toggle() - to add the class if it doesn't exists or remove it from the list if it does already exist
.contains() - returns a boolean based on if the class exists in the list or not
*/
// for more details(https://developer.mozilla.org/en-US/docs/Web/API/Element/classList)





































