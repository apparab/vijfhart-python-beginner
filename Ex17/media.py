#!/usr/bin/env python3

mask = '{{:<{}}}: {{}}'


class Medium(object):
    """Een bibliotheek-medium klasse
    bedoeld als superclass van echte media
    """

    def __init__(self, title, price):
        self.__title = title
        self.__price = price

    def pr(self, min_width=5):
        width = max(min_width, 5)
        to_fill = mask.format(width)
        print(to_fill.format('Title', self.__title))
        print(to_fill.format('Price', self.__price))


class Boek(Medium):
    """Een bibliotheek-boek klasse
    """

    def __init__(self,  author, pages, **kwargs):
        super().__init__(**kwargs)
        self.__author = author
        self.__pages = pages

    def pr(self, min_width=6):
        width = max(min_width, 6)
        super().pr(width)
        to_fill = mask.format(width)
        print(to_fill.format('Author', self.__author))
        print(to_fill.format('Pages', self.__pages))


class Strip(Boek):
    def __init__(self, illustrator, **kwargs):
        super().__init__(**kwargs)
        self.__illustrator = illustrator

    def pr(self, min_width=11):
        width = max(min_width, 11)
        super().pr(width)
        to_fill = mask.format(width)
        print(to_fill.format('Illustrator', self.__illustrator))

        #        titel             prijs   auteur                    aantal blz
lp = Boek(title="Learning Python", price=35.50,
          author="Mark Lutz & David Ascher", pages=595)

#            titel                  prijs  auteur     blz  tekenaar
strx = Strip(title="Asterix en Cleopatra", price=3.95,
             author="Goscinny", pages=32, illustrator="Uderzo")

#          titel                   prijs   regisseur         min leeft
#film=Dvd("2001, a space odyssey", 17.50, "Stanley Kubrick", 12)

# lp.pr()

strx.pr()
# film.pr()
