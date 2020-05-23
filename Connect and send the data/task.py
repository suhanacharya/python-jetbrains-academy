def submit_data(data, client, address):

    data = data.encode()
    client.connect(address)
    client.send(data)
