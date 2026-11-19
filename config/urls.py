from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from apps.campaigns import views as campaigns
from apps.core import views as core
from apps.discovery_routes import views as routes
from apps.establishments import views as establishments
from apps.events import views as events

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.core.urls")),
    path("", establishments.home, name="home"),
    path("entrar/", auth_views.LoginView.as_view(), name="login"),
    path("sair/", auth_views.LogoutView.as_view(), name="logout"),
    path("cadastro/", core.signup, name="signup"),
    path("perfil/", core.profile, name="profile"),
    path("lojas/<slug:slug>/", establishments.establishment_detail, name="establishment_detail"),
    path("rotas/", routes.route_list, name="route_list"),
    path("rotas/<slug:slug>/", routes.route_detail, name="route_detail"),
    path("rotas/<slug:slug>/qr/", routes.route_qr, name="route_qr"),
    path("checkin/<str:token>/", routes.checkin, name="checkin"),
    path("agenda/", events.event_list, name="event_list"),
    path("agenda/<int:pk>/", events.event_detail, name="event_detail"),
    path("painel/", establishments.panel, name="panel"),
    path(
        "painel/<slug:slug>/editar/", establishments.establishment_edit, name="establishment_edit"
    ),
    path("painel/<slug:slug>/produtos/novo/", establishments.product_edit, name="product_create"),
    path("painel/<slug:slug>/produtos/<int:pk>/", establishments.product_edit, name="product_edit"),
    path(
        "painel/<slug:slug>/produtos/<int:pk>/excluir/",
        establishments.product_delete,
        name="product_delete",
    ),
    path("painel/compra/<str:code>/", campaigns.purchase_confirm, name="purchase_confirm"),
    path("painel/cupom/<str:code>/", campaigns.coupon_redeem, name="coupon_redeem"),
]
