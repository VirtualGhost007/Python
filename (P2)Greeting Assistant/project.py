print('Available greetings are Maam/maam/Sir/sir')#asking about the gender of person using it

y=input('What do you want to be called: ')

if y=='Maam':
    z="Maam"
    
    print('format should be (hour)(hour)(minute)(minute))')#to guide user about format of x

    x=int(input('Enter the time here: '))
    if x<1200:
        print('Good Morning',z.title())
    elif 1200<=x<1600:
        print('Good Afternoon',z.title())
    elif 1600<=x<2100:
        print('Good Evening',z.title())
    elif 2100<=x<2400:
        print('Good Night',z.title())
    else:
        print('Wrong format of time is given')

elif y=='maam':
    z="maam"
    
    print('format should be (hour)(hour)(minute)(minute))')#to guide user about format of x

    x=int(input('Enter the time here: '))
    if x<1200:
        print('Good Morning',z.title())
    elif 1200<=x<1600:
        print('Good Afternoon',z.title())
    elif 1600<=x<2100:
        print('Good Evening',z.title())
    elif 2100<=x<2400:
        print('Good Night',z.title())
    else:
        print('Wrong format of time is given')

elif y=='Sir':
    z="Sir"
    
    print('format should be (hour)(hour)(minute)(minute))')#to guide user about format of x

    x=int(input('Enter the time here: '))
    if x<1200:
        print('Good Morning',z.title())
    elif 1200<=x<1600:
        print('Good Afternoon',z.title())
    elif 1600<=x<2100:
        print('Good Evening',z.title())
    elif 2100<=x<2400:
        print('Good Night',z.title())
    else:
        print('Wrong format of time is given')

elif y=='sir':
    z="sir"
    
    print('format should be (hour)(hour)(minute)(minute))')#to guide user about format of x

    x=int(input('Enter the time here: '))
    if x<1200:
        print('Good Morning',z.title())
    elif 1200<=x<1600:
        print('Good Afternoon',z.title())
    elif 1600<=x<2100:
        print('Good Evening',z.title())
    elif 2100<=x<2400:
        print('Good Night',z.title())
    else:
        print('Wrong format of time is given')

else:
    print('Invalid greeting was given')