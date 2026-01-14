# Python Environment Setup

Set up the virtual environment:

```shell
python -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements-dev.txt
pip install -e .
```

# Capstone project setup

### Prerequisites
* Python 3.12.x
* Docker Engine.
* Follow the previous **Python environment Setup** indications.

### Environment settings

Copy and paste the `.env.example` template on your own new `.env` file.

Here a little explanation about what every variable is refering to:


* **KEY_PROVIDER_BASE_URL:** API of you PaaS model providers. I used [Open router platform](https://openrouter.ai/)

  For this project it's highly recommended to create an account and generate a API key.

  If you decide to use Open router, for now API base url is: https://openrouter.ai/api/v1

  However, always check the [Oficial documentation.](https://openrouter.ai/docs/api-reference/get-a-generation)

* **TEXT_MODEL_API_KEY:** API key of you text generation model provider.
* **TEXT_GENERATION_MODEL_NAME:** Name of you text generative model. I recommended to use `deepseek/deepseek-r1:free`
* **IMAGE_GENERATION_API_KEY:** Image generative model API key.
* **IMAGE_GENERATION_MODEL_NAME:** Name of you text generative model. I recommended to use `gemini-2.0-flash-preview-image-generation`

### Run Applications

If you want to run on local:

* `py .\src\main.py` to run API

* `streamlit run .\streamlit_ui\main.py` to run UI

or if you want to use docker:

* `docker-compose up -d`
