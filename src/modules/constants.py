# Курсы валют (фиксированные значения)
DEFAULT_RATES = {
    "USD": 78.50,
    "EUR": 89.31,
    "CNY": 10.86,
    "GBP": 106.20,
    "JPY": 0.54,
    "CHF": 95.49,
    "HKD": 10.02,
    "AED": 21.37,
    "KZT": 0.15,
    "TRY": 2.00,
    "BYN": 26.27
}

# Средняя цена корма Monge (10 кг)
MONGE_PRICE = 9000

# Добавляем список ID стикеров из стикерпака Murmontik
MURMONTIK_STICKERS = [
    "CAACAgIAAxkBAAEPos5oQWqldHypt5ubwuy4TEGHw5aDSQACkhYAAuKRWUrY7HDIc6sjjzYE",
    "CAACAgIAAxkBAAEPotBoQWqo6XK56SlO99fo1X13-p4WYwACRxcAAssRWUpj7REXiwJUuTYE",
    "CAACAgIAAxkBAAEPotJoQWqq2p4kdp8Uu3xML69K0vSHLgAChhYAAjqvYUoD50KXTg5pczYE",
    "CAACAgIAAxkBAAEPotRoQWqsAAEqO91ai_bJtadlr99URYoAAsMWAAIMbGFKagAB9bnxRCAvNgQ",
    "CAACAgIAAxkBAAEPotZoQWquZZow6AOYz9HqG1xj3oUZ6gACJhgAAue8WUpfjumA-c6zmzYE",
    "CAACAgIAAxkBAAEPothoQWqvuZCkHjNLXnL-auqENNgPawAC4hsAArU0WUoQS-e1Z0DE_TYE",
    "CAACAgIAAxkBAAEPotpoQWqwoWk_gidGkrG0UbC1v-S2dwACrhgAAk1yYEq36zvxnDfX0zYE",
    "CAACAgIAAxkBAAEPotxoQWqyT_uX2NonqRzoYZLhdl2efAAC2RkAAu33WErfcBwdAp0yGjYE",
    "CAACAgIAAxkBAAEPot5oQWqzWR4_8quPX1iJ2s94wgehaQACrxQAAohfYEp8LrVWAAFrYSE2BA",
    "CAACAgIAAxkBAAEPouBoQWq0LWKS3hhT2ZN1fuLZVRDUsgACuBgAAnSeWUq2UHAEZ-tDFzYE",
    "CAACAgIAAxkBAAEPouJoQWq1uCnYSK6gUQSNN3hrFyYc8wACuhYAAn82WUr8598MLctJbjYE",
    "CAACAgIAAxkBAAEPouRoQWq2s0pQcouq9m5A0v2f7vzmywACRxsAAq00YEplsKFaSB-VvzYE",
    "CAACAgIAAxkBAAEPouZoQWq4QX4LNeGKQjMIdUt6R9YqrAACkx0AArc2aErPZs65CmDu9TYE",
    "CAACAgIAAxkBAAEPouhoQWq51o4EusO6wjUk-E14JPtbywACeRcAAkyCYEoQFdFn4-tcvTYE",
    "CAACAgIAAxkBAAEPoupoQWq6QYC7wrNaXDXdQXocsE4RiAACax4AArj7YUrvR9r8_O5AszYE",
    "CAACAgIAAxkBAAEPouxoQWq9nuQCdhrkm4_0jiHRSrZLrAACshUAAjHNaEp6nfMxcgv9tTYE",
    "CAACAgIAAxkBAAEPou5oQWq-d4O6zmldCygv4-8gk3ILmAACZhsAAmFjYUohN22YYE3oDzYE",
    "CAACAgIAAxkBAAEPovBoQWq_KNFVfqKPVQABq3iAv8ubCvsAAlgZAAITrWhKtUonzXFceCQ2BA",
    "CAACAgIAAxkBAAEPovJoQWrAlcRD0nZnGU9gT7andJWQBwACBBgAAq57aEpFSB_PAzpkiDYE",
    "CAACAgIAAxkBAAEPovRoQWrCbBtxXfJRK8cJMcLvYj82BwACERgAAsS6aUrsZnQPCLHo0zYE",
    "CAACAgIAAxkBAAEPovZoQWrDagtwHms7f1iRhi7KFU0JegAC0hkAAxZoSh1PrlDbdo7lNgQ",
    "CAACAgIAAxkBAAEPovhoQWrEL_K3OnoRwzMRGw6h4qFJfAACdRkAAvWyaEo3rK_BH0ZejTYE",
    "CAACAgIAAxkBAAEPovpoQWrF6FTa8aV_CX4d_RwHoNyB9AACbBMAAiKocEq36wV0y8tTbjYE",
    "CAACAgIAAxkBAAEPovxoQWrGWd-Nitz_I5fljRmV8Kf-rQAC0BkAAlnHeEpa8z7-N9h16DYE",
    "CAACAgIAAxkBAAEPov5oQWrHgKWkoRVQxA18ErU2fcX1egAC7RkAAiDgeEoGXxCkuX8oCzYE",
    "CAACAgIAAxkBAAEPowABaEFqyDi8Qy-XY818NOQCsI_OB5sAAqEWAAKU0XhKe3OTRfwCxn82BA",
    "CAACAgIAAxkBAAEPowJoQWrJxjuo-IzSjchFVSovzozZFAAC1hgAAjkTgUr1dM223JaPPTYE",
    "CAACAgIAAxkBAAEPowRoQWrKCeaPSgmcIpHt7bGV6Kzr9QAChBoAAvNfeUpJJSAAAb-CM8Q2BA",
    "CAACAgIAAxkBAAEPowZoQWrLEWlHYGdIWYPOfk-PIJGT8QACPBoAAix_eEoqiSB28B9YbDYE",
    "CAACAgIAAxkBAAEPowhoQWrM0BEdjUlOnbAJH38bLL0OEgACHy0AAjOtmEhB4PUaiToy_jYE",
    "CAACAgIAAxkBAAEPowpoQWrNjRNlsxCw-kKFNLS5SnsUlwACH2YAAlEGwEmNJQrvoWbaBjYE",
    "CAACAgIAAxkBAAEPowxoQWrO4XsSul5W73-I7nMdaq3s-AACGXgAAtJnwEnzbOYZH7zirDYE",
    "CAACAgIAAxkBAAEPow5oQWrP-xvLNhewoQLYDZSVEXP9VQAC6G0AAoShuUkmWyhEXjH8jzYE",
    "CAACAgIAAxkBAAEPoxBoQWrQLR2v4AHgjfphFWoiEFKB0wAC3HAAAmCQuEkZrk-6T-ubAzYE",
    "CAACAgIAAxkBAAEPoxJoQWrSGzka57luN2OnuBuMHbHCwwAC72wAApKNuEk3niSU4zP2rjYE",
    "CAACAgIAAxkBAAEPoxRoQWra1T82fTHWBxmUPb0GjUln_AACcXEAAr2juElO_12zRzP-CDYE",
    "CAACAgIAAxkBAAEPoxZoQWrbQFkGJs-tuRFLR86ZvyBwQAACy2EAAkA0wUn_8l1gsqnDFDYE",
    "CAACAgIAAxkBAAEPoxhoQWrdFdG0-YGfvmM9u10YPdwtmAAC5W0AArRpuUlXDYcl_gPT8TYE",
    "CAACAgIAAxkBAAEPoxxoQWreKcr51d4IPJFjtyn7SC6KGAAC32oAAmGHwEkqRAE9-cEzNDYE",
    "CAACAgIAAxkBAAEPox5oQWrgKfUTIkSHdnJOtVLFie4UcQACa3EAAj4muEljafRCPuJNrjYE",
    "CAACAgIAAxkBAAEPoyBoQWrhSIu01bs34lFGII1vKMiIGAACw2gAAivawUmky1iOne3iTjYE",
    "CAACAgIAAxkBAAEPoyNoQWriWmLcodqsy0H1YS6yZN8MRwACu3QAAnDNuUlbXYQSAAELzVQ2BA",
    "CAACAgIAAxkBAAEPoyVoQWrkLd_NPr03kfKhLxD8t-zXtAACKG4AAg1HuEm0vJ8WrCKL8jYE",
    "CAACAgIAAxkBAAEPoydoQWrnph8XMPyKRx0vj65lJRCrdAACOHwAAsPdwElnA-IbOkR5SzYE",
    "CAACAgIAAxkBAAEPoyloQWroiCZz5XbVtxPFXVbMoDnhvAAC0WEAAqtQwEkNa_d_YiOBPzYE",
    "CAACAgIAAxkBAAEPoytoQWrqJLl8ClwtZQktl7Wf_tHyRgACsGAAAk4xwElNiItlm1ZuJTYE",
    "CAACAgIAAxkBAAEPoy1oQWrrdcuess9yZQvwpZ7f21KNZgACd2wAAkchuUl5OAABgBMAAaSLNgQ",
    "CAACAgIAAxkBAAEPoy9oQWrsRoqmfI1f17VmVXpmRqpZeAACRWwAAjIOuEkucUhl3sGgXzYE",
    "CAACAgIAAxkBAAEPozFoQWrtbodCnjU6Sha9jdfUaZF-gQACAnMAAnSZwUkm8Y6gl_4EKjYE",
    "CAACAgIAAxkBAAEPozNoQWrvHhIcdPJ4xV3stylIjjElEwACLXQAAi1mwElXqz7d70OzZzYE",
    "CAACAgIAAxkBAAEPozVoQWrw0EcwwbnJp8d5oKcsCfS1fQACXWwAAv5GwUneQG1UVZcb6zYE",
    "CAACAgIAAxkBAAEPozdoQWrxe6QBw9CODlptZkjBIdGzcwACYHQAAtPmuEnAQYL9nFXkVzYE",
    "CAACAgIAAxkBAAEPozloQWrxqb9WPcImDOEr7d33ym2VpwAC0GcAAjC7uUlaThneaTNRzzYE",
    "CAACAgIAAxkBAAEPoztoQWryq94d8StxdVW4wq_gJeXZHQACZmcAArajwUljdPURPMLzUjYE",
    "CAACAgIAAxkBAAEPoz1oQWrzeNJCIjsLbwJiAXzBYfEvZQACh20AApYAAblJyQABsvlpoKK2NgQ",
    "CAACAgIAAxkBAAEPoz9oQWr2GbP1Ir3sUGbFcuANAybm5AAC82EAAkaiwUmijDOGtja6DDYE",
    "CAACAgIAAxkBAAEPo0FoQWr3AgOmLxwmQgemPnMmSP-giQACC2IAAtEOwEks32Gw3Ppf0zYE",
    "CAACAgIAAxkBAAEPo0NoQWr4uKOazXzSR4uUY_Y5Q_RPPAACIm4AAg4VwEl-GVBBAXRyeDYE",
    "CAACAgIAAxkBAAEPo0VoQWr6JmXsGNHk-JU2GYIiNOdIugACT2IAApqVwEn3jRpe4LrllDYE",
    "CAACAgIAAxkBAAEPo0doQWr7x-7hSEnd_Iwh2qwBsC8UVQACinAAAp3LuElIC4den4ERqzYE",
    "CAACAgIAAxkBAAEPo0loQWr8LOQk5J0Zt403ZxFDASCkjgACGWwAAqEkwEllnAR1GcDlwzYE",
    "CAACAgIAAxkBAAEPo0toQWr9sIx4ASWerxDYazsnoCPNvAACjWsAAk3dwElpvy0kvQABS_g2BA",
    "CAACAgIAAxkBAAEPo01oQWr-YfXV1UwqCt1SeblOMFcEpwACRGoAAtXJuEl8HSbvNIJFMzYE",
    "CAACAgIAAxkBAAEPo09oQWr_kUcWui1hAfFzKNpLx7n8DwACFXUAAtQvwUlbHyTCjanj2jYE",
    "CAACAgIAAxkBAAEPo1FoQWsAATk1x3WcrxT2HsYUNrCM_fwAAhRuAALgirlJ5irhCt9sIgs2BA",
    "CAACAgIAAxkBAAEPo1NoQWsBbTA9Hskxdx486ZgJyhuziQACym8AAprquEmHGsBuQcEc7DYE",
    "CAACAgIAAxkBAAEPo1VoQWsChV53nY_xCLRPz1KsnUVy3AACnW8AAk1wuEmfxoUn7fHUWTYE",
    "CAACAgIAAxkBAAEPo1doQWsD_HgNaaU4q1VoO78J2XBTUgACIXMAAmBJwUmkjK3UlXQikDYE",
    "CAACAgIAAxkBAAEPo1loQWsEppukmy68IhPb9pfA7hLjXgACWm4AAgVIwUlGFJDZlMEGrDYE",
    "CAACAgIAAxkBAAEPo1toQWsFkdTK8RB6tguf43UQ31JSkQACQW8AAuhzuUmCwnk3QgQztjYE",
    "CAACAgIAAxkBAAEPo11oQWsHblsp0ymcRuuuFJttk2XkPgACqmoAAptkwUn0hSkswoZQzTYE",
    "CAACAgIAAxkBAAEPo19oQWsIrYzBRU272vs0aMcm5Lp4_wACS1cAAgZAwUnFd4cvtTEmDDYE",
    "CAACAgIAAxkBAAEPo2FoQWsIRmh9iM4hPzAvJHF5YXZFiAACm1QAAoauwUnC3lkp9ctBpjYE",
    "CAACAgIAAxkBAAEPo2NoQWsJhI0JBXxHYIhVbdG9tlMlTAACPnIAAnxAuEkLUfaBTwYcIDYE",
    "CAACAgIAAxkBAAEPo2VoQWsLhp_xa1rhNyhGQwOrrlxPbgACzGIAAtc2wEn1C_WABk10zDYE",
    "CAACAgIAAxkBAAEPo2doQWsN6DlS_5tdggqCUARjF9Tq9wACDGcAAuPlwUkHBq4Bw5WuNjYE",
    "CAACAgIAAxkBAAEPo2loQWsPAAH1gApfomyJ6VgsYT3lN8YAArZ-AAJj8blJA-sJ93ZAw1M2BA",
    "CAACAgIAAxkBAAEPo2toQWsRCOuwHPTuedQiSN0JWoejJwACKHEAAk79wEmJh9kpjl2GpTYE",
    "CAACAgIAAxkBAAEPo21oQWsTybbyaTIxOtz7HJrVM2YcXQACbmcAAnAsIErGnGT_MODX4TYE",
    "CAACAgIAAxkBAAEPo29oQWsVs3FLeNezQ9t3gr8xmli6jAACw2kAAnWnIEpwFxqS_OT6CzYE",
    "CAACAgIAAxkBAAEPrfJoQ0S6Pn_5lS8UkmLKTkgqnlnmegACkHAAAqByIUp18AoELKKxazYE"
]


BELLY_RUB_RESPONSES = [
    "Мурррр... Аааа! Не надо! *кусь* ",
    "Пушистый животик доволен! Мур-мур-мур",
    "*переворачивается* Вот теперь можно! Но аккуратно! 🐾",
    "Ффффф! *шипит и убегает под диван*",
    "Мяу! *брыкается задними лапками*",
    "Ах ты... Ну ладно, погладь ещё разок",
    "*выпускает когти* Осторожнее! Я же не игрушка!",
    "Мррр... *звонко урчит* Продолжай!",
    "*резко хватает руку лапками* Поймал! Теперь ты мой!",
    "Оммм... помни, если просто его игнорировать, он уйдёт омммм... *не шевелится*"
]

# Случайная прощальная фраза
goodbyes = [
    "Мяу! Возвращаемся к делам!",
    "*прячет фантик* Ладно, поиграем потом!",
    "Фантик устал, и я тоже! Давай позже!"
]

# Реакции кота на бросок фантика
FANTIK_REACTIONS = [
    "Бух-бубух! *шуршит фантиком* Принёс тебе своё сокровище! Кидай ещё!",
    "Мяу-мяу! *гонится за фантиком* Поймал! Лови обратно!",
    "Вжик-вжик! *носится по комнате* Твой фантик теперь мой! ...Ладно, забирай!",
    "*акробатически ловит фантик* Вот так могу! Кидай мне снова фантик!",
    "Шурх-шурх! *играет с фантиком* Ой, кажется, я его немного порвал... Ну, ничего, держи!",
    "Мррр... *прижимает фантик лапкой* Не отдам! ...Ладно, на, лови!"
]

# Особые события (срабатывают с 25% вероятностью)
SPECIAL_EVENTS = {
    "cat_stuck": [
        "Ой! Я застрял! Помоги мне! ...Фух, спасибо!",
        "У меня фантик прилип к лапе. Мяу! Это магия? Помоги снять!",
        "Кот в ловушке! У меня фантик на голове! Выгляжу глупо? Сними его и кидай ещё!"
    ],
    "fantik_lost": [
        "Мяу? *осматривается* Куда же подевался фантик... Найди мне новый!",
        "*роется под диваном* Ты видел куда он закатился? Похоже, нужен новый фантик!",
        "Фантик исчез в четвертом измерении! Кидай ещё один!"
    ]
}

# Случайные ночные реакции кота
NIGHT_REACTIONS = [
    "Тыгыдык! *залезает лапами в миску с водой* Фу, она мокрая!",
    "Мяу-тыгыдык! *опрокидывает цветок* Он всё равно не вкусный!",
    "Тыгыдык-тыгыдык! *бегает за воображаемой добычей*",
    "Мррр! Тыгыдык! *запутывается в проводах* Не так уж и нужен тебе этот компьютер.",
    "Тыгыдык! *прыгает на шкаф*",
    "Мяу! *сбрасывает вещи с полок* У тебя не правильно стоит всё!",
    "Тыгыдык-мяу! *стучит по клавишам* Я вот уже работаю, в отличие от некоторых!",
    "Доброе мур-тро! *прыгает с разбега на спящего человека*",
    "О соле-е-е, о соле мяу-у-у! Хочу кушать именно сейчас! Мяу-у-у!",
    "Р-р-р! *охотится на голубя на балконе*",
    "БУХ! *откуда-то падает* Эй, я вообще-то тоже ударился!"
]

# Дневные отговорки
DAY_EXCUSES = [
    "Котик спит...(тыгыдыкаю с 23:00 до 7:00)",
    "Сейчас дневной сон! Приходи ночью (тыгыдыкаю с 23:00 до 7:00)",
    "*кот поворачивается спиной* Днём не тыгыдыкаю!",
    "Мяу... Солнце слишком яркое для тыгыдыков️",
    "Хозяин запретил дневные тыгыдыки!",
    "Функция доступна только в тёмное время суток (тыгыдыкаю с 23:00 до 7:00)"
]