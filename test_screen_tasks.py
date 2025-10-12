"""
Test script to verify screen tasks functionality between Glass and Open Interface
"""

import requests
import time
import json

# API endpoint
API_URL = "http://localhost:5000/api"

def test_screen_task(command):
    """Test a screen task by sending it to Open Interface API"""
    print(f"\nTesting command: '{command}'")
    
    # Send command to execute endpoint
    response = requests.post(
        f"{API_URL}/execute",
        json={"command": command},
        headers={"Content-Type": "application/json"}
    )
    
    if not response.ok:
        print(f"Error: {response.status_code} - {response.text}")
        return False
    
    result = response.json()
    execution_id = result.get("execution_id")
    
    if not execution_id:
        print("Error: No execution ID returned")
        return False
    
    print(f"Execution started with ID: {execution_id}")
    
    # Poll for status
    max_attempts = 30
    for attempt in range(max_attempts):
        status_response = requests.get(f"{API_URL}/status/{execution_id}")
        
        if not status_response.ok:
            print(f"Error checking status: {status_response.status_code} - {status_response.text}")
            return False
        
        status = status_response.json()
        
        if status.get("status") == "completed":
            print("Command execution completed successfully")
            return True
        
        print(f"Command still running (attempt {attempt+1}/{max_attempts})...")
        time.sleep(2)
    
    print("Command execution timed out")
    return False

def main():
    """Run tests for various screen tasks"""
    print("=== SCREEN TASKS INTEGRATION TEST ===")
    
    # Test health check first
    health_response = requests.get(f"{API_URL}/health")
    if health_response.ok:
        print(f"API Health check: OK - {health_response.json()}")
    else:
        print(f"API Health check failed: {health_response.status_code} - {health_response.text}")
        return
    
    # List of screen tasks to test
    test_commands = [
        "Open Brave",
        "Open Discord",
        "Open file explorer and search for hello",
        "Open notepad and type hello world"
    ]
    
    results = {}
    
    # Run each test with a pause between them
    for command in test_commands:
        results[command] = test_screen_task(command)
        time.sleep(5)  # Wait between commands
    
    # Print summary
    print("\n=== TEST RESULTS SUMMARY ===")
    for command, success in results.items():
        print(f"'{command}': {'✓ PASSED' if success else '✗ FAILED'}")

if __name__ == "__main__":
    main()