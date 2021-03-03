class Diputados:
    def __init__(self, candidatos, departamentos):
        self.candidatos = candidatos
        self.departamentos = departamentos
        self.diputados_N = []
        self.diputados_ARENA = []
        self.diputados_FMLN = []
        self.diputados_GANA = []
        self.diputados_PCN = []
        self.diputados_VAMOS = []
        self.diputados_PDC = []
        self.diputados_NT = []

        for i in range(0, len(candidatos)):
            if (candidatos[i][1] == "N"):
                self.diputados_N.append(candidatos[i])
            elif (candidatos[i][1] == "ARENA"):
                self.diputados_ARENA.append(candidatos[i])
            elif (candidatos[i][1] == "FMLN"):
                self.diputados_FMLN.append(candidatos[i])
            elif (candidatos[i][1] == "GANA"):
                self.diputados_GANA.append(candidatos[i])
            elif (candidatos[i][1] == "PCN"):
                self.diputados_PCN.append(candidatos[i])
            elif (candidatos[i][1] == "VAMOS"):
                self.diputados_VAMOS.append(candidatos[i])
            elif (candidatos[i][1] == "PDC"):
                self.diputados_PDC.append(candidatos[i])
            elif (candidatos[i][1] == "NT"):
                self.diputados_NT.append(candidatos[i])
    
    def getDiputadosDepartamento(self, departamento):
        self.diputados = []

        for i in range(0, len(self.departamentos)):
            if(self.departamentos[i][1] == "N" and self.departamentos[i][0] == departamento):
                index = [k for k, e in enumerate(self.diputados_N) if e[0] == departamento]
                for j in range(0, self.departamentos[i][2]):
                    self.diputados.append(self.diputados_N[index[j]])
            elif(self.departamentos[i][1] == "ARENA" and self.departamentos[i][0] == departamento):
                index = [k for k, e in enumerate(self.diputados_ARENA) if e[0] == departamento]
                for j in range(0, self.departamentos[i][2]):
                    self.diputados.append(self.diputados_ARENA[index[j]])
            elif(self.departamentos[i][1] == "FMLN" and self.departamentos[i][0] == departamento):
                index = [k for k, e in enumerate(self.diputados_FMLN) if e[0] == departamento]
                for j in range(0, self.departamentos[i][2]):
                    self.diputados.append(self.diputados_FMLN[index[j]])
            elif(self.departamentos[i][1] == "GANA" and self.departamentos[i][0] == departamento):
                index = [k for k, e in enumerate(self.diputados_GANA) if e[0] == departamento]
                for j in range(0, self.departamentos[i][2]):
                    self.diputados.append(self.diputados_GANA[index[j]])
            elif(self.departamentos[i][1] == "PCN" and self.departamentos[i][0] == departamento):
                index = [k for k, e in enumerate(self.diputados_PCN) if e[0] == departamento]
                for j in range(0, self.departamentos[i][2]):
                    self.diputados.append(self.diputados_PCN[index[j]])
            elif(self.departamentos[i][1] == "VAMOS" and self.departamentos[i][0] == departamento):
                index = [k for k, e in enumerate(self.diputados_VAMOS) if e[0] == departamento]
                for j in range(0, self.departamentos[i][2]):
                    self.diputados.append(self.diputados_VAMOS[index[j]])
            elif(self.departamentos[i][1] == "PDC" and self.departamentos[i][0] == departamento):
                index = [k for k, e in enumerate(self.diputados_PDC) if e[0] == departamento]
                for j in range(0, self.departamentos[i][2]):
                    self.diputados.append(self.diputados_PDC[index[j]])
            elif(self.departamentos[i][1] == "NT" and self.departamentos[i][0] == departamento):
                index = [k for k, e in enumerate(self.diputados_NT) if e[0] == departamento]
                for j in range(0, self.departamentos[i][2]):
                    self.diputados.append(self.diputados_NT[index[j]])
        return self.diputados