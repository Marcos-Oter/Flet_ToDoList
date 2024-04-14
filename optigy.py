import flet as ft
import math as m
from flet import alignment

def main(page: ft.Page):
    page.title = "Optigy"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    #Color de fondo de la APP
    page.bgcolor = ft.colors.GREY_400

    
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
                    ft.Stack(
                        [     
                        ft.Text(text_align= ft.TextAlign.CENTER,
                            spans=[
                                ft.TextSpan("OPTIGY", 
                                    ft.TextStyle(font_family="serif",letter_spacing= 10, size=25, weight=ft.FontWeight.W_600,
                                        foreground=ft.Paint(
                                            color=ft.colors.BLACK,
                                            stroke_width=4,
                                            stroke_join=ft.StrokeJoin.ROUND,
                                            style=ft.PaintingStyle.STROKE,
                                        ),
                                    ),
                                ),
                            ],
                        ),
                        ft.Text(text_align= ft.TextAlign.CENTER,
                            spans=[
                                ft.TextSpan("OPTIGY",
                                    ft.TextStyle(font_family="serif",letter_spacing= 10,size=25, weight=ft.FontWeight.W_600,color=ft.colors.WHITE,),
                                ),
                            ],
                        ),      
                ],),

                        ft.Text(text_align= ft.TextAlign.CENTER,
                            spans=[
                                ft.TextSpan("Cuida y optimiza tu enegía!",
                                    ft.TextStyle(font_family="serif",size=20, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900,),
                                ),
                            ],
                        ),
                    ft.Container(width=100,
                                height=100,
                                shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.BLACK,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                ),
                                theme= ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN)),
                                border_radius=20,
                                #border= ft.border.all(1, ft.colors.BLUE),
                                content= ft.FloatingActionButton(icon=ft.icons.ADD, on_click=reset_click, bgcolor=ft.colors.GREEN),
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
            ft.Container(
                width=200,
                height=200,
                content=ft.Text("xd"),
                theme= ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN)),
            ),
            #ft.IconButton(ft.icons.REMOVE, on_click= minus_click),
            #txt_number,
            #ft.IconButton(ft.icons.ADD, on_click= plus_click)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)