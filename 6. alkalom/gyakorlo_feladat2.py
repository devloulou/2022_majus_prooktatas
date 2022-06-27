# Egyetemi féléves értékelő: írjatok egy olyan programot - függvények segíségével - ,
# amely az alábbi tanulók féléves jegyét meghatározza.
# Az értékelésnél a következő szabályokat kell betartani:

## a beadando a jegy 10%-át adja
## a vizsga a jegy 70%-át
## a labor gyakorlat pedig a jegy 20%-át

# Az eredmények a következők szerint kell meghatározni
# 90 - 100 => 5
# 80 - 89 => 4
# 70 - 79 => 3
# 60 - 69 => 2
# 0  - 59 => 1

# példa az elvárt eredményre:
#
#
# kriszta = { "tanulo":"Kriszta",
#          "beadando" : [70, 60, 30, 10],
#          "vizsga" : [70, 75],
#          "labor" : [68.20, 77.20]
#        }
# (ez egy lekalkulált eredmény)
# Kriszta
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# Kriszta átlag pontszáma: 69.54
# Kriszta tanuló eredménye: 2

# 2. feladat: az osztály átlag eredményeit is határozzátok meg:
# példa outputra:
#
# Osztály átlag pontszáma 72.79
# Osztály eredménye 3

kriszta = { "tanulo":"Kriszta",
         "beadando" : [70, 60, 30, 10],
         "vizsga" : [70, 75],
         "labor" : [68.20, 77.20]
       }


karcsi = { "tanulo":"Horváth Károly",
         "beadando" : [80, 50, 40, 20],
         "vizsga" : [75, 75],
         "labor" : [78.20, 77.20]
       }


jani = { "tanulo":"Potter János",
          "beadando" : [82, 56, 44, 30],
          "vizsga" : [80, 80],
          "labor" : [67.90, 78.72]
        }


denes = { "tanulo" : "Neumann Dénes",
          "beadando" : [77, 82, 23, 39],
          "vizsga" : [78, 77],
          "labor" : [80, 80]
        }


emese = { "tanulo" : "Morvai Emese",
         "beadando" : [67, 55, 77, 21],
         "vizsga" : [40, 50],
         "labor" : [69, 44.56]
       }


tomi = { "tanulo" : "Kiss Tamás",
        "beadando" : [29, 89, 60, 56],
        "vizsga" : [65, 56],
        "labor" : [50, 40.6]
      }


def get_grade(point):
    if point >= 90:
        return 5
    elif 90 > point and point >= 80:
        return 4
    elif 80 > point and point >= 70:
        return 3
    elif 70 > point and point >= 60:
        return 2
    else:
        return 1

def get_score(student):
    beadando = (sum(student['beadando'])/len(student['beadando']))*0.1 
    vizsga = (sum(student['vizsga'])/len(student['vizsga']))*0.7 
    labor = (sum(student['labor'])/len(student['labor']))*0.2

    return beadando + vizsga + labor

def my_func(student, key, percent):
    return (sum(student[key])/len(student[key]))*percent


def main():
    class_points = 0
    students = (karcsi, denes, emese, tomi, jani)
    for item in students:
        point = get_score(item)
        grade = get_grade(point)

        class_points += point

        print(f"{item['tanulo']}, pontszám: {point}, érdemjegy: {grade}")
        print('--------------------------------------------------------')

    class_points /= len(students)

    class_grade = get_grade(class_points)

    print(f"osztály pontszáma: {class_points}, érdemjegy: {class_grade}")


if __name__ == '__main__':
    main()