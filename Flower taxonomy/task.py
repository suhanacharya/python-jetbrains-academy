iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    d = {id_n: {'species': species, 'petal_length': petal_length,
                'petal_width': petal_width}}
    for k, v in kwargs.items():
        d[id_n][k] = v
    iris.update(d)
