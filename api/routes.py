from api.resources import Index


def initialize_routes(api):
    api.add_resource(Index, '/')
