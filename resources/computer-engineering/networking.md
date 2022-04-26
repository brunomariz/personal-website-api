---
created: 2022-04-02 10:00:00
modified:
title: Networking
---

# Some networking stuff:

## Request For comments (RFC)

Request for comments are a series of documents which define standards for all sorts of different technologies, such as video streaming, wireless internet transmission protocols, etc.

- IP RFC: https://datatracker.ietf.org/doc/html/rfc791
- Search RFC: https://datatracker.ietf.org/

## Submarine fiber-optic cables

Currently, about 95% of the internet traffic depends on submarine fiber-optic cables which run across the ocean floor. Many of them are comissioned by large corporations, such as Google, Amazon, Facebook and Microsoft. They are placed under the sea floor by ships which carry large spools of reinforced cables. These cables contain the fiber-optics, aswell as a copper shell for powering optical signal amplifiers along the way.

- Interactive, real time submarine fiber-optic cables information (terrestrial fiber optics cables information are corporate secrets): https://submarinecablemap.com

- Current "highest-capacity submarine cable in the world" (200 terabits per second), MAREA, owned and funded by Microsoft: https://en.wikipedia.org/wiki/MAREA

## Satellite connection

- Real time satellite tracking: https://www.n2yo.com/satellites/?c=BRAZ&t=country

## Amazon Rainforest

###### Amazônia 4.0 Project

A project aiming to bring technology, research and economical development to the Amazonian rainforest to the benefit of the local population while maintaining the biodiversity and climatic conditions of the rainforest.

Projeto Amazônia 4.0 (pt_BR): http://www.iea.usp.br/pesquisa/pesquisadores-colaboradores/projeto-amazonia-4.0

###### Amazônia Conectada: a subaquatic network in the rainforest

Intended for connecting the brazillian army units located in the eastern amazonian region, this project aimed to install a high-velocity network by laying fiber-optic cables in the riverbeds. The project would also benefit local residents, as areas that were previously untouched could make use of the network, increasing digital inclusion.

- Projeto Amazônia Conectada (pt_BR): http://www.amazoniaconectada.eb.mil.br/

## TCP/IP Model

| Layers         |
| -------------- |
| 5. Application |
| 4. Transport   |
| 3. Internet    |
| 2. Data Link   |
| 1. Physical    |

### 1. Physical Layer

#### Responsibilities

- Physical means of transmission
- Multiplexing techniques: https://www.geeksforgeeks.org/difference-between-tdm-and-fdm/
- Structured Cabling: https://en.wikipedia.org/wiki/ANSI/TIA-568
- Apropriately encoding bits for the specified mean of transmission
- Sending bits over the physical mean of transmission

### 2. Data Link Layer

#### Responsibilities

###### Before fiber-optics:

- Error detection (BER ~10^-6) and correction
- Flow control
  - Start-Stop (feedback-based)
  - Sliding Window (rate-based)

###### After fiber-optics:

- Error detection (no correction, BER ~10^-9 to 10^-12)
- Congestion control
- Frame delimiting
- Sharing a physical medium: https://en.wikipedia.org/wiki/Carrier-sense_multiple_access_with_collision_detection

### 3. Internet Layer

#### Responsibilities

- Routing
- Maximum Transmission Unit (MTU)
- Segmentation

### 4. Transport Layer

#### Responsibilities

### 5. Application Layer

#### Responsibilities
