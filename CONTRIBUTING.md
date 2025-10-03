# Contributing to English Learning Shooter

Thank you for your interest in contributing to English Learning Shooter! 🎯📚

We welcome contributions from developers, educators, and language enthusiasts. This document provides guidelines for contributing to the project.

## 🌟 Ways to Contribute

### 🐛 Report Bugs
- Use the [GitHub issue tracker](https://github.com/yourusername/english-learning-shooter/issues)
- Check if the bug has already been reported
- Provide detailed steps to reproduce the issue
- Include your system information (OS, Python version, etc.)

### 💡 Suggest Features
- Open a [feature request](https://github.com/yourusername/english-learning-shooter/issues/new?template=feature_request.md)
- Describe the educational value of your suggestion
- Explain how it would improve the learning experience

### 📝 Add Content
- **New Questions**: Add vocabulary, grammar, or spelling questions
- **Learning Categories**: Propose new educational topics
- **Difficulty Levels**: Expand existing categories with more levels

### 🎨 Improve Design
- UI/UX enhancements
- Visual effects and animations
- Sound effects and background music
- Accessibility improvements

### 📚 Documentation
- Fix typos and improve clarity
- Add examples and tutorials
- Translate documentation
- Create educational guides

## 🚀 Getting Started

### 1. Fork and Clone
```bash
# Fork the repository on GitHub
git clone https://github.com/yourusername/english-learning-shooter.git
cd english-learning-shooter
```

### 2. Set Up Development Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .[dev]  # Install development dependencies
```

### 3. Run the Game
```bash
python english_learning_shooter.py
```

### 4. Run Tests
```bash
python -m pytest tests/
```

## 📋 Development Guidelines

### Code Style
- Follow [PEP 8](https://pep8.org/) Python style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise

### Adding New Questions
To add new educational content, modify the `vocabulary_sets` dictionary:

```python
vocabulary_sets = {
    "your_category": {
        "beginner": [
            {
                "question": "Clear, educational question?",
                "options": ["Option1", "Option2", "Option3", "Option4"],
                "correct": 0,  # Index of correct answer (0-3)
                "damage": 10,   # Damage value (6-18 range)
                "definition": "Educational explanation of the answer"
            }
        ],
        "intermediate": [...],
        "advanced": [...]
    }
}
```

### Educational Quality Standards
- **Accuracy**: All questions and answers must be correct
- **Age Appropriate**: Content suitable for intended audience
- **Clear Language**: Questions should be unambiguous
- **Educational Value**: Each question should teach something useful
- **Difficulty Progression**: Beginner → Intermediate → Advanced

### Testing New Content
1. Test questions for accuracy
2. Verify difficulty progression
3. Check that definitions are helpful
4. Ensure damage values are balanced

## 🎯 Content Guidelines

### Question Categories
Current categories and their focus:
- **Synonyms**: Words with similar meanings
- **Antonyms**: Words with opposite meanings  
- **Spelling**: Correct spelling identification
- **Grammar**: Verb tenses, articles, pronouns
- **Definitions**: Word meaning comprehension
- **Sentence Completion**: Context and vocabulary
- **Rhyming**: Sound patterns and poetry
- **Plurals**: Irregular plural forms

### Difficulty Levels
- **Beginner**: 6-9 damage, basic vocabulary, simple concepts
- **Intermediate**: 8-13 damage, common advanced words, moderate complexity
- **Advanced**: 12-18 damage, sophisticated vocabulary, complex grammar

### Answer Options
- Provide 4 plausible options
- Avoid obvious wrong answers
- Include common mistakes as distractors
- Ensure only one clearly correct answer

## 🔧 Technical Contributions

### Code Architecture
```
english_learning_shooter.py
├── Game initialization (pygame setup)
├── Data structures (vocabulary_sets)
├── Game logic functions
├── Drawing functions
├── Input handling
└── Main game loop
```

### Key Functions to Understand
- `get_random_question()`: Selects questions based on mode/difficulty
- `fire_bullet()`: Creates bullet objects for correct answers
- `display_question_and_options()`: Renders educational content
- `change_difficulty()`: Handles adaptive learning progression

### Adding New Features
1. **New Learning Modes**: Add to `vocabulary_sets` and update mode cycling
2. **Power-ups**: Extend the power-up system with new abilities
3. **Visual Effects**: Enhance pygame rendering and animations
4. **Sound**: Add audio feedback using pygame.mixer
5. **Data Persistence**: Save progress and high scores

## 📝 Commit Guidelines

### Commit Message Format
```
type(scope): description

Examples:
feat(questions): add advanced grammar questions
fix(gameplay): correct bullet collision detection
docs(readme): update installation instructions
style(code): format according to PEP 8
```

### Commit Types
- `feat`: New feature or educational content
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no logic changes)
- `refactor`: Code restructuring
- `test`: Adding or updating tests
- `chore`: Build process or auxiliary tools

## 🧪 Testing

### Manual Testing
- Test all learning categories
- Verify difficulty progression
- Check power-up functionality
- Ensure educational accuracy

### Writing Tests
```python
def test_question_format():
    """Test that all questions follow the correct format."""
    for category in vocabulary_sets:
        for difficulty in vocabulary_sets[category]:
            for question in vocabulary_sets[category][difficulty]:
                assert "question" in question
                assert "options" in question
                assert len(question["options"]) == 4
                assert "correct" in question
                assert 0 <= question["correct"] <= 3
```

## 📖 Documentation

### README Updates
- Keep feature lists current
- Update screenshots when UI changes
- Maintain installation instructions
- Update educational benefits section

### Code Documentation
- Add docstrings to new functions
- Comment complex game logic
- Document educational design decisions
- Explain algorithm choices

## 🎓 Educational Review Process

### Content Review
All educational content goes through review for:
1. **Accuracy**: Factual correctness
2. **Clarity**: Unambiguous questions and answers
3. **Appropriateness**: Age and skill level suitability
4. **Learning Value**: Educational effectiveness

### Peer Review
- Educational professionals review content
- Native speakers verify language accuracy
- ESL instructors assess difficulty levels
- Beta testers provide gameplay feedback

## 🏆 Recognition

### Contributors
- All contributors are listed in the README
- Major contributions get special recognition
- Educational content creators are credited
- Community helpers are acknowledged

### Types of Recognition
- **Code Contributors**: GitHub contribution graph
- **Educational Contributors**: Special credits section
- **Bug Reporters**: Issue tracking acknowledgments
- **Community Helpers**: Discussion participation

## 📞 Getting Help

### Communication Channels
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Email**: direct contact for sensitive issues
- **Discord**: Real-time community chat (if available)

### Mentorship
- New contributors can request mentorship
- Experienced developers provide guidance
- Educational experts help with content creation
- Code reviews include learning opportunities

## 📋 Pull Request Process

### Before Submitting
1. **Test Your Changes**: Ensure everything works
2. **Update Documentation**: Reflect any changes
3. **Check Code Style**: Follow PEP 8 guidelines
4. **Write Clear Description**: Explain what and why

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Educational content
- [ ] Documentation update

## Testing
- [ ] Tested locally
- [ ] Educational content reviewed
- [ ] No new bugs introduced

## Educational Impact
How does this improve the learning experience?

## Screenshots
If applicable, add screenshots of changes
```

### Review Process
1. **Automated Checks**: Code style and basic tests
2. **Technical Review**: Code quality and functionality
3. **Educational Review**: Content accuracy and appropriateness
4. **Final Testing**: Integration and user experience

## 🙏 Thank You

Your contributions help make English learning more engaging and accessible for students worldwide. Every bug report, feature suggestion, question addition, and code improvement makes a difference in someone's educational journey.

Together, we're building something that truly matters! 🌟📚🎯