def cubrimientoMininoL2(T,L1):
    
    nuevasDependenciasL2=L1;
    nuevaDependenciaImplicante=[];
    nuevaDependenciaImplicado=[];
    combinacionesNuevaDependenciasImplicante=[];
    CierreCNDI=[]

    
    i=0;
    while(i<len(L1)):
        nuevaDependenciaImplicante=L1[i];
        nuevaDependenciaImplicante=nuevaDependenciaImplicante[0];
        nuevaDependenciaImplicado=L1[i];
        nuevaDependenciaImplicado=nuevaDependenciaImplicado[1];
        combinacionesNuevaDependenciasImplicante=ordenaCombinaciones(potencia(nuevaDependenciaImplicante));
        if(len(nuevaDependenciaImplicante)>1):
            j=0;
            while(j<len(combinacionesNuevaDependenciasImplicante)):
        
                if(len(nuevaDependenciaImplicante)!=len(combinacionesNuevaDependenciasImplicante[j])):
                    k=0;
                    combinacionNuevaDependenciasImplicante=combinacionesNuevaDependenciasImplicante[j];
                    #print("combinacionesNuevaDependenciasImplicante[j]")
                    # #print(combinacionesNuevaDependenciasImplicante[j])
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
                            ImplicantesParaEliminar=RestaConjuntos(nuevaDependenciaImplicante,combinacionNuevaDependenciasImplicante[k]);
                            q=0
                            while(q<len(ImplicantesParaEliminar)):
                                nuevaDependenciaImplicante.remove(ImplicantesParaEliminar[q])
                                q=q+1;
                            DFn.append(nuevaDependenciaImplicante)
                            DFn.append(nuevaDependenciaImplicado);
                            #nuevasDependenciasL2.append(DFn)
                            DFn=[]

                        k=k+1;


                j=j+1;
        #print("L2 FINAL")
        #print(nuevasDependenciasL2)
        i=i+1;
    return nuevasDependenciasL2;



   

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

T="ABCDE";
L="AB->C,BC->E,C->B,D->E,A->E";

#T="ABCDEFa";
#L="AE->DF,A->BC,E->a,C->A";

#T="ABCDEFa";
#L="AE->Da,A->BCa,E->B,CD->A,D->A";


#T="ABCDEF";
#L="AB->CE,D->E,D->F,C->A,BE->AC,BC->DA,CF->D,CD->BA,CB->F";

#T="ABCDEFG";
#L="AB->C,BD->FG,AE->C,C->DE";

#T="ABCDEFGHIJ"
#L="C->BD,E->AC,E->D,G->J,BG->F,F->H"

#T="CNLAKFaE"
#L="C->NL,CA->KF,L->E,A->a"

#T="DGPV"
#L="VD->PG"

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

#T="ABCDEFGHIJ";
#L="ABC->BD,EBAF->AC,EFGH->D,GAB->J,BG->F,F->H";





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
                                            print("atributos a eliminar")
                                            print(combinacionesDeV[u])
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
                    #print("Descriptor")
                    #print(M1[k])
                    #print("Ciere")
                    #print(PosibleClave)
                    if(PosibleClave==T):

                        M2.insert(inc,M1[k]);
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
        print("NO SE ENCONTRARON CLAVES")
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

    
    


   





    
