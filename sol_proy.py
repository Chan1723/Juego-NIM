# -*- coding: utf-8 -*-
"""
Created on Mon May 24 21:11:42 2021

@author: tomys
"""

class NIM:
    def __init__(self, Turnos, Maxpalitostomados, chrInit):
        self.T = Turnos #filas
        self.MPt = Maxpalitostomados #columnas
        self.chrInit = chrInit

    def codifica(self, p_im, pt) :#recibe turno par=A o impar=B y palitos tomados
        return self.MPt*p_im+pt#retorna un entero unico para esa casilla

    def decodifica(self, n) :#encuentra el turno y palitos tomados en el mismo
        p_im = int(n / self.MPt)#representada por n que nos
        pt = n % self.MPt#dio codifica
        return p_im, pt#inverso de codifica

    def P(self, p_im, pt) :
        codigo = self.codifica(p_im, pt)#segun el codigo entero que nos da la funcion codifica
        return chr(self.chrInit+codigo)#se retorna el char en ascii de la suma de chrInit y el codigo entero

    def Pinv(self, codigo) :#inverso de P, o sea nos devuelve
        n = ord(codigo)-self.chrInit#el turno y palitos tomados segun la letra proposicional
        return self.decodifica(n)#asignada

class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label

def String2Tree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: - A, lista de caracteres con una formula escrita en notacion polaca inversa
    #        - letrasProposicionales, lista de letras proposicionales
    #        - conectivos, lista de conectivos
    # Output: formula como tree
    if A != None:
        pila = []
        for c in A:
            # print("Examinando " + str(c))
            if c in letrasProposicionales:
                # print(u"El símbolo es letra proposicional")
                pila.append(Tree(c, None, None))
            elif c == '-':
                # print("Negamos")
                formulaAux = Tree(c, None, pila[-1])
                del pila[-1]
                pila.append(formulaAux)
            elif c in conectivos:
            # print("Unimos mediante conectivo")
                formulaAux = Tree(c, pila[-1], pila[-2])
                del pila[-1]
                del pila[-1]
                pila.append(formulaAux)
            else:
                print(u"Hay un problema: el símbolo " + str(c) + " no se reconoce")
        return pila[-1]

def Inorderp(f):
    # Imprime una formula como cadena dada una formula como arbol
    # de manera que las letras proposicionales sean legibles.
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
    if f != None:
        if f.right == None:
            p_im, pt = nim.Pinv(f.label)
            return f"nim({p_im},{pt})"
        elif f.label == '-':
            return f.label + Inorderp(f.right)
        else:
            return "(" + Inorderp(f.left) + f.label + " " + Inorderp(f.right) + ")"

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"


letrasProposicionales = [chr(x) for x in range(256,600)]
conectivos = ["Y", "O", ">", "="]

Turnos = 12 #jugador B=0 o A=1
Maxpalitostomados = 3 # 1 o 2 o 3 palitos

nim = NIM(Turnos, Maxpalitostomados, 256)

def aux_4_less_k(Turno, pt):
    if Turno%2 == 0:
        inicial = True
        for t in range(2):
            if inicial:
                formula = nim.P(Turno,pt)
                inicial = False
            else:
                if pt == 0:
                    formula = nim.P(Turno+1, 2)+formula+">"
                if pt == 1:
                    formula = nim.P(Turno+1, pt)+formula+">"
                if pt == 2:
                    formula = nim.P(Turno+1, 0)+formula+">"
        return formula

def regla1(Turnos, Maxpalitostomados):
    inicial = True
    for t in range(Turnos):
        if t%2 == 0:
            for p in range(Maxpalitostomados):
                if inicial:
                    formula = aux_4_less_k(t, p)
                    inicial = False
                else:
                    formula = aux_4_less_k(t, p)+formula+"O"
    return formula

def aux_123_sticks_per_turn(Turno, palitostomados):
    inicial = True
    rango = [p for p in range(nim.MPt) if p != palitostomados]
    for p in rango:
        if inicial:
            formula = nim.P(Turno, p)
            inicial = False
        else:
            formula = nim.P(Turno, p)+formula+"O"
    return formula + "-" + nim.P(Turno, palitostomados) + ">"

def aux_123_sticks_per_turn2(Turno, Maxpalitostomados):
    inicial = True
    for p in range(Maxpalitostomados):
        if inicial:
            formula = aux_123_sticks_per_turn(Turno, p)
            inicial = False
        else:
            formula = aux_123_sticks_per_turn(Turno, p)+formula+"O"
    return formula

def regla2(Turnos, Maxpalitostomados):
    inicial = True
    for t in range(Turnos):
        if inicial:
            formula =  aux_123_sticks_per_turn2(t, Maxpalitostomados)
            inicial = False
        else:
            formula = aux_123_sticks_per_turn2(t, Maxpalitostomados)+formula+"Y"
    return formula

R1 = regla1(Turnos, Maxpalitostomados)

R2 = regla2(Turnos, Maxpalitostomados)

formula = R2+R1+"Y"

###VISUALIZACIÓN DE UNA SOLUCIÓN
import matplotlib.pyplot as plt
# import matplotlib.patches as patches

def dibujar_tabla(I):
    #Visualiza una tabla 2x2 dad una interpretacion I
    #Input: I, una interpretación
    n1 = "|"
    n2 = "||"
    n3 = "|||"

    #inicializar figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    

    #crear lineas del tablero
    step = 1./4

    offset_x = .225
    offset_y = -.4

    for l in I.keys():
        if I[l] != 0:
            p_im, pt = nim.Pinv(l)
            if  pt == 0:
                p_im, pt= nim.Pinv(l)
                #print(f"f:{f}, c:{c}, n:{n})
                axes.text(
                    pt*step+offset_x, (1-p_im*step+offset_y),
                    n1,style = 'italic', fontsize = 42
                    )
            if pt == 1:
                p_im, pt= nim.Pinv(l)
                #print(f"f:{f}, c:{c}, n:{n})
                axes.text(
                    pt*step+offset_x, (1-p_im*step+offset_y),
                    n2,style = 'italic', fontsize = 42
                    )
            if pt == 2:
                p_im, pt= nim.Pinv(l)
                #print(f"f:{f}, c:{c}, n:{n})
                axes.text(
                    pt*step+offset_x, (1-p_im*step+offset_y),
                    n3,style = 'italic', fontsize = 42
                    )
    plt.show()

#insercion de los palitos de todo el tablero
I = {}
# I[nim.P(0,0)] = 1
# I[nim.P(0,1)] = 1
# I[nim.P(0,2)] = 1 
# I[nim.P(1,0)] = 1 
# I[nim.P(1,1)] = 1
# I[nim.P(1,2)] = 1 
# I[nim.P(17,0)] = 1 
# dibujar_tabla(I)

from random import randint

def diccionario_aleatorio():
    I = {}
    for p_im in range(nim.T):
        for pt in range(nim.MPt):
            numero = randint(0,23)
            letra = nim.P(p_im,pt)
            n = nim.codifica(p_im, pt)
            if n == numero:
                I[letra] = 1
            else:
                I[letra] = 0
    return I

# I = diccionario_aleatorio()
# dibujar_tabla(I)

##SOLUCION MENDIANTE TABLAS DE VERDAD
# Función V_I(A, I)
def V_I(f,I):
    if f.right==None:
        return I[f.label]
    elif f.label== '-':
        return 1-(V_I(f.right,I))
    elif f.label=='Y':
        return V_I(f.left,I)*V_I(f.right,I)
    elif f.label=='O':
        return max(V_I(f.left,I),V_I(f.right,I))
    elif f.label=='>':
        return max(1-(V_I(f.left,I)),V_I(f.right,I))
    elif f.label=='=':
        return 1-(((V_I(f.left,I)-V_I(f.right,I)))**2)

# Función para crear todas las interpretaciones
def crear_interpretaciones(letrasProposicionales):
    interps = [] #lista con todas las posible interpretaciones (diccionarios)
    aux = {} # primera interpretación

    for a in letrasProposicionales:
        aux[a] = 1 # inicializamos la primera interpretacion con todo verdadero

    interps.append(aux)# y se incluye en interps

    for a in letrasProposicionales:
        interps_aux = [i for i in interps] #lista auxiliar de nuevas interpretaciones

        for i in interps_aux:
            aux1 = {} #diccionario auxiliar para crear nuevas interpretaciones

            for b in letrasProposicionales:
                if a==b:
                    aux1[b] = 1-i[b] #cambia el valor de verdad para b
                else:
                    aux1[b] = i[b] #... y mantiene el valor de verdad para las otras letras

            interps.append(aux1) #incluye la nueva interpretación en la lista
    return interps

# Función que recorre las interpretaciones hasta encontrar una
# que hace verdadera a A
def encuentra_interpretacion(A, letrasProposicionales):
    # Encuentra la primera interpretación que hace verdadera a A
    # Input: - A, una fórmula en formato tree
    #        - letrasProposicionales, una lista de letras proposicionales

    interps = crear_interpretaciones(letrasProposicionales)
    # print("Se han creado " + str(len(interps)) + " interpretaciones.")

    for I in interps:
        if V_I(A, I) == 1:
            return I

    return None
## no ejecutar las lineas porque se reinicia el computador
## NO CORRER LAS SIGUIENTES LINEAS
## NO CORRER LAS SIGUIENTES LINEAS
## NO CORRER LAS SIGUIENTES LINEAS
## NO CORRER LAS SIGUIENTES LINEAS
## NO CORRER LAS SIGUIENTES LINEAS
## NO CORRER LAS SIGUIENTES LINEAS
## NO CORRER LAS SIGUIENTES LINEAS
## NO CORRER LAS SIGUIENTES LINEAS
## NO CORRER LAS SIGUIENTES LINEAS
## NO CORRER LAS SIGUIENTES LINEAS
## NO CORRER
## NO CORRER
## NO CORRER
## NO CORRER
## NO CORRER
## NO CORRER

# A = String2Tree(R1)
# I = encuentra_interpretacion(A, letrasProposicionales)
# dibujar_tabla(I)

# A = String2Tree(R2)
# I = encuentra_interpretacion(A, letrasProposicionales)
# dibujar_tabla(I)

# A = String2Tree(formula)
# I = encuentra_interpretacion(A, letrasProposicionales)
# dibujar_tabla(I)