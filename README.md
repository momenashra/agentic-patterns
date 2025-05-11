Multi-Agent Procurement Framework
This project implements a multi-agent system to automate the procurement process for products across multiple e-commerce platforms. The system searches, compares, and generates reports for products based on specific criteria.

Key Features
Automated Product Search: Searches across Amazon.eg, Jumia.com.eg, and Noon.com

Price Comparison: Compares prices, discounts, and specifications

Professional Reporting: Generates detailed HTML procurement reports

Multi-Agent Architecture: Uses specialized agents for each step of the process

Agents Overview
Search Queries Recommendation Agent

Generates optimized search queries for e-commerce platforms

Focuses on specific product attributes and price ranges

Search Engine Agent

Executes searches across multiple platforms

Filters results based on confidence scores and relevance

Web Scraping Agent

Extracts detailed product information

Collects specifications, prices, and images

Procurement Report Author Agent

Generates professional HTML reports

Includes comparisons, analysis, and recommendations

Report Verifier Agent

Enhances and validates the final report

Ensures proper structure and valid URLs

Example Output
The system generates comprehensive reports including:

Product comparisons with prices and specifications

Visual tables with rankings

Detailed analysis and recommendations

Executive summaries and conclusions

Technologies Used
Python 3.11

CrewAI framework

Bootstrap 5 (for HTML reports)

Cohere LLM

Tavily search API

ScrapeGraph web scraping tool

Setup Instructions
Install required packages:
``` bash
pip install -qU crewai[tools,agentops] tavily-python scrapegraph-py
```
Set up API keys for:

Cohere

AgentOps

Tavily

ScrapeGraph

Run the notebook to execute the procurement process

Sample Use Case
The system was used to find and compare waterproof crossbody bags for men under 500 EGP, generating a detailed procurement report with top recommendations.

Output Files
step_1_suggested_search_queries.json: Generated search queries

step_2_search_results.json: Raw search results

step_3_search_results.json: Extracted product details

step_4_procurement_report.html: Initial report

step_5_enhanced_report.html: Final verified report
