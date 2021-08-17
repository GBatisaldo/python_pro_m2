class Fibo:
    def __init__(self, maximo =10000):
        self.elemento_atual, self.proximo_elemento = 0, 1
        self.maximo = maximo

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.elemento_atual > self.maximo:
            raise StopIteration

        valor_de_retorno = self.elemento_atual

        self.elemento_atual, self.proximo_elemento = self.proximo_elemento, self.elemento_atual + self.proximo_elemento

        return valor_de_retorno

if __name__ == '__main__':
    objeto_fibo = Fibo(maximo=10000)

    for fibon in objeto_fibo:
        print("Sequencia: {}".format(fibon))