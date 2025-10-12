# Glass-Open Interface Integration

This integration allows Glass Chat Bar to automatically detect and execute commands through Open Interface, while still handling questions through the existing Glass AI system.

## 🌐 PickleGlass Web Integration

The integration has also been extended to the **PickleGlass Web** interface, providing a modern web-based chat interface with the same command execution capabilities.

### Web Interface Features
- **Modern React Chat UI** - Clean, responsive interface built with Next.js
- **Real-time Status Updates** - Visual feedback for command execution
- **TypeScript Support** - Full type safety and IntelliSense
- **Mobile Responsive** - Works on desktop and mobile devices
- **Auto-scroll Messages** - Smooth message display and navigation

## 🎯 Overview

When users type in Glass's chat bar, the system now:
- **Commands** → Executes through Open Interface (computer control)
- **Questions** → Handles through Glass AI (existing behavior)

## 🏗️ Architecture

```
Glass Chat Bar
     ↓
Command Classifier
     ↓
┌─────────────────┬─────────────────┐
│   Commands      │   Questions     │
│   (Open Interface) │   (Glass AI)   │
└─────────────────┴─────────────────┘
```

## 📁 Files Added/Modified

### Open Interface Side
- **`/Open-Interface/app/api_server.py`** - Flask API server for HTTP communication
- **`/Open-Interface/app/app.py`** - Modified to start API server in thread

### Glass Side (Electron App)
- **`/glass/src/ui/utils/commandClassifier.js`** - Detects commands vs questions
- **`/glass/src/ui/services/openInterfaceClient.js`** - HTTP client for API calls
- **`/glass/src/ui/ask/AskView.js`** - Modified to integrate command detection and execution
- **`/glass/src/ui/utils/testIntegration.js`** - Test script for the integration

### PickleGlass Web Side (Next.js App)
- **`/glass/pickleglass_web/utils/commandClassifier.ts`** - TypeScript command detection
- **`/glass/pickleglass_web/utils/openInterfaceClient.ts`** - TypeScript HTTP client
- **`/glass/pickleglass_web/components/ChatInterface.tsx`** - React chat component
- **`/glass/pickleglass_web/app/chat/page.tsx`** - Chat page route
- **`/glass/pickleglass_web/app/page.tsx`** - Updated homepage with chat link
- **`/glass/pickleglass_web/utils/testIntegration.ts`** - TypeScript test script
- **`/glass/pickleglass_web/INTEGRATION_README.md`** - Web-specific documentation

## 🚀 Setup Instructions

### 1. Install Dependencies

**Open Interface:**
```bash
cd Open-Interface
pip install flask flask-cors
```

**Glass:**
```bash
cd glass
# Dependencies should already be installed
```

### 2. Start Open Interface
```bash
cd Open-Interface
python app.py
```
This will start both the Open Interface application and the API server on `localhost:5000`.

### 3. Start Glass (Choose one)

**Option A: Electron App**
```bash
cd glass
npm start
# or however you normally start Glass
```

**Option B: Web Interface**
```bash
cd glass/pickleglass_web
npm run dev
# Navigate to http://localhost:3000/chat
```

## 🎮 Usage

### Commands (Executed by Open Interface)
Type any of these command patterns:
- `open Chrome browser`
- `click on the settings button`
- `type "hello world" in the text field`
- `close the current window`
- `navigate to google.com`
- `launch Microsoft Word`
- `create a new document`
- `delete the selected file`
- `move the file to desktop`
- `scroll down the page`
- `press the Enter key`
- `search for "python tutorial"`
- `find all PDF files`

### Questions (Handled by Glass AI)
Type any of these question patterns:
- `What is the weather today?`
- `How do I install Python?`
- `Why is my computer slow?`
- `Can you help me with coding?`
- `Explain how this algorithm works`
- `Tell me about machine learning`

## 🔧 Command Keywords

The system detects commands based on these keywords:

**Action Verbs:**
- open, click, type, close, navigate, launch, create, delete, move, scroll, press, search, find
- go to, switch to, minimize, maximize, resize, drag, drop, select, highlight
- copy, paste, cut, undo, redo, save, load, import, export, download, upload
- install, uninstall, update, refresh, reload, start, stop, pause, resume, restart, shutdown
- connect, disconnect, login, logout, sign in, sign out, send, receive, share, invite, join, leave
- add, remove, edit, modify, change, update, show, hide, display, toggle, enable, disable
- activate, deactivate, turn on, turn off, set, get, configure, setup

**Question Indicators:**
- what, how, why, when, where, which, who
- can you, could you, would you, should i, is it, are you, do you, does it, will it, can it
- help me, explain, describe, tell me, show me
- i need, i want, i'm looking for, i'm trying to

## 🎨 UI Features

### Execution Status Display
- **Starting**: Blue status with clock icon
- **Running**: Orange status with clock icon  
- **Completed**: Green status with checkmark icon
- **Error**: Red status with X icon

### Auto-hide Behavior
- **Completed**: Auto-hides after 3 seconds
- **Error**: Auto-hides after 5 seconds

## 🧪 Testing

Run the test script to verify the integration:

```bash
cd glass/src/ui/utils
node testIntegration.js
```

This will test:
- Command classification accuracy
- Question classification accuracy  
- API connection status

## 🔍 How It Works

### 1. Input Classification
```javascript
const classification = commandClassifier.classify(userInput);
if (classification.type === 'command' && classification.confidence > 0.6) {
    // Execute through Open Interface
} else {
    // Handle through Glass AI
}
```

### 2. Command Execution Flow
```
User Input → Command Classifier → Open Interface API → Execution → Status Updates
```

### 3. API Communication
- **POST /api/execute** - Start command execution
- **GET /api/status/{id}** - Check execution status
- **POST /api/stop** - Stop current execution
- **GET /api/health** - Health check

## 🛠️ Configuration

### API Server Settings
- **Host**: localhost
- **Port**: 5000
- **CORS**: Enabled for Glass integration
- **Timeout**: 30 seconds
- **Retry**: 3 attempts with exponential backoff

### Command Classification
- **Confidence Threshold**: 0.6 (60%)
- **Keyword Matching**: Case-insensitive
- **Context Analysis**: UI elements, file types, applications

## 🐛 Troubleshooting

### Common Issues

**1. "Open Interface API server is not available"**
- Ensure Open Interface is running: `python app.py`
- Check if port 5000 is available
- Verify Flask dependencies are installed

**2. Commands not being detected**
- Check command keywords in `commandClassifier.js`
- Lower confidence threshold if needed
- Add custom keywords for your use case

**3. Execution fails**
- Check Open Interface logs
- Verify API server is responding: `curl http://localhost:5000/api/health`
- Check network connectivity

**4. Questions being treated as commands**
- Review question indicators in classifier
- Adjust confidence thresholds
- Add question patterns to classifier

### Debug Mode
Enable debug logging in the browser console to see:
- Classification results
- API communication
- Execution status updates

## 🔮 Future Enhancements

- **Custom Command Training**: Learn from user corrections
- **Context Awareness**: Remember previous commands
- **Batch Commands**: Execute multiple commands in sequence
- **Command History**: Track and replay previous executions
- **Voice Commands**: Integration with speech recognition
- **Smart Suggestions**: Suggest commands based on context

## 📝 License

This integration follows the same license terms as the parent projects (Glass and Open Interface).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues with this integration:
1. Check the troubleshooting section
2. Review the test script output
3. Check browser console for errors
4. Verify Open Interface is running correctly
