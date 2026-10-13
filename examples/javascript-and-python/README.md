# loose-code-samples

Source-only publication package authorized by the owner.

- Loose calculator, Gemini SDK sample and tiny Python sample in home; unrelated manifest shared by loose files.

## Setup and validation

Review dependency manifests and executable cells before running. Use isolated environments and synthetic fixtures. No live provider calls, model training or dataset downloads were run.

## Findings and required improvements

- Calculator, Gemini sample and Python fragment are unrelated; no root manifest promises one runnable application. Provider example must stay mocked.

## Publication status

READY for source-only publication. Ownership and redistribution permission were explicitly confirmed. Application execution is limited to the checks recorded below; missing datasets/assets and unrun training are transparent limitations.

No license is invented. Original copyright/attribution must be resolved before publication. Source variants are preserved under variants/audit-ID. Notebook output, metadata and prose were removed to prevent personal-data disclosure.

## Validation and limitations

- calculator parser precedence, malicious syntax, malformed number, zero division and size/type bounds: PASS
- Node syntax calculator.js: PASS
- Node syntax gemini.js: PASS

No model training, paid-provider requests, dataset downloads, privileged operations or deployment was performed. Notebook packages preserve only source cells; historical outputs/metrics are omitted. Dependency versions are unresolved where no original lock exists. Integration/build checks not explicitly listed as passing were not run.

Use `npm test` for the dependency-free calculator tests. The optional Gemini example requires the declared SDK and a private local GEMINI_API_KEY; running it may incur provider charges and is excluded from offline verification. Python main.py is an independent introductory fragment.

## Validation and limitations

- calculator parser precedence, malicious syntax, malformed number, zero division and size/type bounds: PASS
- Node syntax calculator.js: PASS
- Node syntax gemini.js: PASS

No model training, paid-provider requests, dataset downloads, privileged operations or deployment was performed. Notebook packages preserve only source cells; historical outputs/metrics are omitted. Dependency versions are unresolved where no original lock exists. Integration/build checks not explicitly listed as passing were not run.

Use `npm test` for the dependency-free calculator tests. The optional Gemini example requires the declared SDK and a private local GEMINI_API_KEY; running it may incur provider charges and is excluded from offline verification. Python main.py is an independent introductory fragment.
