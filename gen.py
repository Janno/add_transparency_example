#!/usr/bin/env python3

a1 = open("a1.v", "w")
a2 = open("a2.v", "w")
b1 = open("b1.v", "w")
b2 = open("b2.v", "w")

preamble =\
"""
From Coq Require Import BinNatDef.
Class C (n:N) := MK_C {}.
"""

a1.write(preamble)
a2.write(preamble)

for i in range(1,11000):
  istr = str(i).zfill(5)
  a1.write(f"Definition C{istr} : C {i} := @MK_C {i}.\n")
  a2.write(f"Definition C{istr} : C {i} := @MK_C {i}.\n")

for i in range(1,11000):
  istr = str(i).zfill(5)
  a1.write(f"#[global] Hint Resolve C{istr} : typeclass_instances.\n")
  a2.write(f"#[global] Hint Resolve C{istr} : typeclass_instances.\n")

for i in range(1,1400):
  istr = str(i).zfill(5)
  a1.write(f"#[global] Hint Opaque C{istr} : typeclass_instances.\n")

a2.write("#[global] Hint Opaque\n")
for i in range(1,1400):
  istr = str(i).zfill(5)
  a2.write(f"  C{istr}\n")
a2.write(" : typeclass_instances\n.")

b1.write("Instructions From tmp Require Import a1.")
b2.write("Instructions From tmp Require Import a2.")
