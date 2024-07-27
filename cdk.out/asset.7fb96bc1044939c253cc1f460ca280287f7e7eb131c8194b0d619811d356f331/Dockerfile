FROM public.ecr.aws/lambda/python:3.11

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages with SSL verification disabled for pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copy all files in ./src
COPY src/* ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD [ "main.handler" ]
