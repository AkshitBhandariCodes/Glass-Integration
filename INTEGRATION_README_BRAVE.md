# Glass-Open Interface Integration with Brave Browser Support

## Overview
This integration connects the Pickle Glass web app with Open Interface to enable executing computer commands via LLM. The integration now includes support for Brave browser.

## Components
- **Glass Web App**: Chat interface with OCR capabilities
- **Open Interface**: LLM-powered command execution engine
- **Integration Layer**: API communication between the two systems

## Brave Browser Support
Brave browser has been added as a supported browser option in Open Interface:

1. **UI Settings**: Brave is now available in the browser dropdown alongside Chrome, Firefox, Edge, and Safari
2. **Default Configuration**: The `.env` file has been configured with `DEFAULT_BROWSER=brave`
3. **Path for Windows**: `C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe`

## Integration Flow
1. User enters a command in Glass chat interface
2. Glass sends command to Open Interface API (`http://127.0.0.1:5000/api/execute`)
3. Open Interface processes the command and executes it
4. Status is returned to Glass

## Testing the Integration
To test the integration:
1. Start the Open Interface application
2. Launch the Glass web application
3. Enter a command like "open Brave" or "search in Brave for glass integration"
4. Verify that Brave browser launches correctly

## Troubleshooting
- Ensure Open Interface is running on port 5000
- Check browser path if Brave fails to launch
- Verify CORS settings if API communication fails

## Files Modified
- `/Open-Interface/app/ui.py` - Added Brave to browser dropdown
- `.env` - Confirmed Brave as default browser