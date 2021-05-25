#1ra regla: depediendo cuantos palitos tome el primer jugador (turno impar),
#el segundo jugador(turno par) toma 4 menos la cantidad que tomo el primer 
#jugador en el turno anterior de palitos

#2da regla: por turno se tomar 1, 2 o 3 palitos

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
    
letrasProposicionales = [chr(x) for x in range(410,754)]
conectivos = ["Y", "O", ">", "="]

Turnos = 12 #jugador B=0 o A=1
Maxpalitostomados = 3 # 1 o 2 o 3 palitos

nim = NIM(Turnos, Maxpalitostomados, 410)

def aux_4_less_k(Turno, pt): #funcion auxiliar de la primera regla
    if Turno%2 == 0:#el usuario son los turnos pares
        inicial = True
        for t in range(2):#apartir de la jugada del usuario actua la maquina
            if inicial:
                formula = nim.P(Turno,pt)
                inicial = False
            else:#los codigos generados por codifica no son consiguientes para lo que queremos
                if pt == 0:#por lo tanto se hacen estas condiciones para generar la regla facilmente
                    formula = nim.P(Turno+1, 2)+formula+">"
                if pt == 1:
                    formula = nim.P(Turno+1, pt)+formula+">"
                if pt == 2:
                    formula = nim.P(Turno+1, 0)+formula+">"
        return formula

# aux1 = aux_4_less_k(10,2)
# A = String2Tree(aux1)
# print(Inorderp(A))

def regla1(Turnos, Maxpalitostomados):#1ra regla
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

def aux_123_sticks_per_turn(Turno, palitostomados):#auxiliar para generar la regla a un solo caso
    inicial = True
    rango = [p for p in range(nim.MPt) if p != palitostomados]
    for p in rango:
        if inicial:
            formula = nim.P(Turno, p)
            inicial = False
        else:
            formula = nim.P(Turno, p)+formula+"O"
    return formula + "-" + nim.P(Turno, palitostomados) + ">"

def aux_123_sticks_per_turn2(Turno, Maxpalitostomados):#auxiliar para generar la regla a todo un turno
    inicial = True
    for p in range(Maxpalitostomados):
        if inicial:
            formula = aux_123_sticks_per_turn(Turno, p)
            inicial = False
        else:
            formula = aux_123_sticks_per_turn(Turno, p)+formula+"O"
    return formula

def regla2(Turnos, Maxpalitostomados):#2da regla se genera la regla para todos los turnos
    inicial = True
    for t in range(Turnos):
        if inicial:
            formula =  aux_123_sticks_per_turn2(t, Maxpalitostomados)
            inicial = False
        else:
            formula = aux_123_sticks_per_turn2(t, Maxpalitostomados)+formula+"Y"
    return formula

R1 = regla1(Turnos, Maxpalitostomados)
A = String2Tree(R1)
print(Inorder(A))#usamos Inorder porque se necesita con letras proposicionales
print(" ")
R2 = regla2(Turnos, Maxpalitostomados)
A = String2Tree(R2)
print(Inorder(A))
print(" ")
formula = R2+R1+"Y"
A = String2Tree(formula)
print(Inorder(A))
