__version__ = "0.0.3"


def Client(token: str):
    import vecdb.api.local

    return vecdb.api.local.Client(token)


def Dataset(token: str, dataset_id: str):
    import vecdb.api.local

    client = vecdb.api.local.Client(token)
    return client.create_dataset(dataset_id)
