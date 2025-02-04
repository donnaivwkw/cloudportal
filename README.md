# CloudPortal

CloudPortal is a Python-based program designed to monitor CPU and memory usage on a Windows system. It provides visual feedback through simple graphical displays, allowing users to track the performance of their system in real-time.

## Features

- **Real-time Monitoring:** Continuously display CPU and memory usage using matplotlib.
- **Graphical Feedback:** Provides separate plots for CPU and memory usage to easily visualize system performance.
- **Adjustable View:** Display up to 100 seconds of usage data, automatically updating as new data is collected.

## Requirements

- Python 3.x
- `psutil` library
- `matplotlib` library

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries using pip:
   ```bash
   pip install psutil matplotlib
   ```

## Usage

To run CloudPortal, navigate to the directory containing `cloud_portal.py` and execute the following command in your terminal:

```bash
python cloud_portal.py
```

This will launch a window displaying real-time CPU and memory usage graphs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

- Thanks to the developers of `psutil` and `matplotlib` for providing the tools necessary to create this application.