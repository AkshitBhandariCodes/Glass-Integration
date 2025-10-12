"""
Simple test script to verify Glass integration with Open Interface
"""
import requests
import json
import time

# Test the Open Interface API
def test_api():
    print("Testing Open Interface API...")
    
    # Test health endpoint
    try:
        response = requests.get("http://localhost:5000/api/health")
        if response.status_code == 200:
            print("✓ API health check successful")
            print(f"Response: {response.json()}")
        else:
            print(f"✗ API health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ API health check failed: {str(e)}")
        return False
    
    # Test command execution
    try:
        command = "Open Brave"
        print(f"\nTesting command execution: '{command}'")
        
        response = requests.post(
            "http://localhost:5000/api/execute",
            json={"command": command},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✓ Command execution started: {result}")
            
            # Check execution status
            if "execution_id" in result:
                execution_id = result["execution_id"]
                print(f"Execution ID: {execution_id}")
                
                # Poll for status
                for _ in range(5):
                    time.sleep(2)
                    status_response = requests.get(f"http://localhost:5000/api/status/{execution_id}")
                    status = status_response.json()
                    print(f"Status: {status}")
                    
                    if status.get("status") == "completed":
                        print("✓ Command execution completed")
                        break
                
                return True
            else:
                print("✗ No execution ID returned")
                return False
        else:
            print(f"✗ Command execution failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"✗ Command execution failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("=== GLASS INTEGRATION TEST ===")
    print("This script tests the integration between Glass and Open Interface")
    print("Make sure the Open Interface API server is running on port 5000")
    print("===========================\n")
    
    test_api()