def lcs_length(x,y):
    m,n=len(x),len(y)
    c_arr=np.zeros((m+1,n+1),dtype=int)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                c_arr[i,j]=c_arr[i-1,j-1]
            else:
                c_arr[i,j]=max(c_arr[i-1,j],c_arr[i,j-1])
        return c_arr[m,n]                         
    