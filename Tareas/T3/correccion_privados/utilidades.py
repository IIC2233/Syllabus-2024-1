from collections import namedtuple

# ----------------------------------------------------------------------------
# NO MODIFICAR
# ----------------------------------------------------------------------------

Animales = namedtuple('Animales', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])
Candidatos = namedtuple('Candidatos', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])
Distritos = namedtuple('Distritos', ['id_distrito', 'nombre', 'id_comuna', 'provincia', 'region'])
Locales = namedtuple('Locales', ['id_local', 'nombre_local', 'id_comuna', 'id_votantes'])
Votos = namedtuple('Votos', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])
Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])
