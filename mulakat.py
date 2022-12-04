ornekler = [[20, 5, 15, 35, 10, 50, 80, 40],
            [100, 50, 200, 400, 20, 60, 10, 90, 300, 200],
            [20, 30, 40, 10, 5, 80, 100, 60],
            [20, 10, 5, 30, 60, 90, 40, 50],
            [20, 20, 20, 5, 5, 3, 10, 15, 15, 15, 30],
            [10],
            [10, 15],
            [10, 5]]


def max_revenue(data):
    """
    Girilen dizide alım ve satım noktalarını max/min local değerleriyle belirleyerek maksimum kârı döndürür.
    :param data: Maksimum kârı hesaplanacak değer dizisi.
    :return: Maksimum kâr.
    """
    if len(data) < 2:  # En az birer tane alım ve satım yapabileceği gün olmalı.
        return -1

    # Sırasıyla varlık, varlık satışından elde edilen para ve kârı hesaplarken gereken ilk aldığımız varlığın değeri.
    asset, money, first_assets_value = None, 0, 0

    curr_day = data[0]
    for day in range(len(data) - 1):
        next_day = data[day + 1]

        if asset is not None:
            # SATIM
            if asset > 0 and curr_day > next_day:       # Eğer sonraki günün değeri bugünden KÜÇÜKSE satış yap.
                money += asset * curr_day
                asset = 0
            # ALIM
            elif asset == 0 and curr_day < next_day:    # Eğer sonraki günün değeri bugünden BÜYÜKSE alım yap.
                asset = money // curr_day
                money %= curr_day
        elif curr_day < next_day:                       # İlk defa varlık alım durumu
            asset = 1
            first_assets_value = curr_day
        curr_day = next_day

    # Eğer son günde elimizde hala varlık var ise satışını yapıyoruz
    if asset:
        money += asset * curr_day

    # İlk alım yaptığımız varlığın değerini kazancımızdan çıkarıp kârımızı buluyoruz.
    return money - first_assets_value


for ornek in ornekler:
    print(max_revenue(ornek))
