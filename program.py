# ===== FUNKCJE =====
# Tu definiujemy funkcje których będziemy używać w trakcie działania programu
# Ułatwia to zrozumienie działania programu

# Ta funkcja jest używana na samym końcu by zapisać odpowiedź do pliku
# Przyjmuje trzy parametry: odp_a, odp_b i odp_c
def wypisz_odpowiedz(odp_a, odp_b, odp_c):

    # Otwieramy plik "ZADANIE5.TXT". Drugi parametr mówi nam w jakim trybie otwieramy plik (co chcemy z nim zrobić).
    # W tym wypadku podajemy "w" ("write") żeby móc do niego pisać (zastępując całą obecną w nim zawartość)
    # Ten tryb ("w") również utworzy plik jeśli jeszcze on nie istnieje
    plik_odpowiedzi = open("ZADANIE5.TXT", "w")

    # Taki zapis z "f" przed stringiem (napisem) umożliwia wypisywanie zawartości zmiennych (w tym wypadku odp_a) - musi ona wtedy być obudowana w {}
    # Znak "\n" na koncu to znak nowej linii - za jego pomocą zaznaczamy koniec linii
    plik_odpowiedzi.write(f"5.a: {odp_a} \n")
    plik_odpowiedzi.write("5.b: Napisy rosnace: \n")
    for napis in odp_b:
        plik_odpowiedzi.write(napis + "\n")     # Alternatywny sposob wypisywania zawartosci zmiennej z użyciem "+" - możemy użyć też pierwszej formy, tak jak wyżej, wtedy byłoby: write(f"{napis}\n")
    plik_odpowiedzi.write("5.c: Napisy powtarzajace sie: \n")
    for napis in odp_c:
        plik_odpowiedzi.write(napis + "\n")
    plik_odpowiedzi.close()     # Trzeba pamiętać o zamknięciu pliku na samym końcu aby cała zawartość którą kazaliśmy zapisać komendami powyżej została zrzucona do faktycznego pliku na dysku


# Ta funkcja zmienia kazda litere w napisie w kod ASCII i sumuje je wszystkie - ta suma jest zwracana jako wynik funkcji
def zsumuj_ascii(napis):
    suma = 0                            # Zaczynamy od 0
    litery = list(napis)                # Zapis list(napis) zmienia nasz napis w listę liter
    for litera in litery:               # Iterujemy po liście liter
        kod_ascii_litery = ord(litera)  # ord(litera) zwraca nam kod ASCII danej litery (który jest liczbą całkowitą)
        suma += kod_ascii_litery        # Dodajemy kod ascii do sumy zapisem "+=" aby jednocześnie dodać i zapisać do zmiennej po lewej
    return suma                         # Na końcu zwracamy sumę


# Ta funkcja sprawdza czy dana liczba jest liczbą pierwszą
# Robi to poprzez sprawdzenie czy istnieją jakieś inne dzielniki niż liczba sama w sobie i 1
def sprawdz_czy_liczba_jest_pierwsza(liczba):
    znaleziono_dzielnik = False             # Najpierw definijemy zmienna typu boolean (prawda albo falsz) ktora przechowuje informacje o tym czy znaleziono dzielnik

    if liczba == 1:                         # Jesli liczba wynosi 1 to od razu zwracamy fałsz
        return False
    elif liczba > 1:                        # Jesli liczba jest wieksza od 1 to wykonujemy sprawdzenie
        for i in range(2, liczba):          # Ten zapis pozwala nam przeiterować po kolei po każdej liczbie od 2 (włącznie) do samej liczby minus jeden - należy pamiętać że funkcja range() przyjmuje dwa parametry (od jakiej liczby zacząć i na jakiej skończyć), ale tylko pierwszy parametr jest włączny!
            if (liczba % i) == 0:           # Ten zapis sprawdza czy liczba jest podzielna przez obecnie sprawdzany dzielnik ("%" zwraca resztę z dzielenia, którą od razu porównujemy do zera - jeśli reszta z dzielenia to 0, to znaczy że jest podzielna)
                znaleziono_dzielnik = True  # Jeśli znaleźliśmy dzielnik (reszta z dzielenia to 0) to od razu przypisujemy do zmiennej wartość "True"...
                break                       # ... a następnie zapisem "break" od razu przerywamy naszą pętlę for (nie ma sensu szukać kolejnych dzielników jeśli już jakiś znaleźliśmy - wiemy że to już nie może być liczba pierwsza)

    # Na samym końcu zwracamy wynik w postaci True/False mówiący czy liczba jest pierwsza czy nie.
    # Ten zapis "not znaleziono_dzielnik" zwraca przeciwieństwo tego co jest w zmiennej znaleziono_dzielnik
    # Jeśli znaleźliśmy dzielnik to liczba NIE jest pierwsza a jeśli nie znaleźliśmy dzielnika to liczba JEST pierwsza
    # Dlatego zwracamy odwrotność tej zmiennej
    return not znaleziono_dzielnik


# Ta funkcja sprawdza czy napis jest rosnący, tzn czy kolejne wartości ASCII jego liter są rosnące
# Żeby to osiągnąć musimy przeiterować po każdej literze i porównać jej wartość ASCII do wartości ASCII poprzedniej litery
def sprawdz_czy_napis_jest_rosnacy(napis):
    kod_ascii_poprzedniej_litery = 0                            # Najpierw definiujemy zmienna przechowujaca kod ascii poprzedniej litery i ustawiamy ja na 0
    litery = list(napis)                                        # Ten zapis rozbija nam napis na listę liter
    for litera in litery:                                       # Iterujemy po naszej liście liter, litera po literze
        kod_ascii_litery = ord(litera)                          # Ten zapis zmienia literę w jej kod ASCII, który jest liczbą całkowitą
        if kod_ascii_litery <= kod_ascii_poprzedniej_litery:    # Sprawdzamy czy kod ascii obecnej litery jest mniejszy lub równy poprzedniej literze...
            return False                                        # ... jeśli tak jest to od razu zwracamy wynik False - ten napis nie jest rosnący
        kod_ascii_poprzedniej_litery = kod_ascii_litery         # ... w przeciwnim wypadku, zapisujemy kod ascii obecnej litery jako kod ascii poprzedniej litery i jedziemy dalej z pętlą
    return True                                                 # Jeśli dotarliśmy do tego miejsca to po prostu zwracamy True - jedyna możliwość że tu dotarliśmy jest wtedy gdy napis jest rosnący - w przeciwnym wypadku zwrócilibyśmy False ze środka pętli gdzieś w trakcie sprawdzania liter


# ===== WYNIKI =====
# W tym miejscu definiujemy zmienne, które będziemy aktualizować w trakcie iterowania po zawartości pliku

ilosc_liczb_pierwszych = 0

# Poniższe zapisy definiują nam puste listy ("[]"), będziemy do nich wrzucać odpowiednie napisy w trakcie działania programu
napisy_rosnace = []             # tu wrzucamy wszystkie napisy rosnące (podpunkt b)
zapamietane_napisy = []         # tego uzywamy w podpunkcie c aby zapamietac napotkane napisy
powtarzajace_sie_napisy = []    # tego rowniez uzywamy w podpunkcie c aby zapamietac napisy ktore sie powtarzaja, czyli zostaly juz wczesniej wrzucone do listy "zapamietane_napisy"

# ===== PROGRAM =====

with open("NAPIS.TXT") as zawartosc_pliku:  # otwieramy plik NAPIS.TXT, jego zawartosc jest dostepna pod zmienna zawartpsc_pliku
    for napis in zawartosc_pliku:           # uzywamy petli "for" zeby iterowac po zawratosci linia po linii (napis po napisie) - w zmiennej "napis" mamy obecnie rozwazana linie

        napis = napis[:-1]                  # ten zapis odrzuca ostatni znak linii - robimy to zeby odrzucic niewidzialny znak konca linii (ktory wyglada tak: "\n") (interesuja nas same litery)

        # OBLICZ PODPUNKT A
        # Obliczamy sumę ASCII, sprawdzamy czy jest liczbą pierwszą (za pomocą zdefiniowanych wcześniej funkcji)
        # a następnie zwiększamy sumę liczb pierwszych
        suma_ascii = zsumuj_ascii(napis)
        jest_pierwsza = sprawdz_czy_liczba_jest_pierwsza(suma_ascii)
        if jest_pierwsza:
            ilosc_liczb_pierwszych += 1

        # OBLICZ PODPUNKT B
        # Sprawdzamy czy napis jest rosnący (za pomocą funkcji) i jeśli tak to dodajemy go do listy rosnących napisów
        jest_rosnacy = sprawdz_czy_napis_jest_rosnacy(napis)
        if jest_rosnacy:
            napisy_rosnace.append(napis)

        # OBLICZ PODPUNKT C
        # Jesli napis jest juz w liscie "zapamietane_napisy" (czyli widzielismy go juz wczesniej) to wrzucamy go
        # do listy "powtarzajace_sie_napisy". Jeśli nie widzieliśmy go wcześniej (nie jest w liście "zapamietane_napisy")
        # to zapamiętujemy go poprzez wrzucenie go do niej
        if napis in zapamietane_napisy:
            powtarzajace_sie_napisy.append(napis)
        else:
            zapamietane_napisy.append(napis)

# Na koniec uzyj zdefiniowanej przez nas funkcji (wypisz_odpowiedz) by zapisac odpowiedzi do pliku
wypisz_odpowiedz(str(ilosc_liczb_pierwszych), napisy_rosnace, powtarzajace_sie_napisy)
