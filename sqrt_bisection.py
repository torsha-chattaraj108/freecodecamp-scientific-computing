def sqrt_bisection(sqr_target,tolerance=1e-7,max_iterations=100):
#square root for negative numbers
    if sqr_target<0:
        print(f'Negative numbers do not have real roots')
    elif sqr_target==0:
#square root for 0
        root=0
        print(f'The square root of {sqr_target} is 0')
    elif sqr_target==1:
#square root of 1
        root=1
        print(f'The square root of {sqr_target} is 1')
    else:
#square root foe positive numbers
        low=0
        high=max(1,sqr_target)
        root=None
        for i in range(max_iterations):
            mid=(low+high)/2
            sqr_mid=mid**2
            if abs(sqr_mid-sqr_target)<tolerance:
                root=mid
                break
            elif sqr_mid<sqr_target:
                low=mid
            else:
                high=mid
        if root is None:
            print(f'Failed to print the square root of {sqr_target} within {max_iterations} iterations')
        else:
            print(f'The square root of {sqr_target} is approximately {root}')
    return root
N=int(input('Enter the number here: '))
sqrt_bisection(N)
