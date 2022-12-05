let ornekler = [[20, 5, 15, 35, 10, 50, 80, 40], 
                [100, 50, 200, 400, 20, 60, 10, 90, 300, 200],
                [20, 30, 40, 10, 5, 80, 100, 60],
                [20, 10, 5, 30, 60, 90, 40, 50],
                [20, 20, 20, 5, 5, 3, 10, 15, 15, 15, 30],
                [10],
                [10, 15],
                [10, 5]]


function max_revenue(data){
    /*
    Girilen dizide alım ve satım noktalarını max/min local değerleriyle belirleyerek maksimum kârı döndürür.
    :param data: Maksimum kârı hesaplanacak değer dizisi.
    :return: Maksimum kâr.
    */
    if (data.length < 2) return -1
    
    let asset = null
    let money = 0
    let first_assets_value = 0

    let curr_day = data[0]
    for (let day = 0; day < data.length - 1; day++){
        next_day = data[day + 1]

        if (asset !== null)
        {
            if (asset > 0 && curr_day > next_day)
            {
                money += asset * curr_day
                asset = 0
            }
            else if (asset === 0 && curr_day < next_day)
            {
                asset = Math.floor(money / curr_day)
                money %= curr_day
            }
        }
        else if (curr_day < next_day)
        {
            asset = 1
            first_assets_value = curr_day
        }
        curr_day = next_day
    }
    if (asset) money += asset * curr_day
    
    return (money - first_assets_value)
}
    

for (let i = 0; i < ornekler.length; i++){
    console.log(max_revenue(ornekler[i]))
}
