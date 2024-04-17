import math
import flet as ft
from flet import alignment

def main(page: ft.Page):
    page.title = "Optigy"
    page.window_resizable = True
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    #Color de fondo de la APP
    page.bgcolor = ft.colors.GREY_400

    general_weight= 350

    page.add(
        ft.Row(
            [
            ft.Column(
                [
                    ft.Container(
                        width=general_weight,
                        alignment=alignment.center,
                        content=
                        ft.Container(width=90,
                                height=90,
                                gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.Alignment(0.8, 1),
                                        colors=[
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3dc7a5",
                                            "#3dc7a5",
                                            "#3dc7a5",
                                        ],
                                        tile_mode=ft.GradientTileMode.MIRROR,
                                        rotation=math.pi / 3,
                                    ),
                                    shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.BLACK,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                ),
                                #theme= ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN)),
                                border_radius=20,
                                padding=10,
                                #border= ft.border.all(1, ft.colors.BLUE),
                                content=ft.Image(width=35,src="assets/OptigyLogo.png"),
                            ),
                    ),

                    ft.Container(
                        width=general_weight,
                        #height=500,
                        margin=5,
                        alignment=alignment.center,                     
                        content= ft.Stack(
                                        [
                                            ft.Text(text_align= ft.TextAlign.CENTER,
                                                spans=[
                                                    ft.TextSpan("OPTIGY", 
                                                        ft.TextStyle(font_family="serif", letter_spacing= 10, size=25, weight=ft.FontWeight.W_600,
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
                                        ]
                                        ),
                        ),
                    ft.Container(
                        width=general_weight,
                        alignment=alignment.center,
                        content=ft.Text(text_align= ft.TextAlign.CENTER,
                            spans=[
                                ft.TextSpan("Cuida y optimiza tu enegía!",
                                    ft.TextStyle(font_family="serif",size=20, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900,),
                                ),
                            ],
                        ),
                    ),

                    ft.Container(
                        width=general_weight,
                        height=300,
                        alignment=alignment.center,
                        bgcolor=ft.colors.GREY_700,
                        content= ft.Column([
                            ft.Container(
                                    width=general_weight,
                                    height=100,
                                    alignment=alignment.center,
                                    bgcolor=ft.colors.BLUE_400,
                                    margin=5,
                                    content=ft.Text("Casa 0",text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                    width=general_weight,
                                    height=100,
                                    alignment=alignment.center,
                                    bgcolor=ft.colors.BLUE_400,
                                    margin=5,
                                    content=ft.Text("Casa 1",text_align=ft.TextAlign.CENTER)
                            ),

                                    ft.Container(
                                    width=general_weight,
                                    height=100,
                                    alignment=alignment.center,
                                    bgcolor=ft.colors.BLUE_400,
                                    margin=5,
                                    content=ft.Text("Casa 2",text_align=ft.TextAlign.CENTER)
                            ),

                                    ft.Container(
                                    width=general_weight,
                                    height=100,
                                    alignment=alignment.center,
                                    bgcolor=ft.colors.BLUE_400,
                                    margin=5,
                                    content=ft.Text("Casa 3",text_align=ft.TextAlign.CENTER)
                            ),
                        ],
                            spacing=10,
                            height=200,
                            width=float("inf"),
                            scroll=ft.ScrollMode.ALWAYS,
                        ),
                    ),
               
                    ft.Container(
                        width=general_weight,
                        alignment=alignment.center,
                        content=
                        ft.Container(width=90,
                                height=90,
                                gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.Alignment(0.8, 1),
                                        colors=[
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3dc7a5",
                                            "#3dc7a5",
                                            "#3dc7a5",
                                        ],
                                        tile_mode=ft.GradientTileMode.MIRROR,
                                        rotation=math.pi / 3,
                                    ),
                                    shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.BLACK,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                ),
                                #theme= ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN)),
                                border_radius=20,
                                #border= ft.border.all(1, ft.colors.BLUE),
                                content= ft.FloatingActionButton(icon=ft.icons.ADD, bgcolor=ft.colors.TRANSPARENT, autofocus=True),
                            ),
                    ),


                ],
                alignment= ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.MainAxisAlignment.CENTER),
                
            ], alignment= ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.CENTER,
            
        ),
                                ft.Container(
                        width=general_weight,
                        alignment=alignment.bottom_center,
                        content=ft.Text(text_align= ft.TextAlign.CENTER,
                            spans=[
                                ft.TextSpan("Optigyº Todos derechos reservados 2024.",
                                    ft.TextStyle(font_family="serif",size=15, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900,),
                                ),
                            ],
                        ),
                    ),
    )

ft.app(main)