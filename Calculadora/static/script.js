document.addEventListener('DOMContentLoaded', function() {
    let screen = document.getElementById('expression');
    let expression = '';

    function addToScreen(value) {
        expression += value;
        screen.value = expression;
    }

    function clearScreen() {
        screen.value = '';
        expression = '';
    }

    function calculate() {
        try {
            // Substituímos os caracteres especiais antes de avaliar a expressão
            let sanitizedExpression = expression.replace(/x/g, '*').replace(/÷/g, '/');
            const result = eval(sanitizedExpression);
            screen.value = result;
            expression = '';
        } catch (error) {
            screen.value = 'Error';
            expression = '';
        }
    }

    let buttons = document.querySelectorAll('.keys button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            let buttonValue = this.innerText;
            if (buttonValue === '=') {
                calculate();
            } else if (buttonValue === 'CE') {
                clearScreen();
            } else {
                addToScreen(buttonValue);
            }
        });
    });
});
