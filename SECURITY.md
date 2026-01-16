# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1   | :x:                |

## Reporting a Vulnerability

We take the security of clinical data extremely seriously. If you discover a vulnerability, please do **NOT** open a public issue. 

Instead, please send an email to `security@clinical-llm-guard.org` with the subject line "VULNERABILITY REPORT".

## Zero Data Retention Policy

This library is designed to facilitate compliance with HIPAA and GDPR. However, the `ClinicalAnonymizer` runs locally within your infrastructure.
- **We do not collect any logs.**
- **We do not store any patient data.**
- **No telemetry is sent to our servers.**

It is the user's responsibility to ensure that the anonymized output is safe for transmission to third-party LLM providers (e.g., OpenAI Business API).
