


// hello world

function hello(name){ 
    return "Hello, " + ( name || "world") + "!";
} 

console.log(hello())

// madlib function

function madlib(name, subject){
    return name + "'s favorite subject in school is " + subject + ".";

}

console.log(madlib("Dot", "art"))




function tipCalc(bill, serv){
    switch (true){
        case serv == "good":
            return bill * .20;
            break;
        case serv == "fair":
            return bill * .15;
            break;
        case serv == "bad":
            return bill * .10;
            break;
        default: 
            Error("Unsupported input.")

    }
    }
console.log(tipCalc(100, "good"))


// returns total with tip added
function tipAmount(amt, service){
    switch (true){
        case service == "good":
            return amt + (amt * .20);
            break;
        case service == "fair":
            return amt + (amt * .15);
            break;
        case service == "bad":
            return amt + (amt * .10);
            break;
        default: 
            Error("Unsupported input.")

    }
    }
console.log(tipAmount(100, "good"))


// adds split option
function tipSplit(total, srvc, ppl){
    switch (true){
        case srvc == "good":
            return (total + (total * .20)) / ppl;
            break;
        case srvc == "fair":
            return (total + (total * .15)) / ppl;
            break;
        case srvc == "bad":
            return (total + (total * .10))/ppl;
            break;
        default: 
            Error("Unsupported input.")

    }
    }
console.log(tipSplit(100, "good", 4))
