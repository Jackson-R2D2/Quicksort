# Quicksort


# Descrisão
Código que ordena uma lista criado em python

# Como funciona?
Para o algoritmo funcionar é utilizado uma técnica de programação chamado recursão que vai ser a base do nosso código e assim como todo código de recursão teremos um caso base e como pode ver é o "if len(array) < 2" e caso essa condição seja verdadeira vai retornar o próprio array.A base do código é feito utilizando a técnica de "dividir para conquistar" abreviando fica DC que vocẽ pode aplicar para resolver determinados problemas, mas sim sobre pensar em uma solução, vocẽ pode ver isso acontecendo no altoritmo de Euclides que no qual é uma forma para encontrar o maior divisor comum entre dois números e vai dividindo até encontrar o resultado.
No algoritmo teremos um array(provavelmente com elementos desordenados) e vamos dividindo esse array e aplicar a recursão, como pode ver vamos pegar um valor como referencial (o valor que está na variável "meio" que contêm o valor do primeiro elemento da lista) e vamos dividir esse array, passando os valores que são maiores que esse referencial na lista "lista_maior" e os menores na lista "menor" e vamos aplicar a função sort nessas duas listas, por exemplo na lista_menores vamos chamar a função, mas passando essa lista e vai fazer a mesma coisa pegar um referencial e passar os valores maiores em uma lista e os menos em outra lista com base nesse referencial que vai aplicar a função sort neles até eles ficarem com dois elementos e então vamos pegar um valor da lista e outro valor vai ser passado em uma das lista se for maior na lista_maior e se for menor na lista_menor e vamos aplicar a função sort nessa lista e como tám menor que dois elementos vai retornar essa lista.O ponto é que os valores das lsitas (tanto a menor, como a maior) vão ser colocados na "posição correta", ou seja, se for maior vai estar na frente do referencial e se for menor atŕas do referencial  e vamos retornar essa lista para a chamada anterior e colocamos na posição certa também se os valores são menores que o referencial vai ficar atraś do referencial se for maior depois do referencial

# ️  🖥️ Tecnologias usadas

- `Python`

# Autores
<img src="https://user-images.githubusercontent.com/127449144/225768160-cf3f2a2e-f2c6-4961-b22e-6f08e497387c.png" width="200px" height="200px">
<p>Jackson Rodrigues da Silva</p>
