from operator import itemgetter
import csv

def carica_da_file(file_path):
    #Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta
    album = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file = csv.reader(file, delimiter=",")
            next(file)
            for riga in file:
                album.append(riga)
        return album

    except FileNotFoundError:
        print(f"Errore, File non trovato (FileNotFoundError")

def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    # TODO
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            #file = csv.writer(file, delimiter=",")
            print(f"codice, titolo, autore, mese, anno", file=file)
            for riga in album:
                print(f"{riga[0]},{riga[1]},{riga[2]},{riga[3]},{riga[4]}", file=file)
            print(f"{codice},{titolo},{autore},{mese},{anno}", file=file)
            return True

    except FileNotFoundError:
        print(f"Errore, File non trovato (FileNotFoundError")
        return False
    except OSError:
        print(f"Errore, Impossibile aprire il file (OSError)")
        return False


def cerca_foto(album, codice):

    """Cerca una foto nell'album dato il codice"""
    # TODO
    foto = [el for el in album if el[0] == codice]
    if len(foto) > 1:
        raise ValueError
    else:
        return foto[0]

def elenco_foto_anno_per_titolo(album, anno):
    #Ordina i titoli delle foto di un dato anno in ordine alfabetico
    # TODO

    lista_foto = [el for el in list(album) if int(el[-1].strip()) == anno]
    lista_foto.sort(key=itemgetter(1))
    if lista_foto == []:
        return None
    else:
        return lista_foto

def main():
    album = []
    file_path = "album_fotografico.csv"
    #album = carica_da_file("album_fotografico.csv") #---> Usato solo per velocizzare test
    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    print(f"Album Caricato con successo!")
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
                if (mese > 12) or (mese < 1) or (anno > 2026):
                    raise ValueError
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            try:
                if not(codice[1:].isdigit()) or not(codice[0].isalpha()):
                    raise TypeError
                risultato = cerca_foto(album, codice)
                if risultato:
                    print(f"\nFoto trovata:")
                    print(f"{"Codice":<6}|{"Nome":<30}|{"Autore":<20}|{"Mese e Anno"}")
                    print(f"{risultato[0]:<6}|{risultato[1]:<30}|{risultato[2]:<20}|{risultato[3]}/{risultato[4]}")
                else:
                    print("Foto non trovata.")
            except ValueError:
                print(f"Il codice è associato a più di una foto")
            except TypeError:
                print(f"Codice inserito non valido")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                #print("\n".join([f"- {titolo}" for titolo in titoli]))
                print(f"{"Codice":<6}|{"Nome":<30}|{"Autore":<20}|{"Mese e Anno"}")
                for el in titoli:
                    print(f"{el[0]:<6}|{el[1]:<30}|{el[2]:<20}|{el[3]}/{el[4]}")
                #Modifica per formattare la print su terminale come tabella
            else:
                print(f"\nNessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")



if __name__ == "__main__":
    main()
