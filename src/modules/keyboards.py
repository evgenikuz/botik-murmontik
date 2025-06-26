from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def create_main_keyboard(notifications_enabled: bool):
    """Создает главную клавиатуру"""
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text='Отключить напоминания о дейли и списании времени'
                    if notifications_enabled
                    else 'Напоминать о дейли и списании времени'
                )
            ],
            [KeyboardButton(text='Рассказать о курсе валют')],
            [KeyboardButton(text='Бегать за фантиком')],
            [KeyboardButton(text='Тыгыдыкать ночью')],
            [KeyboardButton(text='Погладить животик')],
            [KeyboardButton(text='Прислать своё фото')],
            [KeyboardButton(text='Остановить бот')]
        ]
    )


def get_schedule_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="9:00 - 18:00", callback_data="schedule_9_18")],
            [InlineKeyboardButton(text="10:00 - 19:00", callback_data="schedule_10_19")]
    ])


def create_game_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text='Бросить фантик'),
             KeyboardButton(text='Закончить игру')]
        ]
    )