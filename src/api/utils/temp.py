from dependency_injector.wiring import Provide, inject


class Deps:
    def __init__(self, container):
        self.container = container

    def fetch_user(self, user_id: str, ):
        container = self.container
        @inject
        def wrapper(user_service = Provide[container.user_service]):
            return user_service.get_user_by_id(user_id)

        return wrapper()
