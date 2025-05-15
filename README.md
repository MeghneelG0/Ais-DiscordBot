# Ais Discord Bot

A modern Discord bot that integrates with Ollama to provide LLM-powered responses to user queries.  
*Upcoming: NLP-based toxicity detection and moderation features.*

## Features

- **LLM Integration:** Uses Ollama to connect with LLaMA 3.2 for intelligent, conversational responses.
- **Easy Setup:** Simple configuration through environment variables.
- **Modular Design:** Utilizes Discord.py's cogs system for extensibility.
- **Planned:** Automated toxicity detection and user moderation using NLP.

## Installation

1. Clone this repository: git clone https://github.com/yourusername/Ais-DiscordBot.git
2. Install required packages: pip install -r requirements.txt
3. Create a `.env` file in the project root with your Discord bot token.
4. Install and set up Ollama with the LLaMA 3.2 model.

## Usage

1. Start the bot:
2. In Discord, use the following commands:
- `>ask [question]` - Ask the LLM bot a question

## Project Structure
Ais-DiscordBot/ 
├── bot.py # Main bot file 
├── config.py # Configuration and settings 
├── cogs/ # Command modules 
│ └── test.py # Test commands 
├── .env # Environment variables (not in repo) 
├── requirements.txt


## Requirements

- Python 3.8+
- discord.py 2.5.2
- python-dotenv 1.0.0
- ollama 0.4.7

## Roadmap

- [x] LLM-powered Q&A via Ollama
- [ ] NLP-based toxicity detection and moderation

## License

MIT

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request