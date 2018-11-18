T="ABCDE";
L="C->B,AB->C,CB->E,D->E,A->E";


def cierreTransitivo(Descriptores,DependenciasFuncionales):
    DependenciasFuncionales=DependenciasFuncionales.split(",");
    i=0;
    cierre=list(Descriptores);
    while (i<len(DependenciasFuncionales)):
        
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


                                n=n+1;
                            
                            m=m+1;

                            
                                
                                
                           
                        #print("Cierre final")
                        #print(cierre)

                k=k+1;
                
            
            
            j=j+1;
        
        
        i=i+1;
        
    return cierre

    Descriptores=['B']
    DependenciasFuncionales="C->B,AB->C,CB->E,D->E,A->E";
    cierreTransitivo(Descriptores,DependenciasFuncionales)
    print(cierreTransitivo(Descriptores,DependenciasFuncionales))
