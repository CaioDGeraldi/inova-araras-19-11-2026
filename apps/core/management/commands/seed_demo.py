from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.campaigns.models import Campaign
from apps.core.models import User
from apps.discovery_routes.models import Route, Stop
from apps.establishments.models import Category, Establishment, Product
from apps.events.models import Event

PASSWORD = "demo12345"
TAG = "[Demonstração]"

STORES = [
    (
        "loja-a",
        "Café do Centro",
        "dono_a",
        "Cafés",
        "19999990001",
        "cafedocentro",
        [("Pão de queijo", "5.50"), ("Café coado", "4.00")],
    ),
    (
        "loja-b",
        "Livraria Esquina",
        "dono_b",
        "Livros",
        "19999990002",
        "",
        [("Romance nacional", "39.90"), ("Caderno artesanal", None)],
    ),
    (
        "loja-c",
        "Brechó da Praça",
        "dono_b",
        "Moda",
        "",
        "brechodapraca",
        [("Jaqueta jeans", "70.00")],
    ),
]


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
        for slug, name, owner, category, whatsapp, instagram, products in STORES:
            store, _ = Establishment.objects.update_or_create(
                slug=slug,
                defaults={
                    "owner": users[owner],
                    "name": f"{name} {TAG}",
                    "description": "Loja fictícia para a demonstração.",
                    "address": "Centro, Araras",
                    "status": Establishment.Status.APPROVED,
                    "whatsapp": whatsapp,
                    "instagram": instagram,
                },
            )
            cat, _ = Category.objects.get_or_create(name=category)
            store.categories.add(cat)
            for product_name, price in products:
                Product.objects.update_or_create(
                    establishment=store,
                    name=f"{product_name} {TAG}",
                    defaults={"price": price, "available": True},
                )
            stores.append(store)

        now = timezone.now()
        for title, days, status in [
            ("Feira de artesanato", 3, Event.Status.PUBLISHED),
            ("Show na praça", 5, Event.Status.CANCELLED),
        ]:
            Event.objects.update_or_create(
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

        route, _ = Route.objects.update_or_create(
            slug="rota-demo",
            defaults={
                "title": f"Rota do Centro {TAG}",
                "description": "Passe pelas paradas obrigatórias para concluir.",
                "published": True,
            },
        )
        for order, (store, required) in enumerate(zip(stores, [True, True, False], strict=True)):
            Stop.objects.update_or_create(
                route=route,
                name=f"Parada {order + 1} {TAG}",
                defaults={"establishment": store, "order": order, "required": required},
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
