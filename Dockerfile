FROM python:3.11-slim

WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the app folder to the container, btw we only care about the ui1.py
COPY ./app /code/app

# Online service usually provide $PORT variable (?)
EXPOSE 7860

# We create a script to run the API on 8000 and Streamlit on 7860
RUN echo "#!/bin/bash\nuvicorn app.main1:app --host 0.0.0.0 --port 8000 &\nstreamlit run app/ui1.py --server.port 7860 --server.address 0.0.0.0" > start.sh
RUN chmod +x start.sh

CMD ["./start.sh"]