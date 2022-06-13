import configparser
import crayons

def log(string):
    return print("{}".format(string))

def openOrCreateFile(nameFile, typeFile, addSectionDefault):
    if (typeFile == "config"):
        try:
            with open(nameFile, 'r') as configfile:
                config = configparser.ConfigParser()
                config.read(nameFile)
                log("Lecture du fichier " + crayons.yellow(nameFile) + "...")
                return config
        except:
            with open(nameFile, 'w') as configfile:
                config = configparser.ConfigParser()
                config.read_dict(addSectionDefault)
                config.sections()
                config.write(configfile)
                log("Création du fichier " + nameFile + "...")
                return config

def rewriteFile(nameFile, writeSection):
    try:
        with open(nameFile, 'w') as configfile:
            config = configparser.ConfigParser()
            config.read_dict(writeSection)
            config.sections()
            config.write(configfile)
            log("réécriture du fichier " + nameFile + "...")
            return config
    except:
        log("Erreur! impossible d'éxecuté le fichier")