---
created: 2022-04-02 10:00:00
modified:
title: TCP/IP Model
---

# The TCP/IP Model

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
