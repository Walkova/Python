# Země, nakažených, mrtvých, uzdravených 
coronavirus = [ 
[ "China", 80967, 3248, 71150 ], 
[ "Italy", 47021, 4032, 5129 ], 
[ "Spain", 20412, 1032, 1588 ], 
[ "Iran", 19644, 1433, 6745 ], 
[ "Germany", 18794, 53, 180 ], 
[ "USA", 16489, 223, 125 ], 
[ "France", 10995, 372, 1295 ], 
[ "South Korea", 8652, 94, 2233 ], 
[ "UK", 3269, 184, 65 ], 
[ "Netherlands", 2994, 106, 2 ], 
[ "Austria", 2491, 6, 9 ], 
[ "Belgium", 2257, 37, 204 ], 
[ "Norway", 1912, 7, 1 ], 
[ "Sweden", 1639, 16, 16 ], 
[ "Denmark", 1255, 9, 1 ], 
[ "Malaysia", 1030, 3, 87 ], 
[ "Portugal", 1020, 6, 5 ], 
[ "Japan", 963, 33, 215 ], 
[ "Canada", 924, 12, 11 ], 
[ "Australia", 876, 7, 46 ], 
[ "Czechia", 833, 0, 4 ], 
[ "Israel", 705, 0, 15 ], 
[ "Brazil", 654, 7, 2 ], 
[ "Ireland", 557, 3, 5 ], 
[ "Pakistan", 500, 3, 13 ], 
[ "Greece", 495, 9, 19 ], 
[ "Luxembourg", 484, 5, 6 ], 
[ "Qatar", 460, 0, 10 ], 
[ "Finland", 450, 0, 10], 
[ "Chile", 434, 0, 6 ], 
[ "Poland", 411, 5, 13 ], 
[ "Iceland", 409, 0, 5 ], 
[ "Singapore", 385, 0, 131 ], 
[ "Indonesia", 369, 32, 17 ]
 ]

#1.Kolik zemí je celkem v tabulce?

#delka seznamu 
sumaStatu=len(coronavirus)
print(f'V tabulce je {sumaStatu} statů')
#34 států



#2.Kolik je celkem nakažených ve všech uvedených zemích dohromady?

#suma druhého sloupce
nakazenych=[sum(int(nakazenych[1]) for nakazenych in coronavirus)]

print(f'Nakažených je{nakazenych}')
#250 750 nakažených




#3.Kolik je největší počet mrtvých v jedné zemi?

#maximalni hodnota tretiho sloupce

mrtvych=[mrtvy[2] for mrtvy in coronavirus]
max_mrtvych=max(mrtvych)
print(f'Nejvyšší počet v jedné zemi je {max_mrtvych} mrtvych')
#4032 mrtvych




#4.Vytáhněte si ze vstupní tabulky seznam všech zemí (ne, že to ručně opíšete, vymyslete na to kód 

#seznam prvniho sloupce
seznam_zemi=[zem[0] for zem in coronavirus]
print(seznam_zemi)




#5.Seznam z předchozího úkolu převeďte na jeden velký řetězec, jednotlivé země v něm budou oddělené pomlčkou.

#seznam prvniho sloupce a vymena carky za pomlcku

seznam_zemi=[zem for zem in seznam_zemi]
#print(seznam_zemi)
seznam_zemi_roz="-".join(seznam_zemi)
print(seznam_zemi_roz)





#6Z dat ve vstupní tabulce vytvořte novou tabulku, kde v prvním sloupci bude název země a ve druhém sloupci bude počet aktuálně nakažených (tedy rozdíl mezi celkovým počtem nakažených a počtem zemřelých a uzdravených).

#vytvoreni souboru ukol.txt kam nahraji vypocet
#vypocet aktualne nemocnych odectenim uzdravenych a mrtvych od poctu nakazenych pro kazdy radek

soubor=open(r"C:\Users\Martina\Desktop\Digitalni akademie\DATA\Python\ukol.txt", encoding='utf8', mode="w")
aktualne_nakazenych=[(nakazenych[1]-nakazenych[2]-nakazenych[3]) for nakazenych in coronavirus]
print(aktualne_nakazenych)

soubor.write('Zeme\t pocet_nakazenych\n')
[soubor.write(f'{seznam_zemi[i]}\t{aktualne_nakazenych[i]}\n') for i in range(len(coronavirus))]
