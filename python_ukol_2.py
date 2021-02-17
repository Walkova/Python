#otevření souboru Psenicka a vytištění řádků
soubor=open(r'C:\Users\Martina\Desktop\Digitalni akademie\DATA\Python\Psenicka.csv', encoding='utf-8')
seznam_plodin=[radek for radek in soubor]
print(seznam_plodin)
soubor.close()

seznam_plodin_upr=[radek.strip().replace(";", " ").replace("t", "") for radek in seznam_plodin]
print(seznam_plodin_upr)
# odstranění ;, \n a hmotnostní jednotky t

soubor=open(r'C:\Users\Martina\Desktop\Digitalni akademie\DATA\Python\psenice.txt', encoding="utf8", mode="w")
# pro každý řádek, pokud začíná slovem pšenice, odstraň "pšenice ", mezeru mezi číselnými hodnoty nahraď "-" a vypiš pro každý řádek rok a výnos,  zapiš do souboru .txt 
for x in seznam_plodin_upr:
  if x.startswith("Pšenice"):
      vynos=x.replace("Pšenice ", "")
      vynos=vynos.replace(" ", "-")
      print(vynos)
      
      soubor.write(vynos+'\n')
soubor.close()
 
 
# pro každý řádek, pokud začíná slovem ječmen, odstraň "ječmen ", mezeru mezi číselnými hodnoty nahraď "-" a vypiš pro každý řádek rok a výnos,  zapiš do souboru .txt 
soubor=open(r'C:\Users\Martina\Desktop\Digitalni akademie\DATA\Python\jecmen.txt', encoding="utf8", mode="w")
for x in seznam_plodin_upr:
  if x.startswith("Ječmen"):
      vynos=x.replace("Ječmen ", "")
      vynos=vynos.replace(" ", "-")
      print(vynos)

      soubor.write(vynos+'\n')
soubor.close()



 
  


  
