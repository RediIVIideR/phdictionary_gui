import eel
from phdictionary import dictionary

eel.init('web')


# Non-file block
@eel.expose
def trans(fro, to, word):
    if fro == 'French' and to == 'English':
        return dictionary.get_french_english(word, 4)
    elif fro == 'English' and to == 'French':
        return dictionary.get_english_french(word, 4)
    elif fro == 'English' and to == 'Russian':
        return dictionary.get_english_russian(word, 4)
    elif fro == 'Russian' and to == 'English':
        return dictionary.get_russian_english(word, 4)
    elif fro == 'French' and to == 'Russian':
        return dictionary.get_french_russian(word, 4)
    elif fro == 'Russian' and to == 'French':
        return dictionary.get_russian_french(word, 4)
    elif fro == "English" and to == 'English':
        return ('Choose the language properly', ['None', 'None'])


@eel.expose
def definition(word):
    return dictionary.get_definition(word, 4)


@eel.expose
def synonyms(word):
    return dictionary.get_synonym(word, 5)


# Working with files block
@eel.expose
def definition_file(name, n):
    dictionary.get_definition_from_file(open(name), int(n))
    return "Process finished successfully!"


@eel.expose
def synonyms_file(name, n):
    dictionary.get_synonyms_from_file(open(name), int(n))
    return "Process finished successfully!"


@eel.expose
def fr_en_file(name, n):
    dictionary.get_french_english_from_file(open(name), int(n))
    return "Process finished successfully!"


@eel.expose
def en_fr_file(name, n):
    dictionary.get_english_french_from_file(open(name), int(n))
    return "Process finished successfully!"


eel.start('index.html', size=(800, 800))
