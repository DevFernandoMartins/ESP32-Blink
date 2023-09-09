# ESP32-Blink
Exemplo pisca-pisca (Blink), no ESP32 usando MicroPython

 <p align="center">
 <img src=https://i.imgur.com/uXOMc90.gif)>
</p>
      O exemplo liga o led embutido, e um led externo e após 0.8s ele desliga e entra em loop, ligando e desligando... esse intervalo pode ser modificado na linha 14 do arquivo main.py ...

## Montagem
<p align="center">
 <img src=https://i.imgur.com/IjUbu8k.png>
</p>

#### Material Necessário
- 1x ESP32
- 1x LED
- 1x Resistor 220 Ω
- 2x Jumpers

Conecte o jumper na saída digital 2 do ESP32 no terminal positivo do LED, em seguida conecte o terminal negativo do LED no resistor, no outro terminal do resistor insira no pino GND do ESP32 

## Como utilizar
 
Baixe o arquivo main.py usando o comando seguinte no seu terminal
```shell
git clone https://github.com/DevFernandoMartins/ESP32-Blink.git
 ```
Abra o diretório que foi instalado
 ```shell
 cd ESP32-Blink
 ```
 Realize o upload do main.py em seu ESP32...

 ## Contribuindo

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorias, por favor, entre em contato via instagram [@DevFernandoMartins](https://instagram.com/DevFernandoMartins)

##
#### Copyright © 2023 / [Fernando Martins](https://github.com/DevFernandoMartins)

A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia deste arquivo, sem restrição nos direitos de usar, copiar, modificar ou mesclar.
