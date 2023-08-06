import pandas as pd


def getRandomSurname(numberSurnames = 1, pairs = False):
    surname = pd.read_csv("apellidos.csv")

    if numberSurnames >= 2:
        result_array = []
        tmp = ""
        for i in range(numberSurnames):
            if pairs:
                tmp = surname.sample()["apellido"].to_string(index=False)
            result_array.append(surname.sample()["apellido"].to_string(index=False) + " " + tmp)
        return result_array
    else:
        tmp = ""
        if pairs:
            tmp = surname.sample()["apellido"].to_string(index=False)
        return f"{surname.sample()['apellido'].to_string(index=False) + ' ' + tmp}"

def getRandomNames(names, numberNames = 1, fullName = False):
    if numberNames >= 2:
        result_array = []
        surnames = getRandomSurname(numberNames, True)
        for i in range(numberNames):
            temporal_return = names.sample()["nombre"].to_string(index=False).strip()

            if fullName:
                temporal_return += " "
                temporal_return += surnames[i]

            result_array.append(temporal_return)
        return result_array
    else:
        result_string = names.sample()["nombre"].to_string(index=False).strip()
        return result_string

def getRandomMaleName(numberNames=1, fullName=False):
    names = pd.read_csv("hombres.csv")
    return getRandomNames(names, numberNames, fullName)

def getRandomFemaleName(numberNames=1, fullName=False):
    names = pd.read_csv("mujeres.csv")
    return getRandomNames(names, numberNames, fullName)
