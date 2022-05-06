## Desafio 02 | Quanam

### Introdução

Quanam é uma federação internacional de empresas cujo objetivo é a inovação e a gestão do conhecimento para o benefício dos clientes e da comunidade através da consultoria empresarial, gestão e aplicação de tecnologias de ponta em diferentes segmentos.

A Quanam mantém diversas atividades a nível internacional, possui 7 escritórios na América, mais de 600 clientes e 400 especialistas altamente especializados

A iniciativa Aleph foi criada e desenvolvida pela Quanam visando um forte compromisso com a inovação e tem como objetivo promover o crescimento constante de todos os atores de um ecossistema (organizações, PMEs, empresas tradicionais, cidadãos , etc.) por meio da dinamização de suas interações e integrações. Essa dinamização é alcançada através da aplicação de metodologias e ferramentas de TI que criam espaços de oportunidades, permitindo acelerar o ritmo de desenvolvimento de determinada comunidade ou ecossistema.

### Desafio de negócio

Em um centro de reabilitação de saúde são instalados sensores para determinar a qualidade das suas condições ambientais. É necessário ter controle da qualidade do ar e outros parâmetros relacionados ao meio ambiente, para agir rapidamente caso sejam detectadas anomalias, que podem ser muito prejudiciais aos pacientes.

Os sensores estão instalados em vários locais como: sala de espera, quartos, banheiros, refeitório, sala de atividades, escritório, jardim.

Os níveis aceitáveis de dados medidos podem variar dependendo da localização do medidor.

Também existem pulseiras que medem a frequência cardíaca, elas são colocadas em pacientes com doenças ou riscos cardíacos. O objetivo é poder controlar e realizar intervenções precoces em pacientes que possuam alterações desses valores.

No escritório, há um servidor disponível para monitoramento dos parâmetros medidos, disponibilizando os níveis dos mesmos em tempo real.

### Objetivo

Desenvolver uma solução capaz de:

- Capturar de dados da central de IoT e persistir os mesmos em algum formato padrão. (por exemplo, arquivo CSV);
- Detectar anomalias em cada uma das séries de dados. O processo deve retornar alertas, dependendo dos valores recebidos dos sensores e do ambiente em que o sensor está localizado.
- Elaborar um modelo que permita prever as condições futuras de uma habitação, com base na análise de dados anteriores. O modelo deverá ser capaz de predizer o ritmo cardíaco de pacientes da - habitação que utilizam a pulseira, baseando-se nas condições do ambiente.