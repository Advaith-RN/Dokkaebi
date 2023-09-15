---
title: PES ASIC CLASS Notes
author: Advaith R Nair
date: 2021-07-01

primary: #000000
secondary: #ffffff 
accent: #5620CB

foreground: #04131A
background: #ffffff
---

# PES ASIC CLASS Notes
This repository contains notes for the process of complete ASIC flow.
<br>**FACULTY** : Mahesh Awati
<br>**GUIDE** : [Kunal Ghosh](https://github.com/kunalg123/)



## Introduction
```ASCII
   HLL         ALP       Binary      (HDL)       GDS
  +------+   +-----+   +---------+   +-----+   +--------+
  | Code |-> | Asm |-> | Machine |-> | RTL |-> | Layout |
  |  Gen |   | Gen |   |  Code   |   |Synth|   | Design |
  +------+   +-----+   +---------+   +-----+   +--------+

```
#### 1. HLL -> High level language (c , c++) 
- A high-level programming language is a type of programming language that is designed to be more human-readable and user-friendly compared to low-level languages like assembly or machine code.

#### 2. ALP -> Assembly level program
- Assembly language is a low-level programming language that is closely related to the architecture of a specific computer's central processing unit (CPU). Assembly language programs are written using mnemonic codes that represent specific machine instructions which the machine can understand.

#### 3. HDL -> Hardware Description Language
- It is a specialized programming language used for designing and describing digital hardware circuits. HDLs allow engineers to model and simulate complex digital systems before physical implementation, aiding in the design and verification of integrated circuits and FPGA configurations.
- Verilog, System Verilog, VHDL

#### 4. GDS -> Graphic Data System (layout)
- Format used in the semiconductor industry to represent the layout and design of integrated circuits at a highly detailed level. GDSII files contain information about the geometric shapes, layers, masks, and other essential details that make up the physical layout of a chip.
- Tools : Klayout, Magic

##### The Hardware needs to understand what the Application software is saying it to do.This relation can be eshtablished by System Software

____System Software____
- OS : Operating System : Handles IO, memory allocation, Low level system function
- Compiler : Convert the input to hardware dependent instruction
- Assembler : Convert the instructions provided by compiler to Binary format
- HDL : A program that understands the Binary pattern and map it to a netlist
- GDS : Layout

## Course Content
### 1. [RISC-V ISA and GNU Compiler toolchain](https://github.com/Advaith-RN/pes_asic_class/blob/main/Day1/Day1.md)
### 2. [Introduction to ABI and Basic Verification Flow](https://github.com/Advaith-RN/pes_asic_class/blob/main/Day2/Day2.md)
### 3. [Introduction to Verilog RTL Design and Synthesis](https://github.com/Advaith-RN/pes_asic_class/blob/main/Day3/Day3.md)
### 4. [Introduction to Timing libs](https://github.com/Advaith-RN/pes_asic_class/blob/main/Day4/Day4.md)
### 5. [Introduction to Optimizations](https://github.com/Advaith-RN/pes_asic_class/blob/main/Day5/Day5.md)
### 6. [GLS Synthesis Simulation Mismatch and Blocking/Non-Blocking Statements](https://github.com/Advaith-RN/pes_asic_class/blob/main/Day6/Day6.md)