# Benny's FastAPI program
An example for fastapi's BackgroundTasks

## Matiti's Requests:

#### Give more generic solution:
in `/app/service/task` I have created a function called `create_and_run_task` which get any function (`unc: Callable[..., Awaitable[Any]]`) and variables (`, *args: Any`).
Now every time I will want to create a background task I will just call to `TaskService.create_and_run_task`.

#### Store task without DB:
insted of a file, the class `TaskService` storing it as a varible called `tasks = {}`

## Setup:
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the application

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.
