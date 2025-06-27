# Habitify Weekly Log Viewer

A Python script that fetches your personal Habitify data and displays your weekly habit log in a clean, visual HTML table — with ✅ and ❌ marks for each day.

No login required — just your Habitify API key.

---

## Features

* Fetches all your current habits from Habitify
* Displays log data in a neat, responsive grid
* Outputs to an HTML file you can open locally
* Shows the current week (Monday to Sunday)

---

## How to Use

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/habitify-weekly-log.git
cd habitify-weekly-log
```

### 2. Install Requirements

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add Your Habitify API Key

Open `main.py` and replace the placeholder:

```python
API_KEY = "your_actual_api_key_here"
```

You can find your key in the Habitify app under `Settings → API`.

---

### 4. Run It

```bash
python main.py
```

It will:

* Fetch your habits and logs
* Generate `weekly_log.html`
* Open it in your browser


## Files

| File                      | Description                         |
| ------------------------- | ----------------------------------- |
| `main.py`                 | Main Python script                  |
| `weekly_log.html`         | Generated report                    |
| `requirements.txt`        | List of Python dependencies         |
| `README.md`               | You're reading it                   |

---

## Requirements

* Python 3.8+
* `requests`
* `pytz`

(Install with `pip install -r requirements.txt`)

---

## Credits

* Built using the [Habitify Open API](https://docs.habitify.me)

---

## License

MIT — free for personal and commercial use.
