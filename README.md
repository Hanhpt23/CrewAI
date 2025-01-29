# CrewAI  

## Building a Multi-Agent System with CrewAI  

CrewAI is a framework for building multi-agent systems using large language models (LLMs) and vision-language models (VLMs). This repository provides implementations for both LLM-based and VLM-based multi-agent systems.  

## Components  

### 1. **LLM-Based Multi-Agent System**  
- **File:** `single_agent.py`  
- **Description:** Implements a multi-agent system using multiple LLM agents to collaborate on tasks.  

### 2. **VLM-Based Multi-Agent System**  
- **File:** `vision_agent.py`  
- **Description:** Implements a multi-agent system utilizing vision-language models (VLMs).  
- **Note:** CrewAI currently only supports OpenAI as the VLM provider.  

## Installation & Setup  

To get started with CrewAI, follow these steps:  

### 1. **Install Dependencies**  
```bash
conda create -n crewai
conda activate crewai

pip install -r requirements.txt
```


### 4. **Set Up API Key (Google Colab Example)**  
If running on Google Colab, set up your OpenAI API key:  

```python
import os
from google.colab import userdata
api_key = userdata.get('API')

os.environ["OPENAI_API_KEY"] = api_key
```

### 5. **Run the Multi-Agent System**  
```bash
crewai run
```
