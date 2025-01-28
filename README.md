# Stock Price Email Alert

This Python project sends email alerts when a stock price crosses a specified threshold. It uses the `smtpd` debugging server for testing email functionality.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This project monitors stock prices using APIs and sends email alerts to notify users when the price of a stock crosses a user-defined threshold. It is ideal for tracking investments or market changes in real-time.

## Features

- Monitor stock prices in real-time.
- Send email alerts using a local `smtpd` debugging server.
- Customizable stock symbols and price thresholds.

## Getting Started

Instructions to set up and run the project.

### Prerequisites

- Python >= 3.9

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo.git
   ```

2. Navigate to the project directory:
   ```bash
   cd stock-price-alert
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the `smtpd` debugging server for testing email functionality:
   ```bash
   python -m smtpd -c DebuggingServer -n localhost:1025
   ```

2. Run the stock price alert script:
   ```bash
   python stock_alert.py
   ```

3. Configure stock symbols and thresholds in the configuration file or environment variables.

## Configuration

Update the `config.py` file or set the following environment variables:

```bash
STOCK_API_KEY=your_api_key
STOCK_SYMBOL=AAPL
PRICE_THRESHOLD=150.0
SMTP_SERVER=localhost
SMTP_PORT=1025
EMAIL_FROM=your_email@example.com
EMAIL_TO=recipient@example.com
```

## Technologies Used

- **Python Libraries**: `requests`, `smtplib`
- **Debugging Server**: `smtpd`

## Contributing

If you would like to contribute, please follow these steps:

1. Fork the repository
2. Create a branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Sangeetha - [LinkedIn Profile](https://linkedin.com/in/sangeethamt) - sangeemt8@gmail.com

Project Link: [https://github.com/sangeethamt/stockpricealert](https://github.com/sangeethamt/stockpricealert)

