keys=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
dict_numbers={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
complete_result = []

def roman_numbers(number):
    result = ""
    more_digit = 0
    if number in keys:
        result += dict_numbers[number]
    else:
        for num in keys:
            if number > num:
                multi = number // num
                more_digit = number % num
                result += dict_numbers[num]*multi
                break
                
    complete_result.append(result)    
    if more_digit > 0 :
        roman_numbers(more_digit)         

def return_result():
    complete_result_aux = complete_result[:]
    complete_result.clear()
    return complete_result_aux
    