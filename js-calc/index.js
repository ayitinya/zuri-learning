let num1;
let num2;
let operand;

const getNumber = (number) => {
    let correctInput = false
    let num;
    while (!correctInput) {
        num = prompt(`Enter a number: ${number}`)
        num = Number(num)
        if (!Number.isNaN(num))  {
            correctInput = true
        } else {
            alert("You entered an invalid number")
        }
    }
    return num
}

num1 = getNumber(1)
num2 = getNumber(2)

let correctInput = false;
while (!correctInput) {
    operand = prompt("Enter the sign: ")

    switch (operand) {
        case "+":
            alert(`The answer is ${num1 + num2}`)
            correctInput = true
            break;
            case "-":
            alert(`The answer is ${num1 - num2}`)
            correctInput = true
            break;
            case "/":
            alert(`The answer is ${num1 / num2}`)
            correctInput = true
            break;
            case "*":
            alert(`The answer is ${num1 * num2}`)
            correctInput = true
            break;

        default:
            alert("You did not enter a valid sign")
            break;
    }
}

