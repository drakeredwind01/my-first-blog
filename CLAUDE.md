# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Always activate the venv first:
```bash
source venv/bin/activate
```

```bash
python manage.py runserver          # dev server
python manage.py makemigrations     # after model changes
python manage.py migrate
python manage.py test               # run all tests
python manage.py test blog          # run tests for one app
python manage.py createsuperuser
python manage.py collectstatic      # before deploying
```

Stripe webhook listener (requires Stripe CLI):
```bash
stripe listen --forward-to localhost:8000/payments/webhook/
```

## Architecture

Multi-app Django 4.2 project. Entry point is `mysite/` (settings, root URLs). Three feature apps:

**`blog/`** — Core blog. `Post` model uses `CKEditor5Field` for rich text. On save, `post_new` and `post_edit` sanitize HTML with `nh3` before writing to the DB, allowing a specific allowlist of tags/attributes. Posts are only shown publicly once `published_date` is set.

**`payments/`** — Stripe Checkout integration for physical products. Flow: JS fetches `/payments/config/` for the publishable key → calls `/payments/create-checkout-session/?product_id=X&quantity=Y` which creates a pending `Order` + `OrderItem` in the DB and returns a Stripe session ID → JS redirects to Stripe hosted checkout → Stripe POSTs to `/payments/webhook/` on completion → `_handle_checkout_complete` marks the order paid, saves the shipping address, and emails per-product notification recipients. Prices are stored in **cents** throughout.

**`tools/`** — Lightweight utility pages (stopwatches). No models; views just render templates.

## Environment

Secrets live in `.env` (not committed). Required keys:
```
STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
STRIPE_ENDPOINT_SECRET=
```

Email is console-backend in dev (`EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`). Switch to SMTP for production.

## Templates

Global base template is `blog/templates/blog/base.html`. Each app has its own `templates/` subdirectory. Static files per-app are in `<app>/static/`; run `collectstatic` before deploying.

## Deployment

Hosted on PythonAnywhere (`ALLOWED_HOSTS` includes `.pythonanywhere.com`). Gunicorn is available in the venv. See `Deploy time!.md` for deployment notes.
