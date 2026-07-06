# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.



def divi(y):
    dividors = []
    for i in range(1, y):
        if y%i==0:
            dividors.append(i)
    dzielniki=len(dividors)
    return(dzielniki)


x=int(input("Podaj liczbę od 1 do 1000: "))

if divi(x)>2:
    print("Liczba nie jest pierwsza")
else:
    print("Liczba jest pierwsza")




