def solution(numbers):
    return [search(int(number)) for number in numbers]

def search(number):
    bits = ['0']+list(bin(number))[2:]
    for i in range(len(bits)-1, -1, -1):
        if bits[i]=='0':
            bits[i]='1'
            if i!=len(bits)-1 and bits[i+1]=='1':
                bits[i+1]='0'
            return int('0b'+''.join(bits), 2)
                
print(solution([2, 7]))