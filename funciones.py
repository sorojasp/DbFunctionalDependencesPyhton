def DescriptoresImplicantesConClave(descriptoresImplicantesDF,claves,tamanoClave):
    DependenciasFuncionalesConClave=[];
    claveAnalizada=[];
    DescriptorImplicanteAnalizado=[];

    m=0
    while(m<len(descriptoresImplicantesDF)):
        
        DescriptorImplicanteAnalizado=descriptoresImplicantesDF[m];
        n=0;
        while(n<tamanoClave):
            claveAnalizada=claves[n];
            o=0;
            while(o<len(claveAnalizada)):

                p=0;

                while(p<len(DescriptorImplicanteAnalizado)):

                    if(DescriptorImplicanteAnalizado[p]==claveAnalizada[o]):
                        counter=counter+1;
                        if(counter==len(DescriptorImplicanteAnalizado)):
                            DependenciasFuncionalesConClave.append(DescriptorImplicanteAnalizado);


                    
                    
                    p=p+1;

                o=o+1;

            
            

            n=n+1;
        
        m=m+1;

