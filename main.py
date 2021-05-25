# -*- coding: utf-8 -*-

# Transformación de una formula en forma clausal
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria FNC
import FNC as fn
letrasProposicionalesA = [chr(x) for x in range(410, 754)]
# # Formula a la cual encontrar su forma clausal
# formula = "-p"
# formula = "(pYq)"
# formula = "(pOq)"
formula = '(((((((((((((((((((ƚ>Ɵ)O(ƛ>ƞ))O(Ɯ>Ɲ))O(Ơ>ƥ))O(ơ>Ƥ))O(Ƣ>ƣ))O(Ʀ>ƫ))O(Ƨ>ƪ))O(ƨ>Ʃ))O(Ƭ>Ʊ))O(ƭ>ư))O(Ʈ>Ư))O(Ʋ>Ʒ))O(Ƴ>ƶ))O(ƴ>Ƶ))O(Ƹ>ƽ))O(ƹ>Ƽ))O(ƺ>ƻ))Y((((((((((((((ƚ>-(ƛOƜ))O(ƛ>-(ƚOƜ)))O(Ɯ>-(ƚOƛ)))Y(((Ɲ>-(ƞOƟ))O(ƞ>-(ƝOƟ)))O(Ɵ>-(ƝOƞ))))Y(((Ơ>-(ơOƢ))O(ơ>-(ƠOƢ)))O(Ƣ>-(ƠOơ))))Y(((ƣ>-(ƤOƥ))O(Ƥ>-(ƣOƥ)))O(ƥ>-(ƣOƤ))))Y(((Ʀ>-(ƧOƨ))O(Ƨ>-(ƦOƨ)))O(ƨ>-(ƦOƧ))))Y(((Ʃ>-(ƪOƫ))O(ƪ>-(ƩOƫ)))O(ƫ>-(ƩOƪ))))Y(((Ƭ>-(ƭOƮ))O(ƭ>-(ƬOƮ)))O(Ʈ>-(ƬOƭ))))Y(((Ư>-(ưOƱ))O(ư>-(ƯOƱ)))O(Ʊ>-(ƯOư))))Y(((Ʋ>-(ƳOƴ))O(Ƴ>-(ƲOƴ)))O(ƴ>-(ƲOƳ))))Y(((Ƶ>-(ƶOƷ))O(ƶ>-(ƵOƷ)))O(Ʒ>-(ƵOƶ))))Y(((Ƹ>-(ƹOƺ))O(ƹ>-(ƸOƺ)))O(ƺ>-(ƸOƹ))))Y(((ƻ>-(ƼOƽ))O(Ƽ>-(ƻOƽ)))O(ƽ>-(ƻOƼ)))))'


# Aplicando el algoritmo de Tseitin a formula
# Se obtiene una cada que representa la formula en FNC
fFNC = fn.Tseitin(formula, letrasProposicionalesA)

# Se obtiene la forma clausal como lista de listas de literales
fClaus = fn.formaClausal(fFNC)

# Imprime el resultado en consola
print(fClaus)
