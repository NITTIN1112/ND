s1 = int(input('ENTER THE FIRST SIDE OF TRIANGLE'))
s2 = int(input('ENTER THE SECOND SIDE OF TRIANGLE'))
s3 = int(input('ENTER THE THIRD SIDE OF TRIANGLE'))
if s1 == (s2 and s3):
    print('EQUILATERAL TRIANGLE')
elif s1 == s2 and s3 != s2 and s3 != s1:
    print('ISOCELES TRIANGLE')

elif s1!=s2 and s2!=s3 and s1!=s3:
    print("SCALENE TRIANGLE")
