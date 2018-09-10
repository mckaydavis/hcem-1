# -*- coding: utf-8 -*-
from xl2py_excel_runtime import *
Interactive_List_M3 = Worksheet('Interactive_List_M3', 10, 10)



@register(Interactive_List_M3)
class A2():
    # 'Interactive_List_M3'!A2
    value = 1

@register(Interactive_List_M3)
class B2():
    # 'Interactive_List_M3'!B2
    value = "Commercial"

@register(Interactive_List_M3)
class C2():
    # 'Interactive_List_M3'!C2
    value = "Petroleum"

@register(Interactive_List_M3)
class D2():
    # 'Interactive_List_M3'!D2
    value = 1960

@register(Interactive_List_M3)
class E2():
    # 'Interactive_List_M3'!E2
    value = "GSP (millions)"

@register(Interactive_List_M3)
class F2():
    # 'Interactive_List_M3'!F2
    value = "/GSP"

@register(Interactive_List_M3)
class A3():
    # 'Interactive_List_M3'!A3
    value = 2

@register(Interactive_List_M3)
class B3():
    # 'Interactive_List_M3'!B3
    value = "Industrial"

@register(Interactive_List_M3)
class C3():
    # 'Interactive_List_M3'!C3
    value = "Aviation gasoline"

@register(Interactive_List_M3)
class D3():
    # 'Interactive_List_M3'!D3
    value = 1961

@register(Interactive_List_M3)
class E3():
    # 'Interactive_List_M3'!E3
    value = "Population (per capita)"

@register(Interactive_List_M3)
class F3():
    # 'Interactive_List_M3'!F3
    value = "/Capita"

@register(Interactive_List_M3)
class A4():
    # 'Interactive_List_M3'!A4
    value = 3

@register(Interactive_List_M3)
class B4():
    # 'Interactive_List_M3'!B4
    value = "Power"

@register(Interactive_List_M3)
class C4():
    # 'Interactive_List_M3'!C4
    value = "Asphalt and road oil"

@register(Interactive_List_M3)
class D4():
    # 'Interactive_List_M3'!D4
    value = 1962

@register(Interactive_List_M3)
class E4():
    # 'Interactive_List_M3'!E4
    value = "Total"

@register(Interactive_List_M3)
class F4():
    # 'Interactive_List_M3'!F4
    value = None
    formula = '''=""'''
    @eval_fn
    def F4():
        return ""

@register(Interactive_List_M3)
class A5():
    # 'Interactive_List_M3'!A5
    value = 4

@register(Interactive_List_M3)
class B5():
    # 'Interactive_List_M3'!B5
    value = "Residential"

@register(Interactive_List_M3)
class C5():
    # 'Interactive_List_M3'!C5
    value = "Distillate fuel oil"

@register(Interactive_List_M3)
class D5():
    # 'Interactive_List_M3'!D5
    value = 1963

@register(Interactive_List_M3)
class A6():
    # 'Interactive_List_M3'!A6
    value = 5

@register(Interactive_List_M3)
class B6():
    # 'Interactive_List_M3'!B6
    value = "Ground/Water Transportation"

@register(Interactive_List_M3)
class C6():
    # 'Interactive_List_M3'!C6
    value = "Jet fuel"

@register(Interactive_List_M3)
class D6():
    # 'Interactive_List_M3'!D6
    value = 1964

@register(Interactive_List_M3)
class A7():
    # 'Interactive_List_M3'!A7
    value = 6

@register(Interactive_List_M3)
class B7():
    # 'Interactive_List_M3'!B7
    value = "Air Transportation"

@register(Interactive_List_M3)
class C7():
    # 'Interactive_List_M3'!C7
    value = "Kerosene"

@register(Interactive_List_M3)
class D7():
    # 'Interactive_List_M3'!D7
    value = 1965

@register(Interactive_List_M3)
class A8():
    # 'Interactive_List_M3'!A8
    value = 7

@register(Interactive_List_M3)
class B8():
    # 'Interactive_List_M3'!B8
    value = "All Sectors"

@register(Interactive_List_M3)
class C8():
    # 'Interactive_List_M3'!C8
    value = "LPG"

@register(Interactive_List_M3)
class D8():
    # 'Interactive_List_M3'!D8
    value = 1966

@register(Interactive_List_M3)
class A9():
    # 'Interactive_List_M3'!A9
    value = 8

@register(Interactive_List_M3)
class C9():
    # 'Interactive_List_M3'!C9
    value = "Lubricants"

@register(Interactive_List_M3)
class D9():
    # 'Interactive_List_M3'!D9
    value = 1967

@register(Interactive_List_M3)
class A10():
    # 'Interactive_List_M3'!A10
    value = 9

@register(Interactive_List_M3)
class C10():
    # 'Interactive_List_M3'!C10
    value = "Motor Gasoline"

@register(Interactive_List_M3)
class D10():
    # 'Interactive_List_M3'!D10
    value = 1968

@register(Interactive_List_M3)
class A11():
    # 'Interactive_List_M3'!A11
    value = 10

@register(Interactive_List_M3)
class C11():
    # 'Interactive_List_M3'!C11
    value = "Other petroleum products"

@register(Interactive_List_M3)
class D11():
    # 'Interactive_List_M3'!D11
    value = 1969

@register(Interactive_List_M3)
class A12():
    # 'Interactive_List_M3'!A12
    value = 11

@register(Interactive_List_M3)
class C12():
    # 'Interactive_List_M3'!C12
    value = "Residual fuel oil"

@register(Interactive_List_M3)
class D12():
    # 'Interactive_List_M3'!D12
    value = 1970

@register(Interactive_List_M3)
class A13():
    # 'Interactive_List_M3'!A13
    value = 12

@register(Interactive_List_M3)
class C13():
    # 'Interactive_List_M3'!C13
    value = "Synthetic Natural Gas"

@register(Interactive_List_M3)
class D13():
    # 'Interactive_List_M3'!D13
    value = 1971

@register(Interactive_List_M3)
class A14():
    # 'Interactive_List_M3'!A14
    value = 13

@register(Interactive_List_M3)
class C14():
    # 'Interactive_List_M3'!C14
    value = "Coal"

@register(Interactive_List_M3)
class D14():
    # 'Interactive_List_M3'!D14
    value = 1972

@register(Interactive_List_M3)
class A15():
    # 'Interactive_List_M3'!A15
    value = 14

@register(Interactive_List_M3)
class C15():
    # 'Interactive_List_M3'!C15
    value = "Biofuels"

@register(Interactive_List_M3)
class D15():
    # 'Interactive_List_M3'!D15
    value = 1973

@register(Interactive_List_M3)
class A16():
    # 'Interactive_List_M3'!A16
    value = 15

@register(Interactive_List_M3)
class C16():
    # 'Interactive_List_M3'!C16
    value = "All Fuels"

@register(Interactive_List_M3)
class D16():
    # 'Interactive_List_M3'!D16
    value = 1974

@register(Interactive_List_M3)
class A17():
    # 'Interactive_List_M3'!A17
    value = 16

@register(Interactive_List_M3)
class D17():
    # 'Interactive_List_M3'!D17
    value = 1975

@register(Interactive_List_M3)
class A18():
    # 'Interactive_List_M3'!A18
    value = 17

@register(Interactive_List_M3)
class D18():
    # 'Interactive_List_M3'!D18
    value = 1976

@register(Interactive_List_M3)
class A19():
    # 'Interactive_List_M3'!A19
    value = 18

@register(Interactive_List_M3)
class D19():
    # 'Interactive_List_M3'!D19
    value = 1977

@register(Interactive_List_M3)
class A20():
    # 'Interactive_List_M3'!A20
    value = 19

@register(Interactive_List_M3)
class D20():
    # 'Interactive_List_M3'!D20
    value = 1978

@register(Interactive_List_M3)
class A21():
    # 'Interactive_List_M3'!A21
    value = 20

@register(Interactive_List_M3)
class D21():
    # 'Interactive_List_M3'!D21
    value = 1979

@register(Interactive_List_M3)
class A22():
    # 'Interactive_List_M3'!A22
    value = 21

@register(Interactive_List_M3)
class D22():
    # 'Interactive_List_M3'!D22
    value = 1980

@register(Interactive_List_M3)
class A23():
    # 'Interactive_List_M3'!A23
    value = 22

@register(Interactive_List_M3)
class D23():
    # 'Interactive_List_M3'!D23
    value = 1981

@register(Interactive_List_M3)
class A24():
    # 'Interactive_List_M3'!A24
    value = 23

@register(Interactive_List_M3)
class D24():
    # 'Interactive_List_M3'!D24
    value = 1982

@register(Interactive_List_M3)
class A25():
    # 'Interactive_List_M3'!A25
    value = 24

@register(Interactive_List_M3)
class D25():
    # 'Interactive_List_M3'!D25
    value = 1983

@register(Interactive_List_M3)
class A26():
    # 'Interactive_List_M3'!A26
    value = 25

@register(Interactive_List_M3)
class D26():
    # 'Interactive_List_M3'!D26
    value = 1984

@register(Interactive_List_M3)
class A27():
    # 'Interactive_List_M3'!A27
    value = 26

@register(Interactive_List_M3)
class D27():
    # 'Interactive_List_M3'!D27
    value = 1985

@register(Interactive_List_M3)
class A28():
    # 'Interactive_List_M3'!A28
    value = 27

@register(Interactive_List_M3)
class D28():
    # 'Interactive_List_M3'!D28
    value = 1986

@register(Interactive_List_M3)
class A29():
    # 'Interactive_List_M3'!A29
    value = 28

@register(Interactive_List_M3)
class D29():
    # 'Interactive_List_M3'!D29
    value = 1987

@register(Interactive_List_M3)
class A30():
    # 'Interactive_List_M3'!A30
    value = 29

@register(Interactive_List_M3)
class D30():
    # 'Interactive_List_M3'!D30
    value = 1988

@register(Interactive_List_M3)
class A31():
    # 'Interactive_List_M3'!A31
    value = 30

@register(Interactive_List_M3)
class D31():
    # 'Interactive_List_M3'!D31
    value = 1989

@register(Interactive_List_M3)
class A32():
    # 'Interactive_List_M3'!A32
    value = 31

@register(Interactive_List_M3)
class D32():
    # 'Interactive_List_M3'!D32
    value = 1990

@register(Interactive_List_M3)
class A33():
    # 'Interactive_List_M3'!A33
    value = 32

@register(Interactive_List_M3)
class D33():
    # 'Interactive_List_M3'!D33
    value = 1991

@register(Interactive_List_M3)
class A34():
    # 'Interactive_List_M3'!A34
    value = 33

@register(Interactive_List_M3)
class D34():
    # 'Interactive_List_M3'!D34
    value = 1992

@register(Interactive_List_M3)
class A35():
    # 'Interactive_List_M3'!A35
    value = 34

@register(Interactive_List_M3)
class D35():
    # 'Interactive_List_M3'!D35
    value = 1993

@register(Interactive_List_M3)
class A36():
    # 'Interactive_List_M3'!A36
    value = 35

@register(Interactive_List_M3)
class D36():
    # 'Interactive_List_M3'!D36
    value = 1994

@register(Interactive_List_M3)
class A37():
    # 'Interactive_List_M3'!A37
    value = 36

@register(Interactive_List_M3)
class D37():
    # 'Interactive_List_M3'!D37
    value = 1995

@register(Interactive_List_M3)
class A38():
    # 'Interactive_List_M3'!A38
    value = 37

@register(Interactive_List_M3)
class D38():
    # 'Interactive_List_M3'!D38
    value = 1996

@register(Interactive_List_M3)
class A39():
    # 'Interactive_List_M3'!A39
    value = 38

@register(Interactive_List_M3)
class D39():
    # 'Interactive_List_M3'!D39
    value = 1997

@register(Interactive_List_M3)
class A40():
    # 'Interactive_List_M3'!A40
    value = 39

@register(Interactive_List_M3)
class D40():
    # 'Interactive_List_M3'!D40
    value = 1998

@register(Interactive_List_M3)
class A41():
    # 'Interactive_List_M3'!A41
    value = 40

@register(Interactive_List_M3)
class D41():
    # 'Interactive_List_M3'!D41
    value = 1999

@register(Interactive_List_M3)
class A42():
    # 'Interactive_List_M3'!A42
    value = 41

@register(Interactive_List_M3)
class D42():
    # 'Interactive_List_M3'!D42
    value = 2000

@register(Interactive_List_M3)
class A43():
    # 'Interactive_List_M3'!A43
    value = 42

@register(Interactive_List_M3)
class D43():
    # 'Interactive_List_M3'!D43
    value = 2001

@register(Interactive_List_M3)
class A44():
    # 'Interactive_List_M3'!A44
    value = 43

@register(Interactive_List_M3)
class D44():
    # 'Interactive_List_M3'!D44
    value = 2002

@register(Interactive_List_M3)
class A45():
    # 'Interactive_List_M3'!A45
    value = 44

@register(Interactive_List_M3)
class D45():
    # 'Interactive_List_M3'!D45
    value = 2003

@register(Interactive_List_M3)
class A46():
    # 'Interactive_List_M3'!A46
    value = 45

@register(Interactive_List_M3)
class D46():
    # 'Interactive_List_M3'!D46
    value = 2004

@register(Interactive_List_M3)
class A47():
    # 'Interactive_List_M3'!A47
    value = 46

@register(Interactive_List_M3)
class D47():
    # 'Interactive_List_M3'!D47
    value = 2005

@register(Interactive_List_M3)
class A48():
    # 'Interactive_List_M3'!A48
    value = 47

@register(Interactive_List_M3)
class D48():
    # 'Interactive_List_M3'!D48
    value = 2006

@register(Interactive_List_M3)
class A49():
    # 'Interactive_List_M3'!A49
    value = 48

@register(Interactive_List_M3)
class D49():
    # 'Interactive_List_M3'!D49
    value = 2007

@register(Interactive_List_M3)
class A50():
    # 'Interactive_List_M3'!A50
    value = 49

@register(Interactive_List_M3)
class D50():
    # 'Interactive_List_M3'!D50
    value = 2008

@register(Interactive_List_M3)
class A51():
    # 'Interactive_List_M3'!A51
    value = 50

@register(Interactive_List_M3)
class D51():
    # 'Interactive_List_M3'!D51
    value = 2009

@register(Interactive_List_M3)
class A52():
    # 'Interactive_List_M3'!A52
    value = 51

@register(Interactive_List_M3)
class D52():
    # 'Interactive_List_M3'!D52
    value = 2010

@register(Interactive_List_M3)
class A53():
    # 'Interactive_List_M3'!A53
    value = 52

@register(Interactive_List_M3)
class D53():
    # 'Interactive_List_M3'!D53
    value = 2011

@register(Interactive_List_M3)
class A54():
    # 'Interactive_List_M3'!A54
    value = 53

@register(Interactive_List_M3)
class D54():
    # 'Interactive_List_M3'!D54
    value = 2012

@register(Interactive_List_M3)
class A55():
    # 'Interactive_List_M3'!A55
    value = 54

@register(Interactive_List_M3)
class D55():
    # 'Interactive_List_M3'!D55
    value = 2013

@register(Interactive_List_M3)
class A56():
    # 'Interactive_List_M3'!A56
    value = 55

@register(Interactive_List_M3)
class D56():
    # 'Interactive_List_M3'!D56
    value = 2014

@register(Interactive_List_M3)
class A57():
    # 'Interactive_List_M3'!A57
    value = 56

@register(Interactive_List_M3)
class D57():
    # 'Interactive_List_M3'!D57
    value = 2015

@register(Interactive_List_M3)
class A58():
    # 'Interactive_List_M3'!A58
    value = 57

@register(Interactive_List_M3)
class D58():
    # 'Interactive_List_M3'!D58
    value = 2016

@register(Interactive_List_M3)
class A59():
    # 'Interactive_List_M3'!A59
    value = 58

@register(Interactive_List_M3)
class D59():
    # 'Interactive_List_M3'!D59
    value = 2017

@register(Interactive_List_M3)
class A60():
    # 'Interactive_List_M3'!A60
    value = 59

@register(Interactive_List_M3)
class D60():
    # 'Interactive_List_M3'!D60
    value = 2018

@register(Interactive_List_M3)
class A61():
    # 'Interactive_List_M3'!A61
    value = 60

@register(Interactive_List_M3)
class D61():
    # 'Interactive_List_M3'!D61
    value = 2019

@register(Interactive_List_M3)
class A62():
    # 'Interactive_List_M3'!A62
    value = 61

@register(Interactive_List_M3)
class D62():
    # 'Interactive_List_M3'!D62
    value = 2020

@register(Interactive_List_M3)
class A63():
    # 'Interactive_List_M3'!A63
    value = 62

@register(Interactive_List_M3)
class D63():
    # 'Interactive_List_M3'!D63
    value = 2021

@register(Interactive_List_M3)
class A64():
    # 'Interactive_List_M3'!A64
    value = 63

@register(Interactive_List_M3)
class D64():
    # 'Interactive_List_M3'!D64
    value = 2022

@register(Interactive_List_M3)
class A65():
    # 'Interactive_List_M3'!A65
    value = 64

@register(Interactive_List_M3)
class D65():
    # 'Interactive_List_M3'!D65
    value = 2023

@register(Interactive_List_M3)
class A66():
    # 'Interactive_List_M3'!A66
    value = 65

@register(Interactive_List_M3)
class D66():
    # 'Interactive_List_M3'!D66
    value = 2024

@register(Interactive_List_M3)
class A67():
    # 'Interactive_List_M3'!A67
    value = 66

@register(Interactive_List_M3)
class D67():
    # 'Interactive_List_M3'!D67
    value = 2025

@register(Interactive_List_M3)
class A68():
    # 'Interactive_List_M3'!A68
    value = 67

@register(Interactive_List_M3)
class D68():
    # 'Interactive_List_M3'!D68
    value = 2026

@register(Interactive_List_M3)
class A69():
    # 'Interactive_List_M3'!A69
    value = 68

@register(Interactive_List_M3)
class D69():
    # 'Interactive_List_M3'!D69
    value = 2027

@register(Interactive_List_M3)
class A70():
    # 'Interactive_List_M3'!A70
    value = 69

@register(Interactive_List_M3)
class D70():
    # 'Interactive_List_M3'!D70
    value = 2028

@register(Interactive_List_M3)
class A71():
    # 'Interactive_List_M3'!A71
    value = 70

@register(Interactive_List_M3)
class D71():
    # 'Interactive_List_M3'!D71
    value = 2029

@register(Interactive_List_M3)
class A72():
    # 'Interactive_List_M3'!A72
    value = 71

@register(Interactive_List_M3)
class D72():
    # 'Interactive_List_M3'!D72
    value = 2030