# Reddit User Persona Generator

A Python tool that analyzes Reddit user profiles to generate detailed user personas using AI. This tool scrapes a user's recent posts and comments, then uses Mistral AI to create a comprehensive persona with cited evidence from their Reddit activity.

## Features

- **Reddit Data Extraction**: Scrapes user posts and comments from Reddit
- **AI-Powered Analysis**: Uses Mistral AI to generate detailed user personas
- **Evidence-Based Insights**: Provides citations from actual posts/comments
- **Structured Output**: Generates organized persona profiles
- **File Export**: Saves personas to text files for easy sharing

## Prerequisites

- Python 3.7+
- Reddit API credentials
- Mistral AI API key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/reddit-persona-generator.git
cd reddit-persona-generator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables by creating a `.env` file:
```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_app_name/1.0
MISTRAL_API_KEY=your_mistral_api_key
```

## Getting API Credentials

### Reddit API Setup
1. Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps)
2. Click "Create App" or "Create Another App"
3. Choose "script" as the app type
4. Note down your `client_id` and `client_secret`
5. Set a descriptive `user_agent` (e.g., "PersonaGenerator/1.0")

### Mistral AI API Setup
1. Visit [Mistral AI](https://mistral.ai/)
2. Sign up for an account
3. Generate an API key from your dashboard
4. Add it to your `.env` file

## Usage

1. Run the script:
```bash
python persona_generator.py
```

2. Enter a Reddit profile URL when prompted:
```
Enter Reddit profile URL: https://www.reddit.com/user/username
```

3. The tool will:
   - Extract the username from the URL
   - Scrape recent posts and comments
   - Generate an AI-powered persona
   - Save the results to a text file

## Configuration

You can modify the following parameters in the `main()` function:

- `post_limit`: Number of recent posts to analyze (default: 30)
- `comment_limit`: Number of recent comments to analyze (default: 30)

## Output

The generated persona includes:
- Estimated demographics (age, location, occupation)
- Interests and hobbies
- Communication style
- Online behavior patterns
- Cited evidence from actual posts/comments

Results are saved as `{username}_persona.txt` in the project directory.

## Requirements

Create a `requirements.txt` file with:
```
praw>=7.7.0
mistralai>=1.0.0
python-dotenv>=1.0.0
```

## Project Structure

```
reddit-persona-generator/
├── persona_generator.py      # Main script
├── requirements.txt          # Python dependencies
├── .env                     # Environment variables (create this)
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Privacy and Ethics

⚠️ **Important Considerations:**

- This tool analyzes publicly available Reddit data
- Respect user privacy and Reddit's Terms of Service
- Use generated personas responsibly and ethically
- Consider the implications of user profiling
- Only analyze profiles you have permission to research

## Error Handling

The script includes basic error handling for:
- Invalid Reddit URLs
- Users with no posts/comments
- API connection issues

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Disclaimer

This tool is for educational and research purposes only. Users are responsible for complying with Reddit's API terms of service and applicable privacy laws. The generated personas are AI interpretations and should not be considered factual profiles of real individuals.

## Support

If you encounter issues or have questions:
1. Check the [Issues](https://github.com/yourusername/reddit-persona-generator/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

## Acknowledgments

- [PRAW](https://praw.readthedocs.io/) for Reddit API access
- [Mistral AI](https://mistral.ai/) for natural language processing
- Reddit community for providing the data platform
