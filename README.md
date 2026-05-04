# GECX Agent with AI Commerce Search

This directory contains the configuration, OpenAPI specifications, and custom scripts required to create and configure a conversational agent in **GECX** (Gemini Enterprise for Customer Experience) that connects to **AI Commerce Search** (formerly known as **VAISC** - Vertex AI Search for Commerce).

## Overview

The objective is to enable the GECX agent to perform product searches and return structured results (like product carousels) by interfacing with the AI Commerce Search API.

## Component Breakdown

### 1. API Specification
- **[aics_openapi.yaml](file:///home/cardi/gecx/aics_openapi.yaml)**: This file contains the OpenAPI 3.0 specification for the AI Commerce Search API. It defines the endpoints, request parameters, and response schemas that the GECX agent uses to communicate with the commerce search service.

### 2. Configuration
- **[variable_aics.json](file:///home/cardi/gecx/variable_aics.json)**: A template JSON file containing the variables required for the API calls.
    - *Note*: You must update the `"project_id"` field with your actual Google Cloud project ID.
    - It configures defaults for `catalog_id` (`default_catalog`), `location_id` (`global`), and search behavior like `queryExpansionSpec`.

### 3. Custom Logic & Tooling
- **[searchMultipleProducts.py](file:///home/cardi/gecx/searchMultipleProducts.py)**: A Python script that defines a function `searchMultipleProducts`.
    - **Purpose**: This function is designed to be used as a custom tool by the GECX agent.
    - **Functionality**: It takes a list of search queries, executes a search for each query using the `tools.search_commerce_Search` method (available in the GECX runtime), and processes the results.
    - **Output**: It formats the product data (Title, URI, Image, Price) into a specific structure with `"type": "products-carrousels"`, which is used by the frontend to render product carousels.

### 4. Agent Prompt
- **[product_search_prompt.txt](file:///home/cardi/gecx/product_search_prompt.txt)**: This file is intended to hold the system prompt or instructions for the GECX agent to guide its behavior during product search interactions. *(Currently empty)*.

### 5. Ready-to-Import Agent
- **[exported_app_Commerce Agent_emeasouth.zip](file:///home/cardi/gecx/exported_app_Commerce Agent_emeasouth.zip)**: This zip archive contains a ready-to-import GECX agent.
    - **Important**: While the agent is ready to be imported, you will need to reimplement some of the tools (or update their configurations) to make it work correctly in your specific environment.
