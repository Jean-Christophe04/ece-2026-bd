import argparse

from faker import Faker

from .serialize import serialize

fake = Faker()
# Génère le même jeu de données à chaque exécution
Faker.seed(42)


def users_generate(count=50, output=""):
    users = []
    for _ in range(count):
        user = {"uuid": fake.uuid4(), **fake.simple_profile()}
        users.append(user)
    serialize(users, output)
    return users


def main():
    parser = argparse.ArgumentParser(prog="dataset-users", description="Générateur d'utilisateurs")
    parser.add_argument(
        "-c", "--count", help="Nombre d'utilisateurs à générer.", type=int, default=50
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Format de sortie.",
        default="json",
        choices=["csv", "json", "jsonline"],
    )
    args = parser.parse_args()
    users_generate(args.count, args.output)


if __name__ == "__main__":
    main()
