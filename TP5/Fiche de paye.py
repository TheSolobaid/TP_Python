while True:
    salnorm=0
    sal25=0
    sal50=0
    tt=int(input("temps travaillé: "))
    th=float(input("salaire horaire (en €): "))
    if tt <= 160:
        tp=tt*th
        salnorm = tt
    elif tt > 160 and tt <= 200:
        tp = 160*th + ((tt-160) * th*1.25)
        salnorm=160
        sal25 = tt - 160
    else:
        tp = 160*th + 40*th*1.25 + ((tt-200)*th*1.50)
        salnorm=160
        sal25=40
        sal50=tt-sal25-salnorm
    print(f"vous etes payer {tp}€")
    print(f"vous avez travailler {tt}h, dont {salnorm}h à {th}€/h, {sal25}h primées +25% et {sal50}h primées +50%")