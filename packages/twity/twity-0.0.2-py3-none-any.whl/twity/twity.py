import fire
from auth import auth
from create import create
from delete import delete

if __name__ == "__main__":
    fire.Fire({
        'auth': auth,
        'create': create,
        'delete': delete,
    })