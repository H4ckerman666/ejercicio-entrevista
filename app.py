from module.roman_numbers import roman_numbers, complete_result, return_result
from beautifultable import BeautifulTable


table = BeautifulTable()
numbers_for_table = []


number = input("type a decimal number: ")
if number != "":
    list_add = []
    roman_numbers(int(number))
    complete_result = return_result()
    result = "".join(complete_result)

    list_add.append(number)
    list_add.append(result)
    numbers_for_table.append(list_add)
    
    
else:         
    for number in range(1,51):
        list_add = []
        roman_numbers(number)
        complete_result = return_result()
        result = "".join(complete_result)

        list_add.append(number)
        list_add.append(result)
        numbers_for_table.append(list_add)
           
for element in numbers_for_table:
    table.rows.append(element)
    
table.columns.header = ["decimal number", "roman_rumber"]
print(table)