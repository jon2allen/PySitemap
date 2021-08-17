###########################################
# test harness for function wp_remove_dup
###########################################
from main import wp_remove_dup

test_list = ["https://www.jibsheet.net/linux", \
    "https://www.jibsheet.net/linux/index.php/2021/07/07",\
    "https://www.jibsheet.net/linux/index.php/2021/",\
    "https://www.jibsheet.net/linux/index.php/page/3/",\
    "https://www.jibsheet.net/linux/index.php/2021/05/08/",
    "https://www.jibsheet.net/linux/index.php/tag/linux/"]
    
print(test_list)

for item in test_list:
    print(wp_remove_dup(item))
    
assert (wp_remove_dup(test_list[0]) == False)    
assert (wp_remove_dup(test_list[1]) == True) 
assert (wp_remove_dup(test_list[2]) == True) 
assert (wp_remove_dup(test_list[3]) == False) 
assert (wp_remove_dup(test_list[4]) == True) 
assert (wp_remove_dup(test_list[5]) == False) 
""""
False
True
True
False
True
False
"""