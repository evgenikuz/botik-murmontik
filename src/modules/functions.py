from datetime import datetime, time, date
import aiosqlite

from src.modules.admin import DB_PATH


async def check_time_in_range(start: time, end: time) -> bool:
    """Проверяет, находится ли текущее время в заданном диапазоне"""
    now = datetime.now().time()
    return start <= now <= end


# Добавляем проверку для всех обработчиков команд
async def check_user_registered(user_id: int) -> bool:
    """Проверяет, зарегистрирован ли пользователь"""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT 1 FROM users WHERE user_id = ?', (user_id,))
        exists = await cursor.fetchone()
        await cursor.close()
        return exists is not None


async def get_notification_status(user_id: int) -> bool:
    """Получение статуса уведомлений пользователя"""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            'SELECT receives_notifications FROM users WHERE user_id = ?',
            (user_id,)
        )
        result = await cursor.fetchone()
        await cursor.close()
        return bool(result[0]) if result else False


async def add_user(user_id, full_name, username):
    """Добавление пользователя в базу данных"""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT 1 FROM users WHERE user_id = ?', (user_id,))
        exists = await cursor.fetchone()
        await cursor.close()

        if not exists:
            await db.execute(
                'INSERT INTO users (user_id, full_name, username) VALUES (?, ?, ?)',
                (user_id, full_name, username)
            )
            await db.commit()


async def set_notification_status(user_id: int, status: bool):
    """Установка статуса получения уведомлений"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            'UPDATE users SET receives_notifications = ? WHERE user_id = ?',
            (1 if status else 0, user_id)
        )
        await db.commit()


async def init_db():
    """Инициализация базы данных"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                full_name TEXT,
                username TEXT,
                receives_notifications INTEGER DEFAULT 0,
                work_schedule TEXT
            )
        ''')
        await db.commit()


def is_night_time():
    """Проверяет, ночное ли сейчас время (23:00-07:00)"""
    now = datetime.now().time()
    return now >= time(23) or now < time(7)


async def set_work_schedule(user_id: int, schedule: str):
    """Устанавливает график работы пользователя в БД"""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE users SET work_schedule = ? WHERE user_id = ?",
            (schedule, user_id))
        await db.commit()


async def get_work_schedule(user_id: int) -> str:
    """Получает график работы пользователя из БД"""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT work_schedule FROM users WHERE user_id = ?",
            (user_id,))
        result = await cursor.fetchone()
        await cursor.close()
        return result[0] if result else None


def is_weekday(date: datetime = None) -> bool:
    """
    Проверяет, является ли день будним (пн-пт)
    :param date: Дата для проверки (по умолчанию текущая)
    :return: True если будний день, False если выходной
    """
    check_date = date or datetime.now()
    return check_date.weekday() < 5  # 0-4 = пн-пт, 5-6 = сб-вс


def is_holiday(check_date: date = None) -> bool:
    """Проверяет, является ли день праздничным (для России)"""
    holidays = {
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),  # Новый год
        (2, 23),  # День защитника
        (3, 8),    # 8 Марта
        (1, 5), (9, 5), # Майские праздники
        (12, 6),    # День России
        (4, 11), # День Народного Единства
    }
    d = check_date or date.today()
    return (d.month, d.day) in holidays


def is_working_day(date: datetime = None) -> bool:
    """Проверяет, является ли день рабочим (не выходной и не праздник)"""
    d = date or datetime.now()
    return is_weekday(d) and not is_holiday(d.date())