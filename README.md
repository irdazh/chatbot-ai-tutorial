## Chatbot AI

Using OpeanAI API from this [youtube tutorial.](https://www.youtube.com/watch?v=q5HiD5PNuck)
Nah, I decided to just follow one from Gemini, and scrape things from the tutorial. Well, what can I do? 

Oh. And another btw, I use groq model. Using FastAPI as the backend and streamlit for the UI yeay. Bye.

## Tutorial steps
1. Installation
2. Create Files
2. Gemini and Copasting Code
    1. Backend Groq brain
    2. Connect to the Frontend UI using Streamlit
    3. Done I guess?
3. Build the (offline) Dockerfile
    1. Create --> Build --> `docker build -f Dockerfile.off -t chatbot-local .` --> help, it took a really long time LOL. --> I guess i try to copy all the files LOL including the .venv and whatsoever hahaha --> either use .dockerignore or just copy one inside the app folder. I guess those are enough.
    2. Run --> `docker run -p 8501:8501 -p 8000:8000 --env-file .env chatbot-local`
    2. Tag --> `docker tag <local-name> <uname>/<repo-name>:<tag>`
    3. Push --> `docker push <uname>/<repo-name>:<tag>`   
    3. Download --> `docker pull (idem as above)`
    4. Run --> `docker run -p 8501:8501 -p 8000:8000 -e GROQ_API_KEY=gsk_THEIR_ACTUAL_KEY <docker-name>`
4. Shall we also build the online one? Hehe. 
    1. Let's see what can we do
    2. Cihuy. 


### Setting things up
```
1. py -3.11 -m venv .venv
2. source .venv/Scripts/activate #or .venv/bin/activate
3. python -m pip install python-dotenv groq google-generativeai ....
```

### Free option you have.
1. Groq
2. Google Gemini -- Later if i got the uhm. 

### Theoretical BG

Things that I don't know at all. I guess. Shame on me but who cares? Not a single one!

Here, Backend 101

1. Localhost --> this machine
    1. in Docker LH --> refer to that specific container (what's that? idk)
    2. Oh, and in Docker, the LH for streamlit are different from the LH for the FastAPI --> enclosed. can't see each other.
    3. Fix: in HF or Render --> replace LH with Public URL --> eg. my-api.onrender.com/chat or what idk hhhh

2. Use Dockerfile to bake an Image! 
    1. Recipe --> text file that said: take python, add groq, copy my code, do this and that.
    2. Image --> frozen meal --> run docker build --> create a static, unchangeable file --> send the file to anyone
    3. Container --> cooked dish --> docker run \[image-name\], the frozen meal comes to life. Uwhooah, great. 
    4. Great. There's no need for user to actually run uvicorn and streamlit. All done in one bake.

3. Async vs sycnc --> busy coffee shop w/ one barista
    1. sync --> one step at a time 
    2. async -- can do parallel work while waiting for the coffee to brew/milk to steam
    3. involves waiting from outside (API/DB) --> use async

