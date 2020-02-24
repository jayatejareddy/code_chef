# title-Tax Slabs
# problem from February Cook-Off 2020 Division 2
# cook your dish here
t=int(input())
for i in range(t):
    inc=int(input())
    tax=0
    if inc<=250000:
        net=inc-tax
    else:
        if inc<=500000:
            tax+=int(((inc-250000)*5)/100)
            net=inc-tax
        else:
            tax+=12500
            if inc<=750000:
                tax+=int(((inc-500000)*10)/100)
                net=inc-tax
            else:
                tax+=25000
                if inc<=1000000:
                    tax+=int(((inc-750000)*15)/100)
                    net=inc-tax
                else:
                    tax+=37500
                    if inc<=1250000:
                        tax+=int(((inc-1000000)*20)/100)
                        net=inc-tax
                    else:
                        tax+=50000
                        if inc<=1500000:
                            tax+=int(((inc-1250000)*25)/100)
                            net=inc-tax
                        else:
                            tax+=62500
                            tax+=int(((inc-1500000)*30)/100)
                            net=inc-tax
    print(net)
