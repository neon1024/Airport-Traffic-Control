from repository.Repo import Repo
from service.Service import Service
from ui.Console import Console


def main():

    repository = Repo()
    service = Service(repository)
    console = Console(service, repository)
    console.run_console()


if __name__ == "__main__":
    main()
