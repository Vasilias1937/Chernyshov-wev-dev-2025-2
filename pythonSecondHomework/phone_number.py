import re  

def wrapper(f):  
    def fun(l):  
        formatted_numbers = []  
        for phone in l:  
            phone = re.sub(r'\D', '', phone)  
            if len(phone) == 11:  
                if phone.startswith('8'):  
                    phone = phone[1:]  
                elif phone.startswith('7'):  
                    phone = phone[1:]  
                else:  
                    phone = phone[1:]  
            elif len(phone) == 12 and phone.startswith('+7'):  
                phone = phone[2:]  

            if len(phone) == 10:  
                formatted_numbers.append('+7 ({}) {}-{}-{}'.format(phone[:3], phone[3:6], phone[6:8], phone[8:]))  
            else:  
                formatted_numbers.append(phone) 

        return f(formatted_numbers)  
    return fun  

@wrapper  
def sort_phone(l):  
    return sorted(l)  

if __name__ == '__main__':  
    l = [input() for _ in range(int(input()))]  
    print(*sort_phone(l), sep='\n')  