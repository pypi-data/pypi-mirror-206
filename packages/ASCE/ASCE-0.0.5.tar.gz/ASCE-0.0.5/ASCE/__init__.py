import math
try:
    class matrix:
        def __init__(self,m):
            self.matrix=m
            self.columns=len(m[0])
            self.lines=len(m)
            if self.lines==self.columns:
                self.size=self.lines
            else:
                self.size=f"{self.lines}*{self.columns}"
        #print
        def __repr__(self):
            h=""
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    print(self.matrix[i][j],end="    ")
                print()
            return h
        
        @classmethod
        #matrice de zero
        def zeros(cls,l=1,c=1):
            k=[]
            for i in range(l):
                p=[]
                for j in range(c):
                    p.append(0)
                k.append(p)
            return matrix(k)
        #random matrix l et c lignes et colonnes et s et e range des nbs
        @classmethod
        def aleatory(cls,l,c,s=0,e=100):
            import random
            p=[]
            for i in range(l):
                k=[]
                for j in range(c):
                    u=random.randint(s,e)
                    k.append(u)
                p.append(k)
            return matrix(p)
        #arange from numpy
        @classmethod
        def arange(cls,s,e,p=1):
            l=[]
            i=s
            while i<e:
                l.append(i)
                i+=p
            return matrix([l])
        #idendity
        @classmethod
        def identity(cls,n):
            l=[]
            for i in range(n):
                s=[]
                for j in range(n):
                    if i!=j:
                        s.append(0)
                    else:
                        s.append(1)
                l.append(s)
            return matrix(l)
        @classmethod
        def triangle_sup(cls,n):
            l=[]
            for i in range(n):
                s=[]
                for j in range(n):
                    if i<=j:
                        s.append(1)
                    else:
                        s.append(0)
                l.append(s)
            return matrix(l)
        @classmethod
        def triangle_inf(cls,n):
            l=[]
            for i in range(n):
                s=[]
                for j in range(n):
                    if i>=j:
                        s.append(1)
                    else:
                        s.append(0)
                l.append(s)
            return matrix(l)
        
        def is_square(self):
            if self.columns==self.lines:
                return True
            else:
                return False

        @classmethod
        def list_of_zeros(cls,nb):
            l=[]
            for i in range(nb):
                l.append(0)
            return l
        def fill_with_zeros(self,other):
            a=max(self.lines,self.columns,other.lines,other.columns)
            deg=int(math.pow(2,math.ceil(math.log2(a))))      #Cette fonction cherche le valeur 2^n la plus proche a l'argument passe entre guillemets
            m1=self.matrix
            m2=other.matrix
            if self.columns<deg:
                for i in range(deg-self.columns):
                    for j in m1:
                        j.append(0)
            if other.columns<deg:
                for i in range(deg-other.columns):
                    for j in m2:
                        j.append(0)
            k=matrix.list_of_zeros(deg)
            if self.lines<deg:
                for i in range(deg-self.lines):
                    m1.append(k)
            if other.lines<deg:
                for i in range(deg-other.lines):
                    m2.append(k)
            return m1,m2
        


                    
        def trace(self):
            if self.lines!=self.columns:
                raise Exception("The matrix isn't a square matrix")
            d=0
            for i in range(len(self.matrix)):
                d+=self.matrix[i][i]
            return d

        def splitm(self):
            m1=self.matrix
            n1=(self.lines)//2
            a=[]
            b=[]
            c=[]
            d=[]
            for i in range(n1):
                s=[]
                for j in range(n1):
                    x=m1[i][j]
                    s.append(x)
                a.append(s)
            for i in range(n1,self.size):
                s=[]
                for j in range(n1,self.size):
                    x=m1[i][j]
                    s.append(x)
                d.append(s) 
            for i in range(n1):
                s=[]
                for j in range(n1,self.size):
                    x=m1[i][j]
                    s.append(x)
                b.append(s)

            for i in range(n1,self.size):
                s=[]
                for j in range(n1):
                    x=m1[i][j]
                    s.append(x)
                c.append(s)
            out=[a,b,c,d]
            return out

        def __add__(a,b):
            if a.lines!=b.lines or a.columns!=b.columns:
                raise Exception("They have to be the same size in order to add them")
            r=[]
            for i in range(a.lines):
                sl=[]
                for j in range(b.columns):
                    elt=a.matrix[i][j]+b.matrix[i][j]
                    sl.append(elt)
                r.append(sl)
            return(matrix(r))
        
        def __sub__(a,b):
            if a.lines!=b.lines or a.columns!=b.columns:
                raise Exception("Different size,math erroe")
            r=[]
            for i in range(a.lines):
                sl=[]
                for j in range(b.columns):
                    elt=a.matrix[i][j]-b.matrix[i][j]
                    sl.append(elt)
                r.append(sl)
            return(matrix(r))

        def twobytwo(a,b):
                C=[]
                for i in range(a.lines):
                    L=[]
                    for j in range(b.columns):
                        s=0
                        for t in range(b.lines):
                            s+=a.matrix[i][t]*b.matrix[t][j]
                        L.append(s)
                    C.append(L)
                return matrix(C)

 
        def trans(m):
            l=[]
            for i in range(m.columns):
                sl=[]
                for j in range(m.lines):
                    elt=m.matrix[j][i]
                    sl.append(elt)
                l.append(sl)
            return matrix(l)
                    


        def strip(m,x):
            l=[]
            for i in range(m.lines):
                s=[]
                for j in range(m.columns):
                    if j!=x:
                        elt=m.matrix[i][j]
                        s.append(elt)
                l.append(s)
            return matrix(l)

                              
                

        def det(m):
            j=m.matrix
            if not m.is_square():
                raise Exception ("It must be a square matrix")
            else:
                mat=m.matrix
                if m.size==2:
                    easy_det=mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]
                    return easy_det
                else:
                    ref=mat[0]
                    c=0
                    result=0
                    wo=matrix(m.matrix[1:])
                    for i in range(len(ref)):
                        a=wo.strip(i)
                        if c%2==0:
                            coef=ref[i]*a.det()
                        else:
                            coef=-ref[i]*a.det()
                        result+=coef
                        c+=1
                    return result

        def f(m,x):
            a=[]
            for i in range(m.lines-1):
                sl=[]
                for j in range(m.columns):
                    if j!=x:
                        elt=m.matrix[i][j]
                        sl.append(elt)
                a.append(sl)
            return(matrix(a))
        
        def cte_m(m,cte):
            l=[]
            for i in range(m.lines):
                l1=[]
                for j in range(m.columns):
                    elt=cte*m.matrix[i][j]
                    l1.append(elt)
                l.append(l1)
            return matrix(l)                    
            
                    

        def inverse(m):
            test=m.is_square()
            if not test:
                raise Exception("The matrix has to be a square matrix")
            if m.det()==0:
                raise Exception("det(matrix)=0, math error")
            if m.size==2:
                a=m.matrix
                deto=m.det()
                k=matrix([[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]])
                answer=k.cte_m(1/deto)
                return answer
                
            if m.size!=2:
                stop=0
                liste=[]
                for r in range(m.lines):
                    new_m=matrix(m.matrix[:])
                    new_m.matrix.pop(r)
                    l1=[]
                    for t in range(new_m.columns):
                        ajout=r+t
                        k=new_m.f(t)
                        nb=k.det()
                        if ajout%2!=0:
                            nb=-nb
                        l1.append(nb)
                    liste.append(l1)
                dete=m.det()
                cofac=matrix(liste).trans()
                reponse=cofac.cte_m(1/dete)
                return reponse
            
        def remove_excess(m,a,b):
            if m.lines==a and m.columns==b:
                return m
            else:
                s=m.matrix
                if m.lines!=a:
                    s=m.matrix[:a]
                if m.columns!=b:
                    l=[]
                    for i in s:
                        i=i[:b]
                        l.append(i)
                    return matrix(l)
                return matrix(s)
                        
            
                
            
        def __mul__(a,b):
            if a.columns!=b.lines:
                raise Exception("These two matrices can't be multiplied")
            if a.size==2 and b.size==2:
                return a.twobytwo(b)
            else:
                mat=a.fill_with_zeros(b)
                mat1=matrix(mat[0])
                mat2=matrix(mat[1])
                ref1=mat1.splitm()
                ref2=mat2.splitm()
                one=matrix(ref1[0])
                two=matrix(ref1[1])
                three=matrix(ref1[2])
                four=matrix(ref1[3])
                one2=matrix(ref2[0])
                two2=matrix(ref2[1])
                three2=matrix(ref2[2])
                four2=matrix(ref2[3])
                x=one*one2+two*three2
                y=one*two2+two*four2
                z=three*one2+four*three2
                h=three*two2+four*four2
                l1=x.matrix[0]+y.matrix[0]
                l2=x.matrix[1]+y.matrix[1]
                l3=z.matrix[0]+h.matrix[0]
                l4=z.matrix[1]+h.matrix[1]
                reponse=[l1,l2,l3,l4]
                return matrix(reponse).remove_excess(a.lines,b.columns)


except Exception as e:
    print(e)

if __name__=="__main__":   
    g=matrix([[1,2,7,1],[1,2,20,1],[1,3,4,1],[1,2,4,20]])
    c=matrix([[1,9],[1,1]])
    a=matrix([[1,2],[2,5],[1,3],[1,2]])
    v=matrix([[10,2],[3,1]])
    m=matrix.aleatory(2,3)
    print(m.matrix)
    print(v.matrix)
    print(c+v)
    print(v)

