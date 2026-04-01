"""
SKA Webhook Receiver — runs on the contributor's Pi (or any client machine).

Listens for loop-end notifications from the SKA server.
On each webhook: stops the current bot process (SIGTERM) and starts a fresh one.

Usage:
    python webhook_receiver.py --bot /path/to/trading_bot.py --symbol XRPUSDT --port 8765 --api https://api.quantiota.org

Setup:
    1. Run this script once — it stays running permanently.
    2. Register your public IP / Tailscale IP with the server (add to webhooks.json).
    3. The bot starts automatically on first webhook and restarts on every loop boundary.

Requirements:
    pip install flask requests
"""


import argparse
import logging
import os
import signal
import subprocess
import sys
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)

bot_proc    = None
loop_count  = 0


def start_bot(symbol: str, api: str) -> subprocess.Popen:
    cmd = [sys.executable, args.bot, "--symbol", symbol, "--api", api]
    logging.info(f"Starting bot: {' '.join(cmd)}")
    return subprocess.Popen(cmd)


def stop_bot():
    global bot_proc
    if bot_proc and bot_proc.poll() is None:
        logging.info(f"Stopping bot PID={bot_proc.pid} (SIGTERM)...")
        bot_proc.send_signal(signal.SIGTERM)
        try:
            bot_proc.wait(timeout=15)
        except subprocess.TimeoutExpired:
            logging.warning("Bot did not stop in 15s — sending SIGKILL")
            bot_proc.kill()
            bot_proc.wait()
        logging.info("Bot stopped")
    bot_proc = None


@app.route("/restart", methods=["POST"])
def restart():
    global bot_proc, loop_count

    data    = request.get_json(silent=True) or {}
    loop_id = data.get("loop_id", "?")
    symbol  = data.get("symbol", args.symbol)

    logging.info(f"Webhook received — loop_id={loop_id} symbol={symbol}")

    stop_bot()
    bot_proc   = start_bot(symbol, args.api)
    loop_count += 1

    logging.info(f"Bot restarted — PID={bot_proc.pid} | client_loop={loop_count}")
    return jsonify({"status": "restarted", "pid": bot_proc.pid, "loop_id": loop_id})


@app.route("/status", methods=["GET"])
def status():
    running = bot_proc is not None and bot_proc.poll() is None
    return jsonify({
        "bot_running":  running,
        "pid":          bot_proc.pid if running else None,
        "loop_count":   loop_count,
    })


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SKA Webhook Receiver")
    parser.add_argument("--bot",    required=True,                         help="Path to client_trading_bot.py")
    parser.add_argument("--symbol", default="XRPUSDT",                    help="Trading pair")
    parser.add_argument("--api",    default="https://api.quantiota.org",   help="SKA API base URL")
    parser.add_argument("--port",   type=int, default=8765,                help="Listener port")
    args = parser.parse_args()

    # Auto-start bot immediately on launch
    bot_proc = start_bot(args.symbol, args.api)
    logging.info(f"Bot started on launch — PID={bot_proc.pid}")

    logging.info(f"SKA Webhook Receiver started — port={args.port} symbol={args.symbol}")
    app.run(host="0.0.0.0", port=args.port)
