

#//////////////////////////////////////////////////////////////////////////
# 1. 문자결합해서 반환


print("1-1. 리턴에서 바로 반환")
print("2개의 문자열을 입력받으세요. \n")
s_num1 = input("1번째 문자입력:")
s_num2 = input("2번째 문자입력:")

def my_join(str1,str2) :
    return str1 + str2

print(my_join(s_num1,s_num2))
print("/"*80)

#//////////////////////////////////////////////////////////////////////////
# 1-2. 변수로 반환한 예

print("1-2. 변수로 반환")
print("2개의 문자열을 입력받으세요. \n")
s_num1 = input("1번째 문자입력:")
s_num2 = input("2번째 문자입력:")

def my_join(str1,str2) :
    s_sum = str1 + str2
    return s_sum

print(my_join(s_num1,s_num2))
print("/"*80)



#//////////////////////////////////////////////////////////////////////////
# 2. 문자 분리해서 list로 반환하기



s_str1 = "HellochIchamchverychhungrychnowccc"
s_str2 = ""
n=0

print("2.문자 분리해서 list로 반환")
print("str에 저장되어있는문자 :", s_str1)


def my_spilt(str,ch):
    str_len= len(str)
    str_box= []
    i = 1
    n = 0

    for i in range(str_len):

        if str[i] == "h":
            if str[i-1] == "c":
                str_box.append(ch)
                ch = ''

        elif str[i] != "c" :
           # print(str[i], end='')
            ch += str[i]
            #str_box.append(str[i])
            #print(str_box)


    print("결과:",str_box)
        

my_spilt(s_str1,s_str2)







