students = ["İngiltere Kralı", "Rahmetli Baskan Kennedy", "Taçsız Kral Pele", "Backenbauer", "Kaleci Mayer", "Nadia Komanaçi", "Brigitte Bardot", "Fenerbahçeli Cemil"]
print(students)

def addStudents():
    name=input("Eklenecek öğrenci ismi girin :")
    students.append(name)
    print(students)

def removeStudent():
    name=input("çıkarılacak öğrenci ismi girin :")
    students.remove(name)
    print(students)

def multiAddStudent():
    adet=input("kaç öğrenci eklenecek :")
    for i in range(0,int(adet)):
        name=input(str(i+1) + ". Eklenecek öğrenci ismi girin :")
        students.append(name)
    print(students)

def printStudents():
    for person in students:
        print(person)

def learnStudentNumber():
    name=input("Numarası öğrenilecek öğrenci ismi girin :")
    print(students.index(name))

def multiRemoveStudent():
    k=0
    adet = int(input("çıkarılacak öğrenci sayısı girin :"))
    while k<adet:
        ogrenciNo = int(input("listeden çıkarılacak öğrenci no girin :"))
        students.pop(ogrenciNo)
        k+=1
    print(students)


#addStudents()
#removeStudent()
#multiAddStudent()
#printStudents()
#learnStudentNumber()
multiRemoveStudent()
