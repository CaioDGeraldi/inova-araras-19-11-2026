from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.campaigns.models import Coupon
from apps.core.forms import SignupForm
from apps.discovery_routes.models import Participation


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect("home")
    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile(request):
    return render(
        request,
        "core/profile.html",
        {
            "coupons": Coupon.objects.filter(consumer=request.user).select_related(
                "campaign__origin", "campaign__destination"
            ),
            "participations": Participation.objects.filter(user=request.user).select_related(
                "route"
            ),
        },
    )


COMMONS = "https://commons.wikimedia.org/wiki/File:"

PHOTO_CREDITS = [
    {
        "image": "cafe-do-centro.jpg",
        "used_for": "Café do Centro",
        "author": "Downtowngal",
        "license": "CC BY-SA 4.0",
        "url": f"{COMMONS}Interior_Johnie%27s_Coffee_Shop_2021.jpg",
    },
    {
        "image": "pao-de-queijo.jpg",
        "used_for": "Pão de queijo",
        "author": "Acfariac",
        "license": "CC BY-SA 4.0",
        "url": f"{COMMONS}Pao_de_queijo_brasil.jpg",
    },
    {
        "image": "cafe-coado.jpg",
        "used_for": "Café coado",
        "author": "Melsj",
        "license": "CC BY-SA 4.0",
        "url": f"{COMMONS}Caf%C3%A9_coado.jpg",
    },
    {
        "image": "livraria-esquina.jpg",
        "used_for": "Livraria Esquina",
        "author": "Sashimi-b",
        "license": "CC BY 4.0",
        "url": f"{COMMONS}Greenlight_Bookstore_interior_2026.jpg",
    },
    {
        "image": "romance-nacional.jpg",
        "used_for": "Romance nacional",
        "author": "Alexander Grey",
        "license": "CC0",
        "url": f"{COMMONS}Stack_of_multicolored_books_on_a_table.jpg",
    },
    {
        "image": "caderno-artesanal.jpg",
        "used_for": "Caderno artesanal",
        "author": "Panpanchik",
        "license": "CC BY-SA 4.0",
        "url": f"{COMMONS}Handmade_notebook_and_wooden_pencil.jpg",
    },
    {
        "image": "brecho-da-praca.jpg",
        "used_for": "Brechó da Praça",
        "author": "MAKY.OREL",
        "license": "CC BY-SA 4.0",
        "url": f"{COMMONS}Clothing_racks_in_second_hand_shop,_Prague.jpg",
    },
    {
        "image": "jaqueta-jeans.jpg",
        "used_for": "Jaqueta jeans",
        "author": "NikosLikomitros",
        "license": "CC0",
        "url": f"{COMMONS}Jean_jacket.jpg",
    },
    {
        "image": "feira-de-artesanato.jpg",
        "used_for": "Feira de artesanato",
        "author": "Andre Carrotflower",
        "license": "CC BY-SA 4.0",
        "url": f"{COMMONS}20220507_-_19_-_Albany,_New_York_-_"
        "Craft_stands_at_the_Albany_Tulip_Festival.jpg",
    },
    {
        "image": "show-na-praca.jpg",
        "used_for": "Show na praça",
        "author": "Shixart1985",
        "license": "CC BY 2.0",
        "url": f"{COMMONS}Live_band_performs_energetic_music_on_stage_during_"
        "evening_concert_in_lively_outdoor_setting.jpg",
    },
    {
        "image": "rota-do-centro.jpg",
        "used_for": "Rota do Centro",
        "author": "Marcelo Luiz Lombi",
        "license": "CC BY-SA 3.0",
        "url": f"{COMMONS}Centro,_Araras_-_SP,_Brazil_-_panoramio_(13).jpg",
    },
]


def credits(request):
    return render(request, "core/credits.html", {"credits": PHOTO_CREDITS})
