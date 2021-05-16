from fastapi import Request


def set_ip_address(request: Request):
    client_host = request.client.host
    return client_host
