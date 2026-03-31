# =========================
# PM40 TELEGRAM NOTIFIER (CLEAN RESULT FIX)
# =========================

import requests

TOKEN = "8337770689:AAHJ1pPK5Q3xbWbv2vzaKx0x9mv25ehzsuw"
CHAT_ID = "1226520868"


def get_chat_id():
    return CHAT_ID


def send_message(text):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    try:
        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": text
        }, timeout=5)
    except Exception as e:
        print(f"[TELEGRAM ERROR] {e}")


def send_signal(symbol, signal, confidence, is_entry, expiration=None):

    if signal == "NEUTRAL":
        return

    if is_entry:

        msg = (
            f"🚀 {symbol}\n"
            f"{signal}\n"
            f"conf: {round(confidence, 2)}"
        )

        if expiration:
            msg += f" | {expiration}m"

    else:
        msg = f"{symbol} {signal}"

    send_message(msg)


def send_result(symbol, result):

    # 🔥 ТІЛЬКИ WIN / LOSS
    msg = f"📊 {symbol} → {result}"
    send_message(msg)


def send_heartbeat():
    send_message("✅ PM40 WORKING")