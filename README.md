# mlops-ci-examples

- Arithmetic CLI plus pytest, Docker and Actions exam exercise; complete manifest compared with loose Downloads copy.
- Arithmetic utility CLI and pytest/CI/Docker exam exercise; not a trained ML production pipeline.
- Small Actions/Docker arithmetic demo archive with tests.
- Small arithmetic calculator module archive with unit/integration tests.

## Source-only publication

The owner explicitly confirmed ownership and permission to publish candidate source. Copyright remains reserved; no permissive license was invented. Third-party media, data, weights and assets were withheld. This repository documents the available source and its actual limits.

## Setup

Python 3: app.py implements arithmetic exercises. For the existing pytest suites, review requirements.txt and install only into an isolated environment. Run each variants/audit-ID test suite in its own working directory. Node: node examples/javascript-and-python/tests/calculator.test.cjs. Gemini is an optional paid-provider sample; do not run it during offline tests.

## Status

READY



## Known limitations and improvements

- Owner-confirmed instructional source; preserve separate variants rather than invent ML functionality.
- Factorial accepts bool as int and uses recursion; large-input limit absent. Deployment workflow deliberately withheld.
- Loose calculator/Gemini/Python samples consolidated under examples/javascript-and-python; optional provider sample excluded from offline runs.
- Unlisted integration/build/training/browser checks were not run. No paid provider or privileged scripts were executed. Dependencies were not installed; original locks retained when available.

## Verification

- arithmetic mean signed/empty/input type: PASS
- palindrome case and spaces: PASS
- factorial normal, zero, negative, noninteger: PASS
- even filtering: PASS
- calculator four operations and invalid methods: PASS
- calculator parser precedence, malicious syntax, malformed number, zero division and size/type bounds: PASS
- Node syntax calculator.js: PASS
- Node syntax gemini.js: PASS
