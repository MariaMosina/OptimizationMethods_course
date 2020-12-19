a, b, eps = 1.5, 2, 0.05
def passive_search(f, x, grad, a = a, b = b, eps = eps):
    
    n = round((b-a)/eps)+1
    x_s = [a+i*eps for i in range(n)]
    y_s = [f(x-i*grad) for i in x_s]
    res = y_s.index(min(y_s))
    print('res', res)
    return x_s[res]
