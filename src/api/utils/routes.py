from glob import glob
from src.config import settings

def allowed_files(files: list = settings.allowed_static_files) -> list:
    _allowed_file = []

    for directory in files:
        files = glob(directory, root_dir="src/")
        _allowed_file.extend(files)
    return _allowed_file


def by_pass_route(path) -> bool:
    if path == "/":  # skip the home path
        return True
    if path[1:] in allowed_files():  # skip the static files
        print(f"[INFO] -> Skipping route to the file access - {path}")
        return True

    if path in settings.skip_routes_for_jwt_auth:  # unauthenticated routes
        print(f"[Warning] -> Skipping the route {path} for JWT authentication")
        return True

    return False
