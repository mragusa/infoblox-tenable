# infoblox-tenable
A collection of tools and templates for integrating the Infoblox NIOS platform to Tenable

## Overview
Summary of notes from Infoblox Tenable integration based on the [Infoblox Deployment Guide](https://insights.infoblox.com/resources-deployment-guides/infoblox-deployment-guide-integration-with-tenable-security-center)

## NIOS Ecosystem Templates

| Name | Purpose |
| --- | --- |
| `TenableAsset.json.txt` | `Tenable Asset Template` |
| `TenableLogin.json.txt` | `Tenable Login Template` |
| `TenableLogout.json.txt` | `Tenable Logout Template` |
| `TenableScan.json.txt` | `Tenable Scan Template` |
| `TenableSession.json.txt` | `Tenable Session Template` |

## NIOS Tenable Tools
| Name | Description |
| --- | --- |
| `TNBL_create_EAs.php` | `PHP Script to create Infoblox Extensible Attributes` |

## [Configure API Keys](https://docs.tenable.com/security-center/Content/GenerateAPIKey.htm)
* Login to Tenable Security Center as admin
* Navigate to the Users Page
* Select the User you wish to generate an API key for
* Click on "Generate API Key"
* Save the API Keys
> [!Important]
> Note: You cannot view API secret keys in the Tenable Security Center interface after initial generation. If you lose your existing secret key, you must generate new API keys.

### Test API Keys
```
curl -X GET -k --header "x-apikey: accesskey=4def6bc216f14c1ab86dfba8738ff4a5; secretkey=a47d1d3a071443449a75821129526b96" https://Tenable.sc/rest/currentUser
```

## Python Setup
1. Setup Python venv
```
python3 -m venv venv
```

2. Change to new venv environment
```
source venv/bin/activate
```

3. Install Required Python Packages
```
pip install -r requirements.txt
```

## Script Details
