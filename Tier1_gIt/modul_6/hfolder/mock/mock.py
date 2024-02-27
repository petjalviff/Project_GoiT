from faker import Faker


fake=Faker()


def get_mocked_user():
    return{
        "name":fake.name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
    }


if __name__ == "__main__":
    user=get_mocked_user()
    print(user)