from django.conf import settings
settings.configure()

from models import Country


def main():
    county = Country('Moscow')
    county.save()


if __name__ == '__main__':
    main()
