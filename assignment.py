
def printprimesum(): 
    '''
    objective:to calculate the sum of prime numbers below 2 million
    input parameter:None
    return value :None
    '''
    max1 = 2000000


    numbers = set(xrange(3, max1 + 1, 2)) 

    for number in xrange(3, int(max1 ** 0.5) + 1):
        if number not in numbers:
       
            continue

        num = number
        while num < max1:
            num += number
            if num in numbers:
            
                numbers.remove(num)

    print"\n sum of prime numbers below 2M =", 2 + sum(numbers)

def printmultiples():
    '''
    objective:to calculate the sum of multiples of 4 and 5
    input parameter:None
    return value :None
    '''
    low=4
    high=20
    total=0
    for i in range(low,high):
        if i%4 == 0 or i%5 == 0:
            total+=i
    print "\n sum of all multiples of 4 and 5 below 20 =",total

def printleastnum():
    '''
    objective:to print least number divisible by every number till 20
    input parameter:None
    output parameter:None
    '''
    least1 = 1
    low=1 
    high=21
    for i in range (low,high):
        if least1 % i > 0:
            for k in range (low,high):
                if (least1 * k) % i == 0:
                    least1 = least1 * k
                    break
    print "\nThe smallest number divisible by all nymber till 20 =",least1


def main1():
    '''
    objective:to invoke required functions
    input parameter:None
    return value :None
    '''
    print "\n welcome"
    #function calls to each function
    printprimesum()
    printmultiples()
    printleastnum()
    input ("press enter key :")

if __name__ == '__main__':
    main1()

    

