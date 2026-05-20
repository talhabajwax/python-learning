# grades ABCD
# A = 90-100
# B = 80-89 
# C = 70-79
# D = 60-69
def grades():
 numbers = int(input('Enter Your numbers: '));
 if numbers >= 90 and numbers <= 100: 
    print('Your Grade is A');
 elif numbers >= 80 and numbers < 90:
    print('Your Grade is B');
 elif numbers >= 70 and numbers < 80:
    print('Your Grade is C');
 elif numbers >= 60 and numbers < 70:
    print('Your Grade is D');
 else:
    print('Your Grade is F');
    
grades();