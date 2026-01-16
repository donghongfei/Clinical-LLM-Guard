# Contributing to Clinical-LLM-Guard

We welcome contributions from the community! 

## Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/your-username/Clinical-LLM-Guard.git
   ```
3. **Install dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

## Development Standards

- **Code Style**: We use `black` for formatting and `flake8` for linting.
- **Testing**: All new features must be accompanied by unit tests. Run tests using `pytest`.
- **Security**: 
  - Do NOT commit any real patient data. 
  - Use the synthetic data generator in `tests/data` for all examples.

## Pull Request Process

1. Create a feature branch (`git checkout -b feature/amazing-feature`).
2. Commit your changes.
3. Push to the branch.
4. Open a Pull Request against the `main` branch.

Thank you for helping us make clinical AI safer!
