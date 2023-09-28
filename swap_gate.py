#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:22:39 2023

@author: abdullahalshihry
"""

import qiskit as qs

N = int(input("choose N"))
qr = qs.QuantumRegister(N, 'Q')
cr = qs.ClassicalRegister(N, 'c')
qc = qs.QuantumCircuit(qr,cr)

qc.x(range(N//2))


def swap_gate():
    for i in range(N // 2):
        qc.swap(qr[i],qr[N-i-1])
        
        
swap_gate()
qc.barrier(range(N))
qc.measure(qr,cr)

job1 = qs.execute(qc, qs.Aer.get_backend('aer_simulator'), shots = 1024)
output1 = job1.result().get_counts()
print(output1)
qc.draw('mpl')
