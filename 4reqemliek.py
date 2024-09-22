# En boyuk
print("4 reqemli eded daxil edin")

abcd = int(input())

if(999 < abcd < 10000):
    abc = abcd // 10
    ab = abc // 10
    c = abc % 10
    b = ab % 10
    a = ab // 10
    d = abcd % 10
    
    A = min(a, b, c, d)
    # --------------------------------------------------------------------------------------------------------------------
    if(A == a):
        B = min(b, c, d)
        if(B == b):
            C = min(c, d)
            
            if(C == c):
                D = d
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = c
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
        elif(B == c):
            C = min(b, d)
            
            if(C == b):
                D = d
                p
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = b
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
            
        else:
            C = min(b, c)
            
            if(C == b):
                D = c
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = b
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
# --------------------------------------------------------------------------------------------------------------------
                
    elif(A == b):
        B = min(a, c, d)
        
        if(B == a):
            C = min(c, d)
            
            if(C == d):
                D = c
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = d
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
            
        elif(B == c):
            C = min(a, d)
            
            if(C == a):
                D =d
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = a
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
            
        else:
            C = min(a, c)
            
            if(C == a):
                D = c
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = a
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
            
# --------------------------------------------------------------------------------------------------------------------
        
    elif(A == c):
        B = min(a, b, d)
        
        if(B == a):
            C = min(b, d)
            
            if(C == b):
                D = d
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = b
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
            
        elif(B == b):
            C = min(a, d)
            
            if(C == a):
                D = d
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = a
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
            
        else:
            C = min(a, b)
            
            if(C == b):
                D = a
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = b
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
            
# --------------------------------------------------------------------------------------------------------------------
        
    else:
        B = min(a, b, c)
        
        if(B == a):
            C = min(b, c)
            
            if(C == b):
                D = c
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = b
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
            
        elif(B == c):
            C = min(a, b)
            
            if(C == b):
                D = a
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = b
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
            
        else:
            C = min(a, c)
            
            if(C == a):
                D = c
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
                
            else:
                D = a
                
                if(A == B == C == 0):
                    print(D, A, B, C, sep='')
                    
                elif(A == B == D == 0):
                    print(C, A, B, D, sep='')
                    
                elif(A == C == D == 0):
                    print(B, A, C, D, sep='')
                    
                elif(B == C == D == 0):
                    print(A, B, C, D, sep='')
                    
                elif(A == B == 0):
                    print(C, A, B, D, sep='')   
                    
                elif(A == C == 0):
                    print(B, A, C, D, sep='')   
                    
                elif(A == D == 0):
                    print(B, A, D, C, sep='')
                
                elif(B == C == 0):
                    print(A, B, C, D, sep='')
                    
                elif(B == D == 0):
                    print(A, B, D, C, sep='')
                    
                elif(C == D == 0):
                    print(A, C, D, B, sep='')
                
                if(A == 0):
                    print(B, A, C, D, sep='')
                
                elif(B == 0):
                    print(A, B, C, D, sep='')   
                    
                elif(C == 0):
                    print(A, C, B, D, sep='')  
                
                else:
                    print(B, D, C, A, sep='')   
# --------------------------------------------------------------------------------------------------------------------
    
else:
    print("daxil etdiyiniz reqem 4 reqemli deyil")
    