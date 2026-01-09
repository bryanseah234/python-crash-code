# Python Crash Code

A collection of Python scripts demonstrating various methods to crash or slow down a computer system.

## Description

This project contains educational examples of different techniques that can be used to consume system resources (memory, CPU, processes) in Python. These scripts demonstrate various stress-testing methods including infinite loops, memory exhaustion, fork bombs, and thread bombs. This repository is intended for educational purposes to understand how resource exhaustion attacks work.

## Features

- **Memory Exhaustion** (`one.py`) - Uses itertools to create an infinite list and exhaust memory
- **Infinite Iterator** (`two.py`) - Demonstrates itertools product with infinite count
- **CPU Stress** (`three.py`) - Simple infinite loop to max out CPU usage
- **Fork Bomb** (`four.py`) - Creates infinite child processes (Linux/Unix only)
- **Thread Bomb** (`five.py`) - Spawns infinite threads recursively
- **Memory Corruption** (`six.py`) - Uses ctypes to write to arbitrary memory addresses

## Technologies Used

- Python 3
- Standard library modules: `itertools`, `os`, `threading`, `ctypes`

## Installation

```bash
# Clone the repository
git clone https://github.com/bryanseah234/python-crash-code.git

# Navigate to project directory
cd python-crash-code
```

No additional dependencies are required - all scripts use Python standard library modules.

## Usage

```bash
# Run any of the crash scripts
python one.py
python two.py
python three.py
python four.py   # Linux/Unix only
python five.py
python six.py
```

⚠️ **Warning:** These scripts are designed to crash your system. Run them in a virtual machine or controlled environment only.

## Disclaimer

1. FOR EDUCATIONAL PURPOSES ONLY
2. USE AT YOUR OWN DISCRETION

⚠️ **Potential Impacts:**
- **Memory exhaustion scripts** (`one.py`, `two.py`) may freeze your system and require a restart
- **CPU stress** (`three.py`) will max out CPU usage until terminated
- **Fork bomb** (`four.py`) may require a system restart to recover
- **Thread bomb** (`five.py`) can crash your Python interpreter and slow down the system
- **Memory corruption** (`six.py`) may cause data loss, crashes, or require a system restart

These scripts can cause system instability, data loss, or crashes. The author is not responsible for any damage caused by running these scripts.

## License

MIT License

---

**Author:** <a href="https://github.com/bryanseah234">bryanseah234</a>
