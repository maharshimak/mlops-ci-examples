# Setup

Python 3: app.py implements arithmetic exercises. For the existing pytest suites, review requirements.txt and install only into an isolated environment. Run each variants/audit-ID test suite in its own working directory. Node: node examples/javascript-and-python/tests/calculator.test.cjs. Gemini is an optional paid-provider sample; do not run it during offline tests.

Keep credentials in an untracked .env or process environment. Use isolated environments and synthetic fixtures. No model training, paid calls, or privileged helper execution is part of verification. See README.md for recorded results.
