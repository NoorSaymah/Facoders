name=str(input('Enter student\'s name :'))
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
if name=='Ahmad':
    name1=s1.remove('Ahmad')
    sum1=sum(s1)
    ruselt=sum1
elif name=='Sami':
    name1=s2.remove('Sami')
    sum1=sum(s2)
    ruselt=sum1
elif name=='Faris':
        name1=s3.remove('Faris')
        sum1=sum(s3)
        ruselt=sum1
else:
    name='Student is not recorded '
    ruselt=0

print(name,ruselt)
