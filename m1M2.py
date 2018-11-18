####Programa escrito por Ing.Stiven Rojas ########
# Programa calcula cierres transitivos, M1, M2 

from tkinter import*
from tkinter import ttk

lista = "123"
lista=list(lista)
adjunto="x"

lista.append(adjunto)
   
c=lista;

def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def ordenaCombinaciones(c):
    
    combinacionesOrdenadas=[];
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
       
        combinacionesOrdenadas.append(e);
    return combinacionesOrdenadas
   
#combinaciones=potencia(c);
#print(combinaciones)






##La variable Dependencias funcionales se esriben así:(AB->CD,E->D)#####
##La variable descriptor se escribe de la siguiente forma: AD #####


def cierreTransitivo(Descriptores,DependenciasFuncionales):
    DependenciasFuncionales=DependenciasFuncionales.split(",");
    i=0;
    cierre=list(Descriptores);
    CONTROLADORi=0;
    while (i<len(DependenciasFuncionales)):
        if(CONTROLADORi==1):
            i=0;

        CONTROLADORi=0;
        DependenciasFuncionalIndividual= DependenciasFuncionales[i].split("->")
        Implicante= DependenciasFuncionalIndividual[0];
        Implicado= DependenciasFuncionalIndividual[1];
        Implicado=list(Implicado)
        Implicante=list(Implicante)
        
        
        j=0;
        comparadorAtributos=0;
        while(j<len(Implicante)):
            k=0
            while(k<len(cierre)):
                if(Implicante[j]==cierre[k]):
                    comparadorAtributos=comparadorAtributos+1;
                    if(comparadorAtributos==len(Implicante)):
                        m=0;
                        #print("Implicante")
                        #print(Implicante)
                        #print("Implicados")
                        #print(Implicado)
                        #print("Cierre Inicial")
                        #print(cierre)
                        while(m<len(Implicado)):
                            n=0;
                            conta=0;
                            while(n<len(cierre)):
                                if(Implicado[m]!=cierre[n]):
                                    conta=conta+1;
                                    if(conta==len(cierre)):
                                        cierre.append(Implicado[m]);
                                        CONTROLADORi=1;
                                        cierre=list(cierre)
                                        
                                        


                                n=n+1;
                            
                            m=m+1;

                            
                                
                                
                           
                        #print("Cierre final")
                        #print(cierre)

                k=k+1;
                
            
            
            j=j+1;
        
      
        i=i+1;

        
    return cierre

###Se determina V y Z a traves del R(T,L)
 ## V= T - (los implicados)
##  T se ingresa de la siguiente manera= "ABCDE"
## Y L se ingresa de la siguiente manera (AB->C,DC->E)

#T="ABCDEF";
#L="AB->C,D->E,D->F,C->A,BE->C,BC->D,CF->D,CD->B,CB->F";

#T="ABCDEF";
#L="AB->C,C->DEF,E->F"

#T="ABCDE";
#L="AB->C,BC->E,C->B,D->E,A->E,E->B";


#T="ABCDE";
#L="AB->CD,BC->E,C->B,D->E,A->E,B->C";

#T="ABCDEFa";
#L="AE->DF,A->BC,E->a,C->A";

#######
#T="ABCDEF";
#L="AB->CE,D->E,D->F,C->A,BE->AC,BC->DA,CF->D,CD->BA,CB->F";

#T="ABCDEFG";
#L="AB->C,BD->FG,AE->C,C->DE";

#T="ABCDEFGHIJ"
#L="C->BD,E->AC,E->D,G->J,BG->F,F->H"

#T="CNLAKFaE"
#L="C->NL,CA->KF,L->E,A->a"

#T="DGPV"
#L="VD->PG,V->G"

#T="AUVWXYZ"
#L="UV->WX,U->YZ,V->A,Z->U"

#SEGUNDA FORMA NORMAL:
#T="CNLSAanF"
#L="C->NLS,A->a,CA->nF"

#TERCERA FORMA NORMAL:
#T="CNLSAanF"
#L="C->NL,L->S,A->a,CA->nF"


#T="CNBKAXFa"
#L="C->NBK,A->a,CA->XF"

#T="ABCDEFGHIJ"
#L="ABC->BD,EBAF->AC,EFGH->D,GAB->J,BG->F,F->H"

#T="ABCDEFGHIJ"
#L="EBAF->AC"




def implicantesEimplicados(L):
    implicanteDF=[];
    implicadoDF=[];
    implicantesDF=[];
    implicadosDF=[];
    descriptoresImplicantesDF=[];
    descriptoresImplicadosDF=[];
    DFs=[];
    L=L.split(",");
    i=0;
    DF1=[];
    while(i<len(L)):
        DF=L[i].split("->")
        implicanteDF=DF[0];
        implicadoDF=DF[1];

        descriptoresImplicadosDF.append(list(implicadoDF));
        descriptoresImplicantesDF.append(list(implicanteDF));
        

        DF1.append(list((sorted(implicanteDF))))
        DF1.append(list((sorted(implicadoDF))))
        DFs.insert(i,DF1);
        DF1=[];
        
        
        #descriptoresImplicadosDF=sorted(descriptoresImplicadosDF);
        #descriptoresImplicantesDF=sorted(descriptoresImplicantesDF);
        j=0;
        while(j<len(implicanteDF)):
            if(not(implicanteDF[j] in implicantesDF)):
                implicantesDF.append(implicanteDF[j])
            j=j+1;
        k=0;
        while(k<len(implicadoDF)):
            if(not(implicadoDF[k] in implicadosDF)):
                implicadosDF.append(implicadoDF[k])
            k=k+1;
        i=i+1;
    return implicantesDF, implicadosDF, descriptoresImplicantesDF, descriptoresImplicadosDF,DFs;

def RestaConjuntos(A,B): #Resta conjuntos A-B
    A=list(A);
    B=list(B)
    contador=0;
    resultado=[]
    
    A=sorted(A);
    B=sorted(B);
    if(A==B):
        A=A
    else:
        i=0;
        q=0;
        while(i<len(A)):
   
            contador=0;
            j=0
            while(j<len(B)):
                if (A[i] != B[j]):
                    contador=contador+1;
                    if(contador==len(B)):
                        
                        resultado.insert(q,A[i])
                        q=q+1;

                    
                j=j+1;
            
            i=i+1;

    resultado=sorted(resultado);

    return resultado;







def Z(T,L):
    T=list(T);
    implicantesDF,implicadosDF,descriptoresImplicantesDF,descriptoresImplicadosDF,DFs=implicantesEimplicados(L);
    #print("esta es L")
    #print(L)
    #print("implicantes")
    #print (implicantesDF)
    #print("implicados")
    #print(implicadosDF)
    #print(len(implicantesDF))
    #print("T es:")
    #print(T)
    #print("implicados")
    #print (implicadosDF)
    #print(len(implicadosDF))
    i=0;
    Z=[];
    
    Z=RestaConjuntos(T,implicadosDF);
    print("**Este es Z**")
    print(Z);
    

   

    





### V se define de la siguiente forma V="ABC" y Z se define de la misma
## manera Z="FG"

def m1M2(T,L):
    WUZcierre=[]
    W=[];
    M2=[];
    claves=[];
    V=[]
    implicantesDF,implicadosDF,descriptoresImplicantesDF,descriptoresImplicadosDF,DFs=implicantesEimplicados(L);
    zeta=RestaConjuntos(T,implicadosDF);
    #print("Esto es Z")
    #print(zeta)
    T=sorted(T)
    Zcierre=cierreTransitivo(zeta,L);
    Zcierre=sorted(Zcierre);
    #print("Zcierre Ordenado")
    #print(Zcierre)
    if(Zcierre==T):
        #print("Zcierre y T son iguales")
        #print("La clave es:")
        #print(zeta)
        claves=zeta;
        

    else:
        #print("Zcierre y T no son iguales")
        
        i=0;
        W=[];

        W=RestaConjuntos(T,implicantesDF);
        
        #print("este es W:")
        #print(W)
        

       

        WUZcierre=Zcierre;
        i=0;
        while(i<len(W)):
            if(not(W[i] in Zcierre)):
                WUZcierre.append(W[i])
            i=i+1;


        #print("este es WUZcierre:")
        #print(WUZcierre)
        if (WUZcierre==T):
            print("WUZcierre es igual a T")
            claves=T;
         
        else:
            #print("WUZcierre No es igual a T")
            V=list(T);
            i=0;
            while(i<len(WUZcierre)):
                if(WUZcierre[i] in T):
                    V.remove(WUZcierre[i]);
                i=i+1;
            #print("Este es V:")
            #print(V)
            
            if(V==T):
                combinacionesDeV=ordenaCombinaciones(potencia(V));
                #print("tamaño de todas la combinaciones")
                #print(len(combinacionesDeV));
                #print("todas las combinaciones")
                #print(combinacionesDeV)
                
                q=0;
                while(q<len(combinacionesDeV)):
                    #print("Descriptor:")
                    #print(q+1)
                    #print(combinacionesDeV[q]);
                    #print("Cierre de descriptor:")
                    CierrePosible=sorted(cierreTransitivo(combinacionesDeV[q],L));
                    #print(CierrePosible)
                    if(CierrePosible==T):
                        #print("es clave: ")
                        #print(q)
                        #print(combinacionesDeV[q])
                        claves.append(combinacionesDeV[q])
                        u=q+1;
                        
                        while(u<len(combinacionesDeV)):
                            conteoAtributosIguales=0;
                            s=0;
                            combinacionAevaluar=combinacionesDeV[u];
                            combinacionClave=combinacionesDeV[q];
                            #print("****COMBINACIÓN A EVALUAR****")
                            #print(u)
                            #print(combinacionAevaluar)
                            while(s<len(combinacionAevaluar)):
                                t=0;
                                while(t<len(combinacionClave)):
                                    if(combinacionAevaluar[s]==combinacionClave[t]):
                                        conteoAtributosIguales=conteoAtributosIguales+1;
                                        if(conteoAtributosIguales==len(combinacionClave)):
                                            #print("atributos a eliminar")
                                            #print(combinacionesDeV[u])
                                            combinacionesDeV.remove(combinacionesDeV[u]);
                                            conteoAtributosIguales=0;
                                            u=u-1;


                                    t=t+1;
                                s=s+1;

                            u=u+1;
                            
                        
                                    
                    else:
                        #print("Descriptor eliminado:")
                        #print(combinacionesDeV[q])
                        combinacionesDeV.remove(combinacionesDeV[q]);
                        q=q-1;
                    
                    q=q+1;
                
                #print("RESULTADO CLAVES:")
                #print(claves)
                #print("combinaciones sobrevivientes:")
                #print(combinacionesDeV)

            else:
                M2=[]
                k=0;
                m=[];
                M1=[]
                i=0;
                while(i<len(V)):
                    m.append(V[i]);
                    j=0;
                    while(j<len(zeta)):
                        m.append(zeta[j]);
                        j=j+1;
                    m=sorted(m);    
                    M1.insert(i,m)
                    m=[];
                    i=i+1;
                k=0;
                
                while(k<len(M1)):
                    inc=0;
                    PosibleClave=sorted(cierreTransitivo(M1[k],L));
                    print("++M2++")
                    print(M2)
                    #print("Descriptor")
                    #print(M1[k])
                    #print("Ciere")
                    #print(PosibleClave)
                    
                    if(PosibleClave==T):

                        #M2.insert(inc,M1[k]);
                        M2.append(M1[k])
                        inc=inc+1;
                

                    


                    k=k+1;
                #print("esto es M1")    
                #print(M1)
                #print("esto es M2")
                #print(M2)
                claves=M2;
                #print("tamaño de M2")
                #print(len(claves))
             

    if(claves==[]):
        
        claves=T;
    return zeta,Zcierre,W,WUZcierre,V,claves;
    
              
                
def DescriptoresImplicantesConClave(descriptoresImplicantesDF,claves,tamanoClave):
    DependenciasFuncionalesConClave=[];
    claveAnalizada=[];
    DescriptorImplicanteAnalizado=[];
    vectorImplicantesConClave=[]
    counter=0;
  

    

    m=0
    while(m<len(descriptoresImplicantesDF)):
        vectorImplicantesConClave.insert(m,0);
        DescriptorImplicanteAnalizado=descriptoresImplicantesDF[m];
        n=0;
        while(n<tamanoClave):
            if(tamanoClave==1):
                claveAnalizada=claves
                
            else:
                claveAnalizada=claves[n];
                
            o=0;

            #print("*claveAnalizada*")
            #print(claveAnalizada)
            #print(len(claveAnalizada))
            
            
            
            counter=0;
            while(o<len(claveAnalizada)):
            
            

                p=0;
                while(p<len(DescriptorImplicanteAnalizado)):
                  

                    if(DescriptorImplicanteAnalizado[p]==claveAnalizada[o]):
                        #print("DescriptorImplicanteAnalizado")
                        #print(DescriptorImplicanteAnalizado)
                        counter=counter+1;
                        
                        if(counter==len(claveAnalizada)):
                            
                            DependenciasFuncionalesConClave.append(DescriptorImplicanteAnalizado);
                            del(vectorImplicantesConClave[m])
                            vectorImplicantesConClave.insert(m,1)
                            
                    p=p+1;

                o=o+1;
            n=n+1;
        m=m+1;
 
    return vectorImplicantesConClave,DependenciasFuncionalesConClave





def SecondFN(T,L):
    RestaEn2FN=True;
    implicantesDF,implicadosDF,descriptoresImplicantesDF,descriptoresImplicadosDF,DFs=implicantesEimplicados(L);
   
    
    T=list(T);
    #print("Esto es T")
    #print(T)
    zeta,Zcierre,W,WUZcierre,V,claves=m1M2(T,L);
    #print("Estas son las claves:")
    #print(claves)
    
    DependenciasFuncionalesConClave=[];
    
    contadorAtributos=0;
    counter=0;
    soloUnaClave=False;
    soloUnDescriptorImplicante=False;
 
    DescriptorImplicanteAnalizado=[];
    r=0;
    
    while(r<len(claves)):
        if(len(claves[r])==1):
            counter=counter+1;
            if(counter==len(claves)):
                soloUnaClave=True;
        r=r+1;
    r=0;

    while(r<len(descriptoresImplicantesDF)):
        if(len(descriptoresImplicantesDF[r])==1):
            counter=counter+1;
            if(counter==len(descriptoresImplicantesDF)):
                soloUnDescriptorImplicante=True;
        r=r+1;

    if(soloUnaClave==True):
        tamanoClave=1;
        vectorImplicantesConClave,DfsConClaves=DescriptoresImplicantesConClave(descriptoresImplicantesDF,claves,tamanoClave);
    else:
        tamanoClave=len(claves);
        vectorImplicantesConClave,DfsConClaves=DescriptoresImplicantesConClave(descriptoresImplicantesDF,claves,tamanoClave);
    
    #print("DfsConClaves:")
    #print(DfsConClaves)
    #print("DFs")
    #print(DFs)
    #print("claves")
    #print(claves)
    #print(vectorImplicantesConClave)


    atributosPrimos=[];
    atributosNoPrimos=[];

    i=0;
    atributosPrimos.append("0");
    while(i<len(DfsConClaves)):
        j=0;
        claveAnalizada=DfsConClaves[i];
        while(j<len(claveAnalizada)):
            k=0;
            contadorAtributos=0;
            while(k<len(atributosPrimos)):
                if(atributosPrimos[k]!=claveAnalizada[j]):
                    contadorAtributos=contadorAtributos+1;
                    if(contadorAtributos==len(atributosPrimos)):
                        atributosPrimos.append(claveAnalizada[j]);

                k=k+1

            j=j+1;

        i=i+1;
        claveAnalizada=[];
    atributosPrimos.remove("0");
 

    if(DfsConClaves==[]):
        atributosPrimos=T;
        RestaEn2FN=False;

    atributosNoPrimos=RestaConjuntos(T,atributosPrimos);
    #print("Estos son los atributos No Primos")
    #print(atributosNoPrimos)

    #print("atributosPrimos")
    #print(atributosPrimos)

    ImplicadoDeClave=[];
    ImplicadosDeClaves=[]

    u=0;
    while(u<len(vectorImplicantesConClave)):
        if(vectorImplicantesConClave[u]==1):
            ImplicadoDeClave=DFs[u];
            ImplicadoDeClave=ImplicadoDeClave[1];
            ImplicadosDeClaves.append(ImplicadoDeClave)
        u=u+1;

    #print("ImplicadosDeClaves")
    #print(ImplicadosDeClaves)

    ImplicadoDeNoPrimo=[];
    ImplicadosDeNoPrimos=[]

    u=0;
    while(u<len(vectorImplicantesConClave)):
        if(vectorImplicantesConClave[u]==0):
            ImplicadoDeNoPrimo=DFs[u];
            ImplicadoDeNoPrimo=ImplicadoDeNoPrimo[1];
            ImplicadosDeNoPrimos.append(ImplicadoDeNoPrimo)
        u=u+1;
    #print("ImplicadosDeNoPrimos")
    #print(ImplicadosDeNoPrimos)

    i=0;
    while(i<len(ImplicadosDeClaves)):
        ImplicadoDeClave=ImplicadosDeClaves[i];
        j=0;
        while(j<len(ImplicadoDeClave)):
            ImplicadoDeClave[j];
            k=0;
            while(k<len(ImplicadosDeNoPrimos)):
                ImplicadoDeNoPrimo=ImplicadosDeNoPrimos[k];
                m=0;
                while(m<len(ImplicadoDeNoPrimo)):
                    if(ImplicadoDeNoPrimo[m]==ImplicadoDeClave[j]):
                        
                        RestaEn2FN=False

                    m=m+1;
                k=k+1;
            j=j+1;
        i=i+1;

      
    
        

    #print(L)
    return RestaEn2FN,atributosPrimos,atributosNoPrimos,vectorImplicantesConClave;
    
#RestaEn2FN,atributosPrimos,atributosNoPrimos,vectorImplicantesConClave=SecondFN(T,L);

#print("RestaEn2FN:")
#print(RestaEn2FN)



def thirdFN(RestaEn2FN,atributosPrimos,atributosNoPrimos,T,L):
    counter=0;
    RestaEn3FN=True;
    #print("RestaEn2FN:")
    #print(RestaEn2FN);

    
    if(RestaEn2FN==True):
        RestaEn2FN,atributosPrimos,atributosNoPrimos,vectorImplicantesConClave=SecondFN(T,L);  
        CombinacionesNoPrimos=ordenaCombinaciones(potencia(atributosNoPrimos));
        q=0;
        while(q<len(atributosNoPrimos)):
        #while(q<len(CombinacionesNoPrimos)):
            #CierreCombinacionNoPrimaEvaluada=cierreTransitivo(CombinacionesNoPrimos[q],L);
            CierreCombinacionNoPrimaEvaluada=cierreTransitivo(atributosNoPrimos[q],L);
            CierreCombinacionNoPrimaEvaluada.remove(atributosNoPrimos[q])
            #print("atributosNoPrimos[q]")
            #print(atributosNoPrimos[q])
            #print("CierreCombinacionNoPrimaEvaluada")
            #print(CierreCombinacionNoPrimaEvaluada)
            k=0;
            while(k<len(atributosNoPrimos)):
                r=0;
                while(r<len(CierreCombinacionNoPrimaEvaluada)):
                    
                    if(CierreCombinacionNoPrimaEvaluada[r]==atributosNoPrimos[k]):
                        #print("**atributosNoPrimos**")
                        #print(atributosNoPrimos[k])
                        #print("**CierreCombinacionNoPrimaEvaluada**")
                        #print(CierreCombinacionNoPrimaEvaluada)

                        counter=counter+1;
                        RestaEn3FN=False;
                    r=r+1;
                k=k+1;
            q=q+1;

    else:
         RestaEn3FN=False;

    return RestaEn3FN;
    
#RestaEn3FN=thirdFN(RestaEn2FN,atributosPrimos,atributosNoPrimos,T,L)
#print("RestaEn3FN")
#print(RestaEn3FN)


def FormaNormalDeBoyceCodd(RestaEn3FN,T,L):
    RestaenFNBC=True
    RestaEn2FN,atributosPrimos,atributosNoPrimos,vectorImplicantesConClave=SecondFN(T,L);
    implicantesDF,implicadosDF,descriptoresImplicantesDF,descriptoresImplicadosDF,DFs=implicantesEimplicados(L)
    if(RestaEn3FN==True):
        i=0;
        while(i<len(DFs)):
            ImplicadoDfs=DFs[i]
            ImplicadoDfs=ImplicadoDfs[1]
            ImplicanteDfs=DFs[i]
            ImplicanteDfs=ImplicanteDfs[0]
            strImplicanteDfs = ''.join(ImplicanteDfs);
            strImplicadoDfs = ''.join(ImplicadoDfs);
            if(strImplicadoDfs in strImplicanteDfs):
                RestaenFNBC=False
            i=i+1;
    else:
        RestaenFNBC=False


    return RestaenFNBC

#RestaenFNBC=FormaNormalDeBoyceCodd(RestaEn3FN,T,L)

#print("RestaenFNBC")
#print(RestaenFNBC)






   
def cubrimientoMininoL1(T,L):
    nuevasDependenciasL1=[];
    DFn=[];
    implicantesDF,implicadosDF,descriptoresImplicantesDF,descriptoresImplicadosDF,DFs=implicantesEimplicados(L);
    i=0;
    j=0;
    while(i<len(descriptoresImplicadosDF)):
        if(len(descriptoresImplicadosDF[i])>1):
            j=0;
            
            descriptorImplicado=descriptoresImplicadosDF[i];
            while(j<len(descriptorImplicado)):
                DFn.append(descriptoresImplicantesDF[i])
                DFn.append(descriptorImplicado[j]);
                nuevasDependenciasL1.insert(j,DFn)
                DFn=[]
                j=j+1;
        else:
            DFn.append(descriptoresImplicantesDF[i])
            DFn.append(descriptoresImplicadosDF[i]);
            nuevasDependenciasL1.insert(j,DFn)
            j=j+1;
            DFn=[];
        i=i+1;
    return nuevasDependenciasL1;

def cubrimientoMininoL2(T,aL1,L):
    L2=[]
    nuevasDependenciasL2=aL1;
    aL1=[]
    #print("L2 INICIAL")
    #print(nuevasDependenciasL2)
    i=0;
    while(i<len(nuevasDependenciasL2)):
        NDI=nuevasDependenciasL2[i];
        nuevaDependenciaImplicante=NDI[0];
        nuevaDependenciaImplicado=NDI[1];
        combinacionesNuevaDependenciasImplicante=ordenaCombinaciones(potencia(nuevaDependenciaImplicante));
     
        j=0;
        while(j<len(combinacionesNuevaDependenciasImplicante)):
            if(len(nuevaDependenciaImplicante)!=len(combinacionesNuevaDependenciasImplicante[j])):
                
                k=0;
                combinacionNuevaDependenciasImplicante=combinacionesNuevaDependenciasImplicante[j];
                #print("combinacionesNuevaDependenciasImplicante[j]")
                #print(combinacionesNuevaDependenciasImplicante[j])

                while(k<len(combinacionNuevaDependenciasImplicante)):
                    CierreCNDI=cierreTransitivo(combinacionNuevaDependenciasImplicante[k],L)
                    strCierreCNDI = ''.join(CierreCNDI);
                    strNuevaDependenciaImplicado=''.join(nuevaDependenciaImplicado)
                    



                    if(strNuevaDependenciaImplicado in strCierreCNDI):
                        DFn=[]
                        

                        #print("***genial**")
                        #print(combinacionNuevaDependenciasImplicante[k])
                        #print(strCierreCNDI )
                        #print(strNuevaDependenciaImplicado)

                        #print("nuevaDependenciaImplicante")
                        #print(nuevaDependenciaImplicante)

                        

                        #if(nuevaDependenciaImplicado!=(RestaConjuntos(nuevaDependenciaImplicante,combinacionNuevaDependenciasImplicante[k]))):
                      
                        
                        
                        resta=RestaConjuntos(nuevaDependenciaImplicado,combinacionNuevaDependenciasImplicante[k])
                     
                        if(resta!=[]):
                            ImplicantesParaEliminar=RestaConjuntos(nuevaDependenciaImplicante,combinacionNuevaDependenciasImplicante);
                            q=0;
                            while(q<len(ImplicantesParaEliminar)):
                                nuevaDependenciaImplicante.remove(ImplicantesParaEliminar[q])
                                q=q+1;
                            DFn=[]
                            DFn.append(nuevaDependenciaImplicante)
                            DFn.append(nuevaDependenciaImplicado);
                            
                            DFn=[]
                       

                    
                
                    k=k+1;


            else:
                hiio=0
            
            j=j+1;


      
        
        

        i=i+1;

    L1=[]

    L2=nuevasDependenciasL2
    return L2


def cubrimientoMininoL3(T,L2):
    L3=[];
    i=0;
    b=0
    nuevasDependenciasL3=[]
    
    while(b<len(L2)):
        L3=[]
        i=0
        while(i<len(L2)):
            if(i!=b):
                L3.insert(i,L2[i])
            else:
                DependenciaFuncional=L2[i];
                DescriptorImplicante=DependenciaFuncional[0]
                DescriptorImplicado=DependenciaFuncional[1]
            i=i+1;

        ResulCierre=cierreTransitivoConDFSenList(DescriptorImplicante,L3)
        strResulCierre = ''.join(ResulCierre);
        strDescriptorImplicado = ''.join(DescriptorImplicado);

        if (not(strDescriptorImplicado in strResulCierre) ):
            nuevasDependenciasL3.insert(b,L2[b])

        
        
        b=b+1
        
        
        
        #print("NUEVO L3")
        #print(L3)
        #print("Descriptor a evaluar")
        #print(DescriptorImplicante)
        #print(" DescriptorImplicado")
        #print( DescriptorImplicado)
        #print("Cierre")
        #print(ResulCierre)
        
       
    
    
    #print("esto es L2")
    #print(L2)
    #print("esto es L3")
    #print(L2)
    

        
    return nuevasDependenciasL3


def cierreTransitivoConDFSenList(Descriptores,DependenciasFuncionales):
    
    i=0;
    cierre=list(Descriptores);
    CONTROLADORi=0;
    while (i<len(DependenciasFuncionales)):
        if(CONTROLADORi==1):
            i=0;

        CONTROLADORi=0;
        DependenciasFuncionalIndividual= DependenciasFuncionales[i]
        Implicante= DependenciasFuncionalIndividual[0];
        Implicado= DependenciasFuncionalIndividual[1];
        Implicado=list(Implicado)
        Implicante=list(Implicante)
        
        
        j=0;
        comparadorAtributos=0;
        while(j<len(Implicante)):
            k=0
            while(k<len(cierre)):
                if(Implicante[j]==cierre[k]):
                    comparadorAtributos=comparadorAtributos+1;
                    if(comparadorAtributos==len(Implicante)):
                        m=0;
                        #print("Implicante")
                        #print(Implicante)
                        #print("Implicados")
                        #print(Implicado)
                        #print("Cierre Inicial")
                        #print(cierre)
                        while(m<len(Implicado)):
                            n=0;
                            conta=0;
                            while(n<len(cierre)):
                                if(Implicado[m]!=cierre[n]):
                                    conta=conta+1;
                                    if(conta==len(cierre)):
                                        cierre.append(Implicado[m]);
                                        CONTROLADORi=1;
                                        cierre=list(cierre)
                                        
                                        


                                n=n+1;
                            
                            m=m+1;

                            
                                
                                
                           
                        #print("Cierre final")
                        #print(cierre)

                k=k+1;
                
            
            
            j=j+1;
        
      
        i=i+1;

        
    return cierre

def convertLisToString(L):
    i=0
    strLx=""
    while(i<len(L)):
        implicanteL=L[i];
        implicanteL=implicanteL[0];
        implicadoL=L[i];
        implicadoL=implicadoL[1];
        strimplicanteL = ''.join(implicanteL);
        strimplicadoL = ''.join(implicadoL);
        if(i==(len(L)-1)):
            strL=strimplicanteL + '->' + strimplicadoL ;
        else:
            strL=strimplicanteL + '->' + strimplicadoL + ',';
        strLx=strLx+strL;
        i=i+1 

        

    return strLx;


###############################################

#nuevasDependenciasL1=cubrimientoMininoL1(T,L);
#L1prueba=[]

#i=0;
#while(i<len(nuevasDependenciasL1)):
#    L1prueba.insert(i,nuevasDependenciasL1[i])
#    i=i+1;

#print("L1prueba")
#print(L1prueba)

#L2=cubrimientoMininoL2(T,L1prueba,L);

#print("++L2++")
#print(L2)

#hola=[]
#hola=cubrimientoMininoL3(T,L2)

#print("**L3***")
#print(hola)


#strHola=convertLisToString(hola)

#print(strHola)


#print(SecondFN(T,strHola))


################# Desde esta parte de inicia la construcción ################ 
#############              de la interfaz gráfica #########################


a="hola";



AspectosR=" "
strClaves=""
strCubrimientoMinimo=""
strRestaen2FN=""
strRestaen3FN=""
strRestaenFNBC=""


master = Tk()
LaspectosR=Label(master,text=AspectosR ,height=3)
LaspectosR.grid(row=3, column=1,sticky=W)

Lclaves=Label(master,text=strClaves, height=3)
Lclaves.grid(row=4, column=1,sticky=W)

LcubrimientoMinimo=Label(master,text=strCubrimientoMinimo, height=3)
LcubrimientoMinimo.grid(row=5, column=1,sticky=W)

LRestaEn2FN=Label(master,text=strRestaen2FN, height=3)
LRestaEn2FN.grid(row=6, column=1,sticky=W)

LRestaen3FN=Label(master,text=strRestaen3FN, height=3)
LRestaen3FN.grid(row=7, column=1,sticky=W)


LRestaenFNBC=Label(master,text=strRestaenFNBC, height=3)
LRestaenFNBC.grid(row=8, column=1,sticky=W)

Label(master, text="Introduzca T").grid(row=0,column=0)
Label(master, text="Introduzca L").grid(row=1,column=0)

entryT = Entry(master, width=300)
entryL = Entry(master, width=300)

entryT.grid(row=0, column=1)
entryL.grid(row=1, column=1)

def calculaAspectosDeR():
    T=entryT.get();
    L=entryL.get();
    implicantesDF, implicadosDF, descriptoresImplicantesDF, descriptoresImplicadosDF,DFs=implicantesEimplicados(L);
    RestaEn2FN,atributosPrimos,atributosNoPrimos,vectorImplicantesConClave=SecondFN(T,L);
    strimplicantesDF= ''.join(implicantesDF);
    strimplicadosDF= ''.join(implicadosDF);
    strAtributosPrimos=''.join(atributosPrimos);
    strAtributosNoPrimos=''.join(atributosNoPrimos);
    #strAspectosDeR="implicantes: "+strimplicantesDF+" - "+"implicados: "+strimplicadosDF + " - " + "Atributos primos: " + strAtributosPrimos + " - " + "Atributos no primos: " + strAtributosNoPrimos
    strAspectosDeR="implicantes: "+strimplicantesDF+" - "+"implicados: "+strimplicadosDF 
    LaspectosR.config(text=strAspectosDeR)

   

def Determina_Claves():
    T=entryT.get();
    L=entryL.get();
    print("Muestra lo que hay en T")
    print(entryT.get())
    print("Muestra lo que hay en L")
    print(entryL.get())
    zeta,Zcierre,W,WUZcierre,V,claves=m1M2(T,L)
    print(claves)
   
    Lclaves.config(text=claves)
    
    print("Esta es la clave")
    print(len(claves))
    print(claves)

def calculaCubrimientoMinimo():
    T=entryT.get();
    L=entryL.get();
    nuevasDependenciasL1=cubrimientoMininoL1(T,L);
    L1prueba=[]
    i=0;
    while(i<len(nuevasDependenciasL1)):
        L1prueba.insert(i,nuevasDependenciasL1[i])
        i=i+1;
    print("L1prueba")
    print(L1prueba)
    L2=cubrimientoMininoL2(T,L1prueba,L);
    print("++L2++")
    print(L2)
    hola=[]
    hola=cubrimientoMininoL3(T,L2)
    print("**L3***")
    print(hola)
    strHola=convertLisToString(hola)
    print(strHola)
    LcubrimientoMinimo.config(text=strHola)

def estaEn2FN():
    T=entryT.get();
    L=entryL.get();
    RestaEn2FN,atributosPrimos,atributosNoPrimos,vectorImplicantesConClave=SecondFN(T,L);
    print("RestaEn2FN:")
    print(RestaEn2FN)
    if(RestaEn2FN==True):
        LRestaEn2FN.config(text="R esta en Segunda forma normal")
    else:
        LRestaEn2FN.config(text="R No esta en Segunda forma normal")

def estaEn3FN():
    T=entryT.get();
    L=entryL.get();
    RestaEn2FN,atributosPrimos,atributosNoPrimos,vectorImplicantesConClave=SecondFN(T,L);
    RestaEn3FN=thirdFN(RestaEn2FN,atributosPrimos,atributosNoPrimos,T,L)
    print("RestaEn3FN:")
    print(RestaEn3FN)
    if(RestaEn3FN==True):
        LRestaen3FN.config(text="R esta en Tercera forma normal")
    else:
        LRestaen3FN.config(text="R No esta en Tercera forma normal")

def estaEnFNBoyceCodd():
    T=entryT.get();
    L=entryL.get();
    RestaEn2FN,atributosPrimos,atributosNoPrimos,vectorImplicantesConClave=SecondFN(T,L);
    RestaEn3FN=thirdFN(RestaEn2FN,atributosPrimos,atributosNoPrimos,T,L)
    RestaenFNBC=FormaNormalDeBoyceCodd(RestaEn3FN,T,L)
    print("RestaenFNBC")
    print(RestaenFNBC)
    if(RestaenFNBC==True):
        LRestaenFNBC.config(text="R esta en  forma normal Boyce Codd")
    else:
        LRestaenFNBC.config(text="R esta No en  forma normal Boyce Codd")




Button(master, text='Calcula aspecto de R', command=calculaAspectosDeR,width=20, height=3).grid(sticky=W,row=3,pady=4)
Button(master, text='Claves', command=Determina_Claves,width=20, height=3).grid(row=4, sticky=W, pady=4)
Button(master, text='Recubrimiento mínimo', command=calculaCubrimientoMinimo,width=20, height=3).grid(row=5, sticky=W, pady=4)
Button(master, text='Esta en 2FN?', command=estaEn2FN,width=20, height=3).grid(row=6, sticky=W, pady=4)
Button(master, text='Esta en 3FN?', command=estaEn3FN,width=20, height=3).grid(row=7, sticky=W, pady=4)
Button(master, text='Esta en FN Boyce-Codd?', command=estaEnFNBoyceCodd,width=20, height=3).grid(row=8, sticky=W, pady=4)
Button(master, text='Quit ', command=master.quit).grid(row=9, sticky=W, pady=4)


mainloop( )


    




    





    

