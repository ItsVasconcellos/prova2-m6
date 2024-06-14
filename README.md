# prova2-m6

# Video final 
![](/assets/video.avi)

# 2. Perguntas técnicas
## 2.1. Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.
R: O modelo escolhido para a detecção foi o haarcascade, o qual funciona a partir de detecção de características simples. Sendo assim, ele calcula a diferença da intensidade de regiões de áreas claras e áreas escuras. Existem alguns tipos de identificação, como o cálcuo de características de dois, três e quatro retângulos. Essas características ajudam a identificar bordas, linhas e outras estruturas simples na imagem. 

## 2.2 Considere as seguintes alternativas para resolver o problema de detecção de faces:
- HAAR Cascade
- CNN
- NN Linear
- Filtros de correlação cruzada
### Classifique-os (coloque em ordem) em termos de viabilidade técnica (se é possível resolver o problema), facilidade de implementação e versatilidade da solução. Justifique sua classificação.

R: 
1 - Haar Cascade: É possível solucionar o problema de identificação de faces com o seu uso, como já foi demonstrado diversas vezes. Além disso, sua implementação não exige de muito hardware, permitindo que seja aplicado em dispostivos até mesmo como um arduino. Todavia, sua desvantagem está na eficiência em detectar variações nas faces.
2 - CNN: O seu funcionamento, segmentando a imagens em partes menores e fazendo uma avaliação disso com o todo permite uma grande eficiência na detecção de rostos, porém a sua grande complexidade computacional não o tora uma alternativa tão simples para resolver esse problema. O uso de bibliotecas pode auxiliar na implementação do CNN.
3 - Filtros de correlação cruzada: O filtro de correlação cruzada é eficiente para imagens que possuem elementos extramamente semelhantes, tanto de característica quanto de angulação. Isso se deve ao fato de que ele é pouco versátil, ao ser um filtro que identifica o quão semelhante aquele trecho é  a uma determinada imagem original.
4 - NN Linear: O problema não é tecnicamente possível de ser solúvel em NN linear devido ao fato de que a única camada de neurônios deveria ser capaz de compreender um todo, o que não é possível. 

## 2.3. Considerando as mesmas alternativas acima, faça uma nova classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face.

R:
1 - CNN: As redes neurais permitem lidar com pequenos trechos da imagem, assim  
2 - Filtro de correlação cruzada: Caso fossem implmentado um número n de filtros, contendo diferentes fotos da pessoa alterando expressões faciais, exisitiria a possibilidade de verificar essa alteração, passando os filtros sobre a imagem. 
3 - Haar Cascade: É possível solucionar o problema de identificação de faces com o seu uso, como já foi demonstrado diversas vezes. Além disso, sua implementação não exige de muito hardware, permitindo que seja aplicado em dispostivos até mesmo como um arduino. Todavia, sua desvantagem está na eficiência em detectar variações nas faces. 
4 - NN Linear: Como dito na resposta anterior, o NN Linear não deveria ser levado em consideração para a resolução desse tipo de problema.

## 2.4. A solução apresentada ou qualquer outra das que foram listadas na questão 2.2. tem a capacidade de considerar variações de um frame para outro (e.g. perceber que em um frame a pessoa está feliz e isso influenciar na detecção do próximo frame)? Se não, quais alterações poderiam ser feitas para que isso seja possível?
R: A solução apresentada não leva em conta alterações realizadas de um frame para o outro. A possível implementação que poderia corrigir isso, seria da implementação de uma CNN, a qual receberia informações do filtro de haar cascade, como por exemplo detecção de boca, nariz, olhos, para compreender se está havendo um movimento e uma diminuição de áreas.


## 2.5. (BONUS - não vale nada)
Quem ganha a bola de ouro 2024?
R: Vini JR trará alegria ao seu povo (especialmente para mim, após essa prova... :/ )

# Instruções de execução 

É necessário estar na pasta src para executar o projeto, portanto:
```bash 
cd src/
```

Para executá-lo basta rodar o comando: (caso esteja no windows utilize apenas python)
```bash
python3 main.py
```