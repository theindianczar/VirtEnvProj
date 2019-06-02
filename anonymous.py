months=['January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December']

# 1. lambda function calculating the kinetic energy Ke=(m*v**2)/2
kinetic_energy = lambda m,v:(m*v**2)/2
print('Kinetic energy: ',kinetic_energy(85,20),'Joules')

# 2. Lambda function calculating energy in E= M*c**2
energy = lambda m,c=299792458  :(m*c**2)
print('energy is ',energy(0.00002),'Joules')

# 3. Lambda function calculating gravitationalforce F=G*m1*m2/r**2
force =lambda m1,m2=5.972*10**24,r=6371000: 6.67408*10**-11*m1*m2/r**2
print('force is ',force(84,62,2),'Newtons')

# 4. Lambda function creating abbreviation for each month from a list
abbr_month =list(map(lambda month:month[:3].upper(),months))
print(abbr_month)
print(type(abbr_month))