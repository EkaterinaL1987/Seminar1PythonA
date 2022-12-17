#Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования
<!DOCTYPE html>
<html lang="en">
 
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
 
<body>
<div><input id="real1" type="number" /> + <input id="img1" type="number" />i</div>
<div><input id="real2" type="number" /> + <input id="img2" type="number" />i</div>
<button onclick="calculate()">Вычислить</button>
    <table>
        <thead>
            <th>Действие</th>
            <th>Результат</th>
        </thead>
        <tbody id="results">
            <tr>
                <td>Сумма</td>
                <td></td>
            </tr>
            <tr>
                <td>Разность</td>
                <td></td>
            </tr>
            <tr>
                <td>Произведение</td>
                <td></td>
            </tr>
            <tr>
                <td>Частное</td>
                <td></td>
            </tr>
        </tbody>
    </table>
    <script>
    function calculate()
        {
            let [results, real1, img1, real2, img2] = "results,real1,img1,real2,img2"
                .split(",").map(id => document.getElementById(id));
            let cplx1 = new Complex(+real1.value, +img1.value), cplx2 = new Complex(+real2.value, +img2.value);
            "add,def,mult,dev".split(",")
                .forEach((ac, i) => results.rows[i].cells[1].textContent = cplx1[ac](cplx2));
        }
 
        function Complex(real, imagine)
        {
            this.real = real;
            this.imagine = imagine;
            // Сложение
            this.add = cplx2 => new Complex(this.real + cplx2.real, this.imagine + cplx2.imagine);
            // Вычитанлие
            this.def = cplx2 => new Complex(this.real - cplx2.real, this.imagine - cplx2.imagine);
            // Умножение
            this.mult = cplx2 =>
            {
                let [{ real: a, imagine: b }, { real: c, imagine: d }] = [this, cplx2];
                return new Complex(a * c - b * d, b * c + a * d);
            };
            // Деление
            this.dev = cplx2 =>
            {
                let [{ real: a, imagine: b }, { real: c, imagine: d }] = [this, cplx2];
                return new Complex((a * c + b * d) / (c * c + d * d), (a * c - b * d) / (c * c + d * d));
            }
            this.toString = () => `${this.real} ${imagine < 0 ? "-" : "+"} ${Math.abs(this.imagine)}i`;
            return this;
        }
 
 
        let cplx1 = new Complex(3, 5);
        let cplx2 = new Complex(2, 8);
 
        console.log("" + cplx1.add(cplx2));
        console.log("" + cplx1.def(cplx2));
        console.log("" + cplx1.mult(cplx2));
        console.log("" + cplx1.dev(cplx2));
    </script>
 
  </body>
</html>
