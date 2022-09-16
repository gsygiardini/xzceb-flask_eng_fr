from machinetranslation import translator as tr

#First random text from French to English
test1 = tr.french_to_english("Le client est très important merci, le client sera suivi par le client. Énée n'a pas de justice, pas de résultat, pas de ligula, et la vallée veut la sauce.")
print(test1)

#Second random French test translated to English
test2 = tr.french_to_english("Morbi mais qui veut vendre une couche de contenu triste d'internet. Être ivre maintenant, mais ne pas être ivre maintenant, mon urne est d'une grande beauté, mais elle n'est pas aussi bien faite que dans un livre. Mécène dans la vallée de l'orc, dans l'élément même. Certaines des exigences faciles du budget, qu'il soit beaucoup de temps pour dignissim et. Je ne m'en fais pas chez moi, ça va être moche dans le vestibule.")
print(test2)

#First random English test translated to French
test3 = tr.english_to_french("Gordon Ramsay has a project in a London prision where he opened up a business and teaches inmates how to bake. This gave the inmates the work experience they need when they finish their sentences.")
print(test3)

#Second random English test translated to French
test4 = tr.english_to_french("Dart frogs are known to be poisonous little frogs. However, when kept as pets, they are completely non-toxic. This is because their toxic coating comes from the bugs they eat in the wild.")
print(test4)

#Test a null input for the frenchToEnglish functio.
test6 = tr.french_to_english()
print(test6)

#Test a null input for the englishToFrench function
test6 = tr.english_to_french()
print(test6)

#Test the translation of a "Hello" input and verify if it is correctly translated to "Bonjour"
test7 = tr.english_to_french("Hello")
print(test7)

#Test the translation of a "Bonjour" input and verify if it is correctly translated to "Hello"
test8 = tr.french_to_english("Bonjour")
print(test8)
