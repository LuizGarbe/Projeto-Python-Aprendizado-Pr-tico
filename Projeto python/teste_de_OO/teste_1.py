class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    @property
    def likes (self):
        return self._likes

    def da_likes (self):
        self._likes += 1

    @property
    def nome (self):
        return self._nome
    
    @nome.setter
    def nome (self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self.nome} - Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} {self.duracao} Minutos - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Nome: {self.nome} {self.temporada} Temporadas - Likes: {self.likes}'
    
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
    
granturismo = Filme("Granturismo", 2023, 210)
balls = Serie ("Balls", 2020, 8)

granturismo.da_likes
balls.da_likes
balls.da_likes

filmes_serie_lissta = [granturismo, balls]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_serie_lissta)

print('Tamanho da playlist: {len(playlist_fim_de_semana})')
for Programa in playlist_fim_de_semana:
    print(Programa)