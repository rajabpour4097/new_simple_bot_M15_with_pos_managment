# ساعات مختلف بازار فارکس بر اساس ساعت ایران

# جلسه سیدنی (05:30 - 14:30 ایران)
SYDNEY_HOURS_IRAN = {
    'start': '05:30',
    'end': '14:30'
}

# جلسه توکیو (07:30 - 16:30 ایران)  
TOKYO_HOURS_IRAN = {
    'start': '07:30',
    'end': '16:30'
}

# جلسه لندن (12:30 - 21:30 ایران)
LONDON_HOURS_IRAN = {
    'start': '12:30',
    'end': '21:30'
}

# جلسه نیویورک (17:30 - 02:30 ایران)
NEWYORK_HOURS_IRAN = {
    'start': '17:30',
    'end': '02:30'  # روز بعد
}

# همپوشانی لندن-نیویورک (17:30 - 21:30 ایران) - بهترین زمان
OVERLAP_LONDON_NY_IRAN = {
    'start': '17:30',
    'end': '21:30'
}

# ساعات فعال ایرانی (09:00 - 21:00)
IRAN_ACTIVE_HOURS = {
    'start': '09:00',
    'end': '21:00'
}

# 24 ساعته
FULL_TIME_IRAN = {
    'start': '00:00',
    'end': '23:59'
}

MY_CUSTOM_TIME_IRAN = {
    'start': '01:00',
    'end': '23:59'
}

BEST_TIME_IRAN = {
    'start': '09:00',
    'end': '18:30'
}

# تنظیمات MT5
MT5_CONFIG = {
    'symbol': 'EURUSD',
    'lot_size': 0.01,
    'win_ratio': 2,
    'magic_number': 234000,
    'deviation': 20,
    'max_spread': 3.0,
    'min_balance': 1,
    'max_daily_trades': 10,
    'trading_hours': IRAN_ACTIVE_HOURS,
    'risk_percent': 0.02,  # 2% ریسک در هر معامله
}

# تنظیمات استراتژی
TRADING_CONFIG = {
    'threshold': 6,  # Changed from 6 to 60 to detect major legs (6 pips minimum)
    'fib_705': 0.705,
    'fib_90': 0.9,
    'window_size': 100,
    'min_swing_size': 4,
    'entry_tolerance': 2.0,
    'lookback_period': 20,
    # Optional: epsilon tolerance for 0.705 touch detection (in pips)
    # 'touch_epsilon_pips': 0.15,
    'prevent_multiple_positions': True,  # جلوگیری از باز کردن پوزیشن‌های متعدد همزمان
    'position_check_mode': 'all',  # 'all': همه پوزیشن‌ها، 'conflicting': فقط پوزیشن‌های مخالف
}

# مدیریت پویا چند مرحله‌ای جدید - 19 مرحله (2.5R تا 20.5R)
# مراحل بر اساس Trailing_2.5R:
# 1) 2.5R: بستن نیمی از پوزیشن (+1.25R قفل)، SL روی BE (0R)، TP به 3.5R
# 2) 3.5R: SL روی +2.5R، TP به 4.5R
# 3) 4.5R: SL روی +3.5R، TP به 5.5R
# ... و همینطور تا 20.5R
DYNAMIC_RISK_CONFIG = {
    'enable': True,
    'commission_per_lot': 4.5,          # کمیسیون کل (رفت و برگشت یا فقط رفت؟ طبق بروکر - قابل تنظیم)
    'commission_mode': 'per_lot',       # per_lot (کل)، per_side (نیمی از رفت و برگشت) در صورت نیاز توسعه
    'round_trip': False,                # اگر True و per_side باشد دو برابر می‌کند
    'base_tp_R': 2.0,                   # TP اولیه تنظیم‌شده هنگام ورود (برای مرجع)
    'stages': [
        {  # 2.5R stage - بستن 50% + SL به BE
            'id': 'stage_2_5R',
            'trigger_R': 2.5,
            'sl_lock_R': 0.0,   # Breakeven
            'tp_R': 3.5
        },
        {  # 3.5R stage
            'id': 'stage_3_5R',
            'trigger_R': 3.5,
            'sl_lock_R': 2.5,
            'tp_R': 4.5
        },
        {  # 4.5R stage
            'id': 'stage_4_5R',
            'trigger_R': 4.5,
            'sl_lock_R': 3.5,
            'tp_R': 5.5
        },
        {  # 5.5R stage
            'id': 'stage_5_5R',
            'trigger_R': 5.5,
            'sl_lock_R': 4.5,
            'tp_R': 6.5
        },
        {  # 6.5R stage
            'id': 'stage_6_5R',
            'trigger_R': 6.5,
            'sl_lock_R': 5.5,
            'tp_R': 7.5
        },
        {  # 7.5R stage
            'id': 'stage_7_5R',
            'trigger_R': 7.5,
            'sl_lock_R': 6.5,
            'tp_R': 8.5
        },
        {  # 8.5R stage
            'id': 'stage_8_5R',
            'trigger_R': 8.5,
            'sl_lock_R': 7.5,
            'tp_R': 9.5
        },
        {  # 9.5R stage
            'id': 'stage_9_5R',
            'trigger_R': 9.5,
            'sl_lock_R': 8.5,
            'tp_R': 10.5
        },
        {  # 10.5R stage
            'id': 'stage_10_5R',
            'trigger_R': 10.5,
            'sl_lock_R': 9.5,
            'tp_R': 11.5
        },
        {  # 11.5R stage
            'id': 'stage_11_5R',
            'trigger_R': 11.5,
            'sl_lock_R': 10.5,
            'tp_R': 12.5
        },
        {  # 12.5R stage
            'id': 'stage_12_5R',
            'trigger_R': 12.5,
            'sl_lock_R': 11.5,
            'tp_R': 13.5
        },
        {  # 13.5R stage
            'id': 'stage_13_5R',
            'trigger_R': 13.5,
            'sl_lock_R': 12.5,
            'tp_R': 14.5
        },
        {  # 14.5R stage
            'id': 'stage_14_5R',
            'trigger_R': 14.5,
            'sl_lock_R': 13.5,
            'tp_R': 15.5
        },
        {  # 15.5R stage
            'id': 'stage_15_5R',
            'trigger_R': 15.5,
            'sl_lock_R': 14.5,
            'tp_R': 16.5
        },
        {  # 16.5R stage
            'id': 'stage_16_5R',
            'trigger_R': 16.5,
            'sl_lock_R': 15.5,
            'tp_R': 17.5
        },
        {  # 17.5R stage
            'id': 'stage_17_5R',
            'trigger_R': 17.5,
            'sl_lock_R': 16.5,
            'tp_R': 18.5
        },
        {  # 18.5R stage
            'id': 'stage_18_5R',
            'trigger_R': 18.5,
            'sl_lock_R': 17.5,
            'tp_R': 19.5
        },
        {  # 19.5R stage
            'id': 'stage_19_5R',
            'trigger_R': 19.5,
            'sl_lock_R': 18.5,
            'tp_R': 20.5
        },
        {  # 20.5R stage (final)
            'id': 'stage_20_5R',
            'trigger_R': 20.5,
            'sl_lock_R': 20.5,
            'tp_R': 20.5
        }
    ]
}

# تنظیمات لاگ
LOG_CONFIG = {
    'log_level': 'INFO',        # DEBUG, INFO, WARNING, ERROR
    'save_to_file': True,       # ذخیره در فایل
    'max_log_size': 10,         # حداکثر حجم فایل لاگ (MB)
}
