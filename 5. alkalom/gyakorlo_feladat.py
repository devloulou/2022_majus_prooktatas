# 1. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
# legkisebb értéket ezek közül!

def my_min(a, b, c):
    if b > a  and c > a:
        return a

    if a > b and c > b:
        return b  

    if a > c and b > c:
        return c

# print(my_min(3,1,2))

def my_min(*args):
    return min(args)

#print(my_min(2,4,3,4))

def my_min():
    temp = []
    for item in range(3):
        num = input("Kérlek addj meg egy számot")
        temp.append(int(num))

    return min(temp)

#print(my_min())

# my_list = input("Kérlej vesszővel tagolva add meg a számokat! ")

# my_list = [int(item) for item in my_list.split(",")]



# 2. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
# legnagyobb értéket ezek közül!

def my_max(*args):
    return max(args)

# def max(p):
#     print("szia")

#max()

my_list = [2,3,4,5]


# 3. Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
# érdemjegyet az alábbiak szerint! 1: ; 2: 50<=x<60; 
# 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

def my_grade(x):
    if x<50:
        return 1    
    elif 50<=x<60:
        return 2    
    elif 60<=x<70:
        return 3
    elif 70<=x<85:
        return 4
    else:
        return 5


# print(my_grade(99))

# 4. Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
# hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!

def my_func(x):
    if x%3==0 and x%5!=0:
        print(f"{x} 3-al osztható")
    elif x%5==0 and x%3!=0:
        print(f"{x} 5-al osztható")
    elif x%5==0 and x%3==0:
        print(f"{x} 5-el is és 3-al osztható")
    else:
        print(f"{x} nem osztható sem 3-al, sem 5-el ")

my_func(15)

# 5. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
# hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!


def my_func(a, b, c):
    if a+b==c or a+c==b or b+c==a:
        return True
    else:
        return False

def my_func(a, b, c):
    return a+b==c or a+c==b or b+c==a
