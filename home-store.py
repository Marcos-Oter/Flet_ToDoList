import flet as ft
import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors


def main(page: ft.Page):
    page.title = "Explore Test"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.bgcolor = ft.colors.GREEN_200

    #page.add(
     #   ft.Text("Explorer",color=ft.colors.BLACK),
      #  ft.Container(width=100,height=100,bgcolor=ft.colors.PURPLE),
    #)

    def route_change(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(tittle=Text("Flet App"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route =="/store":
            page.view.append(
                View(
                    "/store",
                [
                    AppBar(title=Text("Store"), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton("Go home", on_click=lambda _: page.go("/")),
                ],
            )     
        )
    page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(main)