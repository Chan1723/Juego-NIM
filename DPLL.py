# -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:14:57 2021

@author: pc
"""
import copy

def clausula_vacia(s):
    for q in s:
        if q == []:
            return True
    return False
   
def clausula_unitaria(s):
    for q in s:
        if len(q) == 1:
            return q[0]
    return None

def unitPropagate(S, I):
    while not clausula_vacia(S) and clausula_unitaria(S) != None:
        l = clausula_unitaria(S)
        if len(l) == 1:
            lc = "-" + l
            I[l] = 1
        else:
            lc = l[-1]
            I[lc] = 0
        S = [c for c in S if l not in c]
        for c in S:
            if lc in c:
                c.remove(lc)
    return S, I

#print(unitPropagate([["p"],["-p","q"],["-q","r","s"],["u","-s","r"],["r","t"],["p","s","-t"],["-r","u"]],{}))


def DPLL (S,I): #S, conjunto de cl´ausulas, - I, interpretaci´on parcial.
    #paso 1
    y = unitPropagate(S,I)
         
    #paso 2
    for i in y[0]:
        if len(i) == 0:
            return "insatisfacible", {}
        
    #paso 3   
    if len(y[0]) == 0:
        return "satisfacible" ,y[1]
        
    #paso 4
    l_n = str(y[0][0][0])
    s_p = copy.deepcopy(y[0])
    i_p = y[1].copy()
    if len(l_n) == 1:
       new_c = "-"+ l_n
       i_p[l_n] = 1
         
       
    else:
        new_c = l_n[1]
        i_p[l_n] = 0
            
    for cl in s_p:
        if new_c in cl:
            cl.remove(new_c)
                
    it = 0
    while it < len(s_p):
        if l_n in s_p[it]:
           s_p.remove(s_p[it])
           it -= 1
                
        it +=1
            
    if DPLL(s_p, i_p)[0] == "satisfacible":
        return "satisfacible", DPLL(s_p, i_p)[1]
        
        #paso 8
    else:
        s_pp = copy.deepcopy(y[0])
        i_pp = y[1].copy()
        #print(s_pp)
        
        if len(l_n) == 1:
           l_pp = "-" + str(l_n)
           c_pp = l_n
           i_pp[l_n] = 0
                
        else:
           l_pp = l_n[1]
           c_pp = l_n
           i_pp[l_n] = 1
                
        for cl in s_pp:
            if c_pp in cl:
                cl.remove(c_pp)
            it2=0
            while it2 < len(s_pp):
                  if l_pp in s_pp[it2]:
                     s_pp.remove(s_pp[it2])
                     it2 -= 1
                  it2 += 1
        return DPLL(s_pp, i_pp )
        
        
        
        
print(DPLL([['Τ'], ['ƚ', '˲'], ['-Ɵ', '˲'], ['-ƚ', 'Ɵ', '-˲'], ['ƛ', '˳'], ['-ƞ', '˳'], ['-ƛ', 'ƞ', '-˳'], ['-˲', '˴'], ['-˳', '˴'], ['˲', '˳', '-˴'], ['Ɯ', '˵'], ['-Ɲ', '˵'], ['-Ɯ', 'Ɲ', '-˵'], ['-˴', '˶'], ['-˵', '˶'], ['˴', '˵', '-˶'], ['Ơ', '˷'], ['-ƥ', '˷'], ['-Ơ', 'ƥ', '-˷'], ['-˶', '˸'], ['-˷', '˸'], ['˶', '˷', '-˸'], ['ơ', '˹'], ['-Ƥ', '˹'], ['-ơ', 'Ƥ', '-˹'], ['-˸', '˺'], ['-˹', '˺'], ['˸', '˹', '-˺'], ['Ƣ', '˻'], ['-ƣ', '˻'], ['-Ƣ', 'ƣ', '-˻'], ['-˺', '˼'], ['-˻', '˼'], ['˺', '˻', '-˼'], ['Ʀ', '˽'], ['-ƫ', '˽'], ['-Ʀ', 'ƫ', '-˽'], ['-˼', '˾'], ['-˽', '˾'], ['˼', '˽', '-˾'], ['Ƨ', '˿'], ['-ƪ', '˿'], ['-Ƨ', 'ƪ', '-˿'], ['-˾', '̀'], ['-˿', '̀'], ['˾', '˿', '-̀'], ['ƨ', '́'], ['-Ʃ', '́'], ['-ƨ', 'Ʃ', '-́'], ['-̀', '̂'], ['-́', '̂'], ['̀', '́', '-̂'], ['Ƭ', '̃'], ['-Ʊ', '̃'], ['-Ƭ', 'Ʊ', '-̃'], ['-̂', '̄'], ['-̃', '̄'], ['̂', '̃', '-̄'], ['ƭ', '̅'], ['-ư', '̅'], ['-ƭ', 'ư', '-̅'], ['-̄', '̆'], ['-̅', '̆'], ['̄', '̅', '-̆'], ['Ʈ', '̇'], ['-Ư', '̇'], ['-Ʈ', 'Ư', '-̇'], ['-̆', '̈'], ['-̇', '̈'], ['̆', '̇', '-̈'], ['Ʋ', '̉'], ['-Ʒ', '̉'], ['-Ʋ', 'Ʒ', '-̉'], ['-̈', '̊'], ['-̉', '̊'], ['̈', '̉', '-̊'], ['Ƴ', '̋'], ['-ƶ', '̋'], ['-Ƴ', 'ƶ', '-̋'], ['-̊', '̌'], ['-̋', '̌'], ['̊', '̋', '-̌'], ['ƴ', '̍'], ['-Ƶ', '̍'], ['-ƴ', 'Ƶ', '-̍'], ['-̌', '̎'], ['-̍', '̎'], ['̌', '̍', '-̎'], ['Ƹ', '̏'], ['-ƽ', '̏'], ['-Ƹ', 'ƽ', '-̏'], ['-̎', '̐'], ['-̏', '̐'], ['̎', '̏', '-̐'], ['ƹ', '̑'], ['-Ƽ', '̑'], ['-ƹ', 'Ƽ', '-̑'], ['-̐', '̒'], ['-̑', '̒'], ['̐', '̑', '-̒'], ['ƺ', '̓'], ['-ƻ', '̓'], ['-ƺ', 'ƻ', '-̓'], ['-̒', '̔'], ['-̓', '̔'], ['̒', '̓', '-̔'], ['-ƛ', '̕'], ['-Ɯ', '̕'], ['ƛ', 'Ɯ', '-̕'], ['-̖', '-̕'], ['̖', '̕'], ['ƚ', '̗'], ['-̖', '̗'], ['-ƚ', '̖', '-̗'], ['-ƚ', '̘'], ['-Ɯ', '̘'], ['ƚ', 'Ɯ', '-̘'], ['-̙', '-̘'], ['̙', '̘'], ['ƛ', '̚'], ['-̙', '̚'], ['-ƛ', '̙', '-̚'], ['-̗', '̛'], ['-̚', '̛'], ['̗', '̚', '-̛'], ['-ƚ', '̜'], ['-ƛ', '̜'], ['ƚ', 'ƛ', '-̜'], ['-̝', '-̜'], ['̝', '̜'], ['Ɯ', '̞'], ['-̝', '̞'], ['-Ɯ', '̝', '-̞'], ['-̛', '̟'], ['-̞', '̟'], ['̛', '̞', '-̟'], ['-ƞ', '̠'], ['-Ɵ', '̠'], ['ƞ', 'Ɵ', '-̠'], ['-̡', '-̠'], ['̡', '̠'], ['Ɲ', '̢'], ['-̡', '̢'], ['-Ɲ', '̡', '-̢'], ['-Ɲ', '̣'], ['-Ɵ', '̣'], ['Ɲ', 'Ɵ', '-̣'], ['-̤', '-̣'], ['̤', '̣'], ['ƞ', '̥'], ['-̤', '̥'], ['-ƞ', '̤', '-̥'], ['-̢', '̦'], ['-̥', '̦'], ['̢', '̥', '-̦'], ['-Ɲ', '̧'], ['-ƞ', '̧'], ['Ɲ', 'ƞ', '-̧'], ['-̨', '-̧'], ['̨', '̧'], ['Ɵ', '̩'], ['-̨', '̩'], ['-Ɵ', '̨', '-̩'], ['-̦', '̪'], ['-̩', '̪'], ['̦', '̩', '-̪'], ['̟', '-̫'], ['̪', '-̫'], ['-̟', '-̪', '̫'], ['-ơ', '̬'], ['-Ƣ', '̬'], ['ơ', 'Ƣ', '-̬'], ['-̭', '-̬'], ['̭', '̬'], ['Ơ', '̮'], ['-̭', '̮'], ['-Ơ', '̭', '-̮'], ['-Ơ', '̯'], ['-Ƣ', '̯'], ['Ơ', 'Ƣ', '-̯'], ['-̰', '-̯'], ['̰', '̯'], ['ơ', '̱'], ['-̰', '̱'], ['-ơ', '̰', '-̱'], ['-̮', '̲'], ['-̱', '̲'], ['̮', '̱', '-̲'], ['-Ơ', '̳'], ['-ơ', '̳'], ['Ơ', 'ơ', '-̳'], ['-̴', '-̳'], ['̴', '̳'], ['Ƣ', '̵'], ['-̴', '̵'], ['-Ƣ', '̴', '-̵'], ['-̲', '̶'], ['-̵', '̶'], ['̲', '̵', '-̶'], ['̫', '-̷'], ['̶', '-̷'], ['-̫', '-̶', '̷'], ['-Ƥ', '̸'], ['-ƥ', '̸'], ['Ƥ', 'ƥ', '-̸'], ['-̹', '-̸'], ['̹', '̸'], ['ƣ', '̺'], ['-̹', '̺'], ['-ƣ', '̹', '-̺'], ['-ƣ', '̻'], ['-ƥ', '̻'], ['ƣ', 'ƥ', '-̻'], ['-̼', '-̻'], ['̼', '̻'], ['Ƥ', '̽'], ['-̼', '̽'], ['-Ƥ', '̼', '-̽'], ['-̺', '̾'], ['-̽', '̾'], ['̺', '̽', '-̾'], ['-ƣ', '̿'], ['-Ƥ', '̿'], ['ƣ', 'Ƥ', '-̿'], ['-̀', '-̿'], ['̀', '̿'], ['ƥ', '́'], ['-̀', '́'], ['-ƥ', '̀', '-́'], ['-̾', '͂'], ['-́', '͂'], ['̾', '́', '-͂'], ['̷', '-̓'], ['͂', '-̓'], ['-̷', '-͂', '̓'], ['-Ƨ', '̈́'], ['-ƨ', '̈́'], ['Ƨ', 'ƨ', '-̈́'], ['-ͅ', '-̈́'], ['ͅ', '̈́'], ['Ʀ', '͆'], ['-ͅ', '͆'], ['-Ʀ', 'ͅ', '-͆'], ['-Ʀ', '͇'], ['-ƨ', '͇'], ['Ʀ', 'ƨ', '-͇'], ['-͈', '-͇'], ['͈', '͇'], ['Ƨ', '͉'], ['-͈', '͉'], ['-Ƨ', '͈', '-͉'], ['-͆', '͊'], ['-͉', '͊'], ['͆', '͉', '-͊'], ['-Ʀ', '͋'], ['-Ƨ', '͋'], ['Ʀ', 'Ƨ', '-͋'], ['-͌', '-͋'], ['͌', '͋'], ['ƨ', '͍'], ['-͌', '͍'], ['-ƨ', '͌', '-͍'], ['-͊', '͎'], ['-͍', '͎'], ['͊', '͍', '-͎'], ['̓', '-͏'], ['͎', '-͏'], ['-̓', '-͎', '͏'], ['-ƪ', '͐'], ['-ƫ', '͐'], ['ƪ', 'ƫ', '-͐'], ['-͑', '-͐'], ['͑', '͐'], ['Ʃ', '͒'], ['-͑', '͒'], ['-Ʃ', '͑', '-͒'], ['-Ʃ', '͓'], ['-ƫ', '͓'], ['Ʃ', 'ƫ', '-͓'], ['-͔', '-͓'], ['͔', '͓'], ['ƪ', '͕'], ['-͔', '͕'], ['-ƪ', '͔', '-͕'], ['-͒', '͖'], ['-͕', '͖'], ['͒', '͕', '-͖'], ['-Ʃ', '͗'], ['-ƪ', '͗'], ['Ʃ', 'ƪ', '-͗'], ['-͘', '-͗'], ['͘', '͗'], ['ƫ', '͙'], ['-͘', '͙'], ['-ƫ', '͘', '-͙'], ['-͖', '͚'], ['-͙', '͚'], ['͖', '͙', '-͚'], ['͏', '-͛'], ['͚', '-͛'], ['-͏', '-͚', '͛'], ['-ƭ', '͜'], ['-Ʈ', '͜'], ['ƭ', 'Ʈ', '-͜'], ['-͝', '-͜'], ['͝', '͜'], ['Ƭ', '͞'], ['-͝', '͞'], ['-Ƭ', '͝', '-͞'], ['-Ƭ', '͟'], ['-Ʈ', '͟'], ['Ƭ', 'Ʈ', '-͟'], ['-͠', '-͟'], ['͠', '͟'], ['ƭ', '͡'], ['-͠', '͡'], ['-ƭ', '͠', '-͡'], ['-͞', '͢'], ['-͡', '͢'], ['͞', '͡', '-͢'], ['-Ƭ', 'ͣ'], ['-ƭ', 'ͣ'], ['Ƭ', 'ƭ', '-ͣ'], ['-ͤ', '-ͣ'], ['ͤ', 'ͣ'], ['Ʈ', 'ͥ'], ['-ͤ', 'ͥ'], ['-Ʈ', 'ͤ', '-ͥ'], ['-͢', 'ͦ'], ['-ͥ', 'ͦ'], ['͢', 'ͥ', '-ͦ'], ['͛', '-ͧ'], ['ͦ', '-ͧ'], ['-͛', '-ͦ', 'ͧ'], ['-ư', 'ͨ'], ['-Ʊ', 'ͨ'], ['ư', 'Ʊ', '-ͨ'], ['-ͩ', '-ͨ'], ['ͩ', 'ͨ'], ['Ư', 'ͪ'], ['-ͩ', 'ͪ'], ['-Ư', 'ͩ', '-ͪ'], ['-Ư', 'ͫ'], ['-Ʊ', 'ͫ'], ['Ư', 'Ʊ', '-ͫ'], ['-ͬ', '-ͫ'], ['ͬ', 'ͫ'], ['ư', 'ͭ'], ['-ͬ', 'ͭ'], ['-ư', 'ͬ', '-ͭ'], ['-ͪ', 'ͮ'], ['-ͭ', 'ͮ'], ['ͪ', 'ͭ', '-ͮ'], ['-Ư', 'ͯ'], ['-ư', 'ͯ'], ['Ư', 'ư', '-ͯ'], ['-Ͱ', '-ͯ'], ['Ͱ', 'ͯ'], ['Ʊ', 'ͱ'], ['-Ͱ', 'ͱ'], ['-Ʊ', 'Ͱ', '-ͱ'], ['-ͮ', 'Ͳ'], ['-ͱ', 'Ͳ'], ['ͮ', 'ͱ', '-Ͳ'], ['ͧ', '-ͳ'], ['Ͳ', '-ͳ'], ['-ͧ', '-Ͳ', 'ͳ'], ['-Ƴ', 'ʹ'], ['-ƴ', 'ʹ'], ['Ƴ', 'ƴ', '-ʹ'], ['-͵', '-ʹ'], ['͵', 'ʹ'], ['Ʋ', 'Ͷ'], ['-͵', 'Ͷ'], ['-Ʋ', '͵', '-Ͷ'], ['-Ʋ', 'ͷ'], ['-ƴ', 'ͷ'], ['Ʋ', 'ƴ', '-ͷ'], ['-\u0378', '-ͷ'], ['\u0378', 'ͷ'], ['Ƴ', '\u0379'], ['-\u0378', '\u0379'], ['-Ƴ', '\u0378', '-\u0379'], ['-Ͷ', 'ͺ'], ['-\u0379', 'ͺ'], ['Ͷ', '\u0379', '-ͺ'], ['-Ʋ', 'ͻ'], ['-Ƴ', 'ͻ'], ['Ʋ', 'Ƴ', '-ͻ'], ['-ͼ', '-ͻ'], ['ͼ', 'ͻ'], ['ƴ', 'ͽ'], ['-ͼ', 'ͽ'], ['-ƴ', 'ͼ', '-ͽ'], ['-ͺ', ';'], ['-ͽ', ';'], ['ͺ', 'ͽ', '-;'], ['ͳ', '-Ϳ'], [';', '-Ϳ'], ['-ͳ', '-;', 'Ϳ'], ['-ƶ', '\u0380'], ['-Ʒ', '\u0380'], ['ƶ', 'Ʒ', '-\u0380'], ['-\u0381', '-\u0380'], ['\u0381', '\u0380'], ['Ƶ', '\u0382'], ['-\u0381', '\u0382'], ['-Ƶ', '\u0381', '-\u0382'], ['-Ƶ', '\u0383'], ['-Ʒ', '\u0383'], ['Ƶ', 'Ʒ', '-\u0383'], ['-΄', '-\u0383'], ['΄', '\u0383'], ['ƶ', '΅'], ['-΄', '΅'], ['-ƶ', '΄', '-΅'], ['-\u0382', 'Ά'], ['-΅', 'Ά'], ['\u0382', '΅', '-Ά'], ['-Ƶ', '·'], ['-ƶ', '·'], ['Ƶ', 'ƶ', '-·'], ['-Έ', '-·'], ['Έ', '·'], ['Ʒ', 'Ή'], ['-Έ', 'Ή'], ['-Ʒ', 'Έ', '-Ή'], ['-Ά', 'Ί'], ['-Ή', 'Ί'], ['Ά', 'Ή', '-Ί'], ['Ϳ', '-\u038b'], ['Ί', '-\u038b'], ['-Ϳ', '-Ί', '\u038b'], ['-ƹ', 'Ό'], ['-ƺ', 'Ό'], ['ƹ', 'ƺ', '-Ό'], ['-\u038d', '-Ό'], ['\u038d', 'Ό'], ['Ƹ', 'Ύ'], ['-\u038d', 'Ύ'], ['-Ƹ', '\u038d', '-Ύ'], ['-Ƹ', 'Ώ'], ['-ƺ', 'Ώ'], ['Ƹ', 'ƺ', '-Ώ'], ['-ΐ', '-Ώ'], ['ΐ', 'Ώ'], ['ƹ', 'Α'], ['-ΐ', 'Α'], ['-ƹ', 'ΐ', '-Α'], ['-Ύ', 'Β'], ['-Α', 'Β'], ['Ύ', 'Α', '-Β'], ['-Ƹ', 'Γ'], ['-ƹ', 'Γ'], ['Ƹ', 'ƹ', '-Γ'], ['-Δ', '-Γ'], ['Δ', 'Γ'], ['ƺ', 'Ε'], ['-Δ', 'Ε'], ['-ƺ', 'Δ', '-Ε'], ['-Β', 'Ζ'], ['-Ε', 'Ζ'], ['Β', 'Ε', '-Ζ'], ['\u038b', '-Η'], ['Ζ', '-Η'], ['-\u038b', '-Ζ', 'Η'], ['-Ƽ', 'Θ'], ['-ƽ', 'Θ'], ['Ƽ', 'ƽ', '-Θ'], ['-Ι', '-Θ'], ['Ι', 'Θ'], ['ƻ', 'Κ'], ['-Ι', 'Κ'], ['-ƻ', 'Ι', '-Κ'], ['-ƻ', 'Λ'], ['-ƽ', 'Λ'], ['ƻ', 'ƽ', '-Λ'], ['-Μ', '-Λ'], ['Μ', 'Λ'], ['Ƽ', 'Ν'], ['-Μ', 'Ν'], ['-Ƽ', 'Μ', '-Ν'], ['-Κ', 'Ξ'], ['-Ν', 'Ξ'], ['Κ', 'Ν', '-Ξ'], ['-ƻ', 'Ο'], ['-Ƽ', 'Ο'], ['ƻ', 'Ƽ', '-Ο'], ['-Π', '-Ο'], ['Π', 'Ο'], ['ƽ', 'Ρ'], ['-Π', 'Ρ'], ['-ƽ', 'Π', '-Ρ'], ['-Ξ', '\u03a2'], ['-Ρ', '\u03a2'], ['Ξ', 'Ρ', '-\u03a2'], ['Η', '-Σ'], ['\u03a2', '-Σ'], ['-Η', '-\u03a2', 'Σ'], ['̔', '-Τ'], ['Σ', '-Τ'], ['-̔', '-Σ', 'Τ']],{}))