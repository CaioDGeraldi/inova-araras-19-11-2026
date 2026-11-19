from datetime import timedelta

from django.conf import settings
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.campaigns.models import Campaign
from apps.core.models import User
from apps.discovery_routes.models import Route, Stop
from apps.establishments.models import Category, Establishment, Product
from apps.events.models import Event

PASSWORD = "demo12345"
TAG = "[Demonstração]"
DEMO_IMAGES = settings.BASE_DIR / "static" / "img" / "demo"

STORES = [
    (
        "loja-a",
        "Café do Centro",
        "dono_a",
        "Cafés",
        "19999990001",
        "cafedocentro",
        "cafe-do-centro",
        [("Pão de queijo", "5.50", "pao-de-queijo"), ("Café coado", "4.00", "cafe-coado")],
    ),
    (
        "loja-b",
        "Livraria Esquina",
        "dono_b",
        "Livros",
        "19999990002",
        "",
        "livraria-esquina",
        [
            ("Romance nacional", "39.90", "romance-nacional"),
            ("Caderno artesanal", None, "caderno-artesanal"),
        ],
    ),
    (
        "loja-c",
        "Brechó da Praça",
        "dono_b",
        "Moda",
        "",
        "brechodapraca",
        "brecho-da-praca",
        [("Jaqueta jeans", "70.00", "jaqueta-jeans")],
    ),
]


def attach_demo_image(instance, folder, name):
    path = f"{folder}/demo-{name}.jpg"
    if not default_storage.exists(path):
        with (DEMO_IMAGES / f"{name}.jpg").open("rb") as source:
            default_storage.save(path, File(source))
    instance.image.name = path
    instance.save(update_fields=["image"])


class Command(BaseCommand):
    help = "Cria dados fictícios de demonstração, sem duplicar ao repetir."

    def handle(self, *args, **options):
        users = {}
        for username in ["admin", "consumidor", "dono_a", "dono_b"]:
            user, _ = User.objects.update_or_create(
                username=username,
                defaults={
                    "first_name": f"{username} {TAG}",
                    "is_staff": username == "admin",
                    "is_superuser": username == "admin",
                },
            )
            user.set_password(PASSWORD)
            user.save()
            users[username] = user

        stores = []
        for slug, name, owner, category, whatsapp, instagram, image, products in STORES:
            store, _ = Establishment.objects.update_or_create(
                slug=slug,
                defaults={
                    "owner": users[owner],
                    "name": f"{name} {TAG}",
                    "description": "Loja fictícia para a demonstração.",
                    "postal_code": "13600-000",
                    "street": "Rua Voluntários da Pátria",
                    "number": str(100 + len(stores) * 50),
                    "district": "Centro",
                    "city": "Araras",
                    "state": "SP",
                    "status": Establishment.Status.APPROVED,
                    "whatsapp": whatsapp,
                    "instagram": instagram,
                },
            )
            attach_demo_image(store, "lojas", image)
            cat, _ = Category.objects.get_or_create(name=category)
            store.categories.add(cat)
            for product_name, price, product_image in products:
                product, _ = Product.objects.update_or_create(
                    establishment=store,
                    name=f"{product_name} {TAG}",
                    defaults={"price": price, "available": True},
                )
                attach_demo_image(product, "produtos", product_image)
            stores.append(store)

        now = timezone.now()
        events = []
        for title, days, status, image in [
            ("Feira de artesanato", 3, Event.Status.PUBLISHED, "feira-de-artesanato"),
            ("Show na praça", 5, Event.Status.CANCELLED, "show-na-praca"),
        ]:
            event, _ = Event.objects.update_or_create(
                title=f"{title} {TAG}",
                defaults={
                    "description": "Evento fictício para a demonstração.",
                    "starts_at": now + timedelta(days=days),
                    "ends_at": now + timedelta(days=days, hours=3),
                    "location": "Praça central",
                    "category": "Cultura",
                    "organizer": "Prefeitura (fictício)",
                    "status": status,
                },
            )
            attach_demo_image(event, "eventos", image)
            events.append(event)

        route, _ = Route.objects.update_or_create(
            slug="rota-demo",
            defaults={
                "title": f"Rota do Centro {TAG}",
                "description": "Passe pelas paradas obrigatórias para concluir.",
                "published": True,
                "starts_on": timezone.localdate() - timedelta(days=1),
                "ends_on": timezone.localdate() + timedelta(days=30),
            },
        )
        attach_demo_image(route, "rotas", "rota-do-centro")
        for order, (store, required) in enumerate(zip(stores, [True, True, False], strict=True)):
            Stop.objects.update_or_create(
                route=route,
                name=f"Parada {order + 1} {TAG}",
                defaults={
                    "establishment": store,
                    "order": order,
                    "required": required,
                    "event": events[0] if order == 2 else None,
                },
            )

        Campaign.objects.update_or_create(
            title=f"Compre em A, ganhe em B {TAG}",
            defaults={
                "benefit": "10% de desconto na Livraria Esquina",
                "origin": stores[0],
                "destination": stores[1],
                "active": True,
            },
        )

        self.stdout.write(f"Usuários admin, consumidor, dono_a e dono_b criados. Senha: {PASSWORD}")
