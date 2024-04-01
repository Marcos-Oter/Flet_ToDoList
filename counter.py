import flet as ft
import math as m
from flet import alignment

def main(page: ft.Page):
    page.title = "Mi first Counter TEST"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    #Color de fondo de la APP
    page.bgcolor = ft.colors.BLUE_900

    
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    toChange = str(int(txt_number.value))

    if int(toChange) <= 0:
        txt_number.value == 0

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def reset_click(e):
        txt_number.value = str(int(txt_number.value == 0))
        page.update()
        
    page.add(
        ft.Row(
            [
                ft.Column(
                [
                    ft.Text("Counter",size=25,color=ft.colors.GREEN),
                    ft.Container(width=200,
                                height=50,
                                border_radius=30,
                                border= ft.border.all(1, ft.colors.BLUE),
                                content= ft.FilledButton("Reset"),
                                theme= ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN)),
                                on_click=reset_click),
                ],
                alignment= ft.MainAxisAlignment.CENTER
                ),
            ], alignment= ft.MainAxisAlignment.CENTER
        )

    )

    page.add(
        ft.Row(
        [
            ft.IconButton(ft.icons.REMOVE, on_click= minus_click),
            txt_number,
            ft.IconButton(ft.icons.ADD, on_click= plus_click)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)