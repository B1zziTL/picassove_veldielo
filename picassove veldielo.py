#importovanie modulu
import tkinter

#nastavenie platna
canvas = tkinter.Canvas(width = 800, height= 500, background="white")
canvas.pack()

#otvorenie suboru
subor = open("preklopenie_obrazka.txt","r")

#precitanie prveho riadku
prvy_riadok = subor.readline()
riadocek = prvy_riadok.split()

#zadeklarovanie premennych pre pozadovane informacie
ulozisko = subor.read()
jednotky = ulozisko.count("1")

#zatvorenie suboru
subor.close()

#zadeklarovanie pomocnych premennych
strana = 4
daco = 0
x = 0
y = 0

#otvorenie suboru a preskocenie prveho riadku
subor1 = open("preklopenie_obrazka.txt","r")
next(subor1)

def picasso(): #funkcia na vykreslenie obrazka
    #zadeklarovanie globalnych premennych
    global x,y
    global subor1, strana, riadocek, daco
    
    for riadok in subor1: #cyklus na prechadzanie riadkov v subore
        #zmena pomocnej premennej
        daco += 1
        
        for pismeno in riadok: #cyklus na prechadzanie pismen v riadku
            #ak je pismeno 0, vykresli bielu bodku
            if pismeno == "0":
                canvas.create_rectangle(x,y,x+strana,y+strana,fill="white",outline="")
            #ak je pismeno 1, vykresli ciernu bodku
            if pismeno == "1":
                canvas.create_rectangle(x,y,x+strana,y+strana,fill="black",outline="")

            #zmena pomocnej premennej
            x += strana

        #zmena pomocnych premennych
        x = 0
        y += strana

        #podmienka na dalsie ne/vykreslovanie 
        if daco < int(riadocek[1]):
            canvas.after(1,picasso)
        else:
            daco = 0
            x = 0
            y = 0
            return None

def abrakadabra(): #funkcia na prevratenie obrazku
    #vycistenie canvasu
    canvas.delete("all")
    
    def nieco(): #podfunkcia na prevratenie obrazku
        #zadeklarovanie globalnych premennych
        global x,y
        global subor1, strana, riadocek, daco

        #otvorenie suboru a preskoceny prveho riadku
        subor2 = open("preklopenie_obrazka.txt","r")
        next(subor2)
        
        for riadok in subor2: #cyklus na prechadzanie riadkov v subore
            #zmena pomocnej premennej
            daco += 1
            
            for pismeno in riadok[::-1]: #cyklus na prechadzanie pismen v riadku
                #ak je pismeno 0, vykresli bielu bodku
                if pismeno == "0":
                    canvas.create_rectangle(x,y,x+strana,y+strana,fill="white",outline="")
                #ak je pismeno 1, vykresli ciernu bodku
                if pismeno == "1":
                    canvas.create_rectangle(x,y,x+strana,y+strana,fill="black",outline="")

                #zmena pomocnej premennej
                x += strana

            #zmena pomocnych premennych
            x = 0
            y += strana

            #podmienka na dalsie ne/vykreslovanie 
            if daco < int(riadocek[1]):
                canvas.after(1,nieco)
            else:
                return None
            
    #vyvolanie funkcie 
    nieco()

#vyvolanie funkcie
picasso()

#vypisanie pozadovanych hodnot
print("Celkový počet pixelov:",int(riadocek[0])*int(riadocek[1]))
print("Počet jednotiek:",jednotky)

#nastavenie tlacidla
magicke_tlacitko = tkinter.Button(text="Preklop",command=abrakadabra)
magicke_tlacitko.pack()
